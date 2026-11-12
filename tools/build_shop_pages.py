#!/usr/bin/env python3
"""Build static SEO pages for every shop in data/shops.json.

Writes site/shops/index.html, site/shops/<slug>/index.html, site/sitemap.xml, site/robots.txt.
Facts only from shops.json; fields marked 'unknown' are skipped. No photos, no review text, no ratings.
Run: python3 tools/build_shop_pages.py
"""
import html, json, os, re, shutil, unicodedata
from collections import OrderedDict
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sitenav import NAV_CSS, nav, phrase_for  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://yuonozawa.github.io/koru-tokyo-reels'
OUT = os.path.join(ROOT, 'site', 'shops')

AREA_ORDER = ['Akihabara', 'Suehirocho', 'Kanda', 'Jimbocho', 'Ochanomizu', 'Ueno', 'Okachimachi', 'Yushima', 'Asakusa', 'Kuramae']
AREA_JA = {'Akihabara': '秋葉原', 'Suehirocho': '末広町', 'Kanda': '神田', 'Jimbocho': '神保町', 'Ochanomizu': '御茶ノ水',
           'Ueno': '上野', 'Okachimachi': '御徒町', 'Yushima': '湯島', 'Asakusa': '浅草', 'Kuramae': '蔵前'}
GROUP = {'Akihabara': 'akiba', 'Suehirocho': 'akiba', 'Ueno': 'ueno', 'Okachimachi': 'ueno', 'Yushima': 'ueno',
         'Asakusa': 'asakusa', 'Kuramae': 'asakusa', 'Kanda': 'kanda', 'Jimbocho': 'kanda', 'Ochanomizu': 'kanda'}
BUDGET = {'under1500': ('¥', 'Under ¥1,500'), '1500-4000': ('¥¥', '¥1,500–4,000'),
          '4000-10000': ('¥¥¥', '¥4,000–10,000'), '10000plus': ('¥¥¥¥', '¥10,000+')}
TODAY_FIELD = 'checked'


def e(s):
    return html.escape(str(s), quote=True)


def known(v):
    if v is None:
        return False
    if isinstance(v, (list, tuple)):
        return len(v) > 0
    s = str(v).strip()
    return s != '' and s.lower() not in ('unknown', 'n/a', 'none listed')


def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s or 'shop'


def yen(v):
    if not known(v):
        return None
    v = str(v).strip()
    if v.lower().startswith('n/a'):
        return None
    if v.lower().startswith('no '):
        return v[0].upper() + v[1:]
    # put a yen sign before the first number and thousands separators on 4+ digit numbers
    v = re.sub(r'(?<![\d,])(\d{4,})(?! prices)', lambda m: '{:,}'.format(int(m.group(1))), v)
    return re.sub(r'^(\D*?)(?=\d)', lambda m: m.group(1) + ('' if m.group(1).endswith('¥') else '¥'), v, count=1)


def human_date(d):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', d or '')
    if not m:
        return d or 'UNKNOWN'
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return '%s %d, %s' % (months[int(m.group(2)) - 1], int(m.group(3)), m.group(1))


FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@800;900&family=Noto+Sans+JP:wght@900&family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap" rel="stylesheet">')

