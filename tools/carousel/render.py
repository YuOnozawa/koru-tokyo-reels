"""Render a magazine-style Instagram carousel ("KORU · Tokyo Field Notes") from a JSON spec.

  python tools/carousel/render.py tools/carousel/specs/c_01_tenkaippin.json

Writes site/carousels/<id>/01.jpg ... (1080x1350, 4:5) so GitHub Pages can serve them to the
Instagram API. Slide types: cover_photo, cover_type, photo, list, phrase, end.
"""
import html, json, os, sys, tempfile
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONTS = os.path.join(ROOT, 'tools/carousel/fonts')
W, H = 1080, 1350

C = dict(paper='#F3EADB', ink='#141824', night='#0B1020', accent='#C2410C', glow='#FF7A3D',
         mute='#6B6253', rule='#C9BEA8', soft='#3A3428')

CSS = f"""
@font-face{{font-family:Fraunces;src:url('file://{FONTS}/Fraunces.ttf');font-style:normal;font-weight:100 900}}
@font-face{{font-family:Fraunces;src:url('file://{FONTS}/Fraunces-Italic.ttf');font-style:italic;font-weight:100 900}}
*{{box-sizing:border-box}} body{{margin:0;width:{W}px;height:{H}px;overflow:hidden}}
.s{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:Inter,sans-serif;display:flex;flex-direction:column}}
.serif{{font-family:Fraunces,Georgia,serif}} .jp{{font-family:'Noto Serif CJK JP',serif;font-weight:900}}
.mast{{display:flex;justify-content:space-between;align-items:center;font-size:17px;letter-spacing:4px;font-weight:600}}
.logo{{font-family:Fraunces,serif;font-weight:800;font-size:30px;letter-spacing:1px}}
.foot{{display:flex;justify-content:space-between;align-items:center;font-size:16px;letter-spacing:1px}}
"""


def e(s):
    return html.escape(str(s))


def img(path):
    return 'file://' + os.path.join(ROOT, path)


def mast(dark, issue, label):
    col = C['paper'] if dark else C['ink']
    sub = '#B9B2A2' if dark else C['mute']
    return (f'<div class="mast" style="color:{sub}"><div style="display:flex;gap:18px;align-items:baseline">'
            f'<span class="logo" style="color:{col}">KORU</span><span>TOKYO FIELD NOTES</span></div>'
            f'<div>{e(issue)}{" · " + e(label) if label else ""}</div></div>')


def foot(dark, i, n, note=''):
    sub = '#B9B2A2' if dark else C['mute']
    return (f'<div class="foot" style="color:{sub}"><div>{e(note)}</div>'
            f'<div class="serif" style="font-size:22px;color:{C["paper"] if dark else C["ink"]}">{i:02d} / {n:02d}</div></div>')


def cover_photo(s, spec, i, n):
    pos = s.get('pos', 'center')
    return f"""<div class="s" style="background:{C['night']};color:{C['paper']}">
<div style="position:absolute;inset:0;background:url('{img(s['photo'])}') {pos}/cover"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,16,32,.78) 0%,rgba(11,16,32,0) 22%,rgba(11,16,32,0) 42%,rgba(11,16,32,.92) 74%,rgba(11,16,32,1) 100%)"></div>
<div style="position:relative;padding:52px 64px 0">{mast(True, spec['issue'], spec.get('label'))}</div>
<div style="position:relative;margin-top:auto;padding:0 64px 52px">
<div style="font-size:19px;letter-spacing:5px;color:{C['glow']};font-weight:600">{e(s.get('kicker',''))}</div>
<div class="serif" style="font-weight:700;font-size:{s.get('size',112)}px;line-height:.95;letter-spacing:-2px;margin-top:14px">{e(s['title'])}</div>
<div class="serif" style="font-style:italic;font-size:32px;line-height:1.35;margin-top:22px;color:#E4DCCB;max-width:900px">{e(s.get('dek',''))}</div>
<div style="height:1px;background:#3A4260;margin:34px 0 18px"></div>{foot(True, i, n, s.get('note','Swipe →'))}</div></div>"""


