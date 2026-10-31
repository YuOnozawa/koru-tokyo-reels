"""Merged app-intro reel: per-segment render (screen clip in phone / graphic card) + narration slice, then concat.
Usage: python3 compose_app.py lr_03_app"""
import json, subprocess, sys, os, math
from PIL import Image, ImageDraw, ImageFont
from scripts import SCRIPTS
vid = sys.argv[1]
SEG = [('screen', 'hook'), ('pain', None), ('screen', 'plan'), ('screen', 'shop'), ('screen', 'phr'), ('chara', None), ('screen', 'hub')]
F = '/home/claude/fonts/'; CH = '/home/claude/koru-tokyo-reels/tools/chara/'; CL = '/home/claude/render/app/clips/'
dela = lambda n: ImageFont.truetype(F + 'DelaGothicOne-Regular.ttf', n)
dot = lambda n: ImageFont.truetype(F + 'DotGothic16-Regular.ttf', n)
zen = lambda n: ImageFont.truetype(F + 'ZenKakuGothicNew-Black.ttf', n)
INK = '#22303a'; RED = '#d7262e'; AMB = '#ffa22b'; LED = '#17110c'
W, H = 1080, 1920; PH = 1290; PW = round(780 * PH / 1688); PX = (W - PW) // 2; PY = 480
tmp = f'out/_{vid}'; os.makedirs(tmp, exist_ok=True)
def run(cmd): subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + cmd, check=True)
def dur(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]).decode())
def base(led='TOKYO FOOD TICKET MACHINE · 東京めし券売機'):
    bg = Image.new('RGB', (W, H), '#c9d2d7'); d = ImageDraw.Draw(bg)
    d.rounded_rectangle((40, 60, W - 40, 150), 16, fill=LED)
    d.text((W // 2, 106), led, font=dot(34), fill=AMB, anchor='mm')
    return bg
def caption(img, text, y0=250, y1=450):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((50, y0 + 6, W - 50, y1 + 6), 28, fill='#9aa6ae')
    d.rounded_rectangle((50, y0, W - 50, y1), 28, fill='#fbfcfc')
    d.rounded_rectangle((50, y0, W - 50, y0 + 22), 12, fill=RED); d.rectangle((50, y0 + 12, W - 50, y0 + 22), fill='#fbfcfc')
    lines = text.split('\n'); size = 74
    while max(d.textlength(l, font=dela(size)) for l in lines) > W - 160 or len(lines) * (size + 12) > (y1 - y0 - 50): size -= 2
    y = (y0 + 14 + y1) // 2 - (len(lines) * (size + 12)) // 2 + size // 2
    for l in lines: d.text((W // 2, y), l, font=dela(size), fill=INK, anchor='mm'); y += size + 12
tm = json.load(open(f'audio/{vid}_timing.json'))['sentences']
scenes = SCRIPTS[vid]['scenes']; parts = []
for i, (kind, src) in enumerate(SEG):
    s = tm[i]; nar = s['end'] - s['start']
    a0, a1 = max(0, s['start'] - .05), s['end'] + .12
    D = nar + (0.45 if i else 0.3)
    out = f'{tmp}/seg{i}.mp4'; aud = ['-ss', f'{a0:.3f}', '-t', f'{a1 - a0:.3f}', '-i', f'audio/{vid}.mp3']
    afil = f'[A]adelay=150|150,apad=whole_dur={D:.3f},atrim=0:{D:.3f}[aout]'
    if kind == 'screen':
        cd = dur(CL + src + '.mp4'); D = max(D, min(cd, nar + 1.4)); afil = f'[A]adelay=150|150,apad=whole_dur={D:.3f},atrim=0:{D:.3f}[aout]'
        bg = base(); caption(bg, scenes[i]['title']); dd = ImageDraw.Draw(bg)
        B = 16; dd.rounded_rectangle((PX - B, PY - B, PX + PW + B, PY + PH + B), 56, fill='#171e24')
        bg.save(f'{tmp}/bg{i}.png')
        m = Image.new('L', (PW, PH), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, PW - 1, PH - 1), 42, fill=255); m.save(f'{tmp}/mask.png')
        fc = (f'[1:v]scale={PW}:{PH}:flags=lanczos,fps=30,tpad=stop_mode=clone:stop_duration=10,trim=0:{D:.3f},setpts=PTS-STARTPTS[sc];'
              f'[3:v]format=gray[mk];[sc][mk]alphamerge[scm];[0:v][scm]overlay={PX}:{PY}[v];[2:a]anull[A];' + afil)
        run(['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/bg{i}.png', '-i', CL + src + '.mp4'] + aud + ['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/mask.png',
             '-filter_complex', fc.replace('[2:a]', '[2:a]'), '-map', '[v]', '-map', '[aout]', '-t', f'{D:.3f}', '-r', '30',
             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-ar', '44100', '-b:a', '160k', out])
    elif kind == 'pain':
        bg = base('よくある失敗 · COMMON TRAPS'); caption(bg, scenes[i]['title']); bg.save(f'{tmp}/bg{i}.png')
        cards = [('定休日', 'CLOSED TODAY', 'You walked 20 min for nothing'), ('現金のみ', 'CASH ONLY', 'And your card is all you have'), ('何て言う？', 'WHAT DO I SAY?', 'Ticket machine, menu, staff...')]
        for k, (ja, en, sub) in enumerate(cards):
            c = Image.new('RGBA', (W, 340), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
            d.rounded_rectangle((70, 30, W - 70, 310), 30, fill='#fbfcfc', outline='#aeb9c0', width=4)
            d.text((120, 120), ja, font=dela(64), fill=INK, anchor='lm'); d.text((122, 220), sub, font=zen(36), fill='#5d6b75', anchor='lm')
            st = Image.new('RGBA', (520, 150), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
            fs = 64
            while sd.textlength(en, font=dela(fs)) > 440: fs -= 2
            sd.rounded_rectangle((8, 8, 512, 142), 18, outline=RED, width=10); sd.text((260, 75), en, font=dela(fs), fill=RED, anchor='mm')
            st = st.rotate(-8, expand=True, resample=Image.BICUBIC); c.alpha_composite(st, (W - 70 - st.width + 10, 170 - st.height // 2)); c.save(f'{tmp}/card{k}.png')
        t = [0.15, 1.35, 2.65]
        fc = '[0:v]null[v0];'
        for k in range(3):
            fc += f"[{1 + k}:v]format=rgba,fade=in:st={t[k]}:d=0.18:alpha=1[c{k}];[v{k}][c{k}]overlay=0:{560 + k * 360}:enable='gte(t,{t[k]})'[v{k + 1}];"
        fc += '[4:a]anull[A];' + afil
        ins = ['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/bg{i}.png'] + sum([['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/card{k}.png'] for k in range(3)], [])
        run(ins + aud + ['-filter_complex', fc, '-map', '[v3]', '-map', '[aout]', '-t', f'{D:.3f}', '-r', '30', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-ar', '44100', '-b:a', '160k', out])
    elif kind == 'chara':
        bg = base('作ってる人 · WHO MADE THIS'); caption(bg, scenes[i]['title'], 250, 400)
        d = ImageDraw.Draw(bg); d.ellipse((90, 520, 990, 1420), fill='#ffd089'); d.ellipse((150, 580, 930, 1360), fill=AMB)
        d.text((W // 2, 1640), 'Akihabara office worker + his dog', font=zen(44), fill=INK, anchor='mm')
        bg.save(f'{tmp}/bg{i}.png')
        yu = Image.open(CH + 'yu_wave.png'); yu = yu.resize((int(yu.width * 1100 / yu.height), 1100), Image.LANCZOS); yu.save(f'{tmp}/yu.png')
        for nm in ('koru_smile_t', 'koru_happy_t'):
            k = Image.open(CH + nm + '.png'); k = k.resize((470, int(k.height * 470 / k.width)), Image.LANCZOS); k.save(f'{tmp}/{nm}.png')
        kh = Image.open(f'{tmp}/koru_happy_t.png').height
        sw = 2.0  # "this is Koru" moment
        yb = 1540 - kh
        fc = (f"[1:v]format=rgba[yu];[0:v][yu]overlay=150:'480+8*sin(t*3)'[v1];"
              f"[2:v]format=rgba[k0];[v1][k0]overlay=580:{yb}:enable='lt(t,{sw})'[v2];"
              f"[3:v]format=rgba[k1];[v2][k1]overlay=580:'{yb}-abs(sin((t-{sw})*7))*40':enable='gte(t,{sw})'[v3];[4:a]anull[A];" + afil)
        run(['-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/bg{i}.png', '-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/yu.png',
             '-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/koru_smile_t.png', '-loop', '1', '-t', f'{D:.3f}', '-i', f'{tmp}/koru_happy_t.png'] + aud +
            ['-filter_complex', fc, '-map', '[v3]', '-map', '[aout]', '-t', f'{D:.3f}', '-r', '30', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-c:a', 'aac', '-ar', '44100', '-b:a', '160k', out])
    parts.append(out); print(i, kind, src, round(D, 2))
open(f'{tmp}/list.txt', 'w').write(''.join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(['-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k', '-movflags', '+faststart', f'out/{vid}.mp4'])
print(f'out/{vid}.mp4', dur(f'out/{vid}.mp4'))
