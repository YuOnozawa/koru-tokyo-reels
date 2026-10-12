"""Instagram API (Instagram Login) helper for @koru.tokyo_guide.

Commands (run by GitHub Actions; token comes from the IG_TOKEN secret):
  python scripts/ig.py check              -> print account the token belongs to
  python scripts/ig.py publish [--id ID]  -> publish due items from queue.json (or one forced item)
  python scripts/ig.py insights           -> save metrics of recent posts to state/insights.json
  python scripts/ig.py refresh            -> extend the long-lived token (60 days)
Stdlib only.
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone

API = 'https://graph.instagram.com/v23.0'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN = os.environ.get('IG_TOKEN', '').strip()
REPO = os.environ.get('GITHUB_REPOSITORY', 'YuOnozawa/koru-tokyo-reels')
BRANCH = os.environ.get('GITHUB_REF_NAME', 'main')


def call(method, path, params=None, base=API):
    params = dict(params or {}); params['access_token'] = TOKEN
    url = f'{base}/{path}' if not path.startswith('http') else path
    data = None
    if method == 'GET':
        url += '?' + urllib.parse.urlencode(params)
    else:
        data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, data=data, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors='replace')
        raise SystemExit(f'API error {e.code} on {method} {path}: {body}')


def load(name, default):
    p = os.path.join(ROOT, name)
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else default


def save(name, obj):
    p = os.path.join(ROOT, name); os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(obj, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def me():
    return call('GET', 'me', {'fields': 'user_id,username,account_type,media_count'})


def public_url(rel):
    owner, name = REPO.split('/')
    pages = f'https://{owner.lower()}.github.io/{name}/{rel}'
    try:
        with urllib.request.urlopen(urllib.request.Request(pages, method='HEAD'), timeout=20) as r:
            if r.status == 200:
                return pages
    except Exception:
        pass
    return f'https://raw.githubusercontent.com/{REPO}/{BRANCH}/{rel}'


def publish_one(uid, item):
    url = public_url(item['file'])
    print(f"[{item['id']}] video_url={url}")
    c = call('POST', f'{uid}/media', {'media_type': 'REELS', 'video_url': url,
                                      'caption': item['caption'], 'share_to_feed': 'true'})
    cid = c['id']
    for i in range(30):  # up to ~15 min
        time.sleep(30)
        st = call('GET', cid, {'fields': 'status_code,status'})
        print(f"  status {st.get('status_code')} {st.get('status', '')}")
        if st.get('status_code') == 'FINISHED':
            break
        if st.get('status_code') in ('ERROR', 'EXPIRED'):
            raise SystemExit(f"container failed: {st}")
    else:
        raise SystemExit('container not ready in time')
    p = call('POST', f'{uid}/media_publish', {'creation_id': cid})
    info = call('GET', p['id'], {'fields': 'permalink,timestamp,media_product_type'})
    print(f"  published {info}")
    return {'id': item['id'], 'media_id': p['id'], 'permalink': info.get('permalink'),
            'published_at': info.get('timestamp')}


def cmd_publish(force=None):
    u = me(); uid = u['user_id']
    queue = load('queue.json', []); posted = load('state/posted.json', [])
    done = {p['id'] for p in posted}
    now = datetime.now(timezone.utc)
    due = [q for q in queue if q['id'] not in done and
           (q['id'] == force or (force is None and datetime.fromisoformat(q['publish_at']) <= now))]
    if not due:
        print('nothing due'); return
    item = sorted(due, key=lambda q: q['publish_at'])[0]  # one per run, oldest first
    posted.append(publish_one(uid, item)); save('state/posted.json', posted)


def cmd_insights():
    u = me(); uid = u['user_id']
    media = call('GET', f'{uid}/media', {'fields': 'id,caption,permalink,timestamp,media_product_type', 'limit': 50})
    out = {'fetched_at': datetime.now(timezone.utc).isoformat(), 'account': u, 'media': []}
    for m in media.get('data', []):
        row = {k: m.get(k) for k in ('id', 'permalink', 'timestamp', 'media_product_type')}
        row['caption_head'] = (m.get('caption') or '')[:60]
        try:
            ins = call('GET', f"{m['id']}/insights", {
                'metric': 'reach,views,likes,comments,saved,shares,total_interactions,ig_reels_avg_watch_time,ig_reels_video_view_total_time'})
            for d in ins.get('data', []):
                row[d['name']] = (d.get('values') or [{}])[0].get('value', d.get('total_value', {}).get('value'))
        except SystemExit as e:
            row['insights_error'] = str(e)[:300]
        out['media'].append(row)
    try:
        acc = call('GET', f'{uid}', {'fields': 'followers_count,follows_count,media_count'})
        out['account'].update(acc)
    except SystemExit as e:
        out['account_error'] = str(e)[:300]
    save('state/insights.json', out)
    hist = load('state/followers_history.json', [])
    hist.append({'at': out['fetched_at'], 'followers': out['account'].get('followers_count')})
    save('state/followers_history.json', hist)
    print(json.dumps(out, ensure_ascii=False)[:2000])


def cmd_refresh():
    r = call('GET', 'https://graph.instagram.com/refresh_access_token', {'grant_type': 'ig_refresh_token'})
    days = int(r.get('expires_in', 0)) // 86400
    same = r.get('access_token') == TOKEN
    print(f'refreshed: valid for {days} more days; token string unchanged={same}')
    save('state/token_status.json', {'refreshed_at': datetime.now(timezone.utc).isoformat(),
                                     'valid_days': days, 'token_string_unchanged': same})
    if not same:
        print('::warning::Instagram returned a new token string. Update the IG_TOKEN secret with it.')


if __name__ == '__main__':
    if not TOKEN:
        raise SystemExit('IG_TOKEN secret is missing')
    a = sys.argv[1:]
    if not a or a[0] == 'check':
        u = me(); print(json.dumps(u, ensure_ascii=False))
        q = load('queue.json', [])
        probe = public_url(q[0]['file']) if q else None
        save('state/account.json', {'checked_at': datetime.now(timezone.utc).isoformat(),
                                    'username': u.get('username'), 'account_type': u.get('account_type'),
                                    'media_count': u.get('media_count'), 'video_url_used': probe})
    elif a[0] == 'publish':
        cmd_publish(a[2] if len(a) > 2 and a[1] == '--id' else None)
    elif a[0] == 'insights':
        cmd_insights()
    elif a[0] == 'refresh':
        cmd_refresh()