def cover_type(s, spec, i, n):
    stats = ''.join(f'<div style="display:flex;flex-direction:column;gap:6px"><div class="serif" style="font-weight:600;font-size:66px;line-height:1;color:{C["glow"]}">{e(a)}</div><div style="font-size:24px;line-height:1.35">{e(b)}</div></div>' for a, b in s.get('stats', []))
    return f"""<div class="s" style="background:{C['night']};color:{C['paper']};padding:52px 64px">{tower(-60, 560, 470, .38)}
<div style="position:relative;display:flex;flex-direction:column;flex:1">
{mast(True, spec['issue'], spec.get('label'))}
<div style="font-size:19px;letter-spacing:5px;color:{C['glow']};font-weight:600;margin-top:120px">{e(s.get('kicker',''))}</div>
<div class="serif" style="font-weight:700;font-size:{s.get('size',150)}px;line-height:.92;letter-spacing:-4px;margin-top:16px">{e(s['title'])}</div>
<div class="serif" style="font-style:italic;font-size:34px;line-height:1.35;margin-top:26px;color:#E4DCCB">{e(s.get('dek',''))}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px 56px;margin-top:70px">{stats}</div>
<div style="margin-top:auto;border-top:1px solid #3A4260;padding-top:18px">{foot(True, i, n, s.get('note','Swipe →'))}</div></div></div>"""


def photo(s, spec, i, n):
    facts = ''.join(f'<div style="display:flex;gap:18px;padding:13px 0;border-top:1px solid {C["rule"]};font-size:23px;line-height:1.4"><div style="width:130px;flex-shrink:0;font-size:15px;letter-spacing:3px;font-weight:600;color:{C["accent"]};padding-top:5px">{e(k)}</div><div>{e(v)}</div></div>' for k, v in s.get('facts', []))
    jp = f'<div class="jp" style="position:absolute;right:30px;top:30px;writing-mode:vertical-rl;font-size:54px;color:rgba(243,234,219,.92);text-shadow:0 2px 16px rgba(0,0,0,.5)">{e(s["jp"])}</div>' if s.get('jp') else ''
    return f"""<div class="s" style="background:{C['paper']};color:{C['ink']}">
<div style="position:relative;height:{s.get('h',700)}px;background:url('{img(s['photo'])}') {s.get('pos','center')}/cover">{jp}
<div style="position:absolute;left:64px;bottom:-34px;background:{C['accent']};color:#fff;font-family:Fraunces,serif;font-weight:700;font-size:40px;width:68px;height:68px;display:flex;align-items:center;justify-content:center">{e(s.get('num',i-1))}</div></div>
<div style="padding:62px 64px 46px;display:flex;flex-direction:column;flex:1">
<div class="serif" style="font-weight:700;font-size:{s.get('size',60)}px;line-height:1.02;letter-spacing:-1px">{e(s['title'])}</div>
<div class="serif" style="font-style:italic;font-size:27px;line-height:1.4;color:{C['soft']};margin-top:14px">{e(s.get('body',''))}</div>
<div style="margin-top:18px">{facts}</div>
<div style="margin-top:auto">{foot(False, i, n, s.get('note',''))}</div></div></div>"""


def lst(s, spec, i, n):
    rows = ''.join(f'<div style="display:flex;gap:26px;padding:{s.get('pad',30)}px 0;border-top:1px solid {C["rule"]}"><div class="serif" style="font-weight:600;font-size:60px;color:{C["accent"]};width:165px;flex-shrink:0;line-height:1">{e(a)}</div><div style="display:flex;flex-direction:column;gap:8px"><div class="serif" style="font-weight:600;font-size:40px;line-height:1.1">{e(b)}</div><div style="font-size:24px;line-height:1.45;color:#4A4436">{e(c)}</div></div></div>' for a, b, c in s['items'])
    return f"""<div class="s" style="background:{C['paper']};color:{C['ink']};padding:52px 64px 46px">
{mast(False, spec['issue'], spec.get('label'))}
<div style="font-size:18px;letter-spacing:5px;color:{C['accent']};font-weight:600;margin-top:46px">{e(s.get('kicker',''))}</div>
<div class="serif" style="font-weight:700;font-size:{s.get('size',76)}px;line-height:1;letter-spacing:-1.5px;margin-top:10px">{e(s['title'])}</div>
<div style="margin-top:30px;border-bottom:1px solid {C['rule']}">{rows}</div>
<div class="jp" style="margin-top:auto;text-align:right;font-size:120px;letter-spacing:10px;color:#E2D6BF;line-height:1">{e(s.get('stamp',''))}</div>
<div style="margin-top:20px">{foot(False, i, n, s.get('note',''))}</div></div>"""


