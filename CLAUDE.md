# CLAUDE.md — vla-memorization-localization

> This file is the operating brief for Claude Code. Read it fully before acting.
> It defines the **mission**, the **conventions**, the **repo architecture**, the **guardrails**,
> and the **step-by-step build plan**. When in doubt, follow the guardrails over speed.

---

## 1 · Mission

Build the codebase for a research study that **localizes memorization in efficient vision-language-action (VLA) models** to one of two modules: the **vision-language backbone** or the **flow-matching action expert**. When an efficient VLA (SmolVLA-class) fails under a *meaning-changing* perturbation (object swap, instruction rewrite), is the failure caused by the backbone's conditioning representation, or by the action expert replaying a memorized trajectory? We answer it with **causal-mediation (activation-patching)** interventions and quantify the split.

**Definition of done (thesis):** a per-axis, statistically-bounded `BackboneShare` attribution across ≥2 efficient VLAs, plus a publishable robustness benchmark for the efficient-model regime. The real-robot validation is **deferred** (out of scope for now).

**Non-negotiable context for Claude Code:** this is *research* code. Its failure mode is not a crash — it is a clean-looking, confidently **wrong** number that a human then builds a thesis on. Therefore: **you generate and run; the human owns every gate decision and verifies anything that feeds a conclusion.** Never invent or approximate a result. If an experiment cannot run, stop and report — do not fabricate output.

---

## 2 · Conventions (follow exactly)

### Branches
Format: **`<type>/<name>/<brief-summary>`**

- **Types:** `feat`, `fix`, `chore` (also allowed: `docs`, `test`, `refactor`).
- `<name>`: the author handle (`aditya`).
- `<brief-summary>`: kebab-case, ≤5 words.
- **One branch per unit of work. Never commit directly to `main`.** Open a PR; the human merges.

Examples:
```
feat/aditya/phase0-baseline-eval
feat/aditya/activation-patching-core
fix/aditya/seed-nondeterminism
chore/aditya/repo-scaffold
test/aditya/patching-sanity-checks
```

### Commits
- **One or two lines.** Imperative mood. Subject ≤72 chars; optional second line for context.
- **Do NOT add any AI attribution.** No `Co-authored-by: Claude`, no "Generated with Claude Code", no trailer of any kind.

Examples:
```
feat: add SmolVLA LIBERO eval harness
```
```
feat: implement activation patching + BackboneShare
Includes clean/corrupted/patched runs and the mediation ratio.
```

### Repository
- **Private** for now (`gh repo create vla-memorization-localization --private`).
- A public **landing page** comes later (see §7); do not build it yet.

### Code
- Python 3.10+, a single installable package `vlamem`. Type hints + docstrings on public functions.
- **Config-driven, not hard-coded.** All paths, seeds, and hyperparameters live in `configs/`.
- **Determinism:** every run takes a seed; set torch/numpy/python seeds centrally in `utils/seeding.py`.
- **No silent failures.** Assert invariants (tensor shapes, value ranges). Fail loud.
- **Tests are mandatory for `patching/` and `metrics/`** — these produce the numbers the thesis depends on.

---

## 3 · Repository Architecture (with purpose)

