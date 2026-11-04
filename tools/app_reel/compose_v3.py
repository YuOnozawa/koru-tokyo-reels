"""v3 'fast' reel compositor: 1-2 s beats, punch-in zoom, whip transitions, SFX, word-by-word captions.
Usage: python3 compose_v3.py <id>   (reads V3[id] from scripts_v3.py)
"""
import sys, subprocess, math, random, os
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, '/home/claude/render')
import tts
from scripts_v3 import V3

W, H, FPS, SR = 1080, 1920, 30, 44100
FN = '/home/claude/fonts/'; ST = '/home/claude/koru-tokyo-reels/stock/'; CH = '/home/claude/koru-tokyo-reels/tools/chara/'
dela = lambda s: ImageFont.truetype(FN + 'DelaGothicOne-Regular.ttf', s)
pop_ = lambda s: ImageFont.truetype(FN + 'Poppins-Black.ttf', s)
zen = lambda s: ImageFont.truetype(FN + 'ZenKakuGothicNew-Black.ttf', s)
RED, YEL, INK = (232, 52, 45), (255, 214, 10), (20, 22, 26)
vid = sys.argv[1]; SC = V3[vid]; OUT = f'/home/claude/render/out/{vid}.mp4'; TMP = f'/tmp/v3_{vid}'; os.makedirs(TMP, exist_ok=True)

# ---------- audio: voice per beat ----------
k = tts.kok(); beats = []; t = 0.0
for b in SC['beats']:
    a, sr = k.create(tts.phonemes(b['say']), voice=tts.VOICE, speed=SC.get('speed', 1.22), is_phonemes=True)
    a = tts.trim(a.astype(np.float32), sr); a = a / (np.abs(a).max() + 1e-6) * 0.9
    a = np.interp(np.arange(0, len(a), sr / SR), np.arange(len(a)), a).astype(np.float32)  # resample to 44.1k
    d = max(b.get('min', 1.2), len(a) / SR + 0.12)
    beats.append(dict(b, voice=a, start=t, dur=d, vdur=len(a) / SR)); t += d
TOT = t + 0.05; N = int(TOT * FPS)

def sfx_boom():
    n = int(.45 * SR); x = np.arange(n) / SR; return (np.sin(2 * np.pi * (70 - 30 * x) * x) * np.exp(-x * 7) * .9).astype(np.float32)
def sfx_whoosh():
    n = int(.22 * SR); x = np.arange(n) / SR; noise = np.random.RandomState(1).randn(n)
    env = np.sin(np.pi * x / x[-1]) ** 2; s = np.convolve(noise, np.ones(12) / 12, 'same') * env
    return (s / np.abs(s).max() * .35).astype(np.float32)
def sfx_pop():
    n = int(.09 * SR); x = np.arange(n) / SR; return (np.sin(2 * np.pi * (1200 - 5000 * x) * x) * np.exp(-x * 40) * .45).astype(np.float32)
def beat_loop(total):
    n = int(total * SR); m = np.zeros(n, np.float32); bpm = 118; step = 60 / bpm
    kick = sfx_boom()[: int(.25 * SR)] * .5; x = np.arange(int(.04 * SR)) / SR
    hat = (np.random.RandomState(2).randn(len(x)) * np.exp(-x * 120) * .06).astype(np.float32)
    i = 0
    while i * step < total:
        p = int(i * step * SR)
        if i % 2 == 0: m[p:p + len(kick)] += kick[: max(0, min(len(kick), n - p))]
        else: m[p:p + len(hat)] += hat[: max(0, min(len(hat), n - p))]
        i += 1
    return m * .55
mix = beat_loop(TOT)
def put(a, at, g=1.0):
    p = int(at * SR); q = min(len(mix), p + len(a)); mix[p:q] += a[: q - p] * g
for i, b in enumerate(beats):
    put(b['voice'], b['start'] + 0.04, 1.0)
    put(sfx_boom() if i == 0 else sfx_whoosh(), max(0, b['start'] - (0 if i == 0 else .1)), .8)
    if b.get('chips'): put(sfx_pop(), b['start'] + .35, .9)
mix = np.clip(mix, -1, 1); sf.write(f'{TMP}/a.wav', mix, SR)

# ---------- visuals ----------
cache = {}
def photo(name):
    if name not in cache:
        im = Image.open(ST + name).convert('RGB') if not name.startswith('/') else Image.open(name).convert('RGB')
        s = max(W / im.width, H / im.height) * 1.25; im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
        cache[name] = im
    return cache[name]
def frame_bg(b, lt):
    im = photo(b['photo']); z = 1.0 + 0.22 * max(0, 1 - lt / .22) ** 2 + 0.04 * lt   # punch-in then slow push
    cw, ch = min(im.width, W * 1.25 / z), min(im.height, H * 1.25 / z)
    fx, fy = b.get('focus', (.5, .5)); cx, cy = im.width * fx, im.height * fy
    x0 = min(max(0, cx - cw / 2), im.width - cw); y0 = min(max(0, cy - ch / 2), im.height - ch)
    f = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
    dark = Image.new('RGB', (W, H), (0, 0, 0)); return Image.blend(f, dark, .28)
def stroke_text(d, xy, txt, font, fill, sw=10, anchor='mm'):
    d.text(xy, txt, font=font, fill=fill, anchor=anchor, stroke_width=sw, stroke_fill=INK)
def popscale(lt, delay=0.0):
    u = (lt - delay) / .2
    if u <= 0: return 0
    if u >= 1: return 1
    return 0.6 + 0.55 * math.sin(u * math.pi * .75) / math.sin(math.pi * .75) * (1 if u < .8 else 1)
korus = {n: Image.open(CH + n + '.png').convert('RGBA') for n in ('koru_happy_t', 'koru_smile_t')}