def phrase(s, spec, i, n):
    return f"""<div class="s" style="background:{C['night']};color:{C['paper']};padding:52px 64px 46px">{tower(-70, 600, 400, .30)}
<div style="position:relative;display:flex;flex-direction:column;flex:1">
{mast(True, spec['issue'], spec.get('label'))}
<div style="font-size:19px;letter-spacing:5px;color:{C['glow']};font-weight:600;margin-top:190px">{e(s.get('kicker','SAY THIS'))}</div>
<div class="jp" style="font-size:{s.get('size',112)}px;line-height:1.15;margin-top:26px;color:{C['glow']}">{e(s['jp'])}</div>
<div class="serif" style="font-style:italic;font-size:56px;margin-top:22px">{e(s['romaji'])}</div>
<div style="font-size:36px;margin-top:14px;color:#E4DCCB">= {e(s['meaning'])}</div>
<div style="font-size:30px;line-height:1.5;margin-top:60px;color:#CFC7B6;max-width:640px">{e(s.get('body',''))}</div>
<div style="margin-top:auto;border-top:1px solid #3A4260;padding-top:18px">{foot(True, i, n, s.get('note',''))}</div></div></div>"""


def end(s, spec, i, n):
    lines = ''.join(f'<div style="padding:22px 0;border-top:1px solid #3A4260;font-size:31px;line-height:1.35;max-width:720px">{e(x)}</div>' for x in s.get('lines', []))
    return f"""<div class="s" style="background:{C['night']};color:{C['paper']};padding:52px 64px 46px">{tower(-80, 640, 380, .28)}
<div style="position:relative;display:flex;flex-direction:column;flex:1">
{mast(True, spec['issue'], spec.get('label'))}
<div class="serif" style="font-weight:700;font-size:{s.get('size',96)}px;line-height:.98;letter-spacing:-2px;margin-top:150px">{e(s['title'])}</div>
<div class="serif" style="font-style:italic;font-size:32px;line-height:1.4;margin-top:24px;color:#E4DCCB">{e(s.get('dek',''))}</div>
<div style="margin-top:60px;border-bottom:1px solid #3A4260">{lines}</div>
<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end">
<div><div style="font-size:20px;font-weight:600;letter-spacing:3px">KORU &amp; YU</div><div style="font-size:18px;color:#B9B2A2;margin-top:4px">{e(s.get('sign','Checked by a local office worker in Akihabara'))}</div></div>
<div class="serif" style="font-size:22px">{i:02d} / {n:02d}</div></div></div></div>"""


TOWER = open(os.path.join(ROOT, 'tools/carousel/tower.svg')).read()


def tower(right=-40, top=520, w=430, op=.55):
    """Original lattice-tower line drawing (brand mark for dark pages)."""
    return (f'<div aria-hidden="true" style="position:absolute;right:{right}px;top:{top}px;width:{w}px;height:{int(w*910/360)}px;'
            f'color:{C["glow"]};opacity:{op};filter:drop-shadow(0 0 14px {C["glow"]})">{TOWER.replace("<svg ", "<svg style=\"width:100%;height:100%\" ")}</div>')


KINDS = dict(cover_photo=cover_photo, cover_type=cover_type, photo=photo, list=lst, phrase=phrase, end=end)


def render(spec_path):
    spec = json.load(open(spec_path, encoding='utf-8'))
    out = os.path.join(ROOT, 'site/carousels', spec['id']); os.makedirs(out, exist_ok=True)
    n = len(spec['slides']); files = []
    with sync_playwright() as p, tempfile.TemporaryDirectory() as td:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        for i, s in enumerate(spec['slides'], 1):
            doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{KINDS[s["type"]](s, spec, i, n)}</body></html>'
            hp = os.path.join(td, f'{i}.html'); open(hp, 'w', encoding='utf-8').write(doc)
            pg.goto('file://' + hp); pg.wait_for_timeout(300)
            f = os.path.join(out, f'{i:02d}.jpg'); pg.screenshot(path=f, type='jpeg', quality=90)
            files.append(os.path.relpath(f, os.path.join(ROOT, 'site')))
        b.close()
    print(json.dumps(files))
    return files


if __name__ == '__main__':
    for a in sys.argv[1:]:
        render(a)
