"""Phase 1 · Instrument entrypoint — the robustness benchmark (publishable floor).

Runs the full perturbation profile for SmolVLA with bootstrap CIs → results/.
All logic in src/vlamem/.

Usage:
    python experiments/phase1_instrument.py --config configs/experiments/phase1_instrument.yaml
"""

from __future__ import annotations

import argparse

from vlamem.utils.io import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 1 robustness benchmark")
    parser.add_argument("--config", default="configs/experiments/phase1_instrument.yaml")
    args = parser.parse_args()

    config = load_yaml(args.config)
    raise NotImplementedError(f"Phase 1 not implemented yet (config: {config.get('experiment')}).")


if __name__ == "__main__":
    main()
