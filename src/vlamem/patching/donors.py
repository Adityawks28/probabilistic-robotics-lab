"""Minimal-pair donor selection — which clean activation to patch in.

Patching is only valid against a MINIMAL PAIR: the clean donor episode must differ
from the corrupted one by exactly the meaning-changing edit and nothing else, so the
recovered performance is attributable to the conditioning and not to a confound.
This module picks/validates donors; the activation itself is read via models.hooks.
"""

from __future__ import annotations

from typing import Any


def select_donor(clean_episode: Any, corrupted_episode: Any) -> Any:
    """Return the clean episode whose backbone activation is the valid patch donor.

    Must assert the pair is minimal (differs only by the meaning-changing edit).
    """
    raise NotImplementedError("implement minimal-pair donor selection + validation")
