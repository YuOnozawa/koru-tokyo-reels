"""Merge researched batches (data/raw/new_*.json) into data/shops.json after validation.
Drops entries that fail the schema, duplicates (same name_ja or near-same name_en), and anything without a source.
Usage: python3 tools/merge_shops.py [--dry]"""
import glob, json, os, re, sys, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AREAS = {"Akihabara", "Suehirocho", "Kanda", "Jimbocho", "Ochanomizu", "Ueno", "Okachimachi", "Yushima", "Asakusa", "Kuramae"}
BANDS = {"under1500", "1500-4000", "4000-10000", "10000plus"}
KEYS = ["name_en", "name_ja", "area", "genre", "station", "walk_min", "hours", "closed_days", "lunch_price_yen", "dinner_price_yen",
        "budget_band", "awards", "english_menu", "reservation", "what_to_order", "tourist_tip", "yu_pick", "sources", "checked",
        "kind", "lunch_ok", "dinner_ok"]


def norm(s):
    s = unicodedata.normalize('NFKC', str(s)).lower()
    s = re.sub(r'\(.*?\)|（.*?）', '', s)
    s = re.sub(r'(本店|総本店|店|main store|honten|head store|branch)', '', s)
    return re.sub(r'[\s\-・·\'’.,&]', '', s)


def check(x):
    errs = []
    for k in KEYS:
        if k not in x: errs.append('missing ' + k)
    if errs: return errs
    if x['area'] not in AREAS: errs.append('area ' + str(x['area']))
    if x['budget_band'] not in BANDS: errs.append('band ' + str(x['budget_band']))
    if x['kind'] not in ('meal', 'snack'): errs.append('kind')
    if not isinstance(x['sources'], list) or not [u for u in x['sources'] if str(u).startswith('http')]: errs.append('no source')
    if not isinstance(x['awards'], list): errs.append('awards not list')
    if not str(x['name_ja']).strip() or not str(x['name_en']).strip(): errs.append('empty name')
    if any(w in json.dumps(x, ensure_ascii=False).lower() for w in ['閉店', 'permanently closed', 'closed down']): errs.append('closed?')
    return errs


def main(dry):
    p = os.path.join(ROOT, 'data', 'shops.json'); shops = json.load(open(p, encoding='utf-8'))
    seen_ja = {norm(s['name_ja']) for s in shops}; seen_en = {norm(s['name_en']) for s in shops}
    added, dropped = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'raw', 'new_*.json'))):
        try:
            batch = json.load(open(f, encoding='utf-8'))
        except Exception as e:
            print('UNREADABLE', f, e); continue
        for x in batch:
            x = {k: x.get(k) for k in KEYS} if isinstance(x, dict) else {}
            x['yu_pick'] = False; x['checked'] = x.get('checked') or '2026-10-31'
            errs = check(x)
            nj, ne = norm(x.get('name_ja', '')), norm(x.get('name_en', ''))
            if not errs and (nj in seen_ja or ne in seen_en): errs.append('duplicate')
            if errs:
                dropped.append((os.path.basename(f), x.get('name_en'), errs)); continue
            seen_ja.add(nj); seen_en.add(ne); added.append(x)
    print('existing', len(shops), 'added', len(added), 'dropped', len(dropped))
    for d in dropped: print('  drop', d)
    if not dry:
        json.dump(shops + added, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return added


if __name__ == '__main__':
    main('--dry' in sys.argv)
