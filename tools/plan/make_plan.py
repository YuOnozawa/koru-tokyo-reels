"""Date-checked food plan (product A sample). Everything comes from data/shops.json; nothing is invented.
  python3 tools/plan/make_plan.py tools/plan/samples/us_couple.json  -> out/<id>.html, out/<id>.pdf, out/<id>.json
Only shops whose rules were checked (house_rules present) are used. Each pick is tested against the real weekday:
open at the arrival time, at least 75 min (dinner) / 45 min (lunch) before last order, no rule that blocks the party."""
import json, os, re, sys, datetime, html, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, '..', 'sim', 'trip_sim.py')).read().split('shops = []')[0])     # parse(), flags(), S, ROOT, DAYS
T = lambda hm: int(hm.split(':')[0]) * 60 + int(hm.split(':')[1])
F = lambda m: f'{m // 60}:{m % 60:02d}'
HOLIDAYS = {'2026-11-23', '2027-01-01', '2027-01-11'}

def rules(s): return [r for r in (s.get('house_rules') or [])]
def find(s, pat):
    for r in rules(s) + [s.get('tourist_tip') or '']:
        for part in re.split(r'(?<=[.;])\s+', r):
            if re.search(pat, part, re.I): return part.strip().rstrip('.;, ')
    return None

def booking(s):
    r = str(s.get('reservation') or '').strip(); f = flags(s)
    b = find(s, r'book|reserv')
    if r.lower() == 'needed' or (b and 'required' in b.lower()): return 'BOOK', b or 'Booking required'
    if r.lower().startswith('recommended'): return 'BOOK', 'Booking recommended' + ('. ' + b if b and re.search(r'book|reserv', b, re.I) and 'allerg' not in b.lower() else '')
    if f['no_booking'] or r.lower() in ('not_needed', 'no bookings', 'not_accepted'): return 'WALK IN', b or 'No booking needed'
    return ('BOOKABLE', (b or r)[:1].upper() + (b or r)[1:]) if (b or r.lower() not in ('unknown', 'none', '')) else ('WALK IN', 'Booking rule not listed; go early')