CSS = """
.rules{margin:12px 0;padding:10px 12px;border-radius:8px;background:#fff;border:1.5px solid #e2dccb}
.rules-k{font:13px "Archivo","Noto Sans JP",monospace;color:var(--red);letter-spacing:.06em}
.rules ul{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:4px}
.rules li{display:flex;gap:8px;font-weight:700;font-size:15px}
.report{font-size:13px;color:var(--muted);margin:8px 0 0}
.report a{color:var(--red)}
.say{display:grid;gap:2px;margin:14px 0 0;padding:14px 16px;border-radius:12px;background:#17110c;color:#ffa22b;text-decoration:none;box-shadow:inset 0 0 0 3px #000}
.say-k{font:13px "Archivo","Noto Sans JP",monospace;opacity:.85}
.say b{font:900 24px/1.3 "Zen Kaku Gothic New",sans-serif;color:#ffd27a}
.say-r{font:15px "Archivo","Noto Sans JP",monospace}
.say-more{font:700 13px "Zen Kaku Gothic New",sans-serif;color:#fff;margin-top:4px}

:root{--steel:#22272e;--steel2:#2d333b;--edge:#444c56;--amber:#ffa22b;--amber-dim:#7a4a0c;--paper:#fbf8ee;--ink:#22303a;--muted:#6f7287;--red:#d7262e;--green:#2f8f5b}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:#15191e;color:#e9e6dc;font:16px/1.6 'Zen Kaku Gothic New',system-ui,sans-serif}
a{color:inherit}
.wrap{max-width:640px;margin:0 auto;padding:16px}
.machine{background:linear-gradient(180deg,var(--steel2),var(--steel));border:1px solid var(--edge);border-radius:18px;padding:14px;box-shadow:0 10px 30px rgba(0,0,0,.45),inset 0 1px 0 rgba(255,255,255,.06)}
.marquee{background:#0d0905;border:2px solid #000;border-radius:10px;padding:10px 12px;font-family:'Archivo','Noto Sans JP',monospace;color:var(--amber);text-shadow:0 0 6px rgba(255,162,43,.65);letter-spacing:.06em;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.marquee b{font-weight:400;color:#ffd08a}
.crumbs{font-size:13px;color:#9aa3ad;margin:12px 2px 0}
.crumbs a{color:#c9d1d9}
.ticket{position:relative;background:var(--paper);color:var(--ink);border-radius:10px;margin-top:14px;padding:18px 16px 16px;
 -webkit-mask:radial-gradient(circle 7px at 0 50%,transparent 6.5px,#000 7px) left/51% 100% no-repeat,radial-gradient(circle 7px at 100% 50%,transparent 6.5px,#000 7px) right/51% 100% no-repeat;
 mask:radial-gradient(circle 7px at 0 50%,transparent 6.5px,#000 7px) left/51% 100% no-repeat,radial-gradient(circle 7px at 100% 50%,transparent 6.5px,#000 7px) right/51% 100% no-repeat}
.ticket .kicker{font-family:'Archivo','Noto Sans JP',monospace;color:var(--muted);font-size:13px;letter-spacing:.08em}
h1{font-family:'Noto Sans JP',sans-serif;font-weight:400;font-size:clamp(24px,7vw,34px);line-height:1.2;margin:4px 0 2px;overflow-wrap:anywhere}
.ja{font-size:18px;color:var(--muted);font-weight:700}
.genre{margin-top:6px;font-weight:700}
.stamp{position:absolute;top:14px;right:14px;width:62px;height:62px;border:3px solid var(--red);border-radius:50%;color:var(--red);display:flex;align-items:center;justify-content:center;text-align:center;font:400 12px/1.05 'Noto Sans JP',sans-serif;transform:rotate(-12deg);opacity:.9}
.has-stamp h1,.has-stamp .kicker,.has-stamp .ja{padding-right:70px}
.perf{border-top:2px dashed #c9c6ba;margin:14px -16px}
dl{margin:0;display:grid;grid-template-columns:96px 1fr;gap:8px 12px}
dt{font-family:'Archivo','Noto Sans JP',monospace;color:var(--muted);font-size:13px;padding-top:2px}
dd{margin:0;overflow-wrap:anywhere}
.order{background:#fff3d9;border-left:4px solid var(--amber);padding:10px 12px;border-radius:6px;font-weight:700}
.tip{background:#eef6f0;border-left:4px solid var(--green);padding:10px 12px;border-radius:6px}
.note{font-size:13px;color:var(--muted);margin-top:12px}
.btns{display:grid;gap:10px;margin-top:16px}
.btn{display:block;text-align:center;text-decoration:none;border-radius:12px;padding:14px 12px;font-weight:700}
.btn.primary{background:linear-gradient(180deg,#ff4a52,var(--red));color:#fff;font-family:'Noto Sans JP',sans-serif;font-weight:400;font-size:18px;box-shadow:0 4px 0 #8f1218}
.btn.ghost{background:#2d333b;border:1px solid var(--edge);color:#e9e6dc}
h2{font-family:'Noto Sans JP',sans-serif;font-weight:400;font-size:20px;margin:26px 2px 10px;color:var(--amber)}
.list{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.list a{display:flex;justify-content:space-between;gap:10px;background:var(--paper);color:var(--ink);text-decoration:none;border-radius:8px;padding:10px 12px}
.list .n{font-weight:700;overflow-wrap:anywhere}
.list .m{color:var(--muted);font-size:13px;white-space:nowrap}
.pill{display:inline-block;font-size:11px;font-weight:700;color:var(--red);border:1.5px solid var(--red);border-radius:999px;padding:0 6px;margin-left:6px;vertical-align:2px}
.areas{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.areas a{font-size:13px;text-decoration:none;background:#0d0905;color:var(--amber);border:1px solid #000;border-radius:999px;padding:4px 10px;font-family:'Archivo','Noto Sans JP',monospace}
footer{font-size:13px;color:#9aa3ad;text-align:center;margin:28px 0 12px}
footer a{color:#c9d1d9}
"""


