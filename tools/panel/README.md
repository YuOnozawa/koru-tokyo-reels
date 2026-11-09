# Synthetic viewer panel (pre-test) — status: calibrating, NOT a go/no-go gate

What: 100 synthetic personas (personas.py; weights are assumptions) react to storyboards (frames + voice-over + caption).

## Calibration 1 (2026-11-06, blind, 14 posted reels with known results)
- Panel completion ranking vs real: Spearman 0.75. But video length alone: 0.85. Panel after controlling for length: ~0.03 (no extra signal).
- Panel seconds-watched vs real avg watch: 0.34.
- Pairwise (24 pairs, real watch gap >=1.6x): panel 19/24; "shorter reel wins" 22/24.
- Panel errors: over-rated striking food photos on long reels (a 30 s curry reel: real 1.6 s, the worst).
- Method caveat: the 4 batch agents scored personas with seeded heuristics, not 100 separate role-plays.
- Use now: QA flags (visual/voice mismatch, unclear claims) and hook ideas. Prediction: only after it beats the length-only baseline on >=20 reels.

## Calibration 2 (prospective)
- runs/prospective.jsonl: blind forecasts for 20 reels queued 11/6-11/9, made before posting. Score after insights on 11/10.

## Prospective forecast + QA flags (2026-11-06, 20 queued reels)
- Forecasts saved; scored after 11/10 insights.
- Useful QA flags: stock visuals contradict the words (cold soba shown as hot ramen, eel reel shows no eel, mahjong neon used as a food hook, ginkgo line over red maple); same clip reused across reels; "Yu" never introduced.
- False flags (checked against the DB): Mochizuki "1 min from Suehirocho" vs "9 min from JR Akihabara" are two different stations; breakfast "open by 8:30 on weekdays" is true for all four. QA flags must be verified before acting.
- Production rules from this: stock only for atmosphere, never a different dish than the one named; introduce Yu once per reel ("Yu, a local office worker"); don't reuse the same clip within 2 days.

## Prospective scoring (2026-11-10, 20 reels posted 11/6-11/9, forecasts made blind before posting)
- Forecast seconds watched vs real: Spearman -0.10 (no signal). Shorter-is-better rule: -0.41 (reversed this time: short loops get high completion but fewer seconds).
- Forecast P(save/share) vs real saves+shares: 0.35 (weak). The real winner (c_08 late-night list: 322 reach, 4 saves, 4 shares) was ranked 8th of 20.
- Conclusion: still no predictive value. Keep the panel for QA flags only.
