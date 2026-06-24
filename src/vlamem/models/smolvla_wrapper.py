"""SmolVLA wrapped behind ``base_api.VLA`` — the project's baseline model.

Loads ``lerobot/smolvla_base`` (or a fine-tuned LIBERO checkpoint) and exposes
predict / get_repr / set_cond. The conditioning read/override is wired through
``models.hooks`` once the hook points are confirmed (P0.3).
"""

from __future__ import annotations

from typing import Any

from vlamem.models.base_api import VLA


class SmolVLAWrapper(VLA):
    """Adapter over LeRobot's SmolVLA policy."""

    def __init__(self, checkpoint: str, *, device: str = "cuda", dtype: str = "bfloat16") -> None:
        self.checkpoint = checkpoint
        self.device = device
        self.dtype = dtype
        self._policy: Any = None  # lazily loaded LeRobot policy
        self._cond_override: Any = None

    def load(self) -> "SmolVLAWrapper":
        """Load the underlying LeRobot SmolVLA policy onto ``self.device``."""
        raise NotImplementedError("load SmolVLA via LeRobot; confirm API in P0.1/P0.3")

    def predict(self, observation: Any, instruction: str) -> Any:
        raise NotImplementedError

    def get_repr(self, observation: Any, instruction: str) -> Any:
        raise NotImplementedError

    def set_cond(self, conditioning: Any) -> None:
        self._cond_override = conditioning
