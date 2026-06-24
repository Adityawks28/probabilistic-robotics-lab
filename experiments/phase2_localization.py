"""Phase 2 · Localization entrypoint — the headline.

Runs the four converging methods (M1–M4); M3 (activation patching) is the headline
BackboneShare. RE-RUN the patching sanity checks on the full pipeline before trusting
any number (CLAUDE.md §4 hard-stop #3). All logic in src/vlamem/.

Usage:
    python experiments/phase2_localization.py --config configs/experiments/phase2_localization.yaml
"""

from __future__ import annotations

import argparse

from vlamem.utils.io import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 2 core localization")
    parser.add_argument("--config", default="configs/experiments/phase2_localization.yaml")
    args = parser.parse_args()

    config = load_yaml(args.config)
    raise NotImplementedError(f"Phase 2 not implemented yet (config: {config.get('experiment')}).")


if __name__ == "__main__":
    main()
