"""Narration generator (Kokoro-82M, Apache-2.0).
Sentence text may contain {display|IPA} spans for Japanese words so they are
pronounced correctly; the display part is used for subtitles.
Usage: python3 tts.py <video_id>   (reads SCRIPTS from scripts.py)
"""
import json, re, subprocess, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

MODEL = '/home/claude/tts/kokoro-v1.0.onnx'
VOICES = '/home/claude/tts/voices-v1.0.bin'
VOICE = 'am_michael'
GAP = 0.38
SPAN = re.compile(r'\{([^|}]+)\|([^}]+)\}')
_k = None


def kok():
    global _k
    if _k is None:
        _k = Kokoro(MODEL, VOICES)
    return _k


def display(text):
    return SPAN.sub(lambda m: m.group(1), text)


def phonemes(text):
    k = kok(); out = []; pos = 0
    for m in SPAN.finditer(text):
        eng = text[pos:m.start()]
        if eng.strip():
            out.append(k.tokenizer.phonemize(eng, 'en-us'))
        out.append(m.group(2))
        pos = m.end()
    tail = text[pos:]
    if tail.strip():
        out.append(k.tokenizer.phonemize(tail, 'en-us'))
    return ' '.join(o.strip() for o in out if o.strip())


def trim(a, sr, thr=0.01):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0:
        return a
    s = max(0, idx[0] - int(0.03 * sr)); e = min(len(a), idx[-1] + int(0.08 * sr))
    return a[s:e]


def make(vid, sentences, outdir, speed=1.05):
    k = kok(); sr = 24000; parts = []; timing = []; t = 0.25
    parts.append(np.zeros(int(0.25 * sr), np.float32))
    for s in sentences:
        ph = phonemes(s['say'])
        a, sr = k.create(ph, voice=VOICE, speed=speed, is_phonemes=True)
        a = trim(a.astype(np.float32), sr)
        a = a / (np.abs(a).max() + 1e-6) * 0.9
        dur = len(a) / sr
        timing.append({'text': display(s['say']), 'start': round(t, 3), 'end': round(t + dur, 3)})
        parts += [a, np.zeros(int(GAP * sr), np.float32)]
        t += dur + GAP
    wav = f'{outdir}/{vid}_raw.wav'; mp3 = f'{outdir}/{vid}.mp3'
    sf.write(wav, np.concatenate(parts), sr)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, '-af',
                    'loudnorm=I=-15:TP=-1.5:LRA=7', '-ar', '44100', '-b:a', '192k', mp3], check=True)
    json.dump({'sentences': timing, 'total_sec': round(t, 3)}, open(f'{outdir}/{vid}_timing.json', 'w'), indent=1)
    return mp3


if __name__ == '__main__':
    sys.path.insert(0, '/home/claude/render')
    from scripts import SCRIPTS
    import os
    os.makedirs('/home/claude/render/audio', exist_ok=True)
    for vid in sys.argv[1:] or list(SCRIPTS):
        print(vid, make(vid, SCRIPTS[vid]['scenes'], '/home/claude/render/audio'))
