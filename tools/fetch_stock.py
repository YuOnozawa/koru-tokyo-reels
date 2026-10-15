"""Fetch CC0 / public-domain photos from Openverse for reel backgrounds.
Usage: python tools/fetch_stock.py "query1" "query2" ...  (runs on GitHub Actions; needs network)
Saves stock/<slug>_<n>.jpg (max 1600px) and appends license info to stock/credits.json."""
import json, os, re, sys, urllib.parse, urllib.request, io
from PIL import Image
OUT = 'stock'; os.makedirs(OUT, exist_ok=True)
cred_p = f'{OUT}/credits.json'
credits = json.load(open(cred_p)) if os.path.exists(cred_p) else {}
UA = {'User-Agent': 'koru-tokyo-reels/1.0 (github.com/YuOnozawa/koru-tokyo-reels)'}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        return r.read()
for q in sys.argv[1:]:
    slug = re.sub(r'[^a-z0-9]+', '_', q.lower()).strip('_')
    api = 'https://api.openverse.org/v1/images/?' + urllib.parse.urlencode(
        {'q': q, 'license': 'cc0,pdm', 'size': 'large', 'category': 'photograph', 'page_size': 20, 'mature': 'false'})
    try:
        res = json.loads(get(api)).get('results', [])
    except Exception as e:
        print('search failed', q, e); continue
    n = 0
    for r in res:
        if n >= 5: break
        try:
            im = Image.open(io.BytesIO(get(r['url']))).convert('RGB')
        except Exception as e:
            print('  skip', r.get('url'), e); continue
        if min(im.size) < 700: continue
        im.thumbnail((1600, 1600))
        name = f'{slug}_{n}.jpg'; im.save(f'{OUT}/{name}', quality=85)
        credits[name] = {'query': q, 'title': r.get('title'), 'creator': r.get('creator'),
                         'license': r.get('license'), 'license_version': r.get('license_version'),
                         'source': r.get('foreign_landing_url') or r.get('url'), 'provider': r.get('provider')}
        n += 1
    print(q, '->', n)
json.dump(credits, open(cred_p, 'w'), ensure_ascii=False, indent=1)
