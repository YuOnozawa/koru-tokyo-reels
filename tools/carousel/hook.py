"""Hook reel (Yu 2026-11-14: reach fell 5-10x with the slow page-flip reels; reels are for reach, the carousel is the issue).

  python tools/carousel/hook.py c_06_kanazawa [out.mp4]

Reads spec['hook'] from tools/carousel/specs/<id>.json:
  {"q_jp": "金沢で、\\n何を食べる？", "q_en": "What to eat in Kanazawa?", "photo": "stock/yu/x.jpg", "pos": [0.5, 0.5],
   "beats": [{"photo": "stock/yu/y.jpg"|None, "pos": [x, y], "jp": "香箱蟹", "en": "Kobako crab", "fact": "Winter only"}],
   "end_jp": "続きはカルーセルで", "end_en": "Full issue in today's carousel post"}
1080x1920, 30fps, ~15-18 s: 0-2.4 s the question over a moving photo (or bold type when there is no photo),
then one fast beat per item (photo push-in or a big type card), then the issue cover + SAVE. Only Yu's own photos.
"""
import json, os, subprocess, sys, glob
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W, H, FPS = 1080, 1920, 30
ARC = os.path.join(ROOT, 'tools/carousel/fonts/Archivo.ttf')
JPF = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
PAPER, INK, RED, YEL, WHITE = (247, 245, 240), (17, 17, 17), (232, 56, 47), (255, 210, 63), (255, 255, 255)
HOOK_T, BEAT_T, END_T = 2.4, 2.3, 2.6
SAFE_TOP, SAFE_BOT = 230, 1500   # keep text clear of the IG header and the caption/buttons area


def arc(size, wght=800):
    f = ImageFont.truetype(ARC, size); f.set_variation_by_axes([wght, 100]); return f


def jp(size):
    return ImageFont.truetype(JPF, size, index=0)


def ease(t):
    t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3


def wrap(dr, text, font, maxw):
    out, line = [], ''
    for w in text.split(' '):
        t = (line + ' ' + w).strip()
        if dr.textlength(t, font=font) <= maxw: line = t
        else: out.append(line); line = w
    out.append(line); return [l for l in out if l]


def cover(img, zoom, pos):
    """Crop img to fill W x H at the given zoom, centred on pos (fractions)."""
    s = max(W / img.width, H / img.height) * zoom
    w, h = W / s, H / s
    x0 = min(max(pos[0] * img.width - w / 2, 0), img.width - w)
    y0 = min(max(pos[1] * img.height - h / 2, 0), img.height - h)
    return img.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + w, y0 + h))


def shade(f, top=0.0, bottom=0.75):
    g = Image.new('L', (1, H))
    for y in range(H):
        t = y / H; a = top * max(0, 1 - t / 0.25) + bottom * max(0, (t - 0.45) / 0.55)
        g.putpixel((0, y), int(255 * min(1, a)))
    f.paste(Image.new('RGB', (W, H), (0, 0, 0)), (0, 0), g.resize((W, H)))


def block(dr, x, y, text, font, fg, bg, pad=(22, 10)):
    l, t, r, b = dr.textbbox((0, 0), text, font=font)
    dr.rectangle((x, y, x + r - l + pad[0] * 2, y + b - t + pad[1] * 2), fill=bg)
    dr.text((x + pad[0] - l, y + pad[1] - t), text, font=font, fill=fg)
    return y + b - t + pad[1] * 2


def mast(dr):
    dr.text((60, SAFE_TOP - 120), 'with', font=arc(34, 700), fill=WHITE)
    dr.text((60 + dr.textlength('with ', font=arc(34, 700)), SAFE_TOP - 140), 'KORU', font=arc(58, 900), fill=WHITE)


