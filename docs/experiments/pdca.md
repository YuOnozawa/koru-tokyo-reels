# PDCA board — @koru.tokyo_guide (theme: challenge)

Rule: every 2–3 days one hypothesis gets a verdict. Kill fast, double down fast. Log every test here.
North-star: followers. Leading indicators (per reel, from insights): **completion = avg watch time ÷ length**, reach, shares (sends), saves, follows.
Decision rule (until we have more volume): a variant "wins" if completion is ≥30% higher than baseline on ≥3 reels, or it produces follows when baseline produces none.

## Baseline (11/2–11/4, v2 text-card reels, n≈20)
- Reach ~100 per reel, flat. Saves/shares ~0. Follows 0. Followers 4.
- Avg watch ~2–3.8 s on 25–40 s reels → completion ~8–12%.
- First real-photo reel (f_02 ginkgo, 15.7 s): avg watch 4.7 s → ~30%. Real-photo izakaya (f_03, 26.6 s): 3.3 s → ~12%.
- Read: Instagram gives every reel ~100 test views; nothing is earning a second push. Retention is the bottleneck, not posting volume.

## Running / queued tests
| # | Hypothesis | Variant vs control | Dates | Metric | Status |
|---|---|---|---|---|---|
| E1 | Content type drives follows | hacks vs shops vs roundups (v2) | 11/2–11/5 | follower Δ/day | ended early: all ~100 reach, 0 follows → no signal; format is the bottleneck |
| E2 | Fast real-footage format (v3) beats text cards | same scripts as v3 (stock footage, 1–2 s cuts, word captions) vs v2 rounds | 11/6–11/7 vs 11/3–11/4 | completion, reach | running |
| E3 | Shorter wins: ≤12 s single-hook loops beat 20–30 s | 7–12 s "one fact" loops vs 20 s v3 | from 11/8 | completion, reach, shares | queued |
| E4 | Real-life (Yu photos) beats stock | Yu-photo reels vs stock v3 | ongoing as photos arrive | completion | collecting |
| E5 | Comment-bait ending ("which one? 1–4") lifts comments → reach | CTA A/B | from 11/9 | comments, reach | queued |
| E6 | Search pages bring planner users | 31 /find/ pages live 11/4 | weekly | plan_print, *_ig vs web | waiting on Search Console |

## Log
- 2026-11-05: Yu: "PDCAと仮説検証をバンバン、チャレンジがテーマ". Ended E1 early, launched E2 by converting the 11/6–11/7 queue to v3 with stock footage.
- 2026-11-05 (Yu: change from today): 11/5 10:00/13:00/21:00 also switched to v3. 11/6-11/7: 12 reels v3 + caption factorial (H4 question line, H5 comment ask, H6 hashtag count). 11/8: 4 short loops (H3), guess-the-price quiz (H8/H9), silent text+music (H8), POV (H8), stock-footage local moves. Scoreboard auto-updates after the daily insights run.
- 2026-11-06 production run: queued 11/9 s_05_cash (H3 short loop, cash-only 68/299) and b_10_ginkgo_ueno (H11 A: decision-settling seasonal; first-line search sentence). Added H11. Held the 11/6 proposals A (comment→DM) and C (Yu footage) until Yu agrees.
- 2026-11-06: Yu approved all 11/6 proposals. A (comment→DM map) wired: ?via=dm tagging + area links, H12 on b_10 (11/9). PR #2 merge blocked for this session (needs Yu's click). Account Status: all green (no reach limits). Synthetic persona panel tried: no predictive signal beyond video length (see tools/panel/README.md); kept as QA reviewer, forecasts logged for prospective scoring.
- 2026-11-06: PR #2 merged by Yu. Live check: opened the planner with ?via=test → events sheet row 'planner_open_test 1' (test traffic is tagged _test, so no manual subtraction needed). Funnel events now live: planner_open, plan_print, shop_page_click, shop_map_click, route_map_click (+ _ig / _dm suffixes).
- 2026-11-08 production run — verdicts: H1 v3 beats v2 (completion 17% vs 11%, n=15/24, +57%) → v2 stopped; 22 v2 reels for 11/10-16 moved to queue_hold.json (to be remade as v3 only if the topic is still worth it). H4 question line, H6 hashtag count, H7 posting hour: no clear difference (keep testing passively, no more dedicated slots). H5: both arms 0 comments, so no verdict despite the scoreboard's "+inf%" (it is reading saves; fix the metric). Signal to double down: late-night topic (c_08: 4 shares, 2 saves, 3 likes on 140 reach) → 11/10 = three late-night reels (≤15 s where possible).
- 2026-11-08: queued 11/10 late-night series n_02 (07:00, H12 A comment AKIBA), n_03 (13:00, 7.5 s loop), n_04 (21:00, H12 B). New H13: open-at-this-hour topic → saves+shares.
- 2026-11-10 production run — read: c_08 late-night list kept growing (reach 322, saves 4, shares 4): the only reel so far to get a second push. H3 short loops: completion 48% vs 17% but fewer seconds watched (≈3 s) and the same reach (~124) → shorts don't earn more distribution; keep a few, not the priority. H4 "statement beats question" (+44% reach) is carried by c_08 alone; treat as not proven. H12: b_10 (Comment UENO) got 0 comments in 24 h. Link taps still 0. Panel forecasts: no predictive value (tools/panel/README.md).
- Decision: double down on "open after 10pm" lists by area (c_08 format, ~20 s, 4 spots): 11/11 Ueno (Comment UENO), Asakusa (link in bio), Kanda (Comment KANDA).

## 2026-11-12 format change (Yu: 「投稿の形式変えなきゃじゃね？」「勝ち筋ほんとに見えてんのか？」)
- Check: 50 reels, median reach 108, 86% in 90–145 regardless of topic; avg watch 3.6s of ~24s (17%); 50 reels → 18 saves, 7 shares, 0 comments; link taps 0/day. Topic A/B inside one template can't find a win: the template itself fails the first 3 seconds.
- Yu: theme need not be fixed; magazine branding is good; target = adult travelers staying in Tokyo, fairly affluent, don't want a bad meal or to waste money, want delicious over cheap & fun; cheap spots OK as 番外編 (Extra); "店よりも見せ方".
- Act: stopped AI-voice + stock-footage reels. New format: magazine carousels "KORU · Tokyo Field Notes" (tools/carousel). Issues: No.03 Domannaka (11/12 12:00, Yu photos), No.04 Five dinners worth booking (11/12 20:00), Extra 01 Tenkaippin (11/13 19:00). Held: midnight list (mixed with cheap/smoking spots).
- New tests: H14 carousel vs old reel (reach), H15 no-fail vs cheap&fun (saves/reach). Kill rule: if 6 carousels also sit near 100 reach, Instagram stops being the main channel → Search/Maps.
