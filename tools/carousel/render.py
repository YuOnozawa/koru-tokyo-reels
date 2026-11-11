"""KORU · Tokyo Field Notes — carousel pages in the style of a Japanese city magazine (design D, Yu 2026-11-12).

  python tools/carousel/render.py tools/carousel/specs/c_03_domannaka.json

Why this look: Japanese city/catalog magazines sell abroad to readers who can't read Japanese, because the
pages work visually: big Japanese headline, small English, many items per page, each with price and place.
Japanese leads, English supports. Bold gothic (Noto Sans CJK JP) + Archivo. Paper, ink, one red, one yellow.

Writes site/carousels/<id>/NN.jpg (1080x1350) and site/carousels/<id>/zoom.json — the boxes of every element
marked class "z" (with data-cap) per page, which tools/carousel/reel.py uses to make the slow reel.

Slide types (fields):
  cover    photo, pos?, jp ("[...]" = yellow), en, lines:[[jp,en]], sticker?:[top,bottom]
  catalog  kicker, jp, en, sub?, items:[{photo,pos?,jp,en,note?}], info:[[KEY,jp,en]]   (3-6 items)
  list     kicker, jp, en, items:[{jp,en,area,badge?,facts:[[KEY,text]]}], note?          (photo-less shops)
  rules    kicker, jp, en, items:[{jp,en,stat?,do}]                                        (up to 8)
  phrase   kicker?, jp, romaji, meaning, note?
  back     jp, en, checks:[[jp,en]], note?
"""
import html, json, os, re, sys, tempfile
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONTS = os.path.join(ROOT, 'tools/carousel/fonts')
W, H = 1080, 1350
PAPER, INK, RED, YEL, MUTE = '#F7F5F0', '#111111', '#E8382F', '#FFD23F', '#55514A'

CSS = f"""
@font-face{{font-family:Arc;src:url('file://{FONTS}/Archivo.ttf');font-weight:100 900;font-stretch:62% 125%}}
*{{box-sizing:border-box;margin:0}} body{{width:{W}px;height:{H}px;overflow:hidden;background:{PAPER}}}
.s{{width:{W}px;height:{H}px;position:relative;overflow:hidden;color:{INK}}}
.g{{font-family:'Noto Sans CJK JP';font-weight:900}} .gm{{font-family:'Noto Sans CJK JP';font-weight:700}} .gr{{font-family:'Noto Sans CJK JP';font-weight:500}}
.a{{font-family:Arc}} .ph{{background-size:cover;background-position:center}}
.k{{font-family:Arc;font-weight:800;letter-spacing:.22em;font-size:20px}}
.y{{color:{YEL}}}
"""


def e(s):
    return html.escape(str(s))


def jp(s):  # "[word]" -> yellow highlight, "\n" -> line break
    return re.sub(r'\[(.+?)\]', r'<span class="y">\1</span>', e(s)).replace('\n', '<br>')


def img(path):
    return 'file://' + os.path.join(ROOT, path)


def head(spec, kicker, title_jp, title_en, sub=''):
    return f"""<div style="display:flex;justify-content:space-between;align-items:flex-end;border-bottom:6px solid {INK};padding-bottom:12px">
<div><div class="k">{e(kicker)}</div><div class="g" style="font-size:62px;line-height:1.08;margin-top:4px">{jp(title_jp)}</div></div>
<div style="text-align:right"><div class="a" style="font-weight:900;font-stretch:125%;font-size:44px;line-height:1">KORU</div>
<div class="a" style="font-weight:700;font-size:16px;letter-spacing:.12em;margin-top:6px">{e(spec['issue'])}</div></div></div>
<div class="a" style="font-weight:700;font-size:24px;margin-top:10px;letter-spacing:.02em">{e(title_en.upper())}{(' — ' + e(sub)) if sub else ''}</div>"""


def folio(i, n, left='KORU · TOKYO FIELD NOTES'):
    return (f'<div class="a" style="position:absolute;left:44px;right:44px;bottom:22px;display:flex;justify-content:space-between;'
            f'font-weight:700;font-size:15px;letter-spacing:.14em;color:{MUTE}"><span>{e(left)}</span><span>{i:02d} / {n:02d}</span></div>')