def page(title, desc, canonical, body, jsonld=None, og_type='website', prefix='../'):
    ld = ''
    if jsonld:
        ld = '<script type="application/ld+json">%s</script>' % json.dumps(jsonld, ensure_ascii=False).replace('</', '<\\/')
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><meta name="description" content="%s"><link rel="canonical" href="%s">'
            '<meta property="og:type" content="%s"><meta property="og:title" content="%s"><meta property="og:description" content="%s">'
            '<meta property="og:url" content="%s"><meta property="og:site_name" content="Tokyo Food Ticket Machine">'
            '<meta property="og:image" content="' + BASE + '/planner/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            '<meta name="twitter:card" content="summary_large_image"><link rel="manifest" href="' + prefix + 'manifest.webmanifest"><link rel="apple-touch-icon" href="' + prefix + 'apple-touch-icon.png">%s<style>%s</style>%s<link rel="stylesheet" href="' + prefix + 'koru.css"></head><body><div class="wrap">' + nav(prefix, 'shops') + '%s'
            '<footer>Facts only, no paid placement. Yu &amp; Koru · <a href="https://www.instagram.com/koru.tokyo_guide/">@koru.tokyo_guide</a>'
            ' · <a href="../privacy/">Privacy</a></footer></div></body></html>') % (
        e(title), e(desc), e(canonical), og_type, e(title), e(desc), e(canonical), FONTS, CSS + NAV_CSS, ld, body)


def fix_rel(s, depth):
    return s.replace('href="../privacy/"', 'href="%sprivacy/"' % ('../' * depth))


def say_html(s):
    ja, ro, en, anchor = phrase_for(s)
    return ('<a class="say" href="../../phrases/#%s"><span class="say-k">🗣 USEFUL HERE</span><b>%s</b>'
            '<span class="say-r">%s · %s</span><span class="say-more">More restaurant phrases →</span></a>') % (anchor, e(ja), e(ro), e(en))


def house_rules(s):
    """Short, scannable 'house rules' chips derived only from the facts we already store."""
    t = ' '.join(str(s.get(k) or '') for k in ('tourist_tip', 'what_to_order', 'hours')).lower()
    out = []
    def add(icon, label):
        if label not in [x[1] for x in out]:
            out.append((icon, label))
    if re.search(r'cash only|no credit cards|credit cards not accepted|cards not accepted|no cards|bring cash|not accept(ed)? cards', t):
        add('💴', 'Cash only' + (' (PayPay OK)' if re.search(r'paypay (is |are )?accepted|paypay ok|paypay and', t) and 'not accepted' not in t.split('paypay')[1][:20] else ''))
    elif re.search(r'cards? (and [^.]*)?accepted|visa|mastercard|amex|jcb', t):
        add('💳', 'Cards OK')
    if re.search(r'ticket (vending )?machine', t):
        add('🎫', 'Buy a meal ticket at the machine first')
    if re.search(r'pay before|order and pay before', t):
        add('💴', 'Pay before you eat')
    if re.search(r'no reservations|walk-in only|no online booking|reservations not', t) or s.get('reservation') == 'not_needed':
        add('🚶', 'No booking needed' if s.get('reservation') == 'not_needed' and 'no reservation' not in t else 'No reservations, just walk in')
    elif s.get('reservation') in ('recommended', 'required', 'needed'):
        add('📅', 'Book ahead')
    if re.search(r'sold out|sells out|runs out', t):
        add('⏰', 'Closes when sold out, go early')
    if re.search(r'\bqueue|\bline (can|often|forms)|long line|lines? form', t):
        add('⏳', 'Expect a line')
    if re.search(r'takeout only|no seats', t):
        add('🥡', 'Takeout only')
    if re.search(r'smoking allowed|smoking at all seats|smoking and non-smoking', t):
        add('🚬', 'Smoking allowed (check seats)')
    if re.search(r'children (are )?not allowed|not for children|under 12', t):
        add('🚸', 'Child policy: see the tip below')
    m = re.search(r'(\d{1,2}) (counter )?seats', t)
    if m and int(m.group(1)) <= 20:
        add('🪑', 'Small: %s seats' % m.group(1))
    if str(s.get('english_menu', '')).lower() == 'yes':
        add('🇬🇧', 'English menu')
    return out


