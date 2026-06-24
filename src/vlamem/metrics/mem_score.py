"""MemScore — the memorization metric (sensitivity gap).

A memorized policy is INSENSITIVE where it should be sensitive: its action distribution
barely shifts under a meaning-changing edit, while shifting normally under nuisance.

Two pieces:
  * ``action_distribution_shift`` — distance between two sets of action samples. Uses the
    ENERGY DISTANCE: sensitive to both location and shape, so it respects the
    multimodality of a flow-matching expert (a mean-shift metric would miss mode changes).
    PURE + unit-tested.
  * ``mem_score`` — combines per-class sensitivities into one indicator. The exact
    combiner is a research-judgment call the HUMAN owns ([YOU]); the default below is a
    documented, defensible starting point (the sensitivity gap), not a fixed claim.
"""

from __future__ import annotations

import numpy as np


def _pairwise_mean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """Mean Euclidean distance between every row of ``a`` and every row of ``b``."""
    # a: (n, d), b: (m, d) → (n, m) distances, then mean.
    diff = a[:, None, :] - b[None, :, :]
    return float(np.sqrt((diff ** 2).sum(axis=-1)).mean())


def action_distribution_shift(actions_a, actions_b) -> float:
    """Energy distance between two empirical action distributions.

    ``actions_a`` / ``actions_b`` are array-likes of shape (n_samples, action_dim)
    (a 1-D array is treated as (n_samples, 1)). Returns a non-negative scalar that is
    0 iff the two empirical distributions coincide and grows with both mean shift and
    shape/spread change.

        energy = 2·E‖A−B‖ − E‖A−A'‖ − E‖B−B'‖

    Raises:
        ValueError: if either sample set is empty or the action dims disagree.
    """
    a = np.asarray(actions_a, dtype=float)
    b = np.asarray(actions_b, dtype=float)
    if a.ndim == 1:
        a = a[:, None]
    if b.ndim == 1:
        b = b[:, None]
    if a.size == 0 or b.size == 0:
        raise ValueError("action_distribution_shift: sample sets must be non-empty")
    if a.shape[1] != b.shape[1]:
        raise ValueError(
            f"action_distribution_shift: action dims disagree ({a.shape[1]} vs {b.shape[1]})"
        )

    cross = _pairwise_mean_distance(a, b)
    within_a = _pairwise_mean_distance(a, a)
    within_b = _pairwise_mean_distance(b, b)
    energy = 2.0 * cross - within_a - within_b
    # Clamp tiny negative values from floating-point error; energy distance is >= 0.
    return float(max(0.0, energy))


def mem_score(meaning_shift: float, nuisance_shift: float) -> float:
    """Combine per-class sensitivities into a memorization indicator (DEFAULT definition).

    Default = the sensitivity gap ``meaning_shift − nuisance_shift``:
      * large positive → robust (responds to meaning, ignores nuisance),
      * near zero / negative → memorization signal (fails to respond to meaning).

    NOTE: the final metric definition is owned by the human ([YOU]); this default exists
    so the pipeline is runnable and the property (monotone in meaning-sensitivity) is
    testable. Revisit once Phase 1 produces real distributions.
    """
    return float(meaning_shift) - float(nuisance_shift)
