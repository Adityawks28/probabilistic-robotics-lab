"""Sweep runner — orchestrates the experiment grid.

Iterates model × intervention × perturbation axis × seed, calling eval.harness per
cell and writing results to the configured output dir. Sweeps are queued overnight via
claude-ops ONLY AFTER the underlying pipeline is validated (CLAUDE.md: validate before
automate) — an unvalidated sweep runs all night and hands back a confident wrong number.
"""

from __future__ import annotations

from typing import Any


def run_sweep(config: dict[str, Any]) -> Any:
    """Run the full grid defined by ``config`` and persist results.

    Reads the seed set from configs/seeds.yaml and the axes from
    configs/perturbations.yaml. Returns a summary of written result paths.
    """
    raise NotImplementedError("iterate the grid via eval.harness.evaluate once validated")
