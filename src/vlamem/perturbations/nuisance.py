"""Nuisance perturbations — the action SHOULD NOT change.

Background, lighting, texture, camera pose, distractors. A robust model is INVARIANT
here. Sensitivity to nuisance is a different failure (brittleness), not memorization;
keeping these separate from meaning-changing edits is what makes the metric valid.
"""

from __future__ import annotations

from typing import Any


def background(episode: Any, **kwargs: Any) -> Any:
    """Change the scene background (meaning unchanged)."""
    raise NotImplementedError("implement via LIBERO-PRO background swap")


def lighting(episode: Any, **kwargs: Any) -> Any:
    """Change lighting / brightness (meaning unchanged)."""
    raise NotImplementedError


def texture(episode: Any, **kwargs: Any) -> Any:
    """Retexture surfaces (meaning unchanged)."""
    raise NotImplementedError


def camera_pose(episode: Any, **kwargs: Any) -> Any:
    """Jitter camera extrinsics (meaning unchanged)."""
    raise NotImplementedError


def distractors(episode: Any, **kwargs: Any) -> Any:
    """Add task-irrelevant objects (meaning unchanged)."""
    raise NotImplementedError