def info_table(rows):
    cells = ''.join(f'<div style="padding:14px 16px;{"border-left:3px solid " + INK + ";" if i else ""}"><div class="a" style="font-weight:800;font-size:17px;letter-spacing:.15em;color:{RED}">{e(k)}</div>'
                    f'<div class="gm" style="font-size:23px;line-height:1.3;margin-top:4px">{e(j)}</div><div class="a" style="font-size:18px;font-weight:600;margin-top:2px">{e(en)}</div></div>'
                    for i, (k, j, en) in enumerate(rows))
    return f'<div class="z" data-cap="{e(" · ".join(r[2] for r in rows))}" style="border:3px solid {INK};display:grid;grid-template-columns:repeat({len(rows)},1fr);background:{PAPER}">{cells}</div>'


def cover(s, spec, i, n):
    lines = ''.join(f'<div style="margin-bottom:26px"><div class="gm" style="font-size:31px;line-height:1.35">{jp(a)}</div>'
                    f'<div class="a" style="font-size:21px;font-weight:600;margin-top:6px">{e(b)}</div></div>' for a, b in s.get('lines', []))
    st = s.get('sticker')
    sticker = (f'<div style="position:absolute;right:44px;bottom:150px;width:150px;height:150px;border-radius:50%;background:{RED};color:#fff;'
               f'display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);text-align:center">'
               f'<div class="g" style="font-size:34px;line-height:1.1">{e(st[0])}</div><div class="gm" style="font-size:22px;margin-top:4px">{e(st[1])}</div></div>') if st else ''
    bgl = (f"<div class='ph' style=\"position:absolute;inset:0;background-image:url('{img(s['photo'])}');background-position:{s.get('pos','center')}\"></div>" if s.get('photo') else
           f"<div style='position:absolute;inset:0;background:{s.get('bg', RED)}'></div><div class='g' style='position:absolute;right:-40px;top:250px;font-size:{s.get('big_size',900)}px;line-height:.8;color:rgba(255,255,255,.14)'>{e(s.get('big',''))}</div>")
    return f"""<div class="s">{bgl}
<div style="position:absolute;left:0;right:0;top:0;height:420px;background:linear-gradient(180deg,rgba(0,0,0,.45),rgba(0,0,0,0))"></div>
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(0deg,rgba(0,0,0,.78),rgba(0,0,0,0))"></div>
<div class="a" style="position:absolute;left:36px;top:18px;font-weight:900;font-stretch:125%;font-size:215px;line-height:.8;color:#fff;letter-spacing:-.02em">KORU</div>
<div class="a" style="position:absolute;right:40px;top:40px;text-align:right;color:#fff;font-weight:700;font-size:22px;line-height:1.3">{e(spec['issue'])}<br>{e(spec.get('month','NOV 2026'))}<br><span class="gm" style="font-size:20px">{e(spec.get('month_jp','2026年11月号'))}</span></div>
<div class="a" style="position:absolute;left:44px;top:205px;color:#fff;font-weight:600;font-size:22px;letter-spacing:.3em">TOKYO FIELD NOTES FOR HUNGRY TRAVELERS</div>
<div style="position:absolute;left:44px;top:300px;width:{s.get('lines_w',360)}px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.6)">{lines}</div>
{sticker}
<div class="g" style="position:absolute;left:44px;bottom:150px;right:220px;color:#fff;font-size:{s.get('jp_size',128)}px;line-height:1.04;letter-spacing:-.02em;text-shadow:0 4px 24px rgba(0,0,0,.35)">{jp(s['jp'])}</div>
<div class="a" style="position:absolute;left:46px;bottom:72px;right:44px;color:#fff;font-weight:800;font-stretch:75%;font-size:{s.get('en_size',56)}px;letter-spacing:.01em">{e(s['en'].upper())}</div>
</div>"""


def catalog(s, spec, i, n):
    items = s['items']; cols = 3 if len(items) in (3, 5, 6) else 2
    ph_h = 640 if len(items) == 3 else ({3: 330, 2: 380}[cols] if len(items) > 2 else 600)
    cells = ''.join(f"""<div class="z" data-cap="{e(str(k+1) + '. ' + it['en'])}" style="display:flex;flex-direction:column">
<div class="ph" style="height:{ph_h}px;background-image:url('{img(it['photo'])}');background-position:{it.get('pos','center')};border:1px solid {INK}"></div>
<div style="display:flex;gap:10px;align-items:baseline;margin-top:10px"><span class="g" style="font-size:32px;color:{RED}">{'①②③④⑤⑥⑦⑧⑨'[k]}</span><span class="g" style="font-size:32px;line-height:1.15">{e(it['jp'])}</span></div>
<div class="a" style="font-weight:700;font-size:22px;letter-spacing:.02em;margin-top:2px">{e(it['en'].upper())}</div>
<div class="gr" style="font-size:20px;color:#444;margin-top:2px">{e(it.get('note',''))}</div></div>""" for k, it in enumerate(items))
    info = f'<div style="position:absolute;left:44px;right:44px;bottom:56px">{info_table(s["info"])}</div>' if s.get('info') else ''
    return f"""<div class="s" style="padding:44px 44px">{head(spec, s['kicker'], s['jp'], s['en'], s.get('sub',''))}
<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:24px 20px;margin-top:22px">{cells}</div>{info}{folio(i, n)}</div>"""


