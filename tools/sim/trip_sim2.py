"""Trip simulation v2 (2026-11-29): by market, by budget band, and with / without a date-checked plan.
Real shops from data/shops.json; party shares and nights from the JTA 2025 survey (docs/sales/target.md).
  python3 tools/sim/trip_sim2.py -> docs/sales/trip_sim2.md
Assumptions: Tokyo days = 42% of nights in Japan; 2 sit-down meals a day in our areas; meal-time habits per party type."""
import os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'trip_sim.py')).read().split('# JTA 2025')[0])     # parse(), flags(), shops, ROOT, S

MARKETS = {  # solo, couple, family, friends (%), nights, Oct-2026 arrivals where known
    'USA': (33.7, 24.4, 20.8, 18.1, 12.0), 'Australia': (18.8, 31.4, 32.7, 15.3, 13.5), 'UK': (38.6, 29.7, 21.0, 7.4, 14.4),
    'Canada': (25.2, 32.2, 24.8, 15.7, 14.6), 'Singapore': (23.5, 22.7, 37.6, 13.4, 9.1)}
PARTY = {'solo': (13 * 60, 20 * 60, False), 'couple': (13 * 60, 19 * 60 + 30, False),
         'family': (12 * 60 + 30, 18 * 60 + 30, True), 'friends': (13 * 60 + 30, 20 * 60 + 30, False)}
BANDS = {'budget (under ¥1,500)': {'under1500'}, 'mid (¥1,500-4,000)': {'1500-4000'}, 'upper (¥4,000+)': {'4000-10000', '10000plus', '4000+'}}
R = random.Random(20261130)

def pool(band):
    return [x for x in shops if band is None or str(x[0].get('budget_band')) in BANDS[band]]

def meal_time(party):
    lunch = R.random() < 0.5
    t = int(R.gauss(PARTY[party][0] if lunch else PARTY[party][1], 50))
    return lunch, (max(11 * 60, min(15 * 60 + 30, t)) if lunch else max(17 * 60, min(22 * 60 + 30, t)))

def check(shop, party, dow, t):
    s, sc, f = shop
    ev = set()
    inside = [r for r in sc[dow] if r[0] <= t < r[1]]
    if not inside: ev.add('closed')
    else:
        o, c, lo = inside[0]
        if lo is not None and t >= lo: ev.add('after last order')
        elif (lo or c) - t < 45: ev.add('rushed (under 45 min)')
    if f['no_kids'] and PARTY[party][2]: ev.add('no young children')
    if f['booking_needed']: ev.add('booking needed')
    if str(s.get('reservation')).lower().startswith('recommended'): ev.add('booking recommended')
    if f['cash_only']: ev.add('no credit cards')
    if f['charge']: ev.add('cover charge')
    return ev

TURNED = {'after last order', 'no young children', 'booking needed'}

def trip(party, meals, band, plan):
    P = pool(band); start = R.randrange(7); turned = rushed = nocard = 0; choice = []
    for m in range(meals):
        dow = (start + m // 2) % 7
        lunch, t = meal_time(party)
        if plan:   # the plan only offers shops that are open, 45+ min before last order, no blocking rule; card rule is printed
            ok = [x for x in P if not (check(x, party, dow, t) & (TURNED | {'closed', 'rushed (under 45 min)'}))]
            choice.append(len(ok))
            if not ok: turned += 1; continue
            ev = check(R.choice(ok), party, dow, t)
        else:      # careful traveler: checks posted opening hours, nothing else
            op = [x for x in P if any(r[0] <= t < r[1] for r in x[1][dow])]
            if not op: turned += 1; continue
            ev = check(R.choice(op), party, dow, t)
        turned += bool(ev & TURNED); rushed += 'rushed (under 45 min)' in ev; nocard += 'no credit cards' in ev
    return turned, rushed, nocard, choice

N = 6000
def run(party, meals, band, plan):
    a = b = c = 0; ch = []
    for _ in range(N):
        t, r, nc, choice = trip(party, meals, band, plan)
        a += t > 0; b += r > 0; c += nc; ch += choice
    return a / N, b / N, c / N, (sum(ch) / len(ch) if ch else 0)

out = ['# Trip simulation v2 (auto-generated)', '',
       f'{len(shops)} real meal shops with parseable hours. "Without plan" = a careful traveler who checks posted opening hours and nothing else.',
       '"With plan" = shops offered only if open that day and hour, 45+ minutes before last order, and no blocking rule for the party. Rules are only those recorded in our data, so "without plan" is a floor.', '',
       '## By market (party mix and trip length from the JTA 2025 survey; all price bands)', '',
       '| market | Tokyo days (assumed) | meals | turned away at least once, without plan | with plan | meals with no credit cards | rushed at least once, without plan |', '|---|---|---|---|---|---|---|']
mk = {}
for name, (so, co, fa, fr, nights) in MARKETS.items():
    days = max(3, round(nights * 0.42)); meals = days * 2
    w = {'solo': so, 'couple': co, 'family': fa, 'friends': fr}; tot = sum(w.values())
    res = {p: (run(p, meals, None, False), run(p, meals, None, True)) for p in w}
    agg = lambda i, j: sum(w[p] * res[p][i][j] for p in w) / tot
    mk[name] = (days, meals, agg(0, 0), agg(1, 0), agg(0, 2), agg(0, 1), res)
    out.append(f'| {name} | {days} | {meals} | {agg(0,0):.0%} | {agg(1,0):.0%} | {agg(0,2):.1f} of {meals} | {agg(0,1):.0%} |')
out += ['', '## By party and price band (10 meals, without plan -> with plan: turned away at least once)', '',
        '| party | ' + ' | '.join(BANDS) + ' |', '|---|' + '---|' * len(BANDS)]
grid = {}
for p in PARTY:
    row = []
    for b in BANDS:
        a = run(p, 10, b, False); c = run(p, 10, b, True); grid[(p, b)] = (a, c)
        row.append(f'{a[0]:.0%} -> {c[0]:.0%} (choices per meal with plan: {c[3]:.0f} of {len(pool(b))})')
    out.append(f'| {p} | ' + ' | '.join(row) + ' |')
out += ['', '## Rules by price band (share of shops)', '', '| band | shops | no credit cards | last order listed | booking needed or recommended | booking rule unknown |', '|---|---|---|---|---|---|']
for b in BANDS:
    P = pool(b); n = len(P)
    lo = sum(any(r[2] is not None for d in range(7) for r in x[1][d]) for x in P)
    bk = sum(x[2]['booking_needed'] or str(x[0].get('reservation')).lower().startswith('recommended') for x in P)
    unk = sum(str(x[0].get('reservation')).lower() in ('unknown', 'none') for x in P)
    out.append(f"| {b} | {n} | {sum(x[2]['cash_only'] for x in P)/n:.0%} | {lo/n:.0%} | {bk/n:.0%} | {unk/n:.0%} |")
open(os.path.join(ROOT, 'docs/sales/trip_sim2.md'), 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
