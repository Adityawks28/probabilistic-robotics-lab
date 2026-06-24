"""Evaluation harness — one (model × perturbation × seed) cell → metrics.

The single place that ties a model, a perturbation axis, and a seed together and
returns a metrics dict. Seeds via utils.seeding; never hard-codes paths/hyperparams
(reads them from a config dict). Fails loud rather than returning partial results.
"""

from __future__ import annotations

from typing import Any


def evaluate(model: Any, perturbation_name: str, seed: int, config: dict[str, Any]) -> dict[str, float]:
    """Run one evaluation cell and return its metrics.

    Args:
        model: A loaded ``base_api.VLA``.
        perturbation_name: An axis registered in perturbations.registry.
        seed: Seed from configs/seeds.yaml, applied via utils.seeding.set_seed.
        config: Resolved experiment config (base.yaml merged with the experiment yaml).
    """
    raise NotImplementedError("wire model + perturbation + seeded eval; return metrics dict")
