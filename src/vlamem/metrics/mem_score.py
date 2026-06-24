"""MemScore — the memorization metric (sensitivity gap).

A memorized policy is INSENSITIVE where it should be sensitive: its action distribution
barely shifts under a meaning-changing edit, while shifting normally under nuisance.
MemScore operationalizes that asymmetry as the gap between action-distribution shift on
meaning-changing vs. nuisance axes (high meaning-shift, low nuisance-shift = robust;
low meaning-shift = memorization).

Stays a stub until the harness provides real action distributions to compare — the
distribution-shift estimator must be validated before this number is trusted.
"""

from __future__ import annotations

from typing import Any


def action_distribution_shift(actions_a: Any, actions_b: Any) -> float:
    """Distance between two action distributions (e.g. before/after a perturbation)."""
    raise NotImplementedError("choose + validate the distribution-shift estimator")


def mem_score(meaning_shift: float, nuisance_shift: float) -> float:
    """Combine sensitivity on each axis class into a single memorization score.

    Defined once the shift estimator is validated, so the combination rule is fixed
    against real data rather than guessed.
    """
    raise NotImplementedError("define after action_distribution_shift is validated")
