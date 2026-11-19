# Experiments (PDCA)

Loop: find what hits → work out why → test one change at a time → keep the winner → repeat.
Numbers: docs/pdca/summary.md and dataset.csv (auto every 6 h). Reach is compared at 24 h.
Decision rule: an arm needs n ≥ 3 reels; "works" = median reach24 ≥ 80 (the old test-batch floor) or ≥ 2× the control.

## What we know (11/20 retro)
- Stage 1 — getting the test batch: 70 of 75 reels from 10/21–11/11 reached ~100 non-followers in 24 h (median 108).
  From 11/12, 2 of 16. The break is one day, not a slow fade.
- What changed on 11/12 (all at once): audio (AI voice narration → the same Mixkit music track on every reel, no voice);
  visuals (stock/AI photos with narration cards → text-led pages / big type); carousels started; app/about posts.
- Stage 2 — going past the batch: only c_08 late-night (321). The top 3 reels all had watch ≥ 6.5 s
  (late night ×2, otoshi hack). Most v1 reels sat at ~3.6 s and never left the batch.
- Account Status: no recommendation restriction (Yu checked 11/19).

## Benchmarks (11/20, other accounts' top reels, read in the app)
| account | followers | top reel | views | what it is |
|---|---|---|---|---|
| tokyocheapo | 298k | 10 illumination spots | 624k (5.8k sends) | real street footage, "2. Roppongi Hills" one-line label, dates list in caption, seasonal |
| tokyocheapo | 298k | Kagurazaka cat parade | 499k | real footage of the event, one small label, date/times in caption |
| paolofromtokyo | 167k | electric salt spoon | 736k | voiceover + subtitles, hand-held phone video, "Japan changed X" hook |
| japan_walker_ | 2.18M | snowy Sapporo alley | 397k | moody real footage, no text |
| thetokyochapter | 55k | Disney show tip for kids | 121k (3.5k sends) | lo-fi phone video with a text block, practical tip |
| "tokyo eats" search | – | top tiles | – | food in motion (pouring, cutting, eating), "5 spots to try 📍Shibuya" |
Patterns: (1) every top reel is real moving video, none are still photos; (2) the hook is the picture plus ≤6 words or a spoken line;
(3) the caption carries the list (places, dates, hours) → saves and sends; (4) timely/seasonal info drives sends (5.8k);
(5) music is fine for them, so audio alone may not be our block — stills may be.

## Hypotheses (ranked)
| # | Hypothesis | Test | Status |
|---|---|---|---|
| H1 | Voice narration (original audio) instead of the shared music track brings back the test batch | Same clean photo reels, narration instead of music: r_x_08 (11/21), r_x_09, r_x_10. Control r_x_07 (music). | running from 11/21 |
| H2 | Text-led visuals block recommendation | v4 clean (text <10%) + music: r_x_07 (11/19). If H1 arm hits and this doesn't, audio > visuals | reading |
| H3 | Expansion past ~100 needs watch ≥ 6 s; late-night and "money/etiquette hack" topics hold attention | Next 3 voice reels: one late-night, one hack, one normal; compare watch and reach | queued |
| H5 | Real moving video beats still photos (all benchmarks are video) | Free stock video clips (Mixkit/Pexels, no credit needed — Yu OK 11/20) + Yu's clips when he has them, same voice; vs H1 stills+voice | next after H1 |
| H6 | Timely, actionable topics get sends: illuminations near our areas, year-end/New Year hours of our shops (Dec 29–Jan 3) | 2 timely issues in Dec; metric = shares per reach | plan for Dec 1–15 |
| H4 | Time (new-account boost ended) — not format | If H1 and H2 both fail, rerun one old v1 reel style (render_kit) with a new topic | backup |