def draw_beat(b, lt, i):
    img = frame_bg(b, lt).convert('RGBA'); ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    # progress pills for list items
    if SC.get('n'):
        for j in range(SC['n']):
            x = W // 2 - (SC['n'] * 150) // 2 + j * 150
            on = b.get('idx', 0) > j
            d.rounded_rectangle((x + 10, 90, x + 140, 104), 7, fill=(255, 255, 255, 235) if on else (255, 255, 255, 90))
    # kicker tag
    if b.get('tag'):
        f = pop_(46); tw = d.textlength(b['tag'], font=f)
        d.rounded_rectangle((W // 2 - tw / 2 - 28, 190, W // 2 + tw / 2 + 28, 262), 18, fill=RED)
        d.text((W // 2, 226), b['tag'], font=f, fill='white', anchor='mm')
    # big words, popping in
    s = popscale(lt)
    if s > 0:
        layer = Image.new('RGBA', (W, 900), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
        lines = b['big'].split('\n'); size = b.get('size', 150)
        f = dela(size)
        while max(ld.textlength(l, font=f) for l in lines) > W - 90: size -= 6; f = dela(size)
        y = 450 - (len(lines) - 1) * (size + 18) / 2
        for li, l in enumerate(lines):
            stroke_text(ld, (W / 2, y), l, f, YEL if li == b.get('hl', -1) else 'white', sw=max(8, size // 12)); y += size + 18
        rot = b.get('rot', -3) * (1 - min(1, lt / .3))
        lw = layer.resize((int(W * s), int(900 * s)), Image.BILINEAR).rotate(rot, resample=Image.BILINEAR, expand=False)
        ov.alpha_composite(lw, (int((W - lw.width) / 2), int(b.get('y', 620) - lw.height / 2)))
    # chips
    for ci, c in enumerate(b.get('chips', [])):
        cs = popscale(lt, .3 + .12 * ci)
        if cs <= 0: continue
        f = pop_(int(54 * cs)); tw = d.textlength(c, font=f); y = 1120 + ci * 108
        d.rounded_rectangle((W / 2 - tw / 2 - 30, y - 44, W / 2 + tw / 2 + 30, y + 44), 44, fill=(255, 255, 255, 245))
        d.text((W / 2, y), c, font=f, fill=INK, anchor='mm')
    # koru
    if b.get('koru'):
        ks = popscale(lt, .15)
        if ks > 0:
            kimg = korus['koru_happy_t']; kw = int(360 * ks); kimg = kimg.resize((kw, int(kimg.height * kw / kimg.width)))
            bob = int(abs(math.sin(lt * 7)) * 18); ov.alpha_composite(kimg, (W - kw - 40, 1180 - bob))
            if ks >= 1:
                f = pop_(48); txt = b['koru']; tw = d.textlength(txt, font=f)
                d.rounded_rectangle((W - kw - tw - 110, 1150, W - kw - 50, 1250), 30, fill='white', outline=INK, width=5)
                d.text((W - kw - 80 - tw / 2, 1200), txt, font=f, fill=INK, anchor='mm')
    # word-by-word caption
    words = tts.display(b['say']).split(); vd = b['vdur']; tt = lt - .04
    if words and 0 <= tt:
        L = [len(w) + 2 for w in words]; acc = np.cumsum(L) / sum(L) * vd
        k_ = int(np.searchsorted(acc, tt)); k_ = min(k_, len(words) - 1)
        g0 = (k_ // 3) * 3; grp = words[g0:g0 + 3]; fs = 68; f = pop_(fs); y = 1640
        while sum(d.textlength(w + ' ', font=f) for w in grp) > W - 100: fs -= 4; f = pop_(fs)
        widths = [d.textlength(w + ' ', font=f) for w in grp]; x = W / 2 - sum(widths) / 2
        for gi, w in enumerate(grp):
            cur = g0 + gi == k_
            d.text((x, y), w, font=f, fill=YEL if cur else 'white', anchor='lm', stroke_width=7, stroke_fill=INK); x += widths[gi]
    # footer note
    if b.get('note'):
        d.text((W / 2, 1860), b['note'], font=pop_(30), fill=(255, 255, 255, 200), anchor='mm', stroke_width=3, stroke_fill=INK)
    img.alpha_composite(ov)
    if i == 0 and lt < .35:  # hook shake
        a = int(18 * (1 - lt / .35)); img = img.transform(img.size, Image.AFFINE, (1, 0, random.randint(-a, a), 0, 1, random.randint(-a, a)))
    return img.convert('RGB')

ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                       '-i', f'{TMP}/a.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'veryfast',
                       '-c:a', 'aac', '-b:a', '192k', '-shortest', OUT], stdin=subprocess.PIPE)
random.seed(3)
for fi in range(N):
    t = fi / FPS; i = max(j for j, b in enumerate(beats) if b['start'] <= t + 1e-6); b = beats[i]; lt = t - b['start']
    fr = draw_beat(b, lt, i)
    rem = b['start'] + b['dur'] - t
    if i + 1 < len(beats) and rem < .12:  # whip into next beat
        u = 1 - rem / .12; nx = draw_beat(beats[i + 1], 0, i + 1); sh = int(W * u)
        canvas = Image.new('RGB', (W, H)); canvas.paste(fr, (-sh, 0)); canvas.paste(nx, (W - sh, 0))
        fr = canvas.filter(ImageFilter.BoxBlur(0)).transform((W, H), Image.AFFINE, (1, 0, 0, 0, 1, 0))
        fr = Image.blend(fr, fr.filter(ImageFilter.GaussianBlur(14)), .7)
    ff.stdin.write(fr.tobytes())
ff.stdin.close(); ff.wait()
print(OUT, round(TOT, 2))