def lst(s, spec, i, n):
    rows = ''.join(f"""<div class="z" data-cap="{e(str(k+1) + '. ' + it['en'] + ((' — ' + it['cap']) if it.get('cap') else ''))}" style="display:grid;grid-template-columns:70px 1fr 330px;gap:18px;padding:18px 0;border-top:2px solid {INK}">
<div class="g" style="font-size:52px;line-height:1;color:{RED}">{k+1}</div>
<div><div class="g" style="font-size:40px;line-height:1.15">{e(it['jp'])}</div>
<div class="a" style="font-weight:800;font-size:24px;margin-top:4px">{e(it['en'].upper())}</div>
<div class="gr" style="font-size:19px;color:{MUTE};margin-top:4px">{e(it.get('area',''))}</div>
{f'<div class="a" style="display:inline-block;margin-top:10px;background:{INK};color:#fff;font-weight:700;font-size:16px;letter-spacing:.08em;padding:6px 10px">{e(it["badge"])}</div>' if it.get('badge') else ''}</div>
<div style="font-size:21px;line-height:1.35">{''.join(f'<div style="display:flex;gap:10px;margin-bottom:6px"><span class="a" style="font-weight:800;font-size:15px;letter-spacing:.12em;color:{RED};width:84px;flex-shrink:0;padding-top:3px">{e(a)}</span><span class="a" style="font-weight:600">{e(b)}</span></div>' for a, b in it.get('facts', []))}</div>
</div>""" for k, it in enumerate(s['items']))
    note = f'<div class="gr" style="position:absolute;left:44px;right:44px;bottom:56px;font-size:18px;color:{MUTE}">{e(s["note"])}</div>' if s.get('note') else ''
    return f"""<div class="s" style="padding:44px 44px">{head(spec, s['kicker'], s['jp'], s['en'], s.get('sub',''))}
<div style="margin-top:18px;border-bottom:2px solid {INK}">{rows}</div>{note}{folio(i, n)}</div>"""


def rules(s, spec, i, n):
    boxes = ''.join(f"""<div class="z" data-cap="{e(str(k+1) + '. ' + it['en'])}" style="border:3px solid {INK};padding:18px 20px;background:#fff;display:flex;flex-direction:column">
<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="g" style="font-size:44px;color:{RED};line-height:1">{k+1}</span>
<span class="a" style="font-weight:800;font-size:30px;color:{RED}">{e(it.get('stat',''))}</span></div>
<div class="g" style="font-size:38px;line-height:1.15;margin-top:8px">{e(it['jp'])}</div>
<div class="a" style="font-weight:800;font-size:23px;line-height:1.15;margin-top:6px">{e(it['en'].upper())}</div>
<div class="a" style="font-weight:500;font-size:{s.get('do_size',19)}px;line-height:1.3;margin-top:auto;padding-top:8px;color:#333">{e(it.get('do',''))}</div></div>""" for k, it in enumerate(s['items']))
    return f"""<div class="s" style="padding:44px 44px">{head(spec, s['kicker'], s['jp'], s['en'], s.get('sub',''))}
<div style="display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:16px;margin-top:20px;height:{s.get('grid_h',1030)}px">{boxes}</div>{folio(i, n)}</div>"""