def shop_page(s, slug, peers):
    area = s.get('area', '')
    bits = []
    if known(s.get('what_to_order')):
        bits.append('Order: ' + s['what_to_order'])
    if known(s.get('closed_days')):
        bits.append('Closed: ' + s['closed_days'])
    desc = '%s (%s), %s in %s. %s' % (s['name_en'], s['name_ja'], s.get('genre', ''), area, ' '.join(bits))
    desc = re.sub(r'\s+', ' ', desc).strip()
    if len(desc) > 158:
        desc = desc[:155].rsplit(' ', 1)[0] + '…'
    title = '%s (%s) – what to order, hours, closed days | Tokyo Food Ticket Machine' % (s['name_en'], s['name_ja'])
    canonical = '%s/shops/%s/' % (BASE, slug)
    maps = 'https://www.google.com/maps/search/?api=1&query=' + re.sub(r'\s', '+', html.escape(s['name_ja']))
    from urllib.parse import quote
    maps = 'https://www.google.com/maps/search/?api=1&query=' + quote(s['name_ja'])

    rows = []
    def row(k, v):
        if known(v):
            rows.append('<dt>%s</dt><dd>%s</dd>' % (e(k), e(v)))
    if known(s.get('station')):
        st = s['station']
        if known(s.get('walk_min')):
            st = '%s · %s min walk' % (st, s['walk_min'])
        row('STATION', st)
    row('HOURS', s.get('hours'))
    row('CLOSED', s.get('closed_days'))
    row('LUNCH', yen(s.get('lunch_price_yen')))
    row('DINNER', yen(s.get('dinner_price_yen')))
    if known(s.get('budget_band')) and s['budget_band'] in BUDGET:
        row('BUDGET', BUDGET[s['budget_band']][1])
    row('ENGLISH MENU', s.get('english_menu'))
    row('BOOKING', {'not_needed': 'Not needed', 'recommended': 'Recommended', 'required': 'Required'}.get(s.get('reservation'), s.get('reservation')))
    if known(s.get('awards')):
        rows.append('<dt>AWARDS</dt><dd>%s</dd>' % '<br>'.join(e(a) for a in s['awards']))

    stamp = '<div class="stamp">YU\'S<br>PICK</div>' if s.get('yu_pick') else ''
    order = '<p class="order">▶ %s</p>' % e(s['what_to_order']) if known(s.get('what_to_order')) else ''
    tip = '<p class="tip">💡 %s</p>' % e(s['tourist_tip']) if known(s.get('tourist_tip')) else ''
    hr = house_rules(s)
    if hr:
        order += ('<div class="rules"><div class="rules-k">HOUSE RULES · 入店ルール</div><ul>%s</ul></div>'
                  % ''.join('<li><span>%s</span>%s</li>' % (i, e(l)) for i, l in hr))
    tip += ('<p class="report">Something changed (closed, new hours, cash only)? '
            '<a href="https://ig.me/m/koru.tokyo_guide" target="_blank" rel="noopener">Tell us on Instagram</a> and we\'ll fix it.</p>')
    group = GROUP.get(area, '')
    plan_href = '../../planner/' + ('?a=' + group if group else '')
    peer_html = ''
    if peers:
        peer_html = '<h2>More in %s</h2><ul class="list">%s</ul>' % (e(area), ''.join(
            '<li><a href="../%s/"><span class="n">%s%s</span><span class="m">%s</span></a></li>' % (
                ps, e(p['name_en']), '<span class="pill">PICK</span>' if p.get('yu_pick') else '', e(p.get('genre', '')[:28]))
            for ps, p in peers))
    body = (
        '<div class="machine"><div class="marquee">WITH KORU ▸ <b>%s</b> ▸ %s</div>'
        '<nav class="crumbs"><a href="../../planner/">Planner</a> › <a href="../#%s">Shops</a> › %s</nav>'
        '<article class="ticket%s">%s<div class="kicker">食券 · %s %s</div><h1>%s</h1><div class="ja">%s</div><div class="genre">%s</div>'
        '<div class="perf"></div>%s<dl>%s</dl>%s'
        '<p class="note">Facts checked %s from public sources. Hours change, so check Google Maps the same day.</p></article>'
        + say_html(s) +
        '<div class="btns"><a class="btn primary" href="%s">Plan my Tokyo meals free 🎫</a>'
        '<a class="btn ghost" href="%s" target="_blank" rel="noopener">Open in Google Maps</a>'
        '<a class="btn ghost" href="https://www.instagram.com/koru.tokyo_guide/" target="_blank" rel="noopener">Follow @koru.tokyo_guide</a></div></div>%s'
    ) % (e(area.upper()), e(AREA_JA.get(area, '')), e(slugify(area)), e(s['name_en']),
         ' has-stamp' if s.get('yu_pick') else '', stamp, e(area), e(AREA_JA.get(area, '')),
         e(s['name_en']), e(s['name_ja']), e(s.get('genre', '')), order, ''.join(rows), tip,
         e(human_date(s.get(TODAY_FIELD))), e(plan_href), e(maps), peer_html)

    ld = OrderedDict([('@context', 'https://schema.org'), ('@type', 'Restaurant'), ('name', s['name_en']),
                      ('alternateName', s['name_ja']), ('url', canonical)])
    if known(s.get('genre')):
        ld['servesCuisine'] = s['genre']
    if s.get('budget_band') in BUDGET:
        ld['priceRange'] = BUDGET[s['budget_band']][0]
    addr = OrderedDict([('@type', 'PostalAddress'), ('addressLocality', area), ('addressRegion', 'Tokyo'), ('addressCountry', 'JP')])
    ld['address'] = addr
    if known(s.get('hours')):
        ld['description'] = 'Hours: %s' % s['hours'] + ('. Closed: %s' % s['closed_days'] if known(s.get('closed_days')) else '')
    ld['hasMap'] = maps
    return page(title, desc, canonical, body, ld, 'article', '../../')