```
vla-memorization-localization/
├── CLAUDE.md                      # this brief — operating instructions for Claude Code
├── README.md                      # human-facing: one-paragraph pitch + how to run
├── LICENSE                        # private for now; choose later
├── .gitignore                     # ignores datasets, checkpoints, results/, wandb/, __pycache__
│
├── env/                           # PURPOSE: reproducible environment
│   ├── setup.sh                   #   installs LeRobot v0.5.0 + deps, pins versions
│   ├── requirements.txt           #   exact pins
│   └── Dockerfile                 #   optional: wraps ioaitech/lerobot-gpu:v0.5.0
│
├── configs/                       # PURPOSE: every knob lives here, nothing hard-coded
│   ├── base.yaml                  #   model/dataset paths, device, logging
│   ├── seeds.yaml                 #   the fixed seed set for all runs
│   ├── perturbations.yaml         #   the meaning-changing vs nuisance axis definitions
│   └── experiments/               #   one yaml per experiment (phase0_pilot.yaml, ...)
│
├── src/vlamem/                    # PURPOSE: the installable research package
│   ├── models/
│   │   ├── base_api.py            #   uniform VLA interface (predict, get_repr, set_cond)
│   │   ├── smolvla_wrapper.py     #   wraps SmolVLA behind base_api
│   │   ├── tinyvla_wrapper.py     #   (Phase 4) second model behind the same api
│   │   └── hooks.py               #   ★ CRITICAL: freeze backbone, feed custom z, read/patch activations
│   ├── perturbations/
│   │   ├── meaning_changing.py    #   object identity/pose, instruction edits (action SHOULD change)
│   │   ├── nuisance.py            #   background, lighting, texture, camera, distractors (SHOULD NOT change)
│   │   └── registry.py            #   names → perturbation fns; keeps the two classes strictly separate
│   ├── patching/
│   │   ├── activation_patch.py    #   ★ clean/corrupted/patched runs
│   │   ├── causal_mediation.py    #   ★ indirect-effect computation
│   │   └── donors.py              #   minimal-pair donor selection
│   ├── probes/
│   │   ├── representation_sensitivity.py  # M1: does the backbone feature move?
│   │   ├── oracle_conditioning.py         # M2: feed correct z under perturbation
│   │   └── cross_swap.py                  # M4: swap backbone/expert across clean/perturbed
│   ├── metrics/
│   │   ├── mem_score.py           #   memorization metric (sensitivity gap)
│   │   ├── backbone_share.py      #   ★ the headline ratio; unit-tested
│   │   └── bootstrap.py           #   confidence intervals over episodes/seeds
│   ├── fixes/                     # (Phase 3) targeted interventions
│   │   ├── consistency_loss.py    #   perturbation-consistency on the velocity field
│   │   └── representation_align.py
│   ├── eval/
│   │   ├── harness.py             #   runs a model × perturbation × seed, returns metrics
│   │   └── runner.py              #   sweep orchestrator (model × intervention × axis × seed)
│   └── utils/
│       ├── seeding.py             #   one place to seed torch/numpy/python
│       ├── logging.py             #   structured run logs → experiment log
│       └── io.py                  #   save/load configs, results, checkpoints
│
├── experiments/                   # PURPOSE: thin entrypoints, one per phase; all logic in src/
│   ├── phase0_pilot.py
│   ├── phase1_instrument.py
│   ├── phase2_localization.py
│   ├── phase3_fix.py
│   └── phase4_generality.py
│
├── scripts/                       # PURPOSE: shell wrappers for common runs
│   ├── run_eval.sh                #   wraps lerobot-eval
│   ├── run_train.sh               #   wraps lerobot-train
│   └── run_sweep.sh
│
├── tests/                         # PURPOSE: protect the numbers
│   ├── test_patching.py           #   ★ clean→clean ≈ 100%, corrupted→corrupted stays broken
│   ├── test_metrics.py            #   ★ BackboneShare on a hand-checked case
│   └── test_perturbations.py      #   meaning vs nuisance behave as labeled
│
├── notebooks/
│   └── sanity_checks.ipynb        #   interactive verification before trusting a pipeline
│
├── results/                       # generated; gitignored (figures, tables, raw metrics)
├── paper/                         # drafts + figures
└── claude-ops/                    # task files for the overnight runner
    ├── phase0.task.md
    ├── phase1.task.md
    └── ...
```

★ = files whose correctness the thesis depends on. Treat them with extra care and full test coverage.

---

## 4 · Guardrails — what Claude Code may and may NOT do autonomously

**The tag model.** Throughout the plan, work is one of:
- `[CC]` — Claude Code owns it. Safe to run, including overnight via claude-ops **once the relevant pipeline is validated**.
- `[YOU]` — the human's job (understanding/judgment). Claude Code may draft or assist, but must not treat it as done.
- `[VERIFY]` — Claude Code builds/runs it, then **stops and hands to the human to verify before any downstream use.**

**Hard stops (Claude Code must pause and request human sign-off):**
1. **GATE 0** (end of Phase 0): proceed to Phase 1 only after the human confirms a clean backbone-vs-expert split.
2. **Hook discovery** (P0.3): do this *interactively with the human*, not autonomously overnight — getting the patch points wrong silently corrupts everything.
3. **Patching sanity checks** (P0.4, repeated in Phase 2): the human must see `clean→clean ≈ 100%` and `corrupted→corrupted` still broken, and a passing `BackboneShare` unit test, before any sweep is trusted.
4. **The "fix beats baseline" decision** (Phase 3): the human decides whether the targeted fix genuinely beats data augmentation.

**Validate before automate.** Build and verify each pipeline interactively first. Only then write its claude-ops task file and queue overnight runs. Never let an unvalidated pipeline run unattended.

**No fabrication, ever.** If a run errors, a dataset is missing, or a result is implausible, stop and report it. Do not synthesize, estimate, or "fill in" results.

---

## 5 · Step-by-step build plan

Each step lists its **branch**, the **work**, and the **handoff**. Open a PR per branch; the human merges.

### Phase −0 · Scaffold — `chore/aditya/repo-scaffold`
- `[CC]` `gh repo create vla-memorization-localization --private`; create the full tree in §3 with stub files + docstrings.
- `[CC]` Add `.gitignore`, `requirements.txt`, `env/setup.sh`, a stub `README.md`, and empty test files.
- `[CC]` Commit: `chore: scaffold repo structure and env`. Open PR.
- `[YOU]` Skim the scaffold; merge.