def phrase(s, spec, i, n):
    return f"""<div class="s" style="background:{INK};color:#fff;padding:44px">
<div style="display:flex;justify-content:space-between"><div class="k" style="color:{YEL}">{e(s.get('kicker','SAY THIS'))}</div><div class="a" style="font-weight:900;font-stretch:125%;font-size:44px">KORU</div></div>
<div class="z" data-cap="{e(s['romaji'] + ' = ' + s['meaning'])}" style="position:absolute;left:44px;right:44px;top:440px">
<div class="g" style="font-size:{s.get('jp_size',150)}px;line-height:1.08;color:{YEL}">{jp(s['jp'])}</div>
<div class="a" style="font-weight:800;font-size:64px;margin-top:30px">{e(s['romaji'].upper())}</div>
<div class="a" style="font-weight:500;font-size:44px;margin-top:10px">= {e(s['meaning'])}</div>
<div class="a" style="font-weight:500;font-size:30px;line-height:1.35;margin-top:44px;color:#CFCAC0;max-width:880px">{e(s.get('note',''))}</div></div>
<div class="a" style="position:absolute;left:44px;right:44px;bottom:22px;display:flex;justify-content:space-between;font-weight:700;font-size:15px;letter-spacing:.14em;color:#8C877E"><span>KORU · TOKYO FIELD NOTES</span><span>{i:02d} / {n:02d}</span></div></div>"""


def back(s, spec, i, n):
    checks = ''.join(f'<div style="display:flex;gap:18px;padding:18px 0;border-top:2px solid {INK}"><div style="width:40px;height:40px;border:3px solid {INK};flex-shrink:0;margin-top:4px"></div>'
                     f'<div><div class="g" style="font-size:34px;line-height:1.2">{e(a)}</div><div class="a" style="font-weight:600;font-size:23px;margin-top:2px">{e(b)}</div></div></div>' for a, b in s['checks'])
    return f"""<div class="s" style="padding:44px">
<div style="display:flex;justify-content:space-between;align-items:flex-start"><div style="background:{RED};color:#fff;padding:14px 22px" class="g"><span style="font-size:44px">保存版</span></div>
<div class="a" style="font-weight:900;font-stretch:125%;font-size:44px">KORU</div></div>
<div class="g" style="font-size:{s.get('jp_size',78)}px;line-height:1.1;margin-top:40px">{jp(s['jp'])}</div>
<div class="a" style="font-weight:800;font-size:30px;margin-top:10px">{e(s['en'].upper())}</div>
<div style="margin-top:34px;border-bottom:2px solid {INK}">{checks}</div>
{f'<div class="ph" style="position:absolute;left:44px;right:44px;bottom:150px;height:{s.get("photo_h",300)}px;background-image:url({chr(39)}{img(s["photo"])}{chr(39)});background-position:{s.get("pos","center")};border:1px solid {INK}"></div>' if s.get('photo') else ''}
<div style="position:absolute;left:44px;right:44px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end">
<div><div class="a" style="font-weight:800;font-size:20px;letter-spacing:.2em">KORU &amp; YU</div><div class="gr" style="font-size:20px;margin-top:4px">{e(s.get('note','Checked by a local office worker in Akihabara'))}</div></div></div>
{folio(i, n)}</div>"""


# ---- schematic East Tokyo map (not to scale). Pins sit next to the shop's station; no shop coordinates needed.
STATIONS = {  # name -> (jp, lat, lon)
 'Ueno': ('上野', 35.7138, 139.7773), 'Okachimachi': ('御徒町', 35.7075, 139.7748), 'Yushima': ('湯島', 35.7076, 139.7698),
 'Suehirocho': ('末広町', 35.7026, 139.7716), 'Akihabara': ('秋葉原', 35.6984, 139.7731), 'Kanda': ('神田', 35.6918, 139.7709),
 'Awajicho': ('淡路町', 35.6955, 139.7676), 'Ochanomizu': ('御茶ノ水', 35.6995, 139.7650), 'Jimbocho': ('神保町', 35.6960, 139.7577),
 'Asakusabashi': ('浅草橋', 35.6970, 139.7865), 'Kuramae': ('蔵前', 35.7035, 139.7907), 'Asakusa': ('浅草', 35.7110, 139.7964),
 'Tawaramachi': ('田原町', 35.7097, 139.7905), 'Shin-Okachimachi': ('新御徒町', 35.7069, 139.7820), 'Iwamotocho': ('岩本町', 35.6955, 139.7759)}
LINES = [(['Kanda', 'Akihabara', 'Okachimachi', 'Ueno'], '#7FB23A', 12, ''), (['Ochanomizu', 'Akihabara', 'Asakusabashi'], '#F2C200', 10, ''),
         (['Ueno', 'Suehirocho', 'Kanda'], '#F39700', 8, 'stroke-dasharray="2 14"'), (['Asakusabashi', 'Kuramae', 'Asakusa'], '#E85298', 8, 'stroke-dasharray="2 14"'),
         (['Asakusa', 'Tawaramachi', 'Ueno'], '#F39700', 8, 'stroke-dasharray="2 14"'), (['Jimbocho', 'Awajicho'], '#6CBB5A', 8, 'stroke-dasharray="2 14"')]


