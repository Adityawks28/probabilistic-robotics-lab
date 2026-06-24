"""Bootstrap confidence intervals over episodes / seeds.

Robot eval is noisy and small-sample (risk #10). Every headline number (BackboneShare,
MemScore) is reported with a bootstrap CI, not a bare point estimate. Resampling is
seeded from configs/seeds.yaml so intervals are reproducible.
"""

from __future__ import annotations

from typing import Callable, Sequence


def bootstrap_ci(
    samples: Sequence[float],
    statistic: Callable[[Sequence[float]], float],
    *,
    n_resamples: int = 10000,
    ci: float = 0.95,
    seed: int = 0,
) -> tuple[float, float, float]:
    """Return ``(point_estimate, ci_low, ci_high)`` via percentile bootstrap.

    Pure resampling over the provided per-episode/per-seed samples. Implemented in
    Phase 1 alongside the stats protocol; kept a stub here so no CI is reported from
    an unvalidated estimator.
    """
    raise NotImplementedError("implement percentile bootstrap with seeded resampling (Phase 1)")