def index_page(by_area, slugs):
    title = 'Tokyo food near Akihabara, Ueno, Asakusa & Kanda – %d shops, facts checked | Tokyo Food Ticket Machine' % sum(len(v) for v in by_area.values())
    desc = 'What to order, hours and closed days for %d restaurants and sweet shops around Akihabara, Kanda, Ueno, Yushima and Asakusa. Free meal planner included.' % sum(len(v) for v in by_area.values())
    chips = ''.join('<a href="#%s">%s %s</a>' % (slugify(a), e(a), e(AREA_JA.get(a, ''))) for a in by_area)
    secs = []
    for a, shops in by_area.items():
        secs.append('<h2 id="%s">%s <span style="color:#9aa3ad;font-size:15px">%s · %d</span></h2><ul class="list">%s</ul>' % (
            slugify(a), e(a), e(AREA_JA.get(a, '')), len(shops), ''.join(
                '<li><a href="%s/"><span class="n">%s%s</span><span class="m">%s</span></a></li>' % (
                    slugs[id(s)], e(s['name_en']), '<span class="pill">PICK</span>' if s.get('yu_pick') else '',
                    e(BUDGET.get(s.get('budget_band'), ('', ''))[1])) for s in shops)))
    body = ('<div class="machine"><div class="marquee">WITH KORU ▸ <b>FIELD NOTES</b> ▸ 食の手帖</div>'
            '<article class="ticket"><div class="kicker">食券 · SHOP LIST</div><h1>Where to eat around Akihabara, Ueno &amp; Asakusa</h1>'
            '<p style="margin:8px 0 0">Facts only: what to order, hours, closed days and how to pay. <b>PICK</b> = Yu\'s own picks.</p>'
            '<div class="areas">%s</div><p style="margin:10px 0 0"><a href="../find/">Open on Sunday, late night, breakfast, cards OK →</a></p></article>'
            '<div class="btns"><a class="btn primary" href="../planner/">Plan my Tokyo meals free 🎫</a></div></div>%s') % (chips, ''.join(secs))
    ld = {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Tokyo food shops',
          'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': '%s/shops/%s/' % (BASE, slugs[id(s)])}
                              for i, s in enumerate([s for v in by_area.values() for s in v])]}
    return page(title, desc, BASE + '/shops/', body, ld).replace('href="../privacy/"', 'href="../privacy/"')


