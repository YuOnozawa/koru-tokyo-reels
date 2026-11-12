"""Build the 'issues' strip on the home page and site/issues/ (every page of every magazine issue).
Source: tools/carousel/specs/*.json + queue.json (carousel publish time decides the order and the date label).
Run after rendering carousels: python tools/build_issues.py"""
import json, glob, os, html, re, datetime, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sitenav import NAV_CSS, nav
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
e = html.escape

def issues():
    q = json.load(open(os.path.join(ROOT, 'queue.json')))
    when = {x['id']: x['publish_at'][:10] for x in q if x.get('type') == 'carousel'}
    out = []
    for f in glob.glob(os.path.join(ROOT, 'tools/carousel/specs/*.json')):
        s = json.load(open(f)); cid = s['id']
        pages = sorted(glob.glob(os.path.join(ROOT, f'site/carousels/{cid}/*.jpg')))
        today = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)).date().isoformat()
        if not pages or cid not in when or when[cid] > today:  # only issues already out (JST)
            continue
        cov = s['slides'][0]
        title = re.sub(r'[\[\]]', '', cov.get('jp', '')).replace('\n', '')
        out.append(dict(id=cid, issue=s['issue'], place=s.get('place', ''), date=when[cid], jp=title, en=cov.get('en', ''),
                        pages=[os.path.relpath(p, os.path.join(ROOT, 'site')) for p in pages]))
    return sorted(out, key=lambda x: x['date'], reverse=True)

def strip(items, prefix=''):
    cards = ''.join(f'<a href="{prefix}issues/#{i["id"]}"><img src="{prefix}{i["pages"][0]}" alt="{e(i["jp"])}" loading="lazy" width="540" height="675">'
                    f'<b>{e(i["jp"])}</b><span>{e(i["issue"])} · {e(i["date"][5:].replace("-", "/"))}</span></a>' for i in items[:8])
    return (f'<section class="issues" aria-label="Latest issues"><h2>最新号 <small><a href="{prefix}issues/">ALL ISSUES →</a></small></h2>'
            f'<div class="row">{cards}</div></section>')

def page(items):
    body = ''.join(f'<article id="{i["id"]}" class="iss"><p class="kicker">{e(i["issue"])} · {e(i["place"])} · {e(i["date"])}</p>'
                   f'<h2>{e(i["jp"])}</h2><p class="en">{e(i["en"])}</p><div class="pages">'
                   + ''.join(f'<img src="../{p}" alt="{e(i["jp"])} page {n + 1}" loading="lazy" width="1080" height="1350">' for n, p in enumerate(i['pages']))
                   + '</div></article>' for i in items)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Issues — with KORU</title><meta name="description" content="Every issue of with KORU, field notes for hungry travelers in Japan: where to eat, what to order, prices, house rules and maps. By Yu, a local office worker in Tokyo, and his dog Koru.">
<link rel="canonical" href="https://yuonozawa.github.io/koru-tokyo-reels/issues/">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@800;900&family=Noto+Sans+JP:wght@900&family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap">
<style>*{{box-sizing:border-box}}body{{margin:0;padding:20px 16px 64px;font:16px/1.6 "Zen Kaku Gothic New",system-ui,sans-serif}}
main{{max-width:640px;margin:0 auto}}.iss{{margin:28px 0 40px;border-top:3px solid #111;padding-top:10px}}.iss h2{{font-size:28px;margin:4px 0 0}}
.en{{margin:2px 0 12px;font:800 14px "Archivo",sans-serif;letter-spacing:.04em;text-transform:uppercase}}
.pages{{display:grid;gap:12px}}.pages img{{width:100%;height:auto;display:block;border:2px solid #111}}
.top h1{{font-size:40px;margin:16px 0 0}}.top p{{margin:4px 0 0;color:#55514A}}{NAV_CSS}</style>
<link rel="stylesheet" href="../koru.css"></head><body>
{nav('../', '')}
<main><div class="top"><p class="kicker">FIELD NOTES FOR HUNGRY TRAVELERS IN JAPAN</p><h1>全号</h1><p>Every issue, page by page. The same issues come out on Instagram, <a href="https://www.instagram.com/koru.tokyo_guide/">@koru.tokyo_guide</a>.</p></div>
{body}</main><footer style="max-width:640px;margin:0 auto;font-size:13px">Facts only, no paid placement. Photos by Yu. <a href="../privacy/">Privacy</a></footer></body></html>'''

def main():
    items = issues()
    open(os.path.join(ROOT, 'site/issues/index.html'), 'w').write(page(items))
    p = os.path.join(ROOT, 'site/index.html'); t = open(p).read()
    block = '<!--issues-->' + strip(items) + '<!--/issues-->'
    t = re.sub(r'<!--issues-->.*?<!--/issues-->', block, t, flags=re.S) if '<!--issues-->' in t else t.replace('<div class="keys">', block + '\n  <div class="keys">', 1)
    open(p, 'w').write(t)
    print(len(items), 'issues')

if __name__ == '__main__':
    main()
