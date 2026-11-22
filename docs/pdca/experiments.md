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

- 11/20 18:00 read: H2 arm r_x_07 (Yu's photos full screen, text <10%, music) = 3 at 24 h. Hook reels with music since: Asakusa 6, Naha Kokabu 6, mornings 3.
  With the full history: v1 (AI voice, no music; stock video or photos) 91/98 hit, median 110. Every music reel since 11/12: 2/18.
  → The common factor of the drop is music + stills, not text. Next reads: H1 (voice on stills) 11/22, H5 (voice on video) 11/25.

- 11/22 18:00 read: H1 arm r_x_08 (Yu photos + AI voice, no music) = 17 at 24 h. Followers 15 → 18 (follow runs back since 11/20).
  Still pending: H5 (stock video + voice) 11/25–26, H4a (exact v1 format) 11/27–28.

## Weekly retro (11/22, week 11/16–11/22)
- Reels posted: 14 (12 read at 24 h; r_c_17 / r_c_09 pending). Carousels: 9 (all 0–2 reach).
- Reach24 median **10**, hit rate (≥80) **1/12**. Followers 14 → **18** (+4; the rise is from 11/20, when the follow runs came back).
- Top 3: r_x_04_kitasenju 110 (Yu's own Saturday, his photos, one named neighborhood), r_c_08_eel 69 ("where to book eel", concrete & bookable), r_c_10_jimbocho 18.
- Bottom 3: r_c_14_mornings 3 (watch 7.2 s but no batch), r_x_07_naha_miso 3 (Okinawa, stills + music), r_c_12_asakusa 5 (generic "5 no-fail stops" in the most-covered area).
- Why (guess): both reels that got a batch are from 11/16 and are specific (one person's day / one dish you book); generic lists and Okinawa extras stall at <10.
  Watch time does not rescue a reel that never gets the batch (mornings 7.2 s → 3).
- Benchmarks: not refreshed this week (no Chrome on this run).

### Winning pattern (as of 11/22)
1. The only proven format is still v1: AI voice, no music, moving stock video, 6–11 s (91/98 hits). Every music + stills reel since 11/12: median ~8.
2. Within the music era, what still lifts: Yu's own day in one named neighborhood (110) and a concrete, bookable dish (69) — not "5 places in Asakusa".
3. Voice is helping but stills are not enough: stills + voice 17 vs stills + music 3.

### Next week (decide by 11/29) — only these two
- **T1 = H5 (visual only):** stock video + AI voice (r_v_01–04, 11/24–26) vs stills + AI voice (H1: r_x_08/09/10). Same voice, change = video vs photo.
- **T2 = H4a (format reproduction):** exact v1 compose (r_h4_01/02, 11/27). If it hits → the format, not account age, is the cause (closes H4).
- Frozen until T1/T2 read: H3, H6, H7. No new style changes on the music arm (r_c_* keep running as the control).

## Hypotheses (ranked)
| # | Hypothesis | Test | Status |
|---|---|---|---|
| H1 | Voice narration (original audio) instead of the shared music track brings back the test batch | Same clean photo reels, narration instead of music: r_x_08 (11/21), r_x_09, r_x_10. Control r_x_07 (music). | **pending (n=1/3): r_x_08 = 17** (vs r_x_07 3, music reels median 8). Better, not a hit. r_x_09/10 read 11/25–26; now the control arm for H5 |
| H2 | Text-led visuals block recommendation | v4 clean (text <10%) + music: r_x_07 (11/19) | **not supported (11/20): reach24 = 3.** Less text alone does not bring the batch back |
| H3 | Expansion past ~100 needs watch ≥ 6 s; late-night and "money/etiquette hack" topics hold attention | Next 3 voice reels: one late-night, one hack, one normal; compare watch and reach | queued |
| H5 | Real moving video beats still photos (all benchmarks are video) | Free stock video clips (Mixkit/Pexels, no credit needed — Yu OK 11/20) + Yu's clips when he has them, same voice; vs H1 stills+voice | **T1 next week:** r_v_01–04 post 11/24–26, read 11/25–27 |
| H6 | Timely, actionable topics get sends: illuminations near our areas, year-end/New Year hours of our shops (Dec 29–Jan 3) | 2 timely issues in Dec; metric = shares per reach | plan for Dec 1–15 |
| H4a | Exact v1 format (compose_v3: stock video + AI voice + big text + chips, 6–11 s) still works today | r_h4_01 seat charge, r_h4_02 closed Mondays (11/27). v1 had s_03_sunday 294? / s_05_cash ~100 on similar topics | **T2 next week:** posts 11/27, read 11/28 |
| H7 | Volume/duplication: 4 posts a day, each issue posted twice (reel + carousel of the same pages), drags the account | If H4a/H5 hit while hook reels keep failing, cut to 1–2 reels a day and drop the paired carousel | idea |
| H4 | Time (new-account boost ended) — not format | If H1 and H2 both fail, rerun one old v1 reel style (render_kit) with a new topic | backup |
