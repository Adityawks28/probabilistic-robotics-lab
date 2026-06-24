# Phase 0 · Go/No-Go Pilot — GATES EVERYTHING

> ⚠️ Do **not** queue this overnight blindly. Hook discovery (P0.3) and the patching
> sanity checks (P0.4) are interactive hard-stops. Validate, then automate.

**Entrypoint:** `experiments/phase0_pilot.py` · **Config:** `configs/experiments/phase0_pilot.yaml`

- [ ] `[CC]` P0.1 — `scripts/run_eval.sh` baseline eval. → `[VERIFY]` human confirms ~90%+ on ≥1 suite.
- [ ] `[CC]` P0.2 — ≤5 minimal pairs in `src/vlamem/perturbations/meaning_changing.py`. → `[VERIFY]` each drops success.
- [ ] `[CC]`+`[YOU]` P0.3 — **interactive** hook discovery in `src/vlamem/models/hooks.py` (freeze / feed-z / read-patch). Human confirms + writes down `HOOK_POINTS`.
- [ ] `[CC]` P0.4 — `src/vlamem/patching/activation_patch.py` + `src/vlamem/metrics/backbone_share.py` on ~20 episodes.
- [ ] `[VERIFY]` Run `tests/test_patching.py` + `tests/test_metrics.py`; human reviews clean→clean ≈ 100%, corrupted→corrupted broken, BackboneShare unit test.
- [ ] **⛔ GATE 0 `[YOU]`** — clean, stable split (BackboneShare clearly ≠ ~0.5)? PASS → Phase 1. FAIL → pivot to instrument-only. Show Koga-sensei.
