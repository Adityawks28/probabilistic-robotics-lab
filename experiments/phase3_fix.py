"""Phase 3 · Fix entrypoint — causal validation (stretch).

Runs the baselines you must BEAT first (augmentation, dropout), then the targeted fix
chosen by where Phase 2 localized the failure. The human decides whether the fix
genuinely beats the baseline (CLAUDE.md §4 hard-stop #4). All logic in src/vlamem/.

Usage:
    python experiments/phase3_fix.py --config configs/experiments/phase3_fix.yaml
"""

from __future__ import annotations

import argparse

from vlamem.utils.io import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 3 causal validation / fix")
    parser.add_argument("--config", default="configs/experiments/phase3_fix.yaml")
    args = parser.parse_args()

    config = load_yaml(args.config)
    raise NotImplementedError(f"Phase 3 not implemented yet (config: {config.get('experiment')}).")


if __name__ == "__main__":
    main()
