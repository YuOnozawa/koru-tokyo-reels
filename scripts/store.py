"""Video store housekeeping (runs on GitHub Actions).
Videos are kept as assets of the 'video-store' release, not in git, so the repository stays small.
  python scripts/store.py site _site/videos   copy unposted videos into the Pages build
  python scripts/store.py archive             send posted videos to Google Drive (Apps Script endpoint in
                                              config/archive.json), then delete them from the release
Needs GH_TOKEN and GITHUB_REPOSITORY. Never deletes an asset that was not confirmed archived."""
import json, os, subprocess, sys, urllib.request
R = os.environ.get('GITHUB_REPOSITORY', 'YuOnozawa/koru-tokyo-reels')
TAG = 'video-store'


def load(p, d):
    return json.load(open(p)) if os.path.exists(p) else d


def assets():
    out = subprocess.run(['gh', 'release', 'view', TAG, '-R', R, '--json', 'assets', '-q', '.assets[].name'],
                         capture_output=True, text=True)
    return [a for a in out.stdout.split() if a.endswith('.mp4')] if out.returncode == 0 else []


def posted_ids():
    return {p['id'] for p in load('state/posted.json', [])}


def cmd_site(dest):
    os.makedirs(dest, exist_ok=True)
    done = posted_ids()
    want = [a for a in assets() if a[:-4] not in done]
    for a in want:
        subprocess.run(['gh', 'release', 'download', TAG, '-R', R, '-p', a, '-D', dest, '--clobber'], check=True)
    # videos still committed in git (legacy) are served too
    if os.path.isdir('videos'):
        for f in os.listdir('videos'):
            if f.endswith('.mp4') and f[:-4] not in done and not os.path.exists(os.path.join(dest, f)):
                subprocess.run(['cp', os.path.join('videos', f), dest], check=True)
    print('site videos:', sorted(os.listdir(dest)))


def cmd_archive():
    ep = load('config/archive.json', {}).get('archive_endpoint', '').strip()
    if not ep:
        print('archive endpoint not set; keeping videos in the release'); return
    arch = load('state/archived.json', {})
    done = posted_ids()
    for a in assets():
        vid = a[:-4]
        if vid not in done:
            continue
        if vid not in arch:
            url = f'https://github.com/{R}/releases/download/{TAG}/{a}'
            body = json.dumps({'action': 'archive', 'url': url, 'name': a}).encode()
            try:
                req = urllib.request.Request(ep, data=body, headers={'Content-Type': 'text/plain'}, method='POST')
                with urllib.request.urlopen(req, timeout=120) as r:
                    res = json.loads(r.read().decode())
            except Exception as e:
                print('archive failed', a, e); continue
            if not res.get('ok') or not res.get('size'):
                print('archive not confirmed', a, res); continue
            arch[vid] = {'drive_id': res.get('id'), 'size': res.get('size')}
            json.dump(arch, open('state/archived.json', 'w'), indent=1)
            print('archived', a, res)
        subprocess.run(['gh', 'release', 'delete-asset', TAG, a, '-R', R, '-y'], check=False)
        print('removed from release', a)


if __name__ == '__main__':
    {'site': lambda: cmd_site(sys.argv[2]), 'archive': cmd_archive}[sys.argv[1]]()
