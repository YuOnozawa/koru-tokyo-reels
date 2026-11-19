"""Clean reel (2026-11-19 test): moving pictures first, text under ~10% of the screen.

  python tools/carousel/clean.py <cid> [out.mp4] [--voice]
  --voice: AI narration (Kokoro am_michael, no music) instead of the music track (H1 test, 11/20).
  Optional spec['hook']['say'], beats[i]['say'], hook['end_say'] override the spoken lines.

Why: from 11/12 our reels became text-led (pages, big question blocks, list-row clips) and only 3 of 16 reached non-followers.
Instagram lists "reels where text covers most of the screen" as not recommended. Before 11/12, 20 of 20 reels (footage, little text) got 100-150.

Uses the same spec['hook'] as hook.py. Each segment = one picture, full screen, slow push-in, plus ONE subtitle box
(JP line + EN line) low on the screen. Beats with Yu's photo show the photo; beats without a photo show Koru on paper.
No borrowed photos: only stock/yu/* and our own Koru art.
"""
import json, os, subprocess, sys, glob
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hook import ROOT, W, H, FPS, PAPER, INK, YEL, WHITE, arc, jp, ease, cover, wrap

HOOK_T, BEAT_T, END_T = 2.2, 2.1, 1.8
SUB_Y = 1250          # subtitle box top: above the IG caption/buttons zone
KORU = ['tools/chara/koru_happy_t.png', 'tools/chara/chara_wave.png', 'tools/chara/chara_phone.png']


def koru_card(i, t, dur):
    f = Image.new('RGB', (W, H), PAPER)
    p = os.path.join(ROOT, KORU[i % len(KORU)])
    if os.path.exists(p):
        k = Image.open(p).convert('RGBA')
        s = 760 / max(k.size) * (1.0 + 0.04 * t / dur)
        k = k.resize((int(k.width * s), int(k.height * s)), Image.LANCZOS)
        y = 330 + int(18 * (1 - ease(t / 0.5)))
        f.paste(k, ((W - k.width) // 2, y), k)
    return f


def subtitle(f, jp_line, en_line, t):
    a = ease(t / 0.25)
    dr = ImageDraw.Draw(f, 'RGBA')
    fj, fe = jp(54), arc(34, 700)
    jl = wrap(dr, jp_line, fj, 920) if ' ' in jp_line else [jp_line]
    el = wrap(dr, en_line, fe, 920) if en_line else []
    h = 34 + 70 * len(jl) + 46 * len(el) + 20
    y0 = SUB_Y + int(20 * (1 - a))
    dr.rounded_rectangle((60, y0, W - 60, y0 + h), 26, fill=(0, 0, 0, int(150 * a)))
    y = y0 + 26
    for l in jl:
        dr.text((96, y), l, font=fj, fill=(255, 255, 255, int(255 * a))); y += 70
    for l in el:
        dr.text((96, y), l, font=fe, fill=(255, 210, 63, int(255 * a))); y += 46


def mast(f):
    dr = ImageDraw.Draw(f)
    dr.text((60, 120), 'with', font=arc(28, 700), fill=WHITE)
    dr.text((60 + dr.textlength('with ', font=arc(28, 700)), 104), 'KORU', font=arc(46, 900), fill=WHITE)


def photo_frame(img, pos, t, dur, inward=True):
    z = 1.04 + 0.10 * (t / dur) if inward else 1.14 - 0.10 * (t / dur)
    f = cover(img, z, pos)
    g = Image.new('L', (1, H))
    for y in range(H):
        g.putpixel((0, y), int(255 * (0.35 * max(0, 1 - y / 360))))
    f.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), g.resize((W, H)))
    return f


def narrate(lines, path):
    """AI voice (Kokoro, am_michael) per segment; returns segment durations (s) and writes one wav."""
    import numpy as np, soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro('/home/claude/tts/kokoro-v1.0.onnx', '/home/claude/tts/voices-v1.0.bin')
    parts, durs = [], []
    for ln in lines:
        a, sr = k.create(ln, voice='am_michael', speed=1.05, lang='en-us')
        d = max(1.6, len(a) / sr + 0.35)
        pad = np.zeros(int(d * sr) - len(a), dtype=a.dtype)
        parts += [a, pad]; durs.append(d)
    sf.write(path, np.concatenate(parts), sr)
    return durs


