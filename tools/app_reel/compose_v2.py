"""v2 shop reel: full-bleed photo + ticket caption + Koru host bubble + stamp; screen segments reuse the phone frame.
Usage: python3 compose_v2.py <vid>"""
import json, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scripts import SCRIPTS
vid = sys.argv[1]; SC = SCRIPTS[vid]
F = '/home/claude/fonts/'; CH = '/home/claude/koru-tokyo-reels/tools/chara/'; CL = '/home/claude/render/app/clips/'; ST = '/home/claude/koru-tokyo-reels/stock/'
dela = lambda n: ImageFont.truetype(F + 'DelaGothicOne-Regular.ttf', n)
dot = lambda n: ImageFont.truetype(F + 'DotGothic16-Regular.ttf', n)
zen = lambda n: ImageFont.truetype(F + 'ZenKakuGothicNew-Black.ttf', n)
zenb = lambda n: ImageFont.truetype(F + 'ZenKakuGothicNew-Bold.ttf', n)
INK = '#22303a'; RED = '#d7262e'; AMB = '#ffa22b'; LED = '#17110c'
W, H = 1080, 1920
tmp = f'out/_{vid}'; os.makedirs(tmp, exist_ok=True)
def run(cmd): subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + cmd, check=True)
def dur(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).decode())
def fit(d, text, font, maxw, size):
    while d.textlength(text, font=font(size)) > maxw: size -= 2
    return size
