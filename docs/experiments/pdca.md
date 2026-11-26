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

## 2026-11-14 08:00 production run (編集長メモ)
- Numbers (insights 11/13 23:01 UTC): followers 14 (+1). Account reach 83/day, profile views 21, link taps 0, engaged 2.
  - Reels, new format, ~8–19 h old: r_c_04 reach 10 (avg watch 1.0 s), r_x_01 7 (2.4 s), r_f_01 8 (1.0 s). Day-old: r_c_05 39 (2.8 s), r_f_00 20 (2.6 s), r_c_03 16 (3.8 s).
  - Carousels: reach 1–4. Saves 0, shares 0 on everything since 11/12.
  - Old AI-voice reels (11/10–11): 103–152 reach, avg watch 3.5–6.6 s.
- Read: no improvement; the magazine reels hold at ~10–40 reach and the watch time on list-type covers (c_04, f_01) is ~1 s, i.e. people
  swipe on the first frame. The Tenkaippin Extra (photo) holds 2.4 s and c_03 (Yu's food photos) 3.8 s: Yu's photos keep people longer than type covers.
  This supports proposal (b) (moving first 2 s on a real photo + a question), still waiting for Yu's go.
- Made: No.12 浅草の一日 (A, 11/18: reel 12:00, carousel 20:00) and No.13 上野、ゆっくり (B, 11/18: carousel 08:00, reel 17:00).
  10 shops updated in shops.json (Tabelog score/count, 20-review themes, house rules, checked 2026-11-14).
  Corrections: Imahan lunch can't be booked, no seating 14:30–16:00, last entry 19:00 (official site); Umezono now 10:00–17:00 weekdays
  (was 10–20), cash only; Miyako is Tue–Sat 12:00 start, closed Mon + 1st/3rd Sun (was 3rd Sun only); Mihashi weekends to 19:30.

## 2026-11-14 10:00 reels switched to hook reels (Yu: "go, from today")
- Why: page-flip reels reach 7-39 (avg watch 1.0-3.8 s) vs 100-150 for the old reels; type-only covers are swiped in ~1 s.
- New tools/carousel/hook.py: 0-2.4 s the question in big type over a moving Yu photo (red ground when no photo), one 2.3 s beat per
  dish/shop (Yu photo, or the issue's own list row as a clip), then the cover + "続きはカルーセルで" + SAVE. 14-17 s. Caption line 1 = the question.
- Rebuilt every queued reel from today: r_c_06 (12:00), r_x_02 (17:00), then 11/15-11/18. Carousels unchanged.
- Read after 2 days (11/16 08:00 run): reach and avg watch of r_c_06 / r_x_02 / r_c_07 / r_x_03 vs 7-39 and 1-3.8 s. Target: back to 100+.

## 2026-11-15 08:00 production run
- Hook reels, first numbers (insights 11/14 23:01 UTC): r_x_02 noodles reach 113 in 14 h (avg watch 3.1 s);
  r_c_06 Kanazawa 52 in 20 h (1.5 s). Page-flip reels were 8–39. Account reach 203/day (was 83–115). Followers 14.
  Read: the hook format brings reach back toward the old 100–150; watch time still short on Kanazawa (station-night
  first frame was replaced by crab, still 1.5 s). Keep hook reels; compare r_c_07 (type-only, no photo) tonight.
- Carousels still reach 1–4 (followers only). Saves/shares 0 everywhere.
- Made: No.14 東京の朝ごはん (11/19 A) and No.15 神田のそば (11/20 B). 9 shops checked on Tabelog (Shin-Tagoto opens 6:30, not 6:00).
- Kita-Senju Extra 04 moved to 11/16 B on Yu's word; No.09 late to 11/19 B.

## 2026-11-16 08:00 production run
- Insights 11/15 23:01 UTC. Hook reels so far: r_x_02 noodles 115 (3.2 s), r_c_06 Kanazawa 53 (1.9 s), r_x_03 sauna 10 (3.0 s),
  r_c_07 ten lines (type-only) 4 (2.1 s). Account reach/day 152–204. Followers 14. Saves/shares still 0.
- Read: big spread. The two with real food photos of famous bowls/crab did best; the sauna (photo) and the type-only reel did badly.
  Hypothesis: the first frame needs a dish people recognize (ramen, crab) — a lounge/wings or a red type card doesn't stop the scroll.
  Next test: for type-only issues, open on Yu's best food photo that fits the theme, if any; otherwise keep type and see 2 more.
- Made: No.16 上野の喫茶店 (11/20 A; smoking/non-smoking is the useful fact) and Extra 05 蔵前のおやつ (11/21 B). 8 shops checked.

## 2026-11-17 01:40 reel covers (Yu: 赤いトップ画のリールは再生が低い)
- Cause: hook reels without a photo started on a flat red frame with the text still sliding in, so the grid/feed thumbnail was a blank red tile.
  r_c_07 (red) 4 plays, r_c_08 eel (red) ~50; photo-led reels 115.
- Fix: hook.py now shows the question from frame 0, uses the issue's own cover (blurred, darkened) instead of flat red, adds the issue tag,
  and saves site/covers/r_<id>.jpg; ig.py sends it as cover_url. All 9 unposted reels rebuilt; dryrun with cover_url FINISHED.
- Covers for the two posted red reels sent to Yu to set by hand in the app.
- Still true: real food photos win. Ask Yu for photos; for type-only issues, test whether the new cover lifts plays.

## 2026-11-17 08:00 production run (no new issues today)
- Insights 11/16 23:01 UTC. Hook reels: Kita-Senju (Yu's croquette photo) reach 110, avg watch 3.1 s, 1 save (first save since the format change);
  eel (red type card first frame) 45 (1.8 s). Earlier: noodles 115, Kanazawa 53, sauna 12, ten lines 4. Followers 15 (+1). Account reach/day ~165.
- Read: Yu's food photos as the first frame = ~110 reach, every time. Type-only = 4–45. The new covers (text from frame 0, cover_url)
  start with r_c_10 today 12:00 — compare r_c_10/11/12 against 45.
- Not made today: Mac Chrome was not connected (only the Windows browser, which we never use), so Tabelog review counts could not be
  taken the usual way; WebFetch gives only rough counts. The queue is full through 11/21, so 11/22 is left for the next run.

## 2026-11-18 08:00 production run
- Insights 11/17 15:05 UTC. Hook reels: r_x_04 Kita-Senju 111 (3.1 s, 1 save), noodles 115 (3.2 s), eel 70 (1.5 s; was 45), sauna 12,
  ten lines 4. First type-only reels with the new cover (text from frame 0, cover_url): r_c_10 Jimbocho 13 in 11 h (1.4 s),
  r_c_11 Yu's regulars 6 in 7 h (3.6 s, 1 save). Account reach/day 151–167. Followers 15. Carousels reach 1–3.
- Read: the new cover did not lift type-only reels (13 vs eel 45→70 at a similar age). The lever is Yu's food photo, not the cover design.
  Yu's Okinawa issues (x_06–x_09, 11/18–11/24 B) all open on his photos: expect ~110 each. Type-only A issues stay a weak spot.
  Next test: once 11/19–11/21 numbers are in, compare B (Yu photos) vs A (type) on the same days.
- Made: No.17 浅草の天ぷら (中清・葵丸進, 11/22 A) and No.18 秋葉原で一杯 (赤津加・とら八, 11/23 A). Two shops each:
  Tabelog review lists for 大黒家/三定/尾張屋/殿 did not load without Mac Chrome; issues use only shops with 20-review counts.
  Useful facts found: 葵丸進 takes no bookings from overseas travelers; 赤津加 ¥450 cover vs とら八 none.

## 2026-11-19 08:00 Yu: 「ぜんっぜん数字伸びてなくね？」 — test: reel cover_url off
- Fact: every reel since cover_url started (11/17) is low: Jimbocho 18, regulars 9, Asakusa 4, Naha Kokabu (Yu's photo!) 4.
  Before: Yu-photo reels 110–115, eel 70, Kanazawa 53. Account reach/day fell from 150–200 to 29 (11/18). Followers 15 → 14. Likes 0 on every post.
- Two changes landed at the same time: (a) custom cover_url on reels from 11/17, (b) no follow/like runs since 11/15 (Mac Chrome offline).
- Test (reversible): cover_url removed from all 12 unposted reels (kept as cover_off). The first frame already shows the question over the photo,
  so the grid thumbnail is not a blank red tile any more. Read r_c_14 (11/19 12:00) and r_x_07 (17:00) after 6 h and 24 h vs 4.
  If reach stays under 20 with no cover, the cause is (b) or distribution; restart follow runs when Mac Chrome is back.

## 2026-11-19 08:00 production run — no new issues on purpose
- Numbers are in the memo above (reels 4–18 since 11/17, account reach 29/day, followers 14, likes 0 on all posts).
- Decision: do not add more type-only A issues until the cover_url test reads (r_c_14 12:00, r_x_07 17:00 today).
  The queue is full through 11/23 plus 11/24 B and 11/25 B (Yu's Okinawa extras); 11/24 A and 11/25 A stay open for tomorrow's run.
- Tomorrow: if reach comes back without cover_url → keep it off, resume normal production. If not → propose to Yu: fewer posts
  (1 issue/day), Yu-photo issues first, and restart follow runs (needs Mac Chrome).

## 2026-11-19 deeper read (Yu: 分析が浅い。フォローなしでも150あった。市場調査は？)
- Correction: account reach "29" on 11/18 was a partial-day value (period resets 08:00 UTC). Full days were 150–200 through 11/17.
- Correction: reels reach at 6 h is not final (noodles 14 → 113 at 14 h). r_x_06/r_c_12 must be read at 24 h+.
- The real break is 11/12, not 11/17. Before 11/12: 20 of 20 reels got 100–150 (one 325), with stock footage + voiceover, little on-screen text,
  even on days with no follow runs. From 11/12 (magazine relaunch: reels built from text-heavy pages, then hook reels with big type):
  only 3 of 16 reels got ~110 (noodles, Kita-Senju, eel 70), the rest 4–39. Carousels 0–5 (followers only).
- Instagram's own eligibility page lists, as not recommended: reels "where text covers most of the screen", visibly recycled content,
  unoriginal/aggregated content; Account Status shows whether an account/post may be recommended. Mosseri: hashtags don't add reach;
  cap of 5 hashtags since Dec 2025. Top signals: watch time, likes per reach, sends per reach.
- New hypothesis: our post-11/12 reels are text-led (question blocks, list-row clips, slide pages) → often skipped for non-follower recommendation.
- Done: hashtags trimmed to 5 on 10 queued captions. cover_url test stays.
- Asked Yu: check Account Status (Settings → Account → Account status → "content may not be recommended").
- Proposed test (needs Yu's go): reels led by moving pictures, text under ~15% of the screen, short subtitle line only; Yu sends 5–10 s clips.
- 11/19 test started: tools/carousel/clean.py (Yu's photo full screen, one small subtitle box, text <10% of the frame).
  Rebuilt r_x_07 (11/19 17:00), r_x_08, r_x_09, r_x_10 in this format. Control: hook reels with Yu photos (x_02 115, x_04 111, x_06 4?, x_03 12).
  Type-only reels stay as hook reels for now (Koru-card version looked weak). Read each at 24 h.

## 2026-11-20 08:00 production run (new loop: docs/pdca/)
- Retro numbers in docs/pdca/summary.md: v1 (10/21–11/11, stock video or photos + AI voice, no music) 70/75 hit, median 108;
  everything since 11/12 (music, stills, text-led) 2/16. Benchmarks (tokyocheapo, paolofromtokyo…): all top reels are real video.
- Made (reel only, A slots): r_v_01 late night near Ueno/Akihabara (11/24 12:00), r_v_02 Sunday closures 96/310 (11/25 12:00).
  Both = free stock video (Mixkit) + AI voice + one small subtitle (H5). Topics chosen for H3 (late night = our best ever, 321).
- Running: H2 r_x_07 (clean + music) reads 11/20 18:00; H1 r_x_08–10 (clean photo + AI voice) from 11/21; H5 r_v_01–02 from 11/24.

## 2026-11-21 08:00 production run
- summary.md: v1 (AI voice, no music) 91/98 hit, median 110; every music reel since 11/12 2/18; H2 (clean + music) 3. Carousels 18 of 18 under 5.
- Made (reel only, 11/26): r_v_03 cash only (77 of 310 places say cash only), r_v_04 breakfast before 8am — same topic as r_c_14 (hook + music = 3),
  so the only change is the format (H5: stock video + AI voice + one subtitle). Carousels paused for these slots (reach 0–3).
- Follow runs back on (Windows Chrome): ronakbhaiyajee followed back 8 h after our comment.

## 2026-11-22 08:00 production run
- Early reads: r_x_08 (Yu photo + AI voice, H1) 10 at 10 h; Ueno reel 5 at 15 h. H1 reads at 24 h (18:00 today).
- Made 11/27 (reel only): r_h4_01 seat charge (Akatsuka ¥450 vs Torahachi none), r_h4_02 closed Mondays (50/310) in the exact v1 format
  (tools/app_reel/compose_v3.py: stock video + AI voice + big text + chips, 7–11 s). If this format still gets ~100, the cause is our new
  formats; if it doesn't, the account/time changed (H4).

## 2026-11-23 08:00 production run
- summary.md (11/22 19:50 UTC): v1 91/98 batch, median 110; music arms median 3–32; H1 r_x_08 17. Followers 18. Early: r_c_17 Asakusa tempura 27 at 12 h (music arm control).
- Today the T2 arm starts: r_h4_01 seat charge 12:00, r_h4_03 Kuramae 17:00 (exact v1 format). First real read of "is it the format or the account?" = 11/24 evening.
- Made 11/28 (reel only, both inside running arms, one change each): r_v_05 Asakusa sweets (H5: stock video + AI voice; concrete dish + price,
  Kokonoe ¥160 / Umezono ¥703), r_h4_04 Kamiya Bar (H4a v1 format; Denki Bran ¥400, buy tickets first, cash only). H5 n=5, H4a n=5 (incl. r_h6_01).
- Stock: pulled the other 22 Mixkit clips from the stock-video release (autumn leaves, tea, sushi-making, ramen) — no beef/sukiyaki footage, so wagyu topics wait.

## 2026-11-24 08:00 production run
- First T2 read: r_h4_01 seat charge (exact v1 format) **112 reach at ~11 h** — first reel past the 80 test batch since 11/12. r_h4_03 Kuramae sweets, same format, 8 at 6 h.
  So the v1 format can still pass the batch (account isn't blocked); the topic seems to matter too: a surprising rule/charge beat a list of sweets shops. Final read at 24 h.
- Made 11/29 (reel only, v1 format, one change = topic type): r_h4_05 cover charges (Budouya ¥660 / Torisu ¥400+tax / Kurofunetei none) — repeats the winning topic family;
  r_h4_06 smoking inside kissaten (8 places on our list; Bonaru smoke-free) — another surprising rule.
- If both pass 80 and the list-type reels don't: next week = v1 format + "rules/costs travelers don't expect" as the main series.

## 2026-11-25 08:00 production run
- 24 h reads: r_h4_01 seat charge (v1 format) **112**; r_h4_03 Kuramae sweets (v1 format) 9. **r_v_01 late night (H5 stock video + AI voice) 136 at 19 h, avg watch 8.0 s, 2 saves, 1 share** — best since 11/12.
  r_x_09 Naha (Yu photos + voice) 27 at 14 h; carousels still 0. Followers 20 (+2 follow-backs from comments).
- Pattern so far: both winners open with a traveler's problem ("charged for a seat?", "hungry after 10pm?"); both losers were "here are some shops" lists. Format matters less than the opening problem.
- Made 11/30: r_v_06 "eating alone in Akihabara? sit at the counter" (H5, problem framing), r_h4_07 "travelling with kids? some places say no" (v1 format, rule topic).

## 2026-11-26 08:00 production run
- H5 (stock video + AI voice): r_v_01 late night 138 (24 h), r_v_02 Sunday 106 at 18 h — 2 of 2 past the batch; watch 7.9 s / 5.8 s vs v1's 3.7 s. Saves and shares appear only on these.
- Photo + voice: r_x_09 59, r_x_10 8 at 13 h. Carousels 0–1 (28 of 28 under 80). Followers 21.
- Made 12/1: r_v_07 vegetarian near Akihabara (H5, problem), r_h4_08 can tourists book? (v1, rule — Aoi Marushin takes no bookings from overseas travelers).

## 2026-11-27 08:00 production run
- H5 (stock video + AI voice, problem opening): r_v_01 138, r_v_02 106, r_v_03 cash only 114 at 18 h, r_v_04 breakfast 67 at 13 h. 3–4 of 4 past the batch; median watch 6.8 s.
  Photo + voice (v4) is 0/3 (median 17). Carousels 0/28. Followers 21.
- Decision until the 11/29 retro: H5 is the main reel format. Made 12/2 as two H5 reels: "hungry at 3pm?" (115 of ~300 places closed at 3pm) and "Asakusa lunch under ¥1,000".
- Still no 1,000+ hit. Next lever to test after the retro: hook strength (first 1 s) and posting more H5 per day vs carousels.
