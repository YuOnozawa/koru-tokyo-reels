"""Render a magazine-style Instagram carousel ("KORU · Tokyo Field Notes") from a JSON spec.

  python tools/carousel/render.py tools/carousel/specs/c_03_domannaka.json

Design B (Yu picked 2026-11-12): a Japanese food magazine. Full-bleed photos, vertical Mincho headlines,
red KORU stamp, English in Instrument Serif, small caps in Archivo. Text pages sit on washi-cream paper.
Writes site/carousels/<id>/01.jpg ... (1080x1350, 4:5) for GitHub Pages -> Instagram API.

Slide types:
  cover      {photo, pos?, jp, en, en_i?, kicker?}       full-bleed photo, vertical JP headline
  photo      {photo, pos?, num, jp, en, body?, meta?}    full-bleed photo + caption card
  cover_type {jp, en, en_i?, kicker?, stats?, note?}     paper cover without a photo
  entry      {num, jp, en, kicker, body, badge?, facts}  guide entry without a photo
  phrase     {jp, romaji, meaning, body?}                a line to say, vertical
  end        {jp?, en, lines, photo?}                    save-this page
"""
import html, json, os, sys, tempfile
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONTS = os.path.join(ROOT, 'tools/carousel/fonts')
W, H = 1080, 1350
RED, PAPER, INK, MUTE = '#C8102E', '#F6F1E7', '#151515', '#6E675C'

CSS = f"""
@font-face{{font-family:IS;src:url('file://{FONTS}/InstrumentSerif-Regular.ttf')}}
@font-face{{font-family:IS;font-style:italic;src:url('file://{FONTS}/InstrumentSerif-Italic.ttf')}}
@font-face{{font-family:Bod;src:url('file://{FONTS}/BodoniModa.ttf');font-weight:400 900}}
@font-face{{font-family:SM;src:url('file://{FONTS}/ShipporiMincho-Bold.ttf');font-weight:700}}
@font-face{{font-family:SM;src:url('file://{FONTS}/ShipporiMincho-Regular.ttf');font-weight:400}}
@font-face{{font-family:Arc;src:url('file://{FONTS}/Archivo.ttf');font-weight:100 900}}
*{{box-sizing:border-box;margin:0}} body{{width:{W}px;height:{H}px;overflow:hidden}}
.s{{width:{W}px;height:{H}px;position:relative;overflow:hidden}}
.ph{{position:absolute;inset:0;background-size:cover;background-position:center}}
.cap{{font-family:Arc;font-weight:600;letter-spacing:.18em;text-transform:uppercase}}
.jp{{font-family:SM;font-weight:700}} .en{{font-family:IS}}
.v{{writing-mode:vertical-rl}}
.stamp{{width:116px;height:116px;background:{RED};color:#fff;display:flex;align-items:center;justify-content:center;font-family:Bod;font-weight:800;font-size:33px;letter-spacing:.04em}}
"""


def e(s):
    return html.escape(str(s))


def br(s):  # allow "\n" line breaks in headlines
    return e(s).replace('\n', '<br>')


def img(path):
    return 'file://' + os.path.join(ROOT, path)


def stamp(top=60, left=60):
    return f'<div class="stamp" style="position:absolute;left:{left}px;top:{top}px">KORU</div>'


def pager(i, n, color='#fff', shadow=True):
    sh = 'text-shadow:0 1px 10px rgba(0,0,0,.5);' if shadow else ''
    return f'<div class="cap" style="position:absolute;right:60px;bottom:44px;font-size:18px;color:{color};{sh}">{i:02d} / {n:02d}</div>'


def cover(s, spec, i, n):
    en_i = f'<br><i>{e(s["en_i"])}</i>' if s.get('en_i') else ''
    return f"""<div class="s"><div class="ph" style="background-image:url('{img(s['photo'])}');background-position:{s.get('pos','center')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,0) 50%,rgba(0,0,0,.38) 100%),linear-gradient(0deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 38%)"></div>
{stamp()}
<div class="jp v" style="position:absolute;right:60px;top:66px;font-size:{s.get('jp_size',96)}px;color:#fff;letter-spacing:.12em;line-height:1.25;text-shadow:0 2px 20px rgba(0,0,0,.5);max-height:1000px">{br(s['jp'])}</div>
<div style="position:absolute;left:60px;bottom:70px;right:380px;color:#fff;text-shadow:0 2px 16px rgba(0,0,0,.6)">
<div class="cap" style="font-size:20px">{e(s.get('kicker', 'Tokyo Field Notes ' + spec['issue']))}</div>
<div class="en" style="font-size:{s.get('en_size',78)}px;line-height:1;margin-top:12px">{br(s['en'])}{en_i}</div></div>
<div class="cap" style="position:absolute;right:60px;bottom:44px;font-size:18px;color:#fff;text-shadow:0 1px 10px rgba(0,0,0,.5)">Swipe →</div></div>"""


