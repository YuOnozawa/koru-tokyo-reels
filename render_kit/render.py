"""Reel renderer v2 (card style) for @koru.tokyo_guide.
python3 render.py <video_id> [...]   -> out/<video_id>.mp4
Needs audio/<id>.mp3 + audio/<id>_timing.json from tts.py and photos in assets/.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
from scripts import SCRIPTS

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
A = f'{HERE}/assets'
GF = '/usr/share/fonts/truetype/google-fonts'
LF = '/home/claude/fonts'
NOTO = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'

INK = (20, 17, 15); CREAM = (246, 236, 220); RED = (232, 68, 46); MUTE = (246, 236, 220, 200)
BG_COLORS = [(24, 20, 17), (31, 24, 20), (20, 24, 27)]


def font(kind, size):
    path = {'black': f'{LF}/Poppins-Black.ttf', 'xb': f'{LF}/Poppins-ExtraBold.ttf',
            'bold': f'{GF}/Poppins-Bold.ttf', 'semi': f'{LF}/Poppins-SemiBold.ttf'}.get(kind)
    if kind == 'jp':
        return ImageFont.truetype(NOTO, size, index=0)
    if kind == 'mincho':
        return ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSerifCJK-Black.ttc', size, index=0)
    return ImageFont.truetype(path, size)


_cache = {}
def photo(name):
    if name not in _cache:
        path = f'{A}/{name}.jpg'
        if not os.path.exists(path):
            path = f'/home/claude/koru-tokyo-reels/stock/{name}.jpg'
        im = ImageOps.exif_transpose(Image.open(path)).convert('RGB')
        _cache[name] = im
    return _cache[name]


def cover(im, fx, fy, zoom):
    """crop a 9:16 window from im centred on (fx,fy) with zoom>=1, resized to W,H"""
    iw, ih = im.size
    tw = iw if iw / ih < W / H else ih * W / H
    th = tw * H / W
    tw /= zoom; th /= zoom
    cx = min(max(fx * iw, tw / 2), iw - tw / 2); cy = min(max(fy * ih, th / 2), ih - th / 2)
    box = (cx - tw / 2, cy - th / 2, cx + tw / 2, cy + th / 2)
    return im.resize((W, H), Image.BILINEAR, box=box)


def fit(draw, text, kind, start, maxw, minsize=48):
    s = start
    while s > minsize:
        f = font(kind, s)
        w = max(draw.textlength(l, font=f) for l in text.split('\n'))
        if w <= maxw:
            return f
        s -= 4
    return font(kind, minsize)


def grad(h, top_alpha, bottom_alpha):
    g = Image.new('L', (1, h))
    for y in range(h):
        g.putpixel((0, y), int(top_alpha + (bottom_alpha - top_alpha) * y / max(1, h - 1)))
    return g.resize((W, h))


STYLE = 'modern'
SUMI = (30, 26, 23); SHU = (200, 64, 43); PAPER = (243, 234, 216)
_WASHI = None
def washi(w, h):
    """procedural washi paper: warm cream, soft grain and long fibres"""
    global _WASHI
    if _WASHI is None:
        import random
        rnd = random.Random(7)
        base = Image.new('RGB', (W, H), PAPER)
        noise = Image.effect_noise((W, H), 18).convert('L')
        base = Image.composite(Image.new('RGB', (W, H), (232, 221, 200)), base, noise.point(lambda v: max(0, v - 128)))
        dd = ImageDraw.Draw(base)
        for _ in range(900):
            x, y = rnd.randrange(W), rnd.randrange(H); L_ = rnd.randrange(20, 90); a = rnd.uniform(-1, 1)
            dd.line((x, y, x + L_, y + a * L_ * 0.3), fill=(250, 244, 230), width=1)
        _WASHI = base.filter(ImageFilter.GaussianBlur(0.6))
    return _WASHI.crop((0, 0, w, h))


def wa_card(card, hook, end):
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    maxw = 820; items = []
    if card.get('kicker'):
        items.append((card['kicker'], font('xb', 36), SHU, 20))
    if card.get('jp'):
        items.append((card['jp'], fit(d, card['jp'], 'mincho', 180 if '\n' not in card['jp'] else 124, maxw), SUMI, 14))
    if card.get('roman'):
        items.append((card['roman'], fit(d, card['roman'], 'black', 76, maxw), SHU, 12))
    if card.get('big'):
        start = 140 if hook else (110 if not end else 96)
        items.append((card['big'], fit(d, card['big'], 'mincho', start, maxw), SUMI, 18))
    if card.get('sub'):
        _k = 'jp' if any(ord(ch) > 0x2E80 for ch in card['sub']) else 'semi'
        items.append((card['sub'], fit(d, card['sub'], _k, 46 if _k == 'semi' else 40, maxw), (92, 78, 66), 0))
    hs = []
    for t, f, _, g in items:
        bb = d.multiline_textbbox((0, 0), t, font=f, spacing=int(f.size * 0.12), align='center'); hs.append(bb[3] - bb[1])
    total = sum(hs) + sum(g for *_, g in items)
    cy = 1150 if end else (880 if not hook else 780)
    y = cy - total / 2; pad = 56
    x0, y0, x1, y1 = 56, int(y - pad), W - 56, int(y + total + pad)
    paper = washi(x1 - x0, y1 - y0).convert('RGBA')
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle((x0 + 10, y0 + 14, x1 + 10, y1 + 14), fill=(0, 0, 0, 90))
    L = Image.alpha_composite(L, sh.filter(ImageFilter.GaussianBlur(12)))
    L.paste(paper, (x0, y0)); d = ImageDraw.Draw(L)
    d.rectangle((x0 + 16, y0 + 16, x1 - 16, y1 - 16), outline=SUMI, width=3)
    d.rectangle((x0 + 26, y0 + 26, x1 - 26, y1 - 26), outline=SUMI, width=1)
    # hanko stamp
    hx, hy = x1 - 118, y0 - 40
    d.rounded_rectangle((hx, hy, hx + 92, hy + 92), 10, fill=SHU)
    d.rounded_rectangle((hx + 7, hy + 7, hx + 85, hy + 85), 7, outline=(255, 238, 228), width=3)
    fh = font('mincho', 34)
    d.text((hx + 46, hy + 30), 'コ', font=fh, fill=(255, 238, 228), anchor='mm')
    d.text((hx + 46, hy + 64), 'ル', font=fh, fill=(255, 238, 228), anchor='mm')
    for (t, f, fill, g), h in zip(items, hs):
        bb = d.multiline_textbbox((0, 0), t, font=f, spacing=int(f.size * 0.12), align='center')
        d.multiline_text((W / 2 - (bb[2] - bb[0]) / 2 - bb[0], y - bb[1]), t, font=f, fill=fill, spacing=int(f.size * 0.12), align='center')
        y += h + g
    return L


def card_layer(card, hook, has_photo, end):
    if STYLE == 'wa':
        return wa_card(card, hook, end)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    maxw = 880
    items = []  # (text, font, fill, gap_after)
    if card.get('kicker'):
        items.append((card['kicker'], font('xb', 40), RED if not has_photo else (255, 214, 102), 22))
    if card.get('jp'):
        items.append((card['jp'], fit(d, card['jp'], 'jp', 190 if '\n' not in card['jp'] else 130, maxw), CREAM, 18))
    if card.get('roman'):
        items.append((card['roman'], fit(d, card['roman'], 'black', 84, maxw), RED if not has_photo else (255, 214, 102), 14))
    if card.get('big'):
        start = 150 if hook else (118 if not end else 100)
        items.append((card['big'], fit(d, card['big'], 'black', start, maxw), CREAM, 20))
    if card.get('sub'):
        _k = 'jp' if any(ord(ch) > 0x2E80 for ch in card['sub']) else 'semi'
        items.append((card['sub'], fit(d, card['sub'], _k, 52 if _k == 'semi' else 44, maxw), CREAM, 0))
    heights = []
    for t, f, _, g in items:
        bb = d.multiline_textbbox((0, 0), t, font=f, spacing=int(f.size * 0.12), align='center')
        heights.append(bb[3] - bb[1])
    total = sum(heights) + sum(g for *_, g in items)
    cy = 1150 if end else (880 if not hook else 780)
    y = cy - total / 2
    if has_photo:  # dark plate behind text for legibility
        pad = 44
        plate = Image.new('RGBA', (W, H), (0, 0, 0, 0)); pd = ImageDraw.Draw(plate)
        pd.rounded_rectangle((60, y - pad, W - 60, y + total + pad), 36, fill=(12, 10, 9, 175))
        L = Image.alpha_composite(L, plate); d = ImageDraw.Draw(L)
    for (t, f, fill, g), h in zip(items, heights):
        bb = d.multiline_textbbox((0, 0), t, font=f, spacing=int(f.size * 0.12), align='center')
        d.multiline_text((W / 2 - (bb[2] - bb[0]) / 2 - bb[0], y - bb[1]), t, font=f, fill=fill,
                         spacing=int(f.size * 0.12), align='center')
        y += h + g
    return L


def title_layer(title, ai):
    tag = ai if isinstance(ai, str) else ('AI image' if ai else None)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    if STYLE == 'wa':  # noren: vermilion cloth with slits
        f = fit(d, title, 'mincho', 40, 640, 26)
        tw = d.textlength(title, font=f); nw = int(tw + 90)
        d.rectangle((40, 150, 40 + nw, 236), fill=SHU)
        for k in (1, 2):
            sx = 40 + nw * k // 3; d.rectangle((sx - 3, 196, sx + 3, 236), fill=(0, 0, 0, 0))
        d.rectangle((40, 150, 40 + nw, 160), fill=(150, 40, 26))
        d.text((40 + nw / 2, 186), title, font=f, fill=(255, 245, 235), anchor='mm')
    else:
        f = fit(d, title.upper(), 'xb', 38, 700, 26)
        tw = d.textlength(title.upper(), font=f)
        d.rounded_rectangle((60, 168, 60 + tw + 48, 168 + 66), 33, fill=RED)
        d.text((84, 168 + 33), title.upper(), font=f, fill=(255, 255, 255), anchor='lm')
    if tag:
        fa = font('semi', 26)
        d.rounded_rectangle((60, 248, 60 + d.textlength(tag, font=fa) + 28, 288), 20, fill=(0, 0, 0, 140))
        d.text((74, 268), tag, font=fa, fill=(255, 255, 255, 220), anchor='lm')
    return L


ICON = None
def icon_layer():
    global ICON
    if ICON is None:
        im = photo('koru_smile'); s = min(im.size)
        iw, ih = im.size; c = im.crop((0, int(ih * .12), iw, int(ih * .12) + iw)).resize((170, 170), Image.LANCZOS)
        m = Image.new('L', (170, 170), 0); ImageDraw.Draw(m).ellipse((0, 0, 169, 169), fill=255)
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        x, y = W - 170 - 50, 150
        d.ellipse((x - 7, y - 7, x + 177, y + 177), fill=(255, 255, 255))
        L.paste(c, (x, y), m)
        ICON = L
    return ICON


def chunks(text, f, maxw=860):
    words = text.split(); lines = []; cur = ''
    d = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return ['\n'.join(lines[i:i + 2]) for i in range(0, len(lines), 2)]


def sub_layer(text):
    f = font('bold', 46)
    L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    bb = d.multiline_textbbox((0, 0), text, font=f, spacing=10, align='center')
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    x0 = W / 2 - tw / 2; y0 = 1440 - th / 2
    d.rounded_rectangle((x0 - 28, y0 - 20, x0 + tw + 28, y0 + th + 26), 22, fill=(0, 0, 0, 175))
    d.multiline_text((x0 - bb[0], y0 - bb[1]), text, font=f, fill=(255, 255, 255), spacing=10, align='center')
    return L


def background(scene, i):
    if scene.get('bg'):
        return None
    im = Image.new('RGB', (W, H), BG_COLORS[i % len(BG_COLORS)])
    d = ImageDraw.Draw(im)
    # subtle noren-red band + dotted texture for brand feel
    d.rectangle((0, H - 300, W, H), fill=tuple(int(c * .85) for c in BG_COLORS[i % len(BG_COLORS)]))
    for y in range(340, 1300, 48):
        for x in range(24 + (y // 48 % 2) * 24, W, 48):
            d.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, 18) if False else (44, 38, 34))
    return im


def build(vid):
    global STYLE
    spec = SCRIPTS[vid]; scenes = spec['scenes']; STYLE = spec.get('style', 'modern')
    tm = json.load(open(f'{HERE}/audio/{vid}_timing.json'))
    sents = tm['sentences']; total = sents[-1]['end'] + 1.2
    nfr = int(total * FPS)
    starts = [0.0] + [s['start'] for s in sents[1:]]
    ends = starts[1:] + [total]
    title = title_layer(spec['title'], False); icon = icon_layer()
    prepared = []
    for i, (sc, st) in enumerate(zip(scenes, sents)):
        has_photo = bool(sc.get('bg'))
        card = card_layer(sc.get('card', {}), sc.get('hook'), has_photo, sc.get('end'))
        over = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        if has_photo:
            over = Image.alpha_composite(over, Image.merge('RGBA', [Image.new('L', (W, H), 0)] * 3 + [
                grad(H, 70, 150)]))
        hud = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        if not sc.get('hook'):
            hud = Image.alpha_composite(hud, title_layer(spec['title'], sc.get('tag') or sc.get('ai')))
        elif sc.get('ai') or sc.get('tag'):
            tg = sc.get('tag') or 'AI image'
            fa = font('semi', 26); dd = ImageDraw.Draw(hud)
            dd.rounded_rectangle((60, 168, 60 + dd.textlength(tg, font=fa) + 28, 208), 20, fill=(0, 0, 0, 140))
            dd.text((74, 188), tg, font=fa, fill=(255, 255, 255, 220), anchor='lm')
        hud = Image.alpha_composite(hud, icon)
        fsub = font('bold', 46)
        cks = chunks(st['text'], fsub)
        lens = [len(c) for c in cks]; acc = 0; ctimes = []
        for c in cks:
            ctimes.append(st['start'] + (st['end'] - st['start']) * acc / sum(lens)); acc += len(c)
        prepared.append(dict(sc=sc, card=card, over=over, hud=hud, subs=[(t, sub_layer(c)) for t, c in zip(ctimes, cks)],
                             bg=background(sc, i)))
    out = f'{HERE}/out/{vid}.mp4'; os.makedirs(f'{HERE}/out', exist_ok=True)
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                           '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', f'{HERE}/audio/{vid}.mp3',
                           '-af', 'apad', '-t', f'{total:.2f}', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
                           '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', out],
                          stdin=subprocess.PIPE)
    for n in range(nfr):
        t = n / FPS
        i = max(k for k in range(len(starts)) if starts[k] <= t)
        p = prepared[i]; sc = p['sc']
        local = (t - starts[i]) / max(.1, ends[i] - starts[i])
        if sc.get('bg'):
            name, fx, fy = sc['bg']
            z = 1.0 + 0.07 * local if i % 2 == 0 else 1.07 - 0.06 * local
            frame = cover(photo(name), fx, fy, z).convert('RGBA')
        else:
            frame = p['bg'].convert('RGBA')
        frame = Image.alpha_composite(frame, p['over'])
        # pop-in for card
        k = min(1.0, (t - starts[i]) / 0.22)
        if k < 1:
            s = 0.9 + 0.1 * k
            cl = p['card'].resize((int(W * s), int(H * s)), Image.BILINEAR)
            tmp = Image.new('RGBA', (W, H), (0, 0, 0, 0)); tmp.paste(cl, ((W - cl.width) // 2, (H - cl.height) // 2))
            a = tmp.split()[3].point(lambda v: int(v * k)); tmp.putalpha(a)
            frame = Image.alpha_composite(frame, tmp)
        else:
            frame = Image.alpha_composite(frame, p['card'])
        frame = Image.alpha_composite(frame, p['hud'])
        cur = [l for (ts, l) in p['subs'] if ts <= t]
        if cur and t <= sents[i]['end'] + 0.35:
            frame = Image.alpha_composite(frame, cur[-1])
        ff.stdin.write(frame.convert('RGB').tobytes())
    ff.stdin.close(); ff.wait()
    return out


if __name__ == '__main__':
    for v in sys.argv[1:] or list(SCRIPTS):
        print(build(v))
