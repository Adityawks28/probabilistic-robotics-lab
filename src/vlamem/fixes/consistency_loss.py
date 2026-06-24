"""(Phase 3) Perturbation-consistency loss on the velocity field — if EXPERT-localized.

Trains the flow-matching action expert so its action distribution MOVES under a
meaning-changing edit and STAYS under nuisance — directly countering the memorized
replay. Only pursued if Phase 2 localizes the failure to the expert, and only kept if
it beats the augmentation/dropout baselines without harming success/multimodality.
"""

from __future__ import annotations

from typing import Any


def consistency_loss(velocity_clean: Any, velocity_perturbed: Any, perturb_class: str) -> Any:
    """Loss enforcing move-under-meaning / stay-under-nuisance on the velocity field."""
    raise NotImplementedError("Phase 3, only if expert-localized")
