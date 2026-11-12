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

## 2026-11-12 fact fixes from Yu (Domannaka Akihabara Bettei)
- Uni hand roll has NO caviar. Potato-salad tower is topped with shaved CHEESE, not bonito. Fixed in data/shops.json, site/planner/shops.json, c_03 spec + caption.
- Already posted with the caviar error: f_03_domannaka reel (caption + on-screen "UNI + CAVIAR"). API can't edit captions; needs a manual caption edit or archive.
- Taste note from Yu: don't feature trivia like "fresh wasabi in a cup" as the selling point of a dish. Lead with what makes the dish worth ordering.
- Rule: describe only what is visible in Yu's photo or confirmed by Yu; never infer toppings.

## 2026-11-12 08:00 production run (編集長メモ)
- Numbers: no new-format issue has posted yet (first: c_03 Domannaka reel 11/12 12:00, carousel 20:00), so H14/H15/H16 have n=0. Account (11/11 15:05 UTC): 28-day reach 471, profile views 4, link taps 0, engaged 2 — still the old-template baseline. First read on 11/14; kill-rule check after the 6th new issue (11/17).
- Made: Extra 03 「サウナのあとで」 Spa Metsa Otaka (Yu's photos, jumps the queue per plan) → 11/18; No.07 「店で使う十のひとこと」 Ten lines → 11/19.
- Extra 03 facts re-checked on the official site (prices, hours) + FAQ. New house rules found that the old sp_02 reel didn't have: towels are NOT included (¥300 set), lounge wear only with the rock-bath ticket, tattoos only if two of their cover stickers hide them, no outside drinks. These are exactly the "don't fail" details for our reader.
- No.07 has no shops, so no map/review pages (they apply to shop issues). Romaji is set as the big second line of each card, not the small print.
- Fixes: cover masthead — "番外編 EXTRA 0x" touched the KORU logo; covers now show "EXTRA 0x" (番外編 is already in the cover headline). x_01/x_02 covers re-rendered. render.py rules: start / jp_size / en_size / per-item cap. reel.py: zoom_only (page files), pages shown whole are held 1.5 s more.
- Balance note: 3 Extras (x_01–x_03) among 8 issues. Next run should bring main 'no-fail' issues (No.08 東の鰻, No.09 夜10時からの晩ごはん) so H15 gets an A arm.

## 2026-11-12 cadence: 2 issues a day (Yu: 「試験だからもっと出してみない？」)
- Slots (JST): issue A reel 12:00 + carousel 20:00; issue B carousel 08:00 + reel 17:00. Today: c_03 (A) + c_05 (B, 17:00/22:00).
- Queue compressed: the 8 built issues now run 11/12–11/15 (was 11/12–11/19). Six new-format issues are out by 11/14, so the kill-rule read moves up to ~11/16.
- Production runs become daily (2 issues per run). Posting hour becomes a passive variable (08/12/17/20/22).

- 2026-11-12 (same day): made No.08 東の鰻 (A, 11/16) and No.09 夜10時からの晩ごはん (B, 11/16). Tabelog score/count, 20-latest-review themes and house rules saved in shops.json.
- Stale late-night facts found while re-checking (Tabelog, Nov 12): Hon-Tosaya now closes 23:00 (food LO 22:00), not 2:00; Coffee Lodge Akaishi now 9:00–20:00, not 3:00; Daitoryo 23:30, not 24:00. Already-posted reels with the old hours: c_08_late (Akaishi), n_04_midnight (Akaishi, Daitoryo), n_06_asakusa_late (Akaishi, Hon-Tosaya). Suggest Yu archives them with the other old reels. Rule: late-night hours are re-checked within 7 days of posting.
- Scheduling: a production reminder for 11/14 08:00 (old every-2-days chain) could not be cancelled from here; when it fires, do the normal daily run and do NOT schedule another 2-day reminder.

## 2026-11-12 app redesign (Yu: 「アプリ側のデザインも変えないとだね？」)
- The web app (GitHub Pages) now wears the magazine look: site/koru.css is loaded last on all 340 pages and re-maps each page's
  own tokens to paper/ink/red/yellow, square corners, flat ink borders, heavy Noto Sans JP headings, "with KORU" masthead on the nav.
  Fonts: Dela Gothic One / DotGothic16 → Noto Sans JP 900 / Archivo. Builders (build_shop_pages.py, sitenav.py, planner.js) patched so rebuilds keep it.
- Home rebranded: "with KORU — 日本を旅する人の、食の手帖。" + 最新号 strip (issues already out, JST). New page /issues/ with every page of every issue.
  tools/build_issues.py runs in the Pages workflow, which now also runs daily at 00:03 JST.
- Funnel to watch: home_open → issues/ visits, link taps from the bio.

## 2026-11-12 shop pages shaped like an AI answer card (Yu shared ChatGPT's restaurant card)
- ChatGPT answers "where to eat" with: rating + sources, what people say, notable menu, atmosphere, good-to-know (price, booking, English menu),
  and it flagged that hours differ between sources. Our edge for being the cited source: first-hand, dated facts and house rules.
- Shop pages now have the same sections, magazine-styled: 評判 WHAT PEOPLE SAY (Tabelog score/count + our dated 20-review summary, never quoted),
  注目のメニュー WHAT TO ORDER, 知っておきたいこと GOOD TO KNOW (facts + checked house rules + 'checked on' date). Titles now '| with KORU'.
- Next: fill review_summary / house_rules for more shops (13/306 now), Yu's picks first; watch Search Console + referrals from chatgpt.com.

## 2026-11-12 21:20 bug: reel skipped as a "duplicate" of its carousel
- r_f_00_about (19:00) was recorded as already posted (it matched f_00_about's caption start) and its video was archived; nothing posted.
  Same would have hit c_03 (20:00) and c_05 (22:00). Cause: already_posted() compared only the first 80 chars, and a reel and the carousel
  of one issue share the opening. Fix: compare start AND end (the tails differ). r_f_00_about re-queued, video re-pushed.

## 2026-11-13 08:00 production run (編集長メモ)
- First numbers for the new format (insights 11/12 23:01 UTC, 11–19 h after posting):
  - Magazine reels: r_c_03 reach 15 (avg watch 4.0 s), r_c_05 32 (3.2 s), r_f_00 16 (2.7 s).
  - Old AI-voice reels at a similar age: reach 100–150 (avg watch 3.5–6.5 s).
  - Carousels: reach 1–2 each (only ~11 followers see them; carousels get no non-follower push yet). Saves 0, shares 0.
  - Account: profile views 4 → 31/day (follow/like rounds are working), link taps still 0, followers 9 → 11.
- Read: the magazine reels are getting ~1/5 of the old reels' first push. Likely causes: a still, page-turning video looks like a slideshow
  (weak first second, no motion, no voice), and 7 posts in one day split what little push there is. Carousels need followers first.
- Kill rule check (6 new-format issues by 11/14): already below 100. Proposal to Yu (style decision, his call):
  (a) keep the magazine for carousels + the app (reference, saves, AI/search), (b) test one reel variant with a moving first 2 s
  (Yu's own photo, full-bleed push-in + one big question as the hook) and 15–20 s total, (c) put more weight on the shop pages for Google/ChatGPT.
- Made: No.10 神保町、カレーの名店 (A, 11/17) and No.11 Yuが通う、秋葉原の昼 (B, 11/17). Tabelog score/review themes/house rules for 11 shops into shops.json.
  Conflicting hours found and recorded (Onihei dinner, Ippekoppe Monday closure, Minogasa weekends) — Tabelog Nov 2026 used, noted in shops.json.
