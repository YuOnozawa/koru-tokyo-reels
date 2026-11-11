"""Slow 'magazine flip' reel from a rendered carousel (Yu 2026-11-12: calm audience, show things slowly).

  python tools/carousel/reel.py c_03_domannaka [out.mp4]

Reads site/carousels/<id>/NN.jpg + zoom.json (written by render.py). 1080x1920, 30fps, ~20-30 s:
cover 3 s slow push-in -> 1 s page turn -> each content page: whole page 1.5 s, then for each boxed item a 1 s
glide + 1.5 s hold with an English caption fading in -> back to the whole page -> red SAVE sticker.
Optional music: tools/carousel/music/*.m4a|mp3 (first file, or reel.music in the spec), faded in/out.
"""
import glob, json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
W, H, FPS = 1080, 1920, 30
VW, VH = 960, 1200
VX, VY = (W - VW) // 2, (H - VH) // 2 - 50
ARC = os.path.join(ROOT, 'tools/carousel/fonts/Archivo.ttf')
JPF = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'


def arc(size, wght=700):
    f = ImageFont.truetype(ARC, size); f.set_variation_by_axes([wght, 100]); return f


def ease(t):
    t = max(0.0, min(1.0, t)); return t * t * (3 - 2 * t)


def main(cid, out=None):
    d = os.path.join(ROOT, 'site/carousels', cid)
    z = json.load(open(os.path.join(d, 'zoom.json')))
    rc = z.get('reel', {})
    pages = [Image.open(os.path.join(d, p['page'])).convert('RGB') for p in z['pages']]
    out = out or os.path.join(ROOT, 'videos', f'r_{cid}.mp4')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    bg = pages[0].resize((W, int(1350 * W / 1080)))
    bg = bg.resize((int(bg.width * H / bg.height), H)); l = (bg.width - W) // 2
    bg = bg.crop((l, 0, l + W, H)).filter(ImageFilter.GaussianBlur(40))
    bg = Image.blend(bg, Image.new('RGB', (W, H), (10, 8, 6)), 0.6)
    sh = Image.new('RGBA', (VW + 120, VH + 120), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle((60, 70, 60 + VW, 70 + VH), fill=(0, 0, 0, 170)); sh = sh.filter(ImageFilter.GaussianBlur(26))
    fcap = arc(46); fj = ImageFont.truetype(JPF, 40); fs = arc(40, 800)
    music = rc.get('music') or next(iter(sorted(glob.glob(os.path.join(ROOT, 'tools/carousel/music/*.m*')))), None)
    tmp = out + '.silent.mp4'
    proc = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', tmp], stdin=subprocess.PIPE)

    def view(img, cx, cy, zm):
        w, h = 1080 / zm, 1350 / zm
        x0 = min(max(cx - w / 2, 0), 1080 - w); y0 = min(max(cy - h / 2, 0), 1350 - h)
        return img.resize((VW, VH), Image.LANCZOS, box=(x0, y0, x0 + w, y0 + h))

    def frame(img, c, cap='', a=1.0, sticker=0.0):
        f = bg.copy(); f.paste(sh, (VX - 60, VY - 60), sh); f.paste(view(img, *c), (VX, VY))
        dr = ImageDraw.Draw(f)
        if cap and a > 0:
            v = int(255 * a); tw = dr.textlength(cap, font=fcap)
            if tw > W - 80:
                fc = arc(36); tw = dr.textlength(cap, font=fc)
            else:
                fc = fcap
            dr.text(((W - tw) / 2, VY + VH + 50), cap, font=fc, fill=(v, v, v))
        if sticker > 0:
            r = int(100 * sticker); cx, cy = VX + VW - 20, VY + 20
            dr.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(232, 56, 47))
            if sticker >= 1:
                dr.text((cx - 40, cy - 52), '保存', font=fj, fill='white'); tw = dr.textlength('SAVE', font=fs); dr.text((cx - tw / 2, cy + 2), 'SAVE', font=fs, fill='white')
        proc.stdin.write(f.tobytes())

    FULL = (540, 675, 1.0)
    # cover
    N = 90
    for i in range(N):
        frame(pages[0], (540, 675, 1 + 0.04 * i / (N - 1)), rc.get('cover_cap', ''), min(1, i / 20))
    # page turn
    nxt = pages[1] if len(pages) > 1 else pages[0]
    for i in range(27):
        t = ease((i + 1) / 27); f_img = nxt
        f = bg.copy(); f.paste(sh, (VX - 60, VY - 60), sh); f.paste(view(nxt, *FULL), (VX, VY))
        w = max(1, int(VW * (1 - t))); c = view(pages[0], 540, 675, 1.04).resize((w, VH))
        f.paste(Image.blend(c, Image.new('RGB', (w, VH), (0, 0, 0)), 0.35 * t), (VX, VY)); proc.stdin.write(f.tobytes())
    last = pages[1] if len(pages) > 1 else pages[0]
    for pi, (pg, meta) in enumerate(zip(pages[1:], z['pages'][1:]), 1):
        if meta['type'] == 'back':
            continue
        last = pg
        if pi > 1:  # simple crossfade from previous content page
            for i in range(20):
                f_prev = view(pages[pi - 1], *FULL); f_new = view(pg, *FULL)
                f = bg.copy(); f.paste(sh, (VX - 60, VY - 60), sh); f.paste(Image.blend(f_prev, f_new, ease(i / 19)), (VX, VY)); proc.stdin.write(f.tobytes())
        for i in range(45):
            frame(pg, (540, 675, 1 + 0.02 * i / 44), meta.get('caption', ''), min(1, i / 15))
        prev = (540, 675, 1.02)
        zp = rc.get('zoom_pages')  # optional: only zoom into these page types; others are shown whole (keeps reels ~30 s)
        still = meta['type'] in ('phrase', 'map') or (zp is not None and meta['type'] not in zp)
        zo = rc.get('zoom_only')  # optional: only zoom into these page files (e.g. ["02.jpg"])
        still = still or (zo is not None and meta['page'] not in zo)
        if still and meta['type'] not in ('phrase', 'map'):  # a page shown whole: hold it long enough to read
            for i in range(rc.get('still_hold', 45)):
                frame(pg, (540, 675, 1.02), meta.get('caption', ''), 1)
        boxes = [] if still else [b for b in meta['boxes'] if b['w'] < 1000 or b['h'] < 400][:8]
        if still and meta['type'] == 'phrase':  # show the phrase page a little longer
            cap = meta['boxes'][0]['cap'] if meta['type'] == 'phrase' and meta['boxes'] else ''
            for i in range(60):
                frame(pg, (540, 675, 1.02 + 0.02 * i / 59), cap, 1)
        MV, HD = (24, 33) if len(boxes) > 6 else (30, 45)
        for b in boxes:
            cx, cy = b['x'] + b['w'] / 2, b['y'] + b['h'] / 2
            zm = min(2.4, 0.86 * min(1080 / b['w'], 1350 / b['h'])); zm = max(zm, 1.15)
            if b['w'] >= 900:  # a wide row (list page): zoom on its left part, where the name is
                zm = min(1.7, 0.8 * 1350 / b['h']); cx = b['x'] + 1080 / zm / 2 - 24
            tgt = (cx, cy, zm)
            for i in range(MV + HD):
                if i < MV:
                    t = ease(i / (MV - 1)); c = [prev[j] + (tgt[j] - prev[j]) * t for j in range(3)]; a = max(0, (i - MV / 2) / (MV / 2))
                else:
                    c = [tgt[0], tgt[1], tgt[2] * (1 + 0.03 * (i - MV) / HD)]; a = 1
                frame(pg, c, b['cap'], a)
            prev = (tgt[0], tgt[1], tgt[2] * 1.03)
        for i in range(36):
            t = ease(i / 35); frame(pg, [prev[j] + (FULL[j] - prev[j]) * t for j in range(3)])
    for i in range(100):
        frame(last, FULL, rc.get('end_cap', 'Save it for your trip'), min(1, i / 20), sticker=min(1, max(0, (i - 20) / 12)))
    proc.stdin.close(); proc.wait()
    if music and os.path.exists(music):
        dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', tmp]).decode())
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', tmp, '-stream_loop', '-1', '-i', music, '-t', f'{dur:.2f}',
                        '-filter:a', f'volume=0.6,afade=t=in:d=1.5,afade=t=out:st={dur - 2:.2f}:d=2', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', out], check=True)
        os.remove(tmp)
    else:
        os.replace(tmp, out)
    print(out)


if __name__ == '__main__':
    main(*sys.argv[1:])