def write_csv(S, root):
    """Public CSV of the shop DB (for the Google Sheet view via IMPORTDATA)."""
    import csv, io
    cols = ['name_en', 'name_ja', 'area', 'genre', 'station', 'walk_min', 'hours', 'closed_days', 'lunch_price_yen', 'dinner_price_yen',
            'budget_band', 'what_to_order', 'tourist_tip', 'yu_pick', 'awards', 'reservation', 'english_menu', 'checked', 'sources']
    out = io.StringIO(); w = csv.writer(out)
    w.writerow(cols + ['house_rules', 'page_url'])
    for s in S:
        w.writerow([('; '.join(s[c]) if isinstance(s.get(c), list) else s.get(c, '')) for c in cols]
                   + [' / '.join(l for _, l in house_rules(s)), '%s/shops/%s/' % (BASE, slugify(s['name_en']))])
    os.makedirs(os.path.join(root, 'data'), exist_ok=True)
    open(os.path.join(root, 'data', 'shops.csv'), 'w', encoding='utf-8').write(out.getvalue())


# ---------- search-intent pages: /find/<intent>-<area>/ (answers what travelers actually google) ----------
GROUP_NAME = OrderedDict([('akiba', ('Akihabara', 'Akihabara & Suehirocho')), ('ueno', ('Ueno', 'Ueno, Okachimachi & Yushima')),
                          ('asakusa', ('Asakusa', 'Asakusa & Kuramae')), ('kanda', ('Kanda', 'Kanda, Jimbocho & Ochanomizu')),
                          ('all', ('East Tokyo', 'Akihabara, Ueno, Asakusa & Kanda'))])

def _mins(h, m): return int(h) * 60 + int(m)
def first_open(s):
    m = re.search(r'(\d{1,2}):(\d{2})', s.get('hours') or ''); return _mins(*m.groups()) if m else None
def last_close(s):
    xs = re.findall(r'-\s*(\d{1,2}):(\d{2})', s.get('hours') or '')
    return max(_mins(a, b) + (1440 if int(a) < 6 else 0) for a, b in xs) if xs else None
def open_sunday(s):
    c = (s.get('closed_days') or '').lower(); h = (s.get('hours') or '').lower()
    if not known(s.get('closed_days')) and 'daily' not in h: return False
    if 'sunday' in c or re.search(r'\bsun\b', c): return False
    if 'sun' in h or 'daily' in h or 'every day' in h: return True
    return not re.search(r'\b(mon|tue|wed|thu|fri|sat|weekday)', h)
def rule_labels(s): return [l for _, l in house_rules(s)]
def cheap_lunch(s):
    v = str(s.get('lunch_price_yen') or '').lower()
    if 'under 1000' in v or 'up to 1000' in v: return True
    m = re.search(r'(\d{3,5})', v.replace(',', '')); return bool(m) and int(m.group(1)) <= 1000
INTENTS = [
    ('open-sunday', 'Restaurants open on Sunday', 'open on Sundays', open_sunday, 'Many small Tokyo shops close on Sundays. These list Sunday hours.'),
    ('late-night', 'Late-night food (open till 10pm+)', 'open until 10pm or later', lambda s: (last_close(s) or 0) >= 22 * 60, 'Places that list closing at 10pm or later. Last orders are usually 30-60 min before closing.'),
    ('breakfast', 'Breakfast spots (open by 9am)', 'open by 9am', lambda s: (first_open(s) or 999) <= 9 * 60, 'Most Tokyo restaurants open around 11. These open by 9am on at least some days.'),
    ('cards-ok', 'Restaurants that take cards', 'that take cards', lambda s: 'Cards OK' in rule_labels(s), 'Many small shops are cash only. These list card payment.'),
    ('cheap-lunch', 'Lunch under ¥1,000', 'with lunch under ¥1,000', cheap_lunch, 'Lunch at or under about ¥1,000, from listed prices. Prices change, check on the day.'),
    ('english-menu', 'Restaurants with an English menu', 'with an English menu', lambda s: str(s.get('english_menu')).lower() in ('true', 'yes'), 'Places listed as having an English menu.'),
    ('no-booking', 'Walk-in friendly: no booking needed', 'where you can just walk in', lambda s: 'No booking needed' in rule_labels(s), 'Places that list no reservations needed or taken, so you can just show up.'),
]

