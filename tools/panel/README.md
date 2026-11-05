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