### Phase 0 · Pilot — `feat/aditya/phase0-pilot` · GATES EVERYTHING
- `[CC]` `scripts/run_eval.sh` wrapping `lerobot-eval --policy.path=lerobot/smolvla_base --env.type=libero --env.task=libero_spatial,libero_object,libero_goal,libero_10`.
- `[VERIFY]` Human confirms baseline lands near published ~90%+ on ≥1 suite.
- `[CC]` `perturbations/` minimal pairs (≤5) using LIBERO-PRO. `[VERIFY]` human confirms each drops success.
- `[CC]`+`[YOU]` **Interactive:** implement `models/hooks.py` — locate freeze / feed-z / read-patch points in SmolVLA. Human confirms correctness.
- `[CC]` `patching/activation_patch.py` + `metrics/backbone_share.py` on ~20 episodes.
- `[VERIFY]` **Run `tests/test_patching.py` + `tests/test_metrics.py`. Human reviews** clean→clean, corrupted→corrupted, and the unit-tested ratio.
- Commits e.g. `feat: add baseline eval and minimal-pair perturbations` / `feat: implement activation patching + BackboneShare`.
- **⛔ GATE 0 — `[YOU]`:** clean, stable split? PASS → Phase 1. FAIL → pivot to instrument-only. Show Koga the result.

### Phase 1 · Instrument — `feat/aditya/phase1-instrument` · publishable floor
- `[CC]` Full perturbation taxonomy (meaning vs nuisance, strictly separated) in `perturbations/`.
- `[CC]` `metrics/mem_score.py` + `metrics/bootstrap.py` (CIs); `eval/harness.py` with fixed seeds.
- `[CC]` Run the SmolVLA robustness profile → `results/`. `[VERIFY]` human eyeballs the cliff figure.
- `[CC]` Draft `paper/` benchmark section + clean code release. `[YOU]` own the claims.

### Phase 2 · Localization — `feat/aditya/phase2-localization` · the headline
- `[CC]` `probes/representation_sensitivity.py` (M1), `probes/oracle_conditioning.py` (M2), `probes/cross_swap.py` (M4).
- `[VERIFY]` `patching/` full sweep (M3) via `eval/runner.py`; **re-run sanity checks on the full pipeline before trusting it.**
- `[CC]` Generate the per-axis attribution figure with CIs.
- `[YOU]` Check the four methods agree; resolve disagreements (research judgment).

### Phase 3 · Fix — `feat/aditya/phase3-fix` · stretch
- `[CC]`+`[VERIFY]` Run augmentation/dropout **baselines first**; record. `[YOU]` decide whether to continue.
- `[CC]` `fixes/consistency_loss.py` (if expert-localized) or `fixes/representation_align.py` (if backbone-localized).
- `[VERIFY]` Confirm the fix moves the metric **and** beats baseline without harming success. `[YOU]` own the conclusion.

### Phase 4 · Generality — `feat/aditya/phase4-generality`
- `[CC]` `models/tinyvla_wrapper.py` behind the same `base_api`. `[VERIFY]` re-sanity-check patching on the new model.
- `[CC]` Replicate the attribution. `[YOU]` scope the claim to "efficient flow/diffusion-expert VLAs".

### Throughout · Write-up
- `[CC]` Draft paper sections on `docs/aditya/...` branches. `[YOU]` verify every claim.
- `[YOU]` Pin the next ICRA/IROS deadline; reverse-plan.

---

## 6 · Definition of Done & milestones

- **Phase 0:** GATE 0 decided, with reproducible baseline + a tested patching pipeline. *(week 1–2)*
- **Phase 1:** a released, CI'd robustness benchmark + draft paper section. *(≈ month 4–5 → workshop paper)*
- **Phases 2–4:** per-axis `BackboneShare` across ≥2 models, with a fix that confirms localization (or an honest null). *(≈ month 7–10 → conference paper)*

A phase is "done" only when its `★` code has passing tests and the human has signed off on the gate.

---

## 7 · Future (do NOT build yet)

- A public **landing page** explaining the work for a general audience (likely a single-file Signal & Field-style page), and flipping the repo public, **after** the first paper milestone. Track as `feat/aditya/landing-page` when the time comes.

---

### Operating reminder for Claude Code
You build and run; the human decides gates and verifies numbers. Validate every pipeline before automating it. Never fabricate a result. Keep commits clean (no AI attribution), one branch per unit of work, private repo for now. The single most important thing you will build is `patching/` + `metrics/backbone_share.py` — get those provably correct, and the rest is honest engineering.
