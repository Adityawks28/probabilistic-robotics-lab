"""Bootstrap confidence intervals over episodes / seeds.

Robot eval is noisy and small-sample (risk #10). Every headline number (BackboneShare,
MemScore) is reported with a bootstrap CI, not a bare point estimate. Resampling is
seeded (from configs/seeds.yaml) so intervals are reproducible.

PURE function — no model, no IO — so it is provably correct in isolation and fully
unit-tested. Uses only numpy.
"""

from __future__ import annotations

from typing import Callable, Sequence

import numpy as np


def _mean(xs: np.ndarray) -> float:
    return float(np.mean(xs))


def bootstrap_ci(
    samples: Sequence[float],
    statistic: Callable[[np.ndarray], float] = _mean,
    *,
    n_resamples: int = 10000,
    ci: float = 0.95,
    seed: int = 0,
) -> tuple[float, float, float]:
    """Percentile bootstrap CI for a statistic over per-episode/per-seed samples.

    Args:
        samples: Observed values (e.g. per-episode BackboneShare). Must be non-empty.
        statistic: Function mapping a resampled array → scalar. Defaults to the mean.
        n_resamples: Number of bootstrap resamples (with replacement).
        ci: Central interval mass, e.g. 0.95 for a 95% CI.
        seed: Seed for the resampling RNG, for reproducibility.

    Returns:
        ``(point_estimate, ci_low, ci_high)`` where ``point_estimate`` is the statistic
        on the observed sample and the bounds are the percentile-bootstrap interval.

    Raises:
        ValueError: if ``samples`` is empty, ``n_resamples`` < 1, or ``ci`` ∉ (0, 1).
    """
    arr = np.asarray(samples, dtype=float)
    if arr.size == 0:
        raise ValueError("bootstrap_ci: samples must be non-empty")
    if n_resamples < 1:
        raise ValueError("bootstrap_ci: n_resamples must be >= 1")
    if not (0.0 < ci < 1.0):
        raise ValueError(f"bootstrap_ci: ci must be in (0, 1), got {ci}")

    point = statistic(arr)

    rng = np.random.default_rng(seed)
    n = arr.size
    idx = rng.integers(0, n, size=(n_resamples, n))
    resampled = arr[idx]
    stats = np.array([statistic(row) for row in resampled])

    alpha = 1.0 - ci
    lo = float(np.percentile(stats, 100.0 * (alpha / 2.0)))
    hi = float(np.percentile(stats, 100.0 * (1.0 - alpha / 2.0)))
    return point, lo, hi
