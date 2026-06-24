"""Phase 4 · Generality entrypoint — second model.

Replicates the core attribution on TinyVLA behind the same base_api. Re-sanity-check
patching on the new model before trusting it. All logic in src/vlamem/.

Usage:
    python experiments/phase4_generality.py --config configs/experiments/phase4_generality.yaml
"""

from __future__ import annotations

import argparse

from vlamem.utils.io import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 4 generality (TinyVLA)")
    parser.add_argument("--config", default="configs/experiments/phase4_generality.yaml")
    args = parser.parse_args()

    config = load_yaml(args.config)
    raise NotImplementedError(f"Phase 4 not implemented yet (config: {config.get('experiment')}).")


if __name__ == "__main__":
    main()
