"""Meaning-changing perturbations — the action SHOULD change.

Object identity, object pose, and instruction semantics. Built on LIBERO-PRO /
LIBERO-Plus. A robust model is SENSITIVE here; insensitivity is the memorization tell.
Each function takes a scene/episode spec and returns an edited copy + metadata.
"""

from __future__ import annotations

from typing import Any


def object_identity(episode: Any, **kwargs: Any) -> Any:
    """Swap the target object for a different one (meaning changes)."""
    raise NotImplementedError("implement via LIBERO-PRO object swap")


def object_pose(episode: Any, **kwargs: Any) -> Any:
    """Move/rotate the target object (meaning changes)."""
    raise NotImplementedError("implement via LIBERO-PRO pose edit")


def instruction_semantics(episode: Any, **kwargs: Any) -> Any:
    """Rewrite the instruction so it means something else (meaning changes)."""
    raise NotImplementedError("implement instruction rewrite")