def photo(s, spec, i, n):
    body = f'<div class="en" style="font-size:{s.get("body_size",44)}px;line-height:1.15;margin-top:10px">{e(s["body"])}</div>' if s.get('body') else ''
    meta = f'<div class="cap" style="font-size:19px;color:{MUTE};margin-top:22px;line-height:1.5">{e(s["meta"])}</div>' if s.get('meta') else ''
    return f"""<div class="s"><div class="ph" style="background-image:url('{img(s['photo'])}');background-position:{s.get('pos','center')}"></div>
<div class="cap" style="position:absolute;right:60px;top:56px;font-size:18px;color:#fff;text-shadow:0 1px 10px rgba(0,0,0,.55)">{i:02d} / {n:02d}</div>
<div style="position:absolute;left:48px;right:48px;bottom:48px;background:{PAPER};padding:38px 44px 36px;border-radius:4px;color:{INK}">
<div style="display:flex;justify-content:space-between;align-items:baseline;gap:20px"><div class="jp" style="font-size:{s.get('jp_size',58)}px;line-height:1.1">{e(s['jp'])}</div>
<div class="cap" style="font-size:20px;color:{RED};white-space:nowrap">{e(s.get('num',''))} · {e(s['en'])}</div></div>
{body}{meta}</div></div>"""


def cover_type(s, spec, i, n):
    en_i = f'<br><i>{e(s["en_i"])}</i>' if s.get('en_i') else ''
    stats = ''.join(f'<div style="border-top:1.5px solid {INK};padding-top:14px"><div class="en" style="font-size:72px;line-height:1;color:{RED}">{e(a)}</div><div style="font-family:IS;font-size:38px;line-height:1.15;margin-top:8px">{e(b)}</div></div>' for a, b in s.get('stats', []))
    return f"""<div class="s" style="background:{PAPER};color:{INK}">{stamp()}
<div class="jp v" style="position:absolute;right:64px;top:64px;font-size:{s.get('jp_size',104)}px;letter-spacing:.12em;line-height:1.3;max-height:1040px">{br(s['jp'])}</div>
<div style="position:absolute;left:60px;top:250px;width:{s.get('col',640)}px">
<div class="cap" style="font-size:20px;color:{RED}">{e(s.get('kicker', 'Tokyo Field Notes ' + spec['issue']))}</div>
<div class="en" style="font-size:{s.get('en_size',112)}px;line-height:.95;margin-top:18px">{br(s['en'])}{en_i}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:44px 36px;margin-top:80px">{stats}</div></div>
<div class="cap" style="position:absolute;left:60px;bottom:44px;font-size:18px;color:{MUTE}">{e(s.get('note','Swipe →'))}</div>
{pager(i, n, MUTE, False)}</div>"""


def entry(s, spec, i, n):
    facts = ''.join(f'<div style="display:flex;gap:22px;padding:22px 0;border-top:1px solid #CFC5B3"><div class="cap" style="width:120px;flex-shrink:0;font-size:18px;color:{RED};padding-top:12px">{e(k)}</div><div style="font-family:IS;font-size:42px;line-height:1.15">{e(v)}</div></div>' for k, v in s.get('facts', []))
    badge = f'<div class="cap" style="display:inline-block;margin-top:26px;border:2px solid {INK};padding:12px 18px;font-size:20px">{e(s["badge"])}</div>' if s.get('badge') else ''
    return f"""<div class="s" style="background:{PAPER};color:{INK}">
<div class="jp v" style="position:absolute;right:56px;top:60px;font-size:{s.get('jp_size',112)}px;letter-spacing:.1em;line-height:1.2;max-height:1180px">{e(s['jp'])}</div>
<div style="position:absolute;left:60px;top:60px;width:{s.get('col',760)}px">
<div style="display:flex;gap:18px;align-items:center"><div style="width:64px;height:64px;background:{RED};color:#fff;font-family:IS;font-size:44px;display:flex;align-items:center;justify-content:center">{e(s['num'])}</div>
<div class="cap" style="font-size:18px;color:{MUTE}">{e(s.get('kicker',''))}</div></div>
<div class="en" style="font-size:{s.get('en_size',112)}px;line-height:.95;margin-top:40px">{br(s['en'])}</div>
<div class="en" style="font-style:italic;font-size:46px;line-height:1.2;color:#3D3830;margin-top:18px">{e(s.get('body',''))}</div>
{badge}
<div style="margin-top:34px;border-bottom:1px solid #CFC5B3">{facts}</div></div>
<div class="jp" style="position:absolute;left:52px;bottom:84px;font-size:230px;line-height:1;color:#E9DFCC">{e(s.get('kanji',''))}</div>
<div class="cap" style="position:absolute;left:60px;bottom:44px;font-size:17px;color:{MUTE}">{e(s.get('note','KORU · Tokyo Field Notes ' + spec['issue']))}</div>
{pager(i, n, MUTE, False)}</div>"""