def slot(s, date, want, margin):
    """-> (arrive, open, close, last_order) if the shop works that day, else None."""
    if date.isoformat() in HOLIDAYS and re.search(r'holiday', s.get('closed_days') or '', re.I): return None
    cd = (s.get('closed_days') or '').lower()
    if re.search(r'\d(st|nd|rd|th)|irregular|mainly|occasional', cd) and DAYS[date.weekday()] in cd: return None   # can't be sure
    sc = parse(s)
    if not sc: return None
    for o, c, lo in sc[date.weekday()]:
        end = (lo or c) - margin
        if o <= want <= end: return want, o, c, lo
        if o <= end and abs(end - want) <= 60 and o <= want:      # arrive a little earlier
            return (end // 30) * 30, o, c, lo
        if want < o <= want + 45 and o <= end: return o, o, c, lo  # opens slightly later
    return None

def score(s):
    return (3 if s.get('awards') else 0) + (float(s.get('tabelog_score') or 3.3) - 3.3) * 4 + (2 if s.get('yu_pick') else 0) + (1 if s.get('review_summary') else 0)

def main(path):
    P = json.load(open(path)); days = build(P)
    out = os.path.join(ROOT, 'out'); os.makedirs(out, exist_ok=True)
    render(P, days, os.path.join(out, P['id']))

def build(P):
    cand = [s for s in S if s.get('kind') == 'meal' and s.get('house_rules')]
    used, genres, days = set(), [], []
    d0 = datetime.date.fromisoformat(P['start'])
    for i in range(P['days']):
        date = d0 + datetime.timedelta(days=i); areas = P['areas'][i % len(P['areas'])]; day = {'date': date, 'areas': areas, 'meals': []}
        for kind, want, bands, margin in (('LUNCH', T(P['lunch_time']), P['lunch_bands'], 45), ('DINNER', T(P['dinner_time']), P['dinner_bands'], 75)):
            opts = []
            for s in cand:
                if s['name_en'] in used or s.get('area') not in areas or str(s.get('budget_band')) not in bands: continue
                if not s.get('lunch_ok' if kind == 'LUNCH' else 'dinner_ok'): continue
                if P.get('kids') and flags(s)['no_kids']: continue
                sl = slot(s, date, want, margin)
                if not sl: continue
                g = (s.get('genre') or '').split(' ')[0].lower()
                opts.append((score(s) - bands.index(str(s.get('budget_band'))) * (0.6 if kind == 'DINNER' else 0.2) - (2.5 if g in genres else 0) - areas.index(s['area']) * 0.3, s, sl))
            opts.sort(key=lambda x: -x[0])
            if not opts: day['meals'].append({'kind': kind, 'shop': None}); continue
            _, s, sl = opts[0]; used.add(s['name_en']); genres.append((s.get('genre') or '').split(' ')[0].lower())
            backup = next(((b, bs) for _, b, bs in opts[1:] if booking(b)[0] != 'BOOK'), None)
            day['meals'].append({'kind': kind, 'shop': s, 'slot': sl, 'backup': backup})
        days.append(day)
    return days

def card(m, date):
    s = m['shop']
    if not s: return f'<section class="meal"><div class="k">{m["kind"]}</div><p>No checked shop fits this slot. Free choice.</p></section>'
    arrive, o, c, lo = m['slot']; bk, bktxt = booking(s); e = html.escape
    price = re.sub(r'^about\s*', '', str(s.get('lunch_price_yen') if m['kind'] == 'LUNCH' else s.get('dinner_price_yen')))
    pay = find(s, r'card|cash|paypay') or 'Payment not listed: bring cash'
    extra = [x for x in (find(s, r'service charge|otoshi|cover charge|table charge|appetizer'), find(s, r'child|kids|stroller|age \d'), find(s, r'smok'), find(s, r'hour|minutes|drink per')) if x]
    extra = [x for i, x in enumerate(extra) if x not in extra[:i] and x != pay and x != bktxt]
    maps = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(f"{s.get('name_ja')} {s.get('area')}")
    bu = ''
    if m.get('backup'):
        b, bs = m['backup']
        bu = f'<div class="bu"><b>If it is full</b> {e(b["name_en"])} <span class="ja">{e(b.get("name_ja") or "")}</span> · {e((b.get("genre") or "").split("(")[0].strip())} · open until {F(bs[2] % 1440)}{", last order " + F(bs[3] % 1440) if bs[3] else ""} · {e(booking(b)[1])}</div>'
    cls = 'book' if bk == 'BOOK' else 'walk'
    return f'''<section class="meal">
<div class="row1"><div class="k">{m["kind"]}</div><div class="arr">Arrive <b>{F(arrive)}</b></div><div class="tag {cls}">{bk}</div></div>
<h3>{e(s["name_en"])} <span class="ja">{e(s.get("name_ja") or "")}</span></h3>
<div class="meta">{e((s.get("genre") or "").strip())} · {e(str(s.get("area")))} · {e(str(s.get("walk_min")))} min from {e(re.split(r"[;(,]", str(s.get("station")))[0].strip())} · about ¥{e(str(price))} a person</div>
<p class="order"><b>Order</b> {e(s.get("what_to_order") or "")}</p>
<table class="chk">
<tr><th>Open {date.strftime("%a")}</th><td>{F(o)}–{F(c % 1440)}{" · last order " + F(lo % 1440) if lo else " · no last order listed, so be seated 45 min before closing"}</td></tr>
<tr><th>Booking</th><td>{e(bktxt)}</td></tr>
<tr><th>Paying</th><td>{e(pay)}</td></tr>
{"".join(f"<tr><th>Know</th><td>{e(x)}</td></tr>" for x in extra)}
<tr><th>Closed</th><td>{e(s.get("closed_days") or "not listed")}</td></tr>
</table>
<div class="src"><a href="{maps}">Open in Google Maps</a> · rules checked {e(str(s.get("rules_checked") or s.get("checked")))}</div>
{bu}</section>'''

CSS = '''@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:"Noto Sans CJK JP","Noto Sans",sans-serif;color:#1c1a17;font-size:10.2pt;line-height:1.42}
@font-face{font-family:Zen;src:url("file:///home/claude/fonts/ZenKakuGothicNew-Black.ttf")}@font-face{font-family:Pop;src:url("file:///home/claude/fonts/Poppins-Black.ttf")}
.page{width:210mm;height:297mm;padding:16mm 16mm 14mm;background:#f6f1e7;page-break-after:always;position:relative;overflow:hidden}
.mast{display:flex;justify-content:space-between;align-items:baseline;border-bottom:2.2pt solid #1c1a17;padding-bottom:3mm;margin-bottom:6mm}
.mast .b{font-family:Pop;font-size:11pt;letter-spacing:.06em}.mast .r{font-size:8.5pt;letter-spacing:.08em;text-transform:uppercase}
h1{font-family:Pop;font-size:44pt;line-height:.98;margin:18mm 0 4mm;letter-spacing:-.01em}h1 em{font-style:normal;color:#c8321e}
.jp{font-family:Zen;font-size:15pt;margin-bottom:10mm}
.lead{font-size:11.5pt;max-width:150mm;margin-bottom:9mm}
.day h2{font-family:Pop;font-size:27pt;margin:0;line-height:1}.day .sub{font-family:Zen;font-size:11pt;margin:1.5mm 0 6mm;color:#c8321e}
.meal{background:#fffdf8;border:1pt solid #1c1a17;padding:5mm 6mm 4mm;margin-bottom:5.5mm}
.row1{display:flex;align-items:center;gap:4mm;margin-bottom:1.5mm}.k{font-family:Pop;font-size:10pt;letter-spacing:.14em}
.arr{font-size:10pt}.arr b{font-family:Pop;font-size:15pt}.tag{margin-left:auto;font-family:Pop;font-size:8.5pt;letter-spacing:.1em;padding:1.2mm 3mm;border:1pt solid #1c1a17}
.tag.book{background:#c8321e;color:#fff;border-color:#c8321e}
h3{font-family:Pop;font-size:17pt;margin:0 0 .8mm;line-height:1.1}.ja{font-family:Zen;font-size:11pt;font-weight:400;margin-left:2mm}
.meta{font-size:8.8pt;color:#5a554c;margin-bottom:2mm}.order{margin:0 0 2.5mm}
table.chk{width:100%;border-collapse:collapse;font-size:9.3pt}table.chk th{width:24mm;text-align:left;font-weight:700;vertical-align:top;padding:1mm 0;border-top:.5pt solid #cfc7b6;font-size:8.3pt;letter-spacing:.06em;text-transform:uppercase}
table.chk td{padding:1mm 0;border-top:.5pt solid #cfc7b6}
.src{font-size:8pt;color:#5a554c;margin-top:2mm}.src a{color:#1c1a17}
.bu{margin-top:2.5mm;padding-top:2mm;border-top:1pt dashed #1c1a17;font-size:9pt}.bu b{font-family:Pop;font-size:8.3pt;letter-spacing:.08em;text-transform:uppercase;margin-right:2mm}
.foot{position:absolute;left:16mm;right:16mm;bottom:8mm;font-size:7.4pt;color:#5a554c;display:flex;justify-content:space-between;gap:6mm;border-top:.5pt solid #cfc7b6;padding-top:2mm}.foot span:nth-child(2){flex:1;text-align:center}
table.g{width:100%;border-collapse:collapse;font-size:9.6pt}table.g th{text-align:left;font-size:8pt;letter-spacing:.08em;text-transform:uppercase;border-bottom:1.5pt solid #1c1a17;padding:1.5mm 1mm}
table.g td{padding:1.8mm 1mm;border-bottom:.5pt solid #cfc7b6;vertical-align:top}.num{font-family:Pop;font-size:26pt;line-height:1}
.facts{display:flex;gap:8mm;margin:6mm 0 8mm}.facts div{flex:1;border-top:2.2pt solid #1c1a17;padding-top:2mm;font-size:9.4pt}
h4{font-family:Pop;font-size:13pt;margin:7mm 0 2mm}ul{margin:0;padding-left:5mm}li{margin-bottom:1.2mm}'''

def render(P, days, base):
    e = html.escape; meals = [(d, m) for d in days for m in d['meals'] if m['shop']]
    books = [(d, m) for d, m in meals if booking(m['shop'])[0] == 'BOOK']
    nocard = [(d, m) for d, m in meals if flags(m['shop'])['cash_only'] and not (m['kind'] == 'DINNER' and (find(m['shop'], r'card|cash') or '').lower().startswith('lunch'))]
    los = [(d, m) for d, m in meals if m['slot'][3] and m['slot'][3] - m['slot'][0] <= 150]
    d0, d1 = days[0]['date'], days[-1]['date']
    foot = lambda n: f'<div class="foot"><span>with KORU · sample plan</span><span>Hours and rules as listed by the shops and Tabelog, checked Nov 2026. Reconfirm the day before.</span><span>{n}</span></div>'
    pages = [f'''<div class="page"><div class="mast"><span class="b">with KORU</span><span class="r">Tokyo food plan · checked for your dates</span></div>
<h1>Ten meals.<br><em>Zero</em> closed doors.</h1><div class="jp">あなたの日程で確かめた、東京の食事プラン</div>
<p class="lead">{e(P["label"])}. {d0.strftime("%a %-d %b")} to {d1.strftime("%a %-d %b %Y")}, staying in {e(P["hotel"])}. Every shop below was tested against the weekday you will be there: opening hours, last order, booking rule, how you pay.</p>
<div class="facts"><div><span class="num">{len(meals)}</span><br>meals planned, each open at the time shown</div><div><span class="num">{len(books)}</span><br>to book before you fly</div><div><span class="num">{len(nocard)}</span><br>where credit cards are not accepted</div><div><span class="num">{len(los)}</span><br>with a last order earlier than closing</div></div>
<table class="g"><tr><th>Day</th><th>Lunch</th><th>Dinner</th></tr>{"".join(f"<tr><td><b>{d['date'].strftime('%a %-d')}</b><br>{e(' / '.join(d['areas'][:2]))}</td>" + "".join(f"<td>{F(m['slot'][0])} · <b>{e(m['shop']['name_en'])}</b><br>{e((m['shop'].get('genre') or '').split('(')[0].strip())}</td>" if m['shop'] else "<td>free choice</td>" for m in d['meals']) + "</tr>" for d in days)}</table>{foot(1)}</div>''']
    for i, d in enumerate(days):
        pages.append(f'<div class="page day"><div class="mast"><span class="b">with KORU</span><span class="r">Day {i + 1} of {len(days)}</span></div><h2>{d["date"].strftime("%A %-d %B")}</h2><div class="sub">{e(" · ".join(d["areas"]))}</div>{"".join(card(m, d["date"]) for m in d["meals"])}{foot(i + 2)}</div>')
    pages.append(f'''<div class="page"><div class="mast"><span class="b">with KORU</span><span class="r">Before you go</span></div><h2 style="font-family:Pop;font-size:27pt;margin:0 0 4mm">Do these first</h2>
<h4>Book now</h4><ul>{"".join(f"<li><b>{e(m['shop']['name_en'])}</b>, {d['date'].strftime('%a %-d %b')} {m['kind'].lower()} at {F(m['slot'][0])}: {e(booking(m['shop'])[1])}</li>" for d, m in books) or "<li>Nothing needs booking.</li>"}</ul>
<h4>Bring cash for</h4><ul>{"".join(f"<li><b>{e(m['shop']['name_en'])}</b> ({d['date'].strftime('%a')} {m['kind'].lower()}): {e(find(m['shop'], r'card|cash') or '')}</li>" for d, m in nocard) or "<li>Every shop in this plan takes cards.</li>"}</ul>
<h4>Last orders to respect</h4><ul>{"".join(f"<li><b>{e(m['shop']['name_en'])}</b> ({d['date'].strftime('%a')} {m['kind'].lower()}): last order {F(m['slot'][3] % 1440)}, you arrive {F(m['slot'][0])}</li>" for d, m in los)}</ul>
<h4>How this plan was made</h4><p>Shops come from the with KORU list of {len([s for s in S if s.get("kind") == "meal" and s.get("area") in TOKYO])} places to eat in east Tokyo; only the ones whose house rules we checked are used here. A shop is offered for a meal only if it is open on that weekday at your arrival time, you sit down at least 75 minutes (dinner) or 45 minutes (lunch) before last order, and no rule blocks your party.</p>{foot(len(days) + 2)}</div>''')
    doc = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tokyo food plan</title><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
    open(base + '.html', 'w').write(doc)
    json.dump([{'date': d['date'].isoformat(), 'meals': [{'kind': m['kind'], 'shop': m['shop'] and m['shop']['name_en'], 'arrive': m['shop'] and F(m['slot'][0]), 'backup': m.get('backup') and m['backup'][0]['name_en']} for m in d['meals']]} for d in days], open(base + '.json', 'w'), indent=1)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + base + '.html'); pg.pdf(path=base + '.pdf', format='A4', print_background=True)
        pg.set_viewport_size({'width': 794, 'height': 1123}); pg.screenshot(path=base + '.png', full_page=True); b.close()
    print(base + '.pdf'); print(open(base + '.json').read())

if __name__ == '__main__': main(sys.argv[1])
