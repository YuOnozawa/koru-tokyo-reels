"""Hypothesis scoreboard: joins queue.json test tags with state/insights.json and writes docs/experiments/scoreboard.md.
Each queue item may carry "tests": {"H5": "A", "H6": "B", ...} and "len" (video seconds).
Per arm: n reels, mean reach, mean completion (avg watch / length), (saves+shares) per 100 reach, comments per reel.
Verdicts are only suggested when both arms have n>=3; with ~100 views per reel, single reels are noise."""
import json, os, statistics as st
from collections import defaultdict
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda p, d=None: json.load(open(os.path.join(R, p), encoding='utf-8')) if os.path.exists(os.path.join(R, p)) else d
q = {x['id']: x for x in J('queue.json', [])}
posted = J('state/posted.json', {}); posted = posted if isinstance(posted, dict) else {x['id']: x for x in posted}
media = {m['id']: m for m in (J('state/insights.json', {}) or {}).get('media', [])}
H = J('docs/experiments/hypotheses.json', {})
arms = defaultdict(lambda: defaultdict(list))
for qid, item in q.items():
    p = posted.get(qid); m = media.get((p or {}).get('media_id'))
    if not m or not item.get('tests'): continue
    reach = m.get('reach') or 0; L = item.get('len'); aw = (m.get('ig_reels_avg_watch_time') or 0) / 1000
    row = {'id': qid, 'reach': reach, 'comp': (aw / L) if L else None, 'ss': ((m.get('saved') or 0) + (m.get('shares') or 0)) * 100 / reach if reach else 0,
           'com': m.get('comments') or 0, 'likes': m.get('likes') or 0}
    for h, a in item['tests'].items(): arms[h][a].append(row)
def mean(xs):
    xs = [x for x in xs if x is not None]; return st.mean(xs) if xs else None
f = lambda v, pct=False: '–' if v is None else ('%.0f%%' % (v * 100) if pct else '%.1f' % v)
out = ['# Hypothesis scoreboard (auto, after each insights run)', '',
       'completion = avg watch ÷ video length. Verdict needs n≥3 per arm and a ≥30% gap on the hypothesis metric.', '']
for h in sorted(set(H) | set(arms)):
    spec = H.get(h, {}); out.append('## %s — %s' % (h, spec.get('hypothesis', '')))
    out.append('Metric: **%s** · A = %s · B = %s · status: %s' % (spec.get('metric', 'comp'), spec.get('A', ''), spec.get('B', ''), spec.get('status', 'running')))
    out.append(''); out.append('| arm | n | reach | completion | saves+shares /100 | comments | likes |'); out.append('|---|---|---|---|---|---|---|')
    res = {}
    for a in sorted(arms[h]):
        rows = arms[h][a]; res[a] = {'n': len(rows), 'reach': mean([r['reach'] for r in rows]), 'comp': mean([r['comp'] for r in rows]),
                                     'ss': mean([r['ss'] for r in rows]), 'com': mean([r['com'] for r in rows]), 'likes': mean([r['likes'] for r in rows])}
        x = res[a]; out.append('| %s | %d | %s | %s | %s | %s | %s |' % (a, x['n'], f(x['reach']), f(x['comp'], True), f(x['ss']), f(x['com']), f(x['likes'])))
    met = spec.get('metric', 'comp')
    if len(res) >= 2 and all(v['n'] >= 3 for v in res.values()):
        vals = {a: v[met] for a, v in res.items() if v[met] is not None}
        if len(vals) >= 2:
            best, worst = max(vals, key=vals.get), min(vals, key=vals.get)
            gap = 0 if vals[best] == vals[worst] else ((vals[best] - vals[worst]) / vals[worst] if vals[worst] else float('inf'))
            out.append(''); out.append('**Suggested verdict:** %s' % ('%s wins (+%.0f%%)' % (best, gap * 100) if gap >= .3 else 'no clear difference yet'))
    else:
        out.append(''); out.append('_Not enough reels yet (need n≥3 per arm)._')
    out.append('')
open(os.path.join(R, 'docs', 'experiments', 'scoreboard.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out[:40]))