def led(d, text):
    d.rounded_rectangle((40, 60, W - 40, 150), 16, fill=LED); d.text((W // 2, 106), text, font=dot(36), fill=AMB, anchor='mm')
def plate(img, kicker, big, sub, y0=860):
    d = ImageDraw.Draw(img); lines = big.split('\n')
    size = min(fit(d, l, dela, W - 200, 104) for l in lines)
    h = 110 + len(lines) * (size + 14) + (70 if sub else 0) + 26; y1 = y0 + h
    d.rounded_rectangle((50, y0 + 8, W - 50, y1 + 8), 30, fill=(0, 0, 0, 90))
    d.rounded_rectangle((50, y0, W - 50, y1), 30, fill='#fbfcfc')
    d.rounded_rectangle((50, y0, W - 50, y0 + 24), 12, fill=RED); d.rectangle((50, y0 + 14, W - 50, y0 + 24), fill='#fbfcfc')
    d.text((92, y0 + 62), '食券  ' + kicker, font=dot(36), fill=RED, anchor='lm')
    d.line((92, y0 + 92, W - 92, y0 + 92), fill='#c9d2d7', width=3)
    y = y0 + 110 + size // 2
    for l in lines: d.text((92, y), l, font=dela(size), fill=INK, anchor='lm'); y += size + 14
    if sub: d.text((92, y + 6), sub, font=zenb(fit(d, sub, zenb, W - 200, 46)), fill='#5d6b75', anchor='lm')
    return y1
def bubble(img, text, x, y):
    d = ImageDraw.Draw(img); lines = text.split('\n'); f = zen(50)
    w = max(d.textlength(l, font=f) for l in lines) + 70; h = len(lines) * 62 + 44
    d.rounded_rectangle((x, y, x + w, y + h), 34, fill='#ffffff', outline=INK, width=6)
    d.polygon([(x + 10, y + h - 40), (x - 40, y + h + 10), (x + 50, y + h - 8)], fill='#ffffff')
    d.line([(x + 6, y + h - 42), (x - 40, y + h + 10), (x + 50, y + h - 6)], fill=INK, width=6, joint='curve')
    yy = y + 22 + 31
    for l in lines: d.text((x + 35, yy), l, font=f, fill=INK, anchor='lm'); yy += 62
def stamp(img, text, cx, cy):
    st = Image.new('RGBA', (640, 170), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    s = fit(sd, text, dela, 560, 84); sd.rounded_rectangle((8, 8, 632, 162), 20, outline=RED, width=12); sd.text((320, 85), text, font=dela(s), fill=RED, anchor='mm')
    st = st.rotate(-9, expand=True, resample=Image.BICUBIC); img.alpha_composite(st, (cx - st.width // 2, cy - st.height // 2))
tm = json.load(open(f'audio/{vid}_timing.json'))['sentences']; parts = []
korus = {}
for nm in ('koru_smile_t', 'koru_happy_t'):
    k = Image.open(CH + nm + '.png'); korus[nm] = k.resize((330, int(k.height * 330 / k.width)), Image.LANCZOS)
for i, sc in enumerate(SC['scenes']):
    v = sc['v2']; s = tm[i]; nar = s['end'] - s['start']; a0, a1 = max(0, s['start'] - .05), s['end'] + .12
    D = nar + (0.35 if i else 0.25); out = f'{tmp}/seg{i}.mp4'
    aud = ['-ss', f'{a0:.3f}', '-t', f'{a1 - a0:.3f}', '-i', f'audio/{vid}.mp3']
    if v['kind'] == 'photo':
        ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); g = Image.new('L', (1, H))
        for yy in range(H): g.putpixel((0, yy), int(max(0, (yy - 700) / 1220) * 170))
        ov.paste(Image.new('RGBA', (W, H), (10, 14, 18, 255)), (0, 0), g.resize((W, H)))
        d = ImageDraw.Draw(ov); led(d, SC['led'])
        tag = v.get('tag'); 
        if tag: tw = d.textlength(tag, font=zenb(30)) + 40; d.rounded_rectangle((W - 60 - tw, 282, W - 60, 332), 25, fill=(0, 0, 0, 150)); d.text((W - 60 - tw / 2, 307), tag, font=zenb(30), fill='#ffffff', anchor='mm')
        if v.get('pic'):
            nm, (cx0, cy0, cx1, cy1) = v['pic']; ph = Image.open(ST + nm + '.jpg').convert('RGB')
            ph = ph.crop((int(ph.width * cx0), int(ph.height * cy0), int(ph.width * cx1), int(ph.height * cy1)))
            pw_, ph_ = 880, 520; r = max(pw_ / ph.width, ph_ / ph.height); ph = ph.resize((int(ph.width * r), int(ph.height * r)), Image.LANCZOS)
            ph = ph.crop(((ph.width - pw_) // 2, (ph.height - ph_) // 2, (ph.width - pw_) // 2 + pw_, (ph.height - ph_) // 2 + ph_))
            card = Image.new('RGBA', (pw_ + 32, ph_ + 32), (255, 255, 255, 255)); mk = Image.new('L', ph.size, 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, pw_ - 1, ph_ - 1), 18, fill=255)
            card.paste(ph, (16, 16), mk); cm = Image.new('L', card.size, 0); ImageDraw.Draw(cm).rounded_rectangle((0, 0, card.width - 1, card.height - 1), 30, fill=255)
            sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((84, 296, 84 + card.width, 296 + card.height), 30, fill=(0, 0, 0, 70))
            ov.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10))); ov.paste(card, (84, 280), cm)
            d = ImageDraw.Draw(ov); tg = 'Photo: similar dish, not this shop'; tw = d.textlength(tg, font=zenb(28)) + 36
            d.rounded_rectangle((W - 100 - tw, 780, W - 100, 826), 23, fill=(0, 0, 0, 160)); d.text((W - 100 - tw / 2, 803), tg, font=zenb(28), fill='#ffffff', anchor='mm')
        y1 = plate(ov, v['kicker'], v['big'], v.get('sub'))
        if v.get('stamp'): stamp(ov, v['stamp'], 760, 860)
        koru_in = bool(v.get('koru'))
        if koru_in: bubble(ov, v['koru'], 400, 560)
        ov.save(f'{tmp}/ov{i}.png')
        # background: cover-crop + slow push-in (zoom on the egg area if asked)
        if v.get('bg'): bg = Image.open(ST + v['bg'] + '.jpg').convert('RGB')
        else:
            bg = Image.new('RGB', (W, H), '#ffa22b'); bd = ImageDraw.Draw(bg)
            for yy in range(-H, H * 2, 120): bd.line([(0, yy), (W, yy + 700)], fill='#ff9a1a', width=44)
            bd.ellipse((W // 2 - 520, 380, W // 2 + 520, 1420), fill='#ffb648')
        kz = v.get('k', 1.15); sc_ = max(W * kz / bg.width, H * kz / bg.height)
        bg = bg.resize((int(bg.width * sc_), int(bg.height * sc_)), Image.LANCZOS); bg.save(f'{tmp}/bg{i}.jpg')
        bw, bh = bg.size; fx, fy = v.get('f', (0.6, 0.78) if v.get('zoom') == 'egg' else (0.5, 0.45))
        cx = f"({bw}-{W})*{fx}"; cy = f"({bh}-{H})*{fy}"
        z = f"(1+0.08*t/{D:.3f})"
        fc = (f"[0:v]scale=w='{bw}*{z}':h='{bh}*{z}':eval=frame,crop={W}:{H}:x='(iw-{W})*{fx}':y='(ih-{H})*{fy}'[b];"
              f"[b][1:v]overlay=0:0[v1]")
        ins = ['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/bg{i}.jpg', '-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/ov{i}.png']
        last = 'v1'
        if koru_in:
            ins += ['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/koru.png']; korus['koru_happy_t'].save(f'{tmp}/koru.png')
            kh = korus['koru_happy_t'].height; yb = 830 - kh
            fc += f";[2:v]format=rgba[k];[v1][k]overlay=60:'if(lt(t,0.25),{H}-(({H}-{yb})*t/0.25),{yb}-abs(sin((t-0.25)*6))*22)'[v2]"; last = 'v2'
        ai = len(ins) // 6 if False else (3 if koru_in else 2)
        fc += f";[{ai}:a]adelay=150|150,apad=whole_dur={D:.3f},atrim=0:{D:.3f}[aout]"
        run(ins + aud + ['-filter_complex', fc, '-map', f'[{last}]', '-map', '[aout]', '-t', f'{D:.3f}', '-r', '30', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-ar', '44100', '-b:a', '160k', out])
    else:
        PH = 1180; PW = round(780 * PH / 1688); PX = (W - PW) // 2; PY = 470
        cd = dur(CL + v['clip'] + '.mp4'); D = max(D, min(cd, nar + 1.0))
        bg = Image.new('RGBA', (W, H), '#c9d2d7'); d = ImageDraw.Draw(bg); led(d, SC['led'])
        lines = v['title'].split('\n'); size = min(fit(d, l, dela, W - 140, 64) for l in lines)
        d.rounded_rectangle((50, 250, W - 50, 440), 28, fill='#fbfcfc'); d.rounded_rectangle((50, 250, W - 50, 272), 12, fill=RED); d.rectangle((50, 262, W - 50, 272), fill='#fbfcfc')
        yy = 350 - (len(lines) - 1) * (size + 10) // 2
        for l in lines: d.text((W // 2, yy), l, font=dela(size), fill=INK, anchor='mm'); yy += size + 10
        d.rounded_rectangle((PX - 16, PY - 16, PX + PW + 16, PY + PH + 16), 56, fill='#171e24')
        bg.alpha_composite(korus['koru_smile_t'].resize((260, int(korus['koru_smile_t'].height * 260 / 330))), (W - 290, PY + PH - 300))
        bg.convert('RGB').save(f'{tmp}/bg{i}.png')
        m = Image.new('L', (PW, PH), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, PW - 1, PH - 1), 42, fill=255); m.save(f'{tmp}/mask.png')
        fc = (f'[1:v]scale={PW}:{PH}:flags=lanczos,fps=30,tpad=stop_mode=clone:stop_duration=10,trim=0:{D:.3f},setpts=PTS-STARTPTS[sc];'
              f'[3:v]format=gray[mk];[sc][mk]alphamerge[scm];[0:v][scm]overlay={PX}:{PY}[v];[2:a]adelay=150|150,apad=whole_dur={D:.3f},atrim=0:{D:.3f}[aout]')
        run(['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/bg{i}.png', '-i', CL + v['clip'] + '.mp4'] + aud + ['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/mask.png',
             '-filter_complex', fc, '-map', '[v]', '-map', '[aout]', '-t', f'{D:.3f}', '-r', '30', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-ar', '44100', '-b:a', '160k', out])
    parts.append(out); print(i, v['kind'], round(D, 2))
open(f'{tmp}/list.txt', 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(['-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', f'out/{vid}.mp4'])
print(f'out/{vid}.mp4', dur(f'out/{vid}.mp4'))
