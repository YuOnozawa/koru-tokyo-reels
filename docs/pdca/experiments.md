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

## Hypotheses (ranked)
| # | Hypothesis | Test | Status |
|---|---|---|---|
| H1 | Voice narration (original audio) instead of the shared music track brings back the test batch | Same clean photo reels, narration instead of music: r_x_08 (11/21), r_x_09, r_x_10. Control r_x_07 (music). | running from 11/21 |
| H2 | Text-led visuals block recommendation | v4 clean (text <10%) + music: r_x_07 (11/19). If H1 arm hits and this doesn't, audio > visuals | reading |
| H3 | Expansion past ~100 needs watch ≥ 6 s; late-night and "money/etiquette hack" topics hold attention | Next 3 voice reels: one late-night, one hack, one normal; compare watch and reach | queued |
| H4 | Time (new-account boost ended) — not format | If H1 and H2 both fail, rerun one old v1 reel style (render_kit) with a new topic | backup |
