# Phase 2 · Core Localization — the headline

> Re-run the patching sanity checks on the FULL pipeline before trusting any number.

**Entrypoint:** `experiments/phase2_localization.py` · **Config:** `configs/experiments/phase2_localization.yaml`

- [ ] `[CC]` M1 — `src/vlamem/probes/representation_sensitivity.py`. `[YOU]` interpret.
- [ ] `[CC]` M2 — `src/vlamem/probes/oracle_conditioning.py`. `[YOU]` interpret.
- [ ] `[VERIFY]` M3 — `src/vlamem/patching/` full sweep via `src/vlamem/eval/runner.py`; BackboneShare with CIs across axes/episodes; report necessity AND sufficiency.
- [ ] `[CC]` M4 — `src/vlamem/probes/cross_swap.py`.
- [ ] `[YOU]` Check the four methods agree; resolve disagreements (research judgment).
- [ ] `[CC]` Generate the per-axis backbone-vs-expert attribution figure with CIs.
