#!/bin/sh
# Send rendered videos to GitHub without putting them in main's history:
# pushes them to the throwaway branch 'incoming'; the Ingest workflow moves them to the 'video-store'
# release and deletes the branch. Usage: tools/push_videos.sh path/to/a.mp4 [more.mp4 ...]
set -e
T=$(mktemp -d); mkdir -p "$T/videos"; cp "$@" "$T/videos/"
cd "$T" && git init -q && git checkout -q -b incoming && git add videos
git -c user.name=koru-bot -c user.email=koru-bot@users.noreply.github.com commit -qm "incoming videos"
git push -q --force https://github.com/YuOnozawa/koru-tokyo-reels incoming
cd / && rm -rf "$T"; echo "pushed $# video(s) to incoming"
