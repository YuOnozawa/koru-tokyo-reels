# Selling a paid product — plan (started 2026-11-29, Yu)

No personal names in this repo (it is public). The named prospect list lives in Yu's Google Drive:
"with KORU 見込み客リスト v0（非公開・共有しない）" (sheet id 1xGkwbGIrlaCyLdCNSR9iKYWXbXRX311xG3MPCOGEjpE). Keep only: handle, how we met, reaction, warmth, trip stage, next question.

## Yu's direction (11/29)
1. Know buyers by name: analyze **100** real people (was 50).
2. Build a list of people who really want to buy.
3. Use AI persona simulation as a pre-launch check (find blockers); the pass mark is real people paying, not a simulated %.
4. Story/vision goes where people decide (profile, pinned post, sales page, replies); reach reels stay "traveler's problem / rule" openers.
5. Product: as automated as possible, and genuinely valuable.

## Facts so far
- Outreach 10/31–11/28: 253 follows → 23 followers. 31 comments on travelers' posts → 10+ replies/likes/follows. Comments work better than follows.
- Demand evidence for a paid product: none yet (0 keyword comments, 0 DMs in a month).
- Most people we reach are in Tokyo right now; buyers are people before the trip.
- Finding pre-trip people by searching Instagram: tested 11/29 (keyword search → 3 top posts, comment sections are mostly other creators) → 0 found. GET search/tag APIs return 404. Reddit is blocked for our fetch tool.
- So pre-trip people must identify themselves: a reel/post that invites "comment your month".

## Product candidates (11/29) — first recommendation: A
A. **Date-checked food plan** ("Your Tokyo food plan, checked for your dates"): traveler gives dates, area, party (kids / vegetarian / cash), and wishes → generated from data/shops.json: per day, what is open (weekday, holiday, 3pm break, last order), booking rule, cash/cards, kids, smoking, a nearby backup, Google Maps links, magazine-style PDF. Automation: rule engine over shops.json; human spot check. Price test: US$9 presale.
B. Yu's Tokyo Map: Google Maps list of places Yu ate at + one-line notes. Easiest; static and easy to copy. Use a 10-place version as the free sample instead.
C. In-trip daily "open near you today" messages: most useful mid-trip, needs messaging infrastructure; later.
Risk for A: hours must be re-verified before each delivery (data checked Nov 2026).

## Next
- Grow the list to 100: 2–3 comments per follow run (cap 5/day), log trip stage; self-identify reel ("Going to Tokyo? Comment your month").
- Ask the 10 warmest people one question (draft in chat; send only after Yu approves).
- Build a sample of A from shops.json; run persona check; then presale. Payment account = Yu.

## 2026-11-29 update (Yu): do not ask customers on SNS
- Dropped: the question to warm followers, and the "comment your month" reel. No research questions to customers.
- Instead the gaps are filled by (1) government survey data (docs/sales/target.md), (2) mechanistic simulation on our own shop data
  (tools/sim/trip_sim.py -> docs/sales/trip_sim.md), (3) public evidence (reviews, trip reports) read by us.
- Note: the opinion-style persona panel (tools/panel) was tested twice against real reel results and had no predictive value
  (Spearman -0.10 on 20 reels). So "would they like it / buy it" is not taken from role-played opinions. Purchase is tested by putting the product on sale.
- First simulation result (213 real meal shops, 10 meals in 5 Tokyo days): even a traveler who checks opening hours first is turned away
  at least once in 20-52% of trips (last order / children / booking), and 3.7-4.0 of 10 meals do not take credit cards.
  Late eaters (friends, solo) are hit most; families least.
