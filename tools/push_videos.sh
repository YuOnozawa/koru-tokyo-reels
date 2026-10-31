#!/bin/sh
# Send rendered videos to GitHub without putting them in main's history:
# pushes them to the throwaway branch 'incoming'; the Ingest workflow moves them to the 'video-store'
# release and deletes the branch. Then check: gh run list --workflow ingest.yml -L 1 Usage: tools/push_videos.sh path/to/a.mp4 [more.mp4 ...]
set -e
T=$(mktemp -d); mkdir -p "$T/videos"; cp "$@" "$T/videos/"
cd "$T" && git init -q && git checkout -q -b incoming && git add videos
git -c user.name=koru-bot -c user.email=koru-bot@users.noreply.github.com commit -qm "incoming videos"
git push -q --force https://github.com/YuOnozawa/koru-tokyo-reels incoming
cd / && rm -rf "$T"
# a push to 'incoming' can't trigger the workflow (the branch has no workflow files), so start it explicitly
gh api -X POST repos/YuOnozawa/koru-tokyo-reels/actions/workflows/ingest.yml/dispatches -f ref=main
echo "pushed $# video(s) to incoming; ingest started"
