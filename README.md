# vla-memorization-localization

**Localizing memorization in efficient vision-language-action (VLA) models** — is a failure under a
*meaning-changing* perturbation (object swap, instruction rewrite) caused by the vision-language
**backbone**'s conditioning representation, or by the flow-matching **action expert** replaying a
memorized trajectory? We answer it with causal-mediation (activation-patching) interventions on
SmolVLA-class models and quantify the split as a per-axis, statistically-bounded `BackboneShare`.

> **This is research code.** Its failure mode is not a crash — it is a clean-looking, confidently
> **wrong** number that a human then builds a thesis on. Claude Code generates and runs; the human
> owns every gate decision and verifies anything that feeds a conclusion. Nothing is ever fabricated.
> Read [`CLAUDE.md`](./CLAUDE.md) — the full operating brief — before working in this repo.

## Status

Scaffold (Phase −0). Pipelines are stubs (`NotImplementedError`) until built and validated
interactively per `CLAUDE.md` §4. **Validate before you automate.**

## Repository layout

```
vla-memorization-localization/
├── CLAUDE.md            # operating brief — read first
├── env/                 # reproducible environment (LeRobot v0.5.0 + pins, Dockerfile)
├── configs/             # every knob lives here; nothing hard-coded
├── src/vlamem/          # the installable research package
│   ├── models/          # uniform VLA API + SmolVLA/TinyVLA wrappers + ★ hooks
│   ├── perturbations/   # meaning-changing vs nuisance axes (strictly separated)
│   ├── patching/        # ★ activation patching + causal mediation
│   ├── probes/          # representation-sensitivity / oracle-conditioning / cross-swap
│   ├── metrics/         # ★ BackboneShare, MemScore, bootstrap CIs
│   ├── fixes/           # (Phase 3) targeted interventions
│   ├── eval/            # harness + sweep runner
│   └── utils/           # seeding, logging, io
├── experiments/         # thin per-phase entrypoints
├── scripts/             # shell wrappers (lerobot-eval / lerobot-train / sweep)
├── tests/               # ★ protect the numbers (patching, metrics, perturbations)
├── notebooks/           # interactive sanity checks
├── results/             # generated; gitignored
├── paper/               # drafts + figures
└── claude-ops/          # task files for the overnight runner
```

`★` = files whose correctness the thesis depends on — full test coverage required.

## Quickstart

```bash
# 1. Environment (installs LeRobot v0.5.0 + pinned deps)
bash env/setup.sh

# 2. Install the research package (editable)
pip install -e .

# 3. Verify the skeleton
pytest -q
```

Then download the baseline checkpoint (`lerobot/smolvla_base`) and dataset
(`HuggingFaceVLA/libero`), and begin Phase 0 — see `CLAUDE.md` §5.

## License

Private for now; license TBD (see `LICENSE`).
