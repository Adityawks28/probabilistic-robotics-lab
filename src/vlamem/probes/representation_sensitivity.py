"""M1 — Representation-sensitivity probe.

Does the backbone's conditioning feature MOVE under a meaning-changing edit? If the
feature barely shifts when the meaning changes, the failure is upstream (the backbone
isn't encoding the change). Measure representation distance and correlate it with
whether the action actually changed.
"""

from __future__ import annotations

from typing import Any


def representation_distance(repr_clean: Any, repr_perturbed: Any) -> float:
    """Distance between backbone conditioning representations (clean vs. perturbed)."""
    raise NotImplementedError


def run(model: Any, episode: Any, perturbation: Any) -> dict[str, float]:
    """Return the representation shift and whether the action changed, for correlation."""
    raise NotImplementedError
