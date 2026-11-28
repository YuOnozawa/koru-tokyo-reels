"""Delivery check: can the generator fill a complete plan for simulated orders? (2026-11-29)
Random orders (dates Dec 2026 - Mar 2027, 3-6 Tokyo days, party, budget) -> share of meal slots filled with a checked shop, and with a backup.
  python3 tools/plan/order_sim.py -> docs/sales/order_sim.md"""
import os, random, datetime, collections, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('mp', os.path.join(HERE, 'make_plan.py')); mp = importlib.util.module_from_spec(spec); spec.loader.exec_module(mp)
R = random.Random(7)
AREAS = [["Ueno", "Yushima", "Okachimachi"], ["Asakusa", "Kuramae"], ["Akihabara", "Suehirocho"], ["Kanda", "Jimbocho", "Ochanomizu"]]
BUD = {'budget': (["under1500"], ["under1500", "1500-4000"]), 'mid': (["under1500", "1500-4000"], ["1500-4000", "4000-10000"]),
       'upper': (["under1500", "1500-4000"], ["4000-10000", "10000plus", "4000+", "1500-4000"])}
PARTY = {'solo': ('12:30', '20:00', False), 'couple': ('12:30', '19:00', False), 'family with kids': ('12:00', '18:00', True), 'friends': ('13:00', '20:30', False)}
res = collections.defaultdict(lambda: [0, 0, 0, 0, 0])   # orders, complete, slots, filled, with backup
for _ in range(1200):
    party = R.choice(list(PARTY)); bud = R.choice(list(BUD)); days = R.randint(3, 6)
    start = datetime.date(2026, 12, 1) + datetime.timedelta(days=R.randrange(110))
    ar = AREAS[:]; R.shuffle(ar)
    P = {'party': party, 'kids': PARTY[party][2], 'start': start.isoformat(), 'days': days, 'lunch_time': PARTY[party][0], 'dinner_time': PARTY[party][1],
         'lunch_bands': BUD[bud][0], 'dinner_bands': BUD[bud][1], 'areas': ar}
    plan = mp.build(P); meals = [m for d in plan for m in d['meals']]
    for key in ((party, bud), ('ALL', bud), (party, 'ALL'), ('ALL', 'ALL')):
        r = res[key]; r[0] += 1; r[1] += all(m['shop'] for m in meals); r[2] += len(meals); r[3] += sum(bool(m['shop']) for m in meals); r[4] += sum(bool(m['shop'] and m.get('backup')) for m in meals)
out = ['# Delivery check: simulated orders (auto-generated)', '', '1,200 random orders: 3-6 Tokyo days from Dec 2026 to Mar 2027, four party types, three budgets, areas in random order.',
       'Only shops with checked house rules are used (%d meal shops).' % len([s for s in mp.S if s.get('kind') == 'meal' and s.get('house_rules')]), '',
       '| party | budget | orders | plans with every meal filled | meal slots filled | slots with a walk-in backup |', '|---|---|---|---|---|---|']
for key in sorted(res, key=lambda k: (k[0] != 'ALL', k[0], k[1] != 'ALL', k[1])):
    n, c, s, f, b = res[key]; out.append(f'| {key[0]} | {key[1]} | {n} | {c/n:.0%} | {f/s:.0%} | {b/s:.0%} |')
open(os.path.join(mp.ROOT, 'docs/sales/order_sim.md'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
