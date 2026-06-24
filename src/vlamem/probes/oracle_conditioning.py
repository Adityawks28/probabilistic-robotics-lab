"""M2 — Oracle-conditioning probe.

Feed the action expert the CORRECT conditioning z (as if the backbone perfectly
understood the perturbed world) while the world is actually perturbed:
  * still fails → the EXPERT memorized (a correct z doesn't rescue it).
  * recovers   → the BACKBONE was the problem.
Uses base_api.set_cond to inject the oracle z.
"""

from __future__ import annotations

from typing import Any


def run(model: Any, episode: Any, perturbation: Any, oracle_z: Any) -> float:
    """Performance on the perturbed episode with the expert fed an oracle conditioning."""
    raise NotImplementedError