def main(cid, out=None):
    spec = json.load(open(os.path.join(ROOT, 'tools/carousel/specs', cid + '.json')))
    hk = spec['hook']
    out = out or os.path.join(ROOT, 'videos', f'r_{cid}.mp4')
    load = lambda p: Image.open(os.path.join(ROOT, p)).convert('RGB') if p else None
    tmp = out + '.silent.mp4'
    proc = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', tmp], stdin=subprocess.PIPE)
    put = lambda im: proc.stdin.write(im.tobytes())
    n_frames = 0

    # 1) hook: the question, big, over a photo that punches in then drifts
    hp = load(hk.get('photo'))
    lines = hk['q_jp'].split('\n'); qs = hk.get('q_size', 118)
    _d = ImageDraw.Draw(Image.new('RGB', (8, 8)))
    while qs > 60 and max(_d.textlength(l, font=jp(qs)) for l in lines) > W - 180: qs -= 4
    fq = jp(qs); fen = arc(50)
    cdir = os.path.join(ROOT, 'site/carousels', cid)
    zoom = json.load(open(os.path.join(cdir, 'zoom.json')))
    listp = next((p for p in zoom['pages'] if p['type'] == 'list' and p['boxes']), None)

    def clip_for(bi, b):
        if b.get('clip'):
            pg = zoom['pages'][b['clip'][0]]; bx = pg['boxes'][b['clip'][1]]
        elif listp and bi < len(listp['boxes']):
            pg, bx = listp, listp['boxes'][bi]
        else:
            return None
        im = Image.open(os.path.join(cdir, pg['page'])).convert('RGB')
        pad = 16; c = im.crop((max(0, bx['x'] - pad), max(0, bx['y'] - pad), min(1080, bx['x'] + bx['w'] + pad), min(1350, bx['y'] + bx['h'] + pad)))
        sc = min(1000 / c.width, 560 / c.height)
        return c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS)
    for i in range(int(HOOK_T * FPS)):
        t = i / FPS
        if hp:
            z = 1.32 - 0.22 * ease(t / 0.6) - 0.06 * (t / HOOK_T)
            f = cover(hp, z, hk.get('pos', (0.5, 0.5))); shade(f, 0.5, 0.85)
        else:
            f = Image.new('RGB', (W, H), RED)
        dr = ImageDraw.Draw(f); mast(dr)
        y = 980 - 75 * len(lines)
        for k, ln in enumerate(lines):          # each line slides in, staggered
            a = ease((t - 0.08 * k) / 0.35)
            x = 60 - int((1 - a) * 700)
            if a > 0: y = block(dr, x, y, ln, fq, INK, YEL, (26, 14)) + 14
        if t > 0.5:
            a = ease((t - 0.5) / 0.4); yy = y + 20 + int((1 - a) * 40)
            for ln in wrap(dr, hk['q_en'], fen, W - 160):
                yy = block(dr, 60, yy, ln, fen, WHITE, INK, (20, 10)) + 6
        put(f); n_frames += 1

    # 2) beats
    beats = hk['beats']
    for bi, b in enumerate(beats):
        bp = load(b.get('photo'))
        clip = None if bp else clip_for(bi, b)
        for i in range(int(BEAT_T * FPS)):
            t = i / FPS
            if bp:
                z = 1.04 + 0.10 * (t / BEAT_T) if bi % 2 == 0 else 1.14 - 0.10 * (t / BEAT_T)
                f = cover(bp, z, b.get('pos', (0.5, 0.5))); shade(f, 0.45, 0.9); fg_sub = WHITE
            else:
                f = Image.new('RGB', (W, H), PAPER); fg_sub = INK
                d0 = ImageDraw.Draw(f)
                num = str(bi + 1); fn = arc(900, 900)
                d0.text((W - 60 - d0.textlength(num, font=fn) + int(40 * (1 - t / BEAT_T)), 120), num, font=fn, fill=(232, 228, 220))
            if clip is not None:
                a0 = ease(t / 0.35); cy = 330 + int((1 - a0) * 120)
                sc = 1.0 + 0.04 * (t / BEAT_T); cc = clip.resize((int(clip.width * sc), int(clip.height * sc)))
                cx = (W - cc.width) // 2
                d0.rectangle((cx + 12, cy + 14, cx + cc.width + 12, cy + cc.height + 14), fill=(210, 205, 196))
                f.paste(cc, (cx, cy)); d0.rectangle((cx, cy, cx + cc.width - 1, cy + cc.height - 1), outline=INK, width=4)
            dr = ImageDraw.Draw(f); mast(dr) if bp else None
            if not bp:
                dr.text((60, SAFE_TOP - 140), 'with', font=arc(34, 700), fill=INK)
                dr.text((60 + dr.textlength('with ', font=arc(34, 700)), SAFE_TOP - 160), 'KORU', font=arc(58, 900), fill=INK)
            a = ease(t / 0.3)
            y = 1020 if not bp else 1060
            x = 60 - int((1 - a) * 600)
            dr.rectangle((x, y - 96, x + 84, y - 12), fill=RED)
            dr.text((x + 42, y - 54), str(bi + 1), font=arc(60, 900), fill=WHITE, anchor='mm')
            sz = b.get('jp_size', 92)
            while sz > 48 and max(dr.textlength(l, font=jp(sz)) for l in b['jp'].split('\n')) > W - 170: sz -= 4
            fj = jp(sz)
            for ln in b['jp'].split('\n'):
                y = block(dr, x, y, ln, fj, INK, YEL, (24, 12)) + 10
            a2 = ease((t - 0.25) / 0.3)
            if a2 > 0:
                yy = y + 8 + int((1 - a2) * 30)
                for ln in wrap(dr, b['en'], arc(52), W - 160):
                    yy = block(dr, 60, yy, ln, arc(52), WHITE, INK, (20, 10)) + 6
                if b.get('fact'):
                    yy += 10
                    for ln in wrap(dr, b['fact'], arc(42, 700), W - 140):
                        dr.text((62, yy), ln, font=arc(42, 700), fill=fg_sub); yy += 54
            put(f); n_frames += 1

    # 3) end: the carousel cover + where the rest is
    cov = Image.open(os.path.join(ROOT, 'site/carousels', cid, '01.jpg')).convert('RGB')
    cw = 760; ch = int(cov.height * cw / cov.width); cov = cov.resize((cw, ch), Image.LANCZOS)
    for i in range(int(END_T * FPS)):
        t = i / FPS
        f = Image.new('RGB', (W, H), RED); dr = ImageDraw.Draw(f)
        a = ease(t / 0.35)
        cx, cy = (W - cw) // 2, 300 + int((1 - a) * 200)
        dr.rectangle((cx + 14, cy + 18, cx + cw + 14, cy + ch + 18), fill=(150, 30, 25))
        f.paste(cov, (cx, cy))
        y = cy + ch + 40
        y = block(dr, (W - dr.textlength(hk.get('end_jp', '続きはカルーセルで'), font=jp(64)) - 44) // 2, y,
                  hk.get('end_jp', '続きはカルーセルで'), jp(64), INK, YEL, (22, 10)) + 10
        e = hk.get('end_en', "Full issue in today's carousel post")
        dr.text((W // 2, y + 36), e, font=arc(42), fill=WHITE, anchor='mm')
        if t > 0.6:
            s = ease((t - 0.6) / 0.25)
            r = int(95 * (0.6 + 0.4 * s)); sx, sy = cx + cw - 30, cy + 40
            dr.ellipse((sx - r, sy - r, sx + r, sy + r), fill=INK)
            dr.text((sx, sy - 18), '保存', font=jp(int(44 * s) + 1), fill=YEL, anchor='mm')
            dr.text((sx, sy + 28), 'SAVE', font=arc(int(34 * s) + 1, 900), fill=WHITE, anchor='mm')
        put(f); n_frames += 1

    proc.stdin.close(); proc.wait()
    dur = n_frames / FPS
    music = spec.get('reel', {}).get('music') or next(iter(sorted(glob.glob(os.path.join(ROOT, 'tools/carousel/music/*.m*')))), None)
    if music and not os.path.isabs(music): music = os.path.join(ROOT, music)
    if music and os.path.exists(music):
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-stream_loop', '-1', '-i', music, '-t', f'{dur:.2f}',
                        '-filter:a', f'volume=0.7,afade=t=in:d=0.3,afade=t=out:st={dur - 1.2:.2f}:d=1.2', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', out], check=True)
        os.remove(tmp)
    else:
        os.replace(tmp, out)
    print(out, f'{dur:.1f}s')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
