# Phase 3 · Causal Validation / Fix — stretch

> The fix only counts if it BEATS the cheap baseline. Run baselines first.

**Entrypoint:** `experiments/phase3_fix.py` · **Config:** `configs/experiments/phase3_fix.yaml`

- [ ] `[CC]`+`[VERIFY]` Run augmentation/dropout **baselines first**; record numbers. `[YOU]` decide: if augmentation already wins, say so and stop.
- [ ] `[CC]` If expert-localized: `src/vlamem/fixes/consistency_loss.py`. If backbone-localized: `src/vlamem/fixes/representation_align.py`.
- [ ] `[VERIFY]` Confirm the fix moves the metric in the predicted direction AND beats the baseline without harming success/multimodality. `[YOU]` owns this conclusion.
