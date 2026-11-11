"""Cross-post newly published reels to YouTube Shorts (runs inside publish.yml, before the archive step).
Needs repo secrets YT_CLIENT_ID / YT_CLIENT_SECRET / YT_REFRESH_TOKEN (scope youtube.upload). Without them it exits quietly.
Note: until the Google API project passes YouTube's API audit, uploads are forced to private (YouTube policy)."""
import json, os, sys, urllib.request, urllib.parse, datetime
REPO = os.environ.get('GITHUB_REPOSITORY', 'YuOnozawa/koru-tokyo-reels')
CID, CSEC, RTOK = (os.environ.get(k, '') for k in ('YT_CLIENT_ID', 'YT_CLIENT_SECRET', 'YT_REFRESH_TOKEN'))
STATE = 'state/yt_posted.json'

def token():
    data = urllib.parse.urlencode({'client_id': CID, 'client_secret': CSEC, 'refresh_token': RTOK, 'grant_type': 'refresh_token'}).encode()
    return json.load(urllib.request.urlopen('https://oauth2.googleapis.com/token', data))['access_token']

def meta(cap):
    lines = [l for l in cap.split('\n') if l.strip()]
    title = lines[0][:90].strip() if lines else 'Tokyo food tip'
    if '#shorts' not in title.lower(): title = (title[:90 - 8] + ' #Shorts')
    desc = cap + '\n\nFree Tokyo food planner: https://yuonozawa.github.io/koru-tokyo-reels/'
    return title, desc[:4900]

def upload(tok, path, title, desc):
    body = json.dumps({'snippet': {'title': title, 'description': desc, 'categoryId': '19',
                                   'tags': ['Tokyo', 'Japan travel', 'Tokyo food', 'Akihabara', 'Asakusa', 'Ueno']},
                       'status': {'privacyStatus': 'public', 'selfDeclaredMadeForKids': False}}).encode()
    size = os.path.getsize(path)
    req = urllib.request.Request('https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status', body,
                                 {'Authorization': 'Bearer ' + tok, 'Content-Type': 'application/json; charset=UTF-8',
                                  'X-Upload-Content-Type': 'video/mp4', 'X-Upload-Content-Length': str(size)})
    loc = urllib.request.urlopen(req).headers['Location']
    put = urllib.request.Request(loc, open(path, 'rb').read(), {'Content-Type': 'video/mp4'}, method='PUT')
    return json.load(urllib.request.urlopen(put))

def main():
    if not (CID and CSEC and RTOK):
        print('yt: no credentials, skip'); return
    posted = json.load(open('state/posted.json'))
    done = json.load(open(STATE)) if os.path.exists(STATE) else []
    seen = {d['id'] for d in done}
    q = {it['id']: it for it in json.load(open('queue.json'))}
    since = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=24)
    todo = [p for p in posted if p['id'] not in seen and p['id'] in q and 'file' in q[p['id']] and
            datetime.datetime.strptime(p['published_at'][:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=datetime.timezone.utc) > since]
    if not todo:
        print('yt: nothing new'); return
    tok = token()
    for p in todo[:2]:
        name = os.path.basename(q[p['id']]['file'])
        url = 'https://github.com/%s/releases/download/video-store/%s' % (REPO, name)
        path = '/tmp/' + name
        try:
            urllib.request.urlretrieve(url, path)
            title, desc = meta(q[p['id']]['caption'])
            r = upload(tok, path, title, desc)
            done.append({'id': p['id'], 'yt_id': r.get('id'), 'privacy': r.get('status', {}).get('privacyStatus'), 'at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%MZ')})
            print('yt: uploaded', p['id'], r.get('id'))
        except Exception as e:
            print('yt: failed', p['id'], e)
    json.dump(done, open(STATE, 'w'), indent=1)

if __name__ == '__main__':
    main()