def phrase(s, spec, i, n):
    return f"""<div class="s" style="background:{INK};color:{PAPER}">{stamp()}
<div class="jp v" style="position:absolute;right:90px;top:90px;font-size:{s.get('jp_size',120)}px;letter-spacing:.14em;line-height:1.3;color:#fff;max-height:1100px">{br(s['jp'])}</div>
<div style="position:absolute;left:60px;bottom:110px;width:{s.get('col',600)}px">
<div class="cap" style="font-size:20px;color:#E8A0A8">{e(s.get('kicker','Say this'))}</div>
<div class="en" style="font-style:italic;font-size:70px;line-height:1;margin-top:18px">{e(s['romaji'])}</div>
<div class="en" style="font-size:46px;margin-top:14px;color:#E9E2D4">= {e(s['meaning'])}</div>
<div class="en" style="font-size:36px;line-height:1.25;margin-top:34px;color:#BDB6A8">{e(s.get('body',''))}</div></div>
{pager(i, n, '#9C9588', False)}</div>"""


def end(s, spec, i, n):
    lines = ''.join(f'<div style="padding:20px 0;border-top:1px solid rgba(255,255,255,.35);font-family:IS;font-size:40px;line-height:1.2">{e(x)}</div>' for x in s.get('lines', []))
    bg = (f"<div class='ph' style=\"background-image:url('{img(s['photo'])}');background-position:{s.get('pos','center')}\"></div>"
          f"<div style='position:absolute;inset:0;background:rgba(12,10,8,.72)'></div>") if s.get('photo') else ''
    return f"""<div class="s" style="background:{INK};color:#fff">{bg}{stamp()}
<div class="jp v" style="position:absolute;right:64px;top:64px;font-size:{s.get('jp_size',88)}px;letter-spacing:.14em;line-height:1.3">{br(s.get('jp','保存版'))}</div>
<div style="position:absolute;left:60px;top:250px;width:{s.get('col',720)}px">
<div class="en" style="font-size:{s.get('en_size',84)}px;line-height:.98">{br(s['en'])}</div>
<div style="margin-top:44px;border-bottom:1px solid rgba(255,255,255,.35)">{lines}</div></div>
<div style="position:absolute;left:60px;bottom:44px"><div class="cap" style="font-size:19px">Koru &amp; Yu</div><div class="en" style="font-size:28px;color:#D9D2C4;margin-top:4px">{e(s.get('sign','Checked by a local office worker in Akihabara'))}</div></div>
{pager(i, n, '#D9D2C4', False)}</div>"""


KINDS = dict(cover=cover, photo=photo, cover_type=cover_type, entry=entry, phrase=phrase, end=end)


def render(spec_path):
    spec = json.load(open(spec_path, encoding='utf-8'))
    out = os.path.join(ROOT, 'site/carousels', spec['id']); os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        os.remove(os.path.join(out, f))
    n = len(spec['slides']); files = []
    with sync_playwright() as p, tempfile.TemporaryDirectory() as td:
        b = p.chromium.launch(); pg = b.new_page(viewport={'width': W, 'height': H})
        for i, s in enumerate(spec['slides'], 1):
            doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{KINDS[s["type"]](s, spec, i, n)}</body></html>'
            hp = os.path.join(td, f'{i}.html'); open(hp, 'w', encoding='utf-8').write(doc)
            pg.goto('file://' + hp); pg.wait_for_timeout(400)
            f = os.path.join(out, f'{i:02d}.jpg'); pg.screenshot(path=f, type='jpeg', quality=90)
            files.append(os.path.relpath(f, os.path.join(ROOT, 'site')))
        b.close()
    print(json.dumps(files))
    return files


if __name__ == '__main__':
    for a in sys.argv[1:]:
        render(a)
