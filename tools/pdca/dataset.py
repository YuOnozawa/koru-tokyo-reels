"""PDCA dataset: every post with its reach over time (from the git history of state/insights.json) and its features.

  python tools/pdca/dataset.py   -> docs/pdca/dataset.csv, docs/pdca/summary.md

Reach is read at a fixed age (24 h, first snapshot >= 20 h) so new and old posts compare fairly.
"""
import csv, json, os, subprocess, statistics as st
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
sh = lambda *a: subprocess.check_output(a, text=True)

snaps = {}   # media_id -> list of (age_h, reach, views, avg_watch_ms)
meta = {}
for c in sh('git', 'log', '--format=%H', '--', 'state/insights.json').split():
    try:
        I = json.loads(sh('git', 'show', f'{c}:state/insights.json'))
    except Exception:
        continue
    t = datetime.fromisoformat(I['fetched_at'])
    for m in I.get('media', []):
        ts = datetime.strptime(m['timestamp'], '%Y-%m-%dT%H:%M:%S%z')
        age = (t - ts).total_seconds() / 3600
        snaps.setdefault(m['id'], []).append((age, m.get('reach'), m.get('views'), m.get('ig_reels_avg_watch_time'), m.get('saved'), m.get('shares'), m.get('likes')))
        meta[m['id']] = m
posted = {p['media_id']: p for p in json.load(open('state/posted.json')) if isinstance(p, dict) and p.get('media_id')}


def style(qid, typ, ts):
    d = ts[:10]
    if typ != 'REELS':
        return 'carousel' if (qid and not qid.startswith('r_')) or 'CAROUSEL' in typ else 'image'
    if d < '2026-11-12':
        return 'v1 voice narration, no music'
    if d < '2026-11-14':
        return 'v2 page-flip + music'
    if qid.startswith('r_h4_'):
        return 'v1 replica (H4)'
    if qid.startswith('r_v_'):
        return 'v5 stock video + AI voice'
    if qid.startswith('r_x_') and qid[4:6] >= '08' and d >= '2026-11-21':
        return 'v4 clean photo + AI voice'
    if qid.startswith('r_x_') and qid[4:6] >= '07' and d >= '2026-11-19':
        return 'v4 clean photo + music'
    spec = f'tools/carousel/specs/{qid[2:]}.json'
    if qid.startswith('r_') and os.path.exists(spec):
        h = json.load(open(spec)).get('hook', {})
        return 'v3 hook + music, Yu photo' if h.get('photo') else 'v3 hook + music, type only'
    return 'v3 hook ?'


rows = []
now = datetime.now(timezone.utc)
for mid, s in snaps.items():
    m = meta[mid]; s.sort()
    ts = m['timestamp']; age_now = (now - datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S%z')).total_seconds() / 3600
    s = [x for x in s if x[1] is not None] or s
    at24 = next((x for x in s if x[0] >= 20 and x[1] is not None), None)
    last = s[-1]
    qid = posted.get(mid, {}).get('id', '')
    rows.append(dict(id=qid or '?', media_id=mid, posted=ts[:16], type=m['media_product_type'], style=style(qid, m['media_product_type'], ts),
                     reach24=at24[1] if at24 else '', age24=round(at24[0]) if at24 else '', reach_last=last[1], age_last=round(last[0]),
                     views=last[2], watch_s=round((last[3] or 0) / 1000, 1) if last[3] else '', saved=last[4], shares=last[5], likes=last[6],
                     caption=(m.get('caption_head') or '').split('\n')[0][:50]))
rows.sort(key=lambda r: r['posted'])
os.makedirs('docs/pdca', exist_ok=True)
with open('docs/pdca/dataset.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

out = ['# PDCA summary (auto)', '', f'Updated {now:%Y-%m-%d %H:%M} UTC. Reach at 24 h (first snapshot ≥20 h). Batch = reach ≥ 80 (passed the test batch). Hit = reach ≥ 1,000 (latest). Goal = 10,000.', '',
       '| style | n | median reach 24h | batch ≥80 | hit ≥1,000 | best reach | median watch (s) |', '|---|---|---|---|---|---|---|']
by = {}
for r in rows:
    if r['reach24'] not in ('', None): by.setdefault(r['style'], []).append(r)
for k, v in sorted(by.items()):
    re = [x['reach24'] for x in v]; wa = [x['watch_s'] for x in v if x['watch_s'] != '']
    la = [max(x['reach24'], x['reach_last'] or 0) for x in v]
    out.append(f"| {k} | {len(v)} | {st.median(re):.0f} | {sum(x >= 80 for x in re)}/{len(v)} | {sum(x >= 1000 for x in la)}/{len(v)} | {max(la)} | {round(st.median(wa),1) if wa else '-'} |")
pend = [r for r in rows if r['reach24'] == '']
out += ['', 'Pending (<20 h old): ' + ', '.join(f"{r['id']} {r['reach_last']}@{r['age_last']}h" for r in pend)]
open('docs/pdca/summary.md', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
