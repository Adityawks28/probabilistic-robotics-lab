"""(Phase 3) Representation alignment / invariance — if BACKBONE-localized.

Aligns the backbone conditioning so it is SENSITIVE to meaning-changing edits and
INVARIANT to nuisance, at the point where it conditions the expert. Pursued only if
Phase 2 localizes the failure to the backbone, and only kept if it beats the cheap
baselines without harming success.
"""

from __future__ import annotations

from typing import Any


def alignment_loss(repr_clean: Any, repr_perturbed: Any, perturb_class: str) -> Any:
    """Loss enforcing sensitivity-to-meaning / invariance-to-nuisance on the conditioning."""
    raise NotImplementedError("Phase 3, only if backbone-localized")