def smap(s, spec, i, n):
    pins = s['pins']; used = {p['station'] for p in pins} | set(s.get('stations', []))
    pts = [STATIONS[k] for k in used]
    la0, la1 = min(p[1] for p in pts) - .004, max(p[1] for p in pts) + .004
    lo0, lo1 = min(p[2] for p in pts) - .006, max(p[2] for p in pts) + .006
    top, bot = 240, 1350 - 90 - 62 * len(pins) - 60
    sc = min(960 / (lo1 - lo0) / 0.81, (bot - top) / (la1 - la0))  # keep lon/lat aspect (cos 35.7 deg ~ .81)
    cxm, cym = 540, (top + bot) / 2; mlo, mla = (lo0 + lo1) / 2, (la0 + la1) / 2
    X = lambda lo: cxm + (lo - mlo) * sc * 0.81
    Y = lambda la: cym - (la - mla) * sc
    svg = ''
    for names, col, w, dash in LINES:
        ok = [k for k in names if k in used]
        if len(ok) >= 2:
            svg += f'<polyline points="{" ".join(f"{X(STATIONS[k][2]):.0f},{Y(STATIONS[k][1]):.0f}" for k in ok)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" {dash}/>'
    river = f'<path d="M {X(139.8015):.0f} {Y(35.725):.0f} C {X(139.8000):.0f} {Y(35.706):.0f}, {X(139.7950):.0f} {Y(35.699):.0f}, {X(139.7935):.0f} {Y(35.680):.0f}" stroke="#9CC9E8" stroke-width="40" fill="none"/>'
    kanda = f'<path d="M {X(139.750):.0f} {Y(35.7000):.0f} C {X(139.7700):.0f} {Y(35.6985):.0f}, {X(139.7820):.0f} {Y(35.6965):.0f}, {X(139.7935):.0f} {Y(35.6955):.0f}" stroke="#9CC9E8" stroke-width="20" fill="none"/>'
    left = set(s.get('label_left', []))
    st = ''
    for k in used:
        j, la, lo = STATIONS[k]; side = f'right:{1080 - X(lo) + 14:.0f}px' if k in left else f'left:{X(lo) + 14:.0f}px'
        st += (f'<div style="position:absolute;left:{X(lo) - 8:.0f}px;top:{Y(la) - 8:.0f}px;width:16px;height:16px;background:#fff;border:4px solid {INK};border-radius:50%"></div>'
               f'<div class="gm" style="position:absolute;{side};top:{Y(la) - 17:.0f}px;font-size:21px;white-space:nowrap">{j}<span class="a" style="font-size:15px;font-weight:700;margin-left:6px">{k.upper()}</span></div>')
    pn = ''; seen = {}
    for k, p in enumerate(pins, 1):
        j, la, lo = STATIONS[p['station']]; m = seen.get(p['station'], 0); seen[p['station']] = m + 1
        dx, dy = p.get('dx', -40 + 46 * m), p.get('dy', -64)
        x, y = X(lo) + dx, Y(la) + dy
        pn += (f'<div style="position:absolute;left:{x - 26:.0f}px;top:{y:.0f}px;width:52px;height:52px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:{RED};border:3px solid {INK}"></div>'
               f'<div class="g" style="position:absolute;left:{x - 26:.0f}px;top:{y + 4:.0f}px;width:52px;text-align:center;font-size:28px;color:#fff">{k}</div>')
    legend = ''.join(f'<div class="z" data-cap="{e(str(k) + ". " + p["en"] + " — " + p.get("walk", ""))}" style="display:flex;gap:12px;align-items:baseline;padding:10px 0;border-top:2px solid {INK}">'
                     f'<span class="g" style="color:{RED};font-size:28px;width:28px">{k}</span><span class="g" style="font-size:27px">{e(p["jp"])}</span>'
                     f'<span class="a" style="font-weight:700;font-size:18px">{e(p["en"].upper())}</span><span class="a" style="margin-left:auto;font-weight:700;font-size:19px">{e(p.get("walk", ""))}</span></div>'
                     for k, p in enumerate(pins, 1))
    return f"""<div class="s" style="background:#EFEADF"><svg width="1080" height="1350" style="position:absolute;left:0;top:0">{river}{kanda}{svg}</svg>{st}{pn}
<div style="position:absolute;left:0;right:0;top:0;background:{PAPER};padding:40px 44px 14px;border-bottom:6px solid {INK}">
<div class="k">{e(s.get('kicker', 'MAP · NOT TO SCALE'))}</div>
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div class="g" style="font-size:60px;line-height:1.1">{jp(s['jp'])}</div><div class="a" style="font-weight:900;font-stretch:125%;font-size:44px">KORU</div></div></div>
<div style="position:absolute;left:44px;right:44px;bottom:56px;background:{PAPER};border:3px solid {INK};padding:6px 20px 0">{legend}</div>{folio(i, n)}</div>"""