def intent_row(s, slug):
    bits = [e(s['area']) + ' · ' + e(s.get('genre') or '')]
    if known(s.get('hours')): bits.append('<b>Hours</b> ' + e(s['hours']))
    if known(s.get('closed_days')): bits.append('<b>Closed</b> ' + e(s['closed_days']))
    lp = yen(s.get('lunch_price_yen')); dp = yen(s.get('dinner_price_yen'))
    if lp or dp: bits.append('<b>Price</b> ' + ' / '.join(x for x in [('lunch ' + lp) if lp else '', ('dinner ' + dp) if dp else ''] if x))
    if known(s.get('what_to_order')): bits.append('<b>Order</b> ' + e(s['what_to_order'][:140]))
    return ('<li style="display:block;padding:12px 4px;border-bottom:1px dashed #d9cdb8"><a href="../../shops/%s/" style="font-weight:800">%s</a>%s'
            '<span style="color:#9aa3ad"> %s</span><div style="font-size:14px;line-height:1.5;margin-top:4px">%s</div></li>') % (
        slug, e(s['name_en']), '<span class="pill">PICK</span>' if s.get('yu_pick') else '', e(s.get('name_ja') or ''), '<br>'.join(bits))

def intent_pages(shops, slugs, root):
    out = os.path.join(root, 'site', 'find')
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(out); made = []
    import datetime as _dt
    _c = max(s.get('checked', '') for s in shops)[:7]; checked = _dt.date(int(_c[:4]), int(_c[5:7]), 1).strftime('%b %Y')
    for key, h1, phrase, fn, note in INTENTS:
        for g, (short, long_) in GROUP_NAME.items():
            lst = [s for s in shops if fn(s) and (g == 'all' or GROUP.get(s['area']) == g)]
            if len(lst) < 4 or (g == 'all' and key not in ('english-menu', 'breakfast', 'late-night', 'open-sunday', 'cards-ok')): continue
            lst.sort(key=lambda s: (not s.get('yu_pick'), AREA_ORDER.index(s['area']) if s['area'] in AREA_ORDER else 99, s['name_en'].lower()))
            slug = '%s-%s' % (key, 'east-tokyo' if g == 'all' else short.lower())
            near = 'in' if g == 'all' else 'near'
            title = '%s %s %s – %d places, checked %s | Tokyo Food Ticket Machine' % (h1, near, short, len(lst), checked)
            desc = '%d restaurants and cafes in %s %s, with hours, closed days, prices and what to order. Facts from public sources, free meal planner included.' % (len(lst), long_, phrase)
            other = ''.join('<a href="../%s-%s/">%s</a>' % (key, 'east-tokyo' if gg == 'all' else GROUP_NAME[gg][0].lower(), e(GROUP_NAME[gg][0]))
                            for gg in GROUP_NAME if gg != g)
            body = ('<div class="machine"><div class="marquee">WITH KORU ▸ <b>FIELD NOTES</b> ▸ 食の手帖</div>'
                    '<article class="ticket"><div class="kicker">食券 · %s</div><h1>%s %s %s</h1>'
                    '<p style="margin:8px 0 0">%d places in %s %s. %s Checked %s; hours change, so check Google Maps on the day. <b>PICK</b> = Yu\'s own picks.</p>'
                    '<div class="areas">%s</div></article>'
                    '<div class="btns"><a class="btn primary" href="../../planner/">Plan my Tokyo meals free 🎫</a></div></div>'
                    '<ul class="list" style="list-style:none;padding:0">%s</ul>'
                    '<div class="btns" style="margin-top:18px"><a class="btn primary" href="../../planner/">Plan lunch, sweets &amp; dinner that are all open 🎫</a></div>') % (
                e(h1.upper()), e(h1), near, e(short), len(lst), e(long_), e(phrase), e(note), e(checked), other, ''.join(intent_row(s, slugs[id(s)]) for s in lst))
            ld = {'@context': 'https://schema.org', '@type': 'ItemList', 'name': '%s %s %s' % (h1, near, short),
                  'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': '%s/shops/%s/' % (BASE, slugs[id(s)])} for i, s in enumerate(lst)]}
            d = os.path.join(out, slug); os.makedirs(d)
            open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(fix_rel(page(title, desc, '%s/find/%s/' % (BASE, slug), body, ld, prefix='../../'), 2))
            made.append((slug, h1, near + ' ' + short, len(lst)))
    links = ''.join('<li><a href="%s/"><span class="n">%s %s</span><span class="m">%d</span></a></li>' % (sl, e(h), e(sh), n) for sl, h, sh, n in made)
    body = ('<div class="machine"><div class="marquee">WITH KORU ▸ <b>FIELD NOTES</b> ▸ 食の手帖</div><article class="ticket"><div class="kicker">食券 · FIND</div>'
            '<h1>Find food in East Tokyo that is actually open</h1><p style="margin:8px 0 0">Sunday, late night, breakfast, cards, cheap lunch, English menu, walk-in. Facts only.</p></article>'
            '<div class="btns"><a class="btn primary" href="../planner/">Plan my Tokyo meals free 🎫</a></div></div><ul class="list">%s</ul>') % links
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page('Find open restaurants in Akihabara, Ueno, Asakusa & Kanda | Tokyo Food Ticket Machine',
        'Restaurants open on Sunday, late at night or for breakfast, that take cards or have English menus, around Akihabara, Ueno, Asakusa and Kanda.',
        BASE + '/find/', body))
    return ['find/'] + ['find/%s/' % m[0] for m in made]