def main(cid, out=None, voice=False):
    spec = json.load(open(os.path.join(ROOT, 'tools/carousel/specs', cid + '.json')))
    hk = spec['hook']
    global HOOK_T, BEAT_T, END_T
    durs = None
    if voice:
        lines = [hk.get('say') or hk.get('q_en', '')] + [b.get('say') or f"{b.get('en','')}. {b.get('fact','')}." for b in hk['beats']] + [hk.get('end_say', 'Save this for your trip.')]
        durs = narrate(lines, f'/tmp/clean_{cid}_voice.wav')
    out = out or os.path.join(ROOT, 'videos', f'r_{cid}.mp4')
    tmp = os.path.join('/tmp', f'clean_{cid}'); os.makedirs(tmp, exist_ok=True)
    for p in glob.glob(tmp + '/*.jpg'): os.remove(p)
    load = lambda p: Image.open(os.path.join(ROOT, p)).convert('RGB') if p else None
    n = 0

    def put(f):
        nonlocal n
        f.save(f'{tmp}/{n:05d}.jpg', quality=90); n += 1

    hp = load(hk.get('photo'))
    q = hk['q_jp'].replace('\n', '')
    if durs: HOOK_T = durs[0]
    for i in range(int(HOOK_T * FPS)):
        t = i / FPS
        f = photo_frame(hp, hk.get('pos', [0.5, 0.5]), t, HOOK_T) if hp else koru_card(0, t, HOOK_T)
        if hp: mast(f)
        subtitle(f, q, hk.get('q_en', ''), 1.0)          # text from frame 0: the first frame is the thumbnail
        put(f)
    for bi, b in enumerate(hk['beats']):
        img = load(b.get('photo'))
        if durs: BEAT_T = durs[bi + 1]
        line = b['jp'] + ('  ' + b['fact'] if False else '')
        for i in range(int(BEAT_T * FPS)):
            t = i / FPS
            f = photo_frame(img, b.get('pos', [0.5, 0.5]), t, BEAT_T, bi % 2 == 0) if img else koru_card(bi + 1, t, BEAT_T)
            if img: mast(f)
            subtitle(f, b['jp'], (b.get('en', '') + ' · ' + b.get('fact', '')).strip(' ·'), t)
            put(f)
    if durs: END_T = durs[-1]
    for i in range(int(END_T * FPS)):
        t = i / FPS
        f = photo_frame(hp, hk.get('pos', [0.5, 0.5]), HOOK_T + t, HOOK_T + END_T) if hp else koru_card(0, t, END_T)
        if hp: mast(f)
        subtitle(f, '保存して、旅のときに。', "Save it for your trip · full issue in today's carousel", t)
        put(f)
    music = sorted(glob.glob(os.path.join(ROOT, 'tools/carousel/music/*')))
    dur = n / FPS
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', '-framerate', str(FPS), '-i', f'{tmp}/%05d.jpg']
    if voice:
        cmd += ['-i', f'/tmp/clean_{cid}_voice.wav', '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '160k']
    elif music:
        cmd += ['-i', music[0], '-filter_complex', f'[1:a]atrim=0:{dur},afade=t=in:d=0.3,afade=t=out:st={dur-0.8}:d=0.8[a]', '-map', '0:v', '-map', '[a]', '-c:a', 'aac', '-b:a', '160k']
    cmd += ['-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-movflags', '+faststart', '-shortest', out]
    subprocess.run(cmd, check=True)
    cov = os.path.join(ROOT, 'site/covers', f'r_{cid}.jpg')
    Image.open(f'{tmp}/00000.jpg').save(cov, quality=90)
    print(out, f'{dur:.1f}s')


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    main(a[0], a[1] if len(a) > 1 else None, voice='--voice' in sys.argv)
