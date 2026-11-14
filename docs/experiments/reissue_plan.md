# Re-issue plan: old posts → KORU · Tokyo Field Notes issues (design D)

Yu, 2026-11-12: re-post earlier content in the new magazine format, regrouped. Target reader (Yu): adult travelers
staying in Tokyo, fairly well off, who don't want a bad meal. Main issues = no-fail picks; cheap/fun = 番外編 Extra.
Each issue = 1 hook reel (since 11/14) (12:00 JST) + 1 carousel (20:00 JST). One issue per day.


> **2026-11-15 note for the next production run:** 11/19 already has the B issue (No.09 late dinner, moved from 11/16 so Extra 04 北千住 could go out on 11/16 — Yu: 明日出してもいい).
> The **A slot of 11/19 (reel 12:00 + carousel 20:00) is still empty: fill it first**, then continue from 11/20.
> Kita-Senju is a new series (Yu: 「北千住シリーズ」). Next Kita-Senju issues come when Yu sends more photos.

| Issue | Theme (JP / EN) | Old posts folded in | Photos |
|---|---|---|---|
| No.03 ✅ | 秋葉原で、海鮮の夜 / Domannaka | f_03 | Yu |
| No.04 ✅ | 予約して行く五軒 / Worth booking | b_04 + awards in DB | none (type cover) |
| No.05 ✅ | 外食の八つの決まり / Eight rules | h_01–h_12, s_02–s_05, b5_07–09, w2_03 | Yu (atmosphere) |
| Extra 01 ✅ | 天下一品 / Tenkaippin | y_01 | Yu |
| No.06 | 店で使う十のひとこと / Ten lines to say | h_04, s_04, b5_06, w3_03, b5_04 allergy, b5_12 okawari, h_09 urikire | none |
| No.07 | 東の鰻 / Eel in East Tokyo | b_04, c_12 (3 with English menu), Irokawa | none / Yu if any |
| No.08 | 夜10時からの晩ごはん / Dinner after 10pm | c_08, n_02–n_07 (sit-down picks first) | none |
| No.09 | 神保町、カレーと喫茶 / Jimbocho curry & coffee | v2_03–05, c_01 kissaten, Bondy/Gavial (Tabelog 100) | none |
| No.10 | 浅草の一日 / A day in Asakusa | c_10 English menu, c_02 sweets, b_03 Pelican, b_07 Azuma | none |
| No.11 | Yuが通う店 / Yu's regulars | b_02 A-un, v2_06 Tamazen, b_05 Onihei, b_09 Shinpuku, v2_02 Mochizuki, v2_01 Indira | ask Yu |
| No.12 | 上野、ゆっくり / Ueno | Ponta Honke (Bib), b_01 Shoryu, b5_11 Ameyoko, c_05 sweets, b_10 ginkgo (Nov 26) | none |
| No.13 | 朝ごはんの東京 / Tokyo mornings | c_07, c_09, s_01, n_01, w4_06 | Yu coffee |
| Extra 02 | コンビニとデパ地下 / Konbini & depachika | w4_01, w4_03, w4_04 | none |
| Extra 03 | サ飯 / After the sauna (Spa Metsa) | sp_02 | Yu |
| Extra 04 | 回転寿司と立ち食いそば / Conveyor sushi & standing soba | w3_01, b5_13, w3_02 | none |

Rules: facts only from data/shops.json or Yu; describe only what's visible in Yu's photo; never show another shop's
dish for a named shop (photo-less issues use the solid type cover). Old reels: suggest Yu archive them in the app
once the new issues are out (archive, not delete; Yu decides).

## 2026-11-12 update: no borrowed photos (Yu)
Yu: quoting/borrowing shop photos is risky — don't. No permission requests either. Until Yu shoots, change the CONTENT,
not just the design. Visuals we can make ourselves:
1. Schematic maps (render.py `map` type: pins next to the shop's station, "not to scale") — the city-magazine staple.
2. Big type covers (solid colour + giant numeral/kanji: `cover` without `photo`, with `bg` and `big`).
3. Data pages: lists, rules, phrases, checklists (no photos needed).
4. Yu's own photos only (stock/yu/). Street/station photos by Yu are welcome, food or not.
5. Later: line illustrations of dish genres, labelled "Illustration" (never presented as a specific shop's dish).
So photo-less issues lean on information that saves a traveler from a bad meal: where (map), when (hours/closed days),
how much (budget), how to book, what to say. Every photo-less issue gets a map page.

## 2026-11-12: official info + reviews (Yu: 「あとはお店の公式情報と口コミだよね」)
- Official info (restaurant's own listing / site): facts we may use, paraphrased — prices, courses, hours, booking method,
  house rules (dress code, perfume, children, late-arrival and cancellation fees, service charge, payment). These are the
  most useful "don't fail" details for our target reader. data/shops.json fields: house_rules, rules_checked.
- Reviews: use the Tabelog score and review count with a date (tabelog_score, tabelog_reviews). Summarise review themes in
  our own words only when several reviews say the same thing; never quote review text, never use Google review text.
- New page type in use: `rules` as "House rules before you book" (No.04).

## 2026-11-12: with KORU travel issues (Yu's photos come first)
- No.06 金沢（ささ舟の懐石＋四代目菊川）11/16 · Extra 02 麺で旅する（すみれ・瓦そば・一幸舎・福岡空港）11/17.
- The re-issue list above shifts by one: its "No.06 Ten lines to say" becomes No.07, and so on. Yu's real-photo issues
  (any region) always jump the queue. Shops Yu didn't name stay unnamed (e.g. the Shimonoseki kawara soba shop).

## 2026-11-12: Okinawa — on hold
- Yu: burger at the clubhouse restaurant of the golf course in Eibi (栄野比), Uruma. Menu reads TAIYO Steak House =
  Taiyo Steakhouse, 2F Taiyo Golf Club clubhouse, run by MCCS Okinawa (US Marine Corps community services), aimed at
  service members and families. Public access for tourists not confirmed → don't publish as a recommendation.
  Yu (11/12): he went in with a member. Decision: never as a pick; at most a line in a future Okinawa diary issue,
  clearly labelled "members and their guests only". Wait for more Okinawa photos before making that issue. Photos saved (burger only; the table photo shows other diners' faces, not used).
