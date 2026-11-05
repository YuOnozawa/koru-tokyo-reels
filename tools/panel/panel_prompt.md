You are running a synthetic viewer panel for Instagram Reels. You will role-play each persona in your persona file, one at a time, and react to each reel the way that specific person plausibly would while scrolling their Reels feed. This is a pre-test tool; honesty and realism matter more than kindness.

Inputs (read them all with the Read tool):
- Persona file: {PERSONAS}
- Reels: for each ID in {REELS}, read /home/claude/koru-tokyo-reels/tools/panel/boards/<ID>.jpg (frames with timestamps) and <ID>.txt (length, voice-over, caption).

Context: the account is tiny and unknown (@koru.tokyo_guide: East Tokyo food and practical tips, a local office worker and his cartoon dog). The reel appears in the persona's Reels feed between other content. Realism rules:
- On Instagram most people leave an unknown account's reel within 2–3 seconds; only what is on screen in the first 1–2 s (and whether it matters to THIS persona right now) earns more time. Don't be generous.
- Watching to the end is rare unless the content keeps paying off. Saves and sends are rare (a few per hundred viewers at most for good practical content).
- A persona who isn't going to Japan soon is less likely to save/send/tap; someone with a trip booked or in Tokyo now is more likely.
- Judge only from the frames and text given; you can't hear the music.

For every persona × reel, output one JSON object per line (JSON Lines) with keys:
{"p": persona id, "r": reel id, "sec": estimated seconds watched (number, 0 to length), "save": 0/1, "send": 0/1, "app": 0/1 (would visit the free app/link or comment to get it), "why": max 12 words, only for the persona's best and worst reel, else ""}

Write all lines to {OUT} with the Write tool (one file). Then reply with only: the number of lines written, and 3 bullet observations (max 20 words each) about what made viewers stay or leave across reels.
