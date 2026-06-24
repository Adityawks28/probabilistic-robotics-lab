"""(Phase 4) TinyVLA wrapped behind the same ``base_api.VLA``.

A second efficient flow/diffusion-expert VLA, used to show the localization finding
isn't SmolVLA-specific. Re-run the patching sanity checks on this model before
trusting any number it produces (CLAUDE.md Phase 4).
"""

from __future__ import annotations

from typing import Any

from vlamem.models.base_api import VLA


class TinyVLAWrapper(VLA):
    """Adapter over TinyVLA. Mirrors SmolVLAWrapper so the harness is unchanged."""

    def __init__(self, checkpoint: str, *, device: str = "cuda", dtype: str = "bfloat16") -> None:
        self.checkpoint = checkpoint
        self.device = device
        self.dtype = dtype
        self._policy: Any = None
        self._cond_override: Any = None

    def load(self) -> "TinyVLAWrapper":
        raise NotImplementedError("integrate TinyVLA in Phase 4")

    def predict(self, observation: Any, instruction: str) -> Any:
        raise NotImplementedError

    def get_repr(self, observation: Any, instruction: str) -> Any:
        raise NotImplementedError

    def set_cond(self, conditioning: Any) -> None:
        self._cond_override = conditioning
