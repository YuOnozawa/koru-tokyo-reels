"""Mechanistic trip simulation (2026-11-29). Not an opinion panel: simulated travelers pick real shops from data/shops.json
at realistic meal times, and we count what goes wrong. Population shares come from the JTA 2025 survey (docs/sales/target.md).

  python3 tools/sim/trip_sim.py  -> docs/sales/trip_sim.md

Assumptions (stated in the output): 5 Tokyo days, 2 sit-down meals a day in our areas, shop picked uniformly among meal shops.
"""
import json, re, random, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
S = json.load(open(os.path.join(ROOT, 'data/shops.json'))); S = S if isinstance(S, list) else S['shops']
DAYS = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
TOKYO = {'Asakusa', 'Akihabara', 'Jimbocho', 'Kanda', 'Suehirocho', 'Ueno', 'Yushima', 'Okachimachi', 'Kuramae', 'Ochanomizu'}

def dayset(spec):
    spec = spec.lower()
    out = set()
    if re.search(r'daily|every day', spec): return set(range(7))
    for a, b in re.findall(r'(mon|tue|wed|thu|fri|sat|sun)[a-z]*\s*[-–]\s*(mon|tue|wed|thu|fri|sat|sun)', spec):
        i, j = DAYS.index(a), DAYS.index(b)
        out |= {k % 7 for k in range(i, i + ((j - i) % 7) + 1)}
    for a in re.findall(r'(mon|tue|wed|thu|fri|sat|sun)', re.sub(r'(mon|tue|wed|thu|fri|sat|sun)[a-z]*\s*[-–]\s*(mon|tue|wed|thu|fri|sat|sun)[a-z]*', ' ', spec)):
        out.add(DAYS.index(a))
    return out

def parse(shop):
    """-> {day: [(open, close, last_order)]} in minutes, or None if unparseable."""
    h = shop.get('hours') or ''
    h = re.sub(r'^(Tabelog|Retty)[^:]*:\s*', '', h)
    sched = {d: [] for d in range(7)}
    found = False
    for seg in re.split(r';', h):
        m = re.search(r'\d{1,2}:\d{2}', seg)
        if not m: continue
        ds = dayset(seg[:m.start()]) or set(range(7))
        for mm in re.finditer(r'(\d{1,2}):(\d{2})\s*[-–~]\s*(\d{1,2}):(\d{2})(\s*\((?:food )?(?:LO|L\.O\.|last order)\s*(\d{1,2}):(\d{2}))?', seg, re.I):
            o = int(mm.group(1)) * 60 + int(mm.group(2)); c = int(mm.group(3)) * 60 + int(mm.group(4))
            if c <= o: c += 1440
            lo = None
            if mm.group(6):
                lo = int(mm.group(6)) * 60 + int(mm.group(7))
                if lo < o: lo += 1440
            for d in ds: sched[d].append((o, c, lo))
            found = True
    if not found: return None
    cd = (shop.get('closed_days') or '').lower()
    if not re.search(r'\d(st|nd|rd|th)|irregular|mainly|occasional', cd):       # weekly closures only
        for d in dayset(re.sub(r'none.*', '', cd)): sched[d] = []
    return sched

def flags(shop):
    t = json.dumps([shop.get('tourist_tip'), shop.get('house_rules'), shop.get('reservation')], ensure_ascii=False).lower()
    return {
        'cash_only': bool(re.search(r'cash only|no credit cards|no cards|credit cards not accepted|cash or', t)) and not re.search(r'cards? (ok|accepted)|visa', t.replace('no credit cards', '')),
        'no_kids': bool(re.search(r'no children|not for children|adults only', t)),
        'booking_needed': str(shop.get('reservation')).lower() in ('needed',) or 'booking required' in t,
        'no_booking': bool(re.search(r'no bookings|no reservations|not_accepted|not for overseas', t)),
        'charge': bool(re.search(r'cover charge|table charge|seat charge|otoshi|appetizer charge', t)) and 'no service or table charge' not in t,
    }

shops = []
for s in S:
    if s.get('area') not in TOKYO or s.get('kind') != 'meal': continue
    sc = parse(s)
    if sc: shops.append((s, sc, flags(s)))
total_meal = sum(1 for s in S if s.get('area') in TOKYO and s.get('kind') == 'meal')

# JTA 2025: party shares for the US (largest English-speaking market); dinner time habits are assumptions.
PERSONAS = [  # name, share, lunch mean, dinner mean (minutes), has young kids
    ('solo', 33.7, 13 * 60, 20 * 60, False),
    ('couple', 24.4, 13 * 60, 19 * 60 + 30, False),
    ('friends', 18.1, 13 * 60 + 30, 20 * 60 + 30, False),
    ('family with kids', 20.8, 12 * 60 + 30, 18 * 60 + 30, True),
]
R = random.Random(20261129)

