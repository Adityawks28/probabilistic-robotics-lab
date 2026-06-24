"""M4 — Cross-swap probe.

Triangulate by pairing components across clean/perturbed exposure:
  * clean backbone  + perturbation-exposed expert
  * perturbation-exposed backbone + clean expert
Which pairing carries the failure isolates the responsible module from another angle.
"""

from __future__ import annotations

from typing import Any


def run(model: Any, episode: Any, perturbation: Any) -> dict[str, float]:
    """Return performance for each cross-swapped backbone/expert pairing."""
    raise NotImplementedError