def main():
    shops = json.load(open(os.path.join(ROOT, 'data', 'shops.json'), encoding='utf-8'))
    slugs, used = {}, set()
    for s in shops:
        base = slugify(s['name_en'])
        sl, n = base, 2
        while sl in used:
            sl = '%s-%d' % (base, n); n += 1
        used.add(sl); slugs[id(s)] = sl
    write_csv(shops, os.path.join(ROOT, 'site'))
    areas = [a for a in AREA_ORDER if any(s['area'] == a for s in shops)] + sorted({s['area'] for s in shops} - set(AREA_ORDER))
    by_area = OrderedDict()
    for a in areas:
        by_area[a] = sorted([s for s in shops if s['area'] == a], key=lambda s: (not s.get('yu_pick'), s['name_en'].lower()))

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for a, lst in by_area.items():
        for s in lst:
            others = [p for p in lst if p is not s]
            # prefer different genres first, then fill
            peers = sorted(others, key=lambda p: (p.get('genre') == s.get('genre'), not p.get('yu_pick'), p['name_en']))[:5]
            if len(peers) < 3:  # pad from same planner group
                grp = [p for p in shops if GROUP.get(p['area']) == GROUP.get(a) and p is not s and p not in peers]
                peers += grp[:3 - len(peers)]
            d = os.path.join(OUT, slugs[id(s)])
            os.makedirs(d)
            with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(fix_rel(shop_page(s, slugs[id(s)], [(slugs[id(p)], p) for p in peers]), 2))
    with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_page(by_area, slugs))

    # keep the shop count on the home page in sync
    hub = os.path.join(ROOT, 'site', 'index.html')
    if os.path.exists(hub):
        h = open(hub, encoding='utf-8').read()
        open(hub, 'w', encoding='utf-8').write(re.sub(r'\b\d+ shops', '%d shops' % len(shops), h))

    # planner data: same facts plus the page slug (used for share links and "shop page" links)
    with open(os.path.join(ROOT, 'site', 'planner', 'shops.json'), 'w', encoding='utf-8') as f:
        json.dump([dict(s, slug=slugs[id(s)]) for s in shops], f, ensure_ascii=False)

    find_urls = intent_pages(shops, slugs, ROOT)
    lastmod = max(s.get('checked', '') for s in shops) or None
    urls = ['', 'planner/', 'phrases/', 'tips/', 'privacy/', 'shops/'] + ['shops/%s/' % slugs[id(s)] for v in by_area.values() for s in v] + find_urls
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append('  <url><loc>%s/%s</loc>%s</url>' % (BASE, u, '<lastmod>%s</lastmod>' % lastmod if lastmod and u.startswith(('shops', 'find')) else ''))
    sm.append('</urlset>')
    open(os.path.join(ROOT, 'site', 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
    open(os.path.join(ROOT, 'site', 'robots.txt'), 'w').write('User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n' % BASE)
    print('pages:', len(shops), 'index + sitemap urls:', len(urls))


if __name__ == '__main__':
    main()