def voices(s, spec, i, n):
    """What diners love: positive-first summary of reviews in our own words, with how many reviews it is based on."""
    rows = ''.join(f"""<div class="z" data-cap="{e(it['en'] + ': ' + it['loved_en'])}" style="display:grid;grid-template-columns:1fr 300px;gap:20px;padding:16px 0;border-top:2px solid {INK}">
<div><div style="display:flex;gap:12px;align-items:baseline"><span class="g" style="font-size:34px">{e(it['jp'])}</span><span class="a" style="font-weight:800;font-size:19px">{e(it['en'].upper())}</span></div>
<div class="a" style="font-weight:600;font-size:22px;line-height:1.35;margin-top:6px">{e(it['praise'])}</div></div>
<div style="background:{YEL};padding:12px 14px;align-self:start"><div class="a" style="font-weight:800;font-size:14px;letter-spacing:.15em">MOST LOVED</div>
<div class="g" style="font-size:26px;line-height:1.2;margin-top:4px">{e(it['loved_jp'])}</div><div class="a" style="font-weight:700;font-size:17px;margin-top:2px">{e(it['loved_en'])}</div>
<div class="a" style="font-weight:600;font-size:14px;color:{MUTE};margin-top:6px">{e(it.get('basis',''))}</div></div></div>""" for it in s['items'])
    note = f'<div class="gr" style="position:absolute;left:44px;right:44px;bottom:56px;font-size:17px;color:{MUTE}">{e(s["note"])}</div>' if s.get('note') else ''
    return f"""<div class="s" style="padding:44px 44px">{head(spec, s['kicker'], s['jp'], s['en'], s.get('sub',''))}
<div style="margin-top:16px;border-bottom:2px solid {INK}">{rows}</div>{note}{folio(i, n)}</div>"""


KINDS = dict(voices=voices, map=smap, cover=cover, catalog=catalog, list=lst, rules=rules, phrase=phrase, back=back)


def render(spec_path):
    spec = json.load(open(spec_path, encoding='utf-8'))
    out = os.path.join(ROOT, 'site/carousels', spec['id']); os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    n = len(spec['slides']); files = []; zoom = []
    with sync_playwright() as p, tempfile.TemporaryDirectory() as td:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        for i, s in enumerate(spec['slides'], 1):
            doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{KINDS[s["type"]](s, spec, i, n)}</body></html>'
            hp = os.path.join(td, f'{i}.html'); open(hp, 'w', encoding='utf-8').write(doc)
            pg.goto('file://' + hp); pg.wait_for_timeout(400)
            boxes = pg.evaluate("""[...document.querySelectorAll('.z')].map(el=>{const r=el.getBoundingClientRect();
                return {x:r.x,y:r.y,w:r.width,h:r.height,cap:el.dataset.cap||''}})""")
            over = pg.evaluate("document.querySelector('.s').scrollHeight > 1350 || document.querySelector('.s').scrollWidth > 1080")
            if over:
                print(f'WARNING page {i}: content overflows the page', file=sys.stderr)
            f = os.path.join(out, f'{i:02d}.jpg'); pg.screenshot(path=f, type='jpeg', quality=90)
            files.append(os.path.relpath(f, os.path.join(ROOT, 'site')))
            zoom.append({'page': f'{i:02d}.jpg', 'type': s['type'], 'caption': s.get('reel_cap', s.get('en', '')), 'boxes': boxes})
        b.close()
    json.dump({'id': spec['id'], 'reel': spec.get('reel', {}), 'pages': zoom}, open(os.path.join(out, 'zoom.json'), 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(files))
    return files


if __name__ == '__main__':
    for a in sys.argv[1:]:
        render(a)
