"""Phase 0 · Go/No-Go pilot entrypoint — GATES EVERYTHING.

Thin wrapper: parse the config, then drive the clean → corrupted → patched loop on a
handful of episodes so the human can run the §4 sanity checks and decide GATE 0. All
logic lives in src/vlamem/. Does NOT proceed past the gate autonomously.

Usage:
    python experiments/phase0_pilot.py --config configs/experiments/phase0_pilot.yaml
"""

from __future__ import annotations

import argparse

from vlamem.utils.io import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 0 Go/No-Go pilot")
    parser.add_argument("--config", default="configs/experiments/phase0_pilot.yaml")
    args = parser.parse_args()

    config = load_yaml(args.config)
    raise NotImplementedError(
        f"Phase 0 pilot not implemented yet (loaded config: {config.get('experiment')}). "
        "Build + validate the patching pipeline interactively before running (CLAUDE.md §4)."
    )


if __name__ == "__main__":
    main()