CAREFUL = False   # True: the traveler checks posted opening hours first and only goes to shops that are open then

def attempt(p, dow):
    lunch = R.random() < 0.5
    t = int(R.gauss(p[2] if lunch else p[3], 50))
    t = max(11 * 60, min(15 * 60 + 30, t)) if lunch else max(17 * 60, min(22 * 60 + 30, t))
    while True:
        s, sc, f = R.choice(shops)
        if not CAREFUL or any(r[0] <= t < r[1] for r in sc[dow]): break
    ev = []
    ranges = sc[dow]
    if not ranges: ev.append('closed that weekday')
    else:
        inside = [r for r in ranges if r[0] <= t < r[1]]
        if not inside: ev.append('closed at that hour (break or not open yet)')
        else:
            o, c, lo = inside[0]
            if lo is not None and t >= lo: ev.append('after last order')
            elif c - t < 30: ev.append('under 30 min to closing')
    if f['cash_only']: ev.append('credit cards not accepted')
    if f['no_kids'] and p[4]: ev.append('no young children')
    if f['booking_needed']: ev.append('booking needed')
    if f['charge']: ev.append('cover / seat charge')
    return ev

HIDDEN = {'after last order', 'under 30 min to closing', 'credit cards not accepted', 'no young children', 'booking needed', 'cover / seat charge'}
VISIBLE = {'closed that weekday', 'closed at that hour (break or not open yet)'}
N, MEALS = 20000, 10

def run():
    res = {}
    for p in PERSONAS:
        cnt = collections.Counter(); trip_any = trip_door = trip_hidden = 0
        for _ in range(N):
            start = R.randrange(7); a = d = h = False
            for m in range(MEALS):
                ev = attempt(p, (start + m // 2) % 7)
                for e in ev: cnt[e] += 1
                if ev: a = True
                if set(ev) & (VISIBLE | {'after last order', 'no young children', 'booking needed'}): d = True
                if set(ev) & HIDDEN: h = True
            trip_any += a; trip_door += d; trip_hidden += h
        res[p[0]] = (cnt, trip_any / N, trip_door / N, trip_hidden / N)
    return res

res = run()
CAREFUL = True
res2 = run()

out = ['# Trip simulation: what goes wrong at the door (auto-generated)', '',
       f'Real shops: {len(shops)} of {total_meal} meal shops in our Tokyo areas have parseable hours (data/shops.json, checked Nov 2026).',
       f'Each simulated traveler: {MEALS} sit-down meals over 5 Tokyo days, shop picked at random, arriving at a typical lunch or dinner time. {N:,} trips per group.',
       'Group shares: JTA 2025 survey, US visitors. Meal times and "family = young kids" are assumptions.', '',
       '## Careless traveler: picks a shop without checking hours', '', '| group | share | turned away at least once in the trip | hits a rule Google Maps does not show at least once |', '|---|---|---|---|']
for p in PERSONAS:
    cnt, a, d, h = res[p[0]]
    out.append(f'| {p[0]} | {p[1]}% | {d:.0%} | {h:.0%} |')
out += ['', 'Per meal attempt (share of attempts where it happens):', '', '| event | ' + ' | '.join(p[0] for p in PERSONAS) + ' |', '|---|' + '---|' * len(PERSONAS)]
for e in ['closed that weekday', 'closed at that hour (break or not open yet)', 'after last order', 'under 30 min to closing', 'credit cards not accepted', 'no young children', 'booking needed', 'cover / seat charge']:
    out.append(f'| {e} | ' + ' | '.join(f'{res[p[0]][0][e] / (N * MEALS):.1%}' for p in PERSONAS) + ' |')
out += ['', '## Careful traveler: checks posted opening hours first (only goes to shops open at that time)', '',
        '| group | turned away at least once (last order / children / booking) | meals out of 10 where credit cards are not accepted | arrives with under 30 min to closing at least once |', '|---|---|---|---|']
for p in PERSONAS:
    cnt, a, d, h = res2[p[0]]
    late = 1 - (1 - cnt['under 30 min to closing'] / (N * MEALS)) ** MEALS
    out.append(f"| {p[0]} | {d:.0%} | {cnt['credit cards not accepted'] / N:.1f} | {late:.0%} |")
out += ['', '"Turned away" = closed that weekday, closed at that hour, after last order, children not accepted, or booking needed.',
        '"Rule Google Maps does not show" = last order, under 30 min to closing, cash only, children, booking, cover charge.',
        'Limits: random shop choice overstates closed-day misses for people who check hours first; rule flags exist only where our DB recorded them (house_rules on 68 shops), so hidden-rule rates are a floor.']
os.makedirs(os.path.join(ROOT, 'docs/sales'), exist_ok=True)
open(os.path.join(ROOT, 'docs/sales/trip_sim.md'), 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
