"""★ CRITICAL — the engineering make-or-break (CLAUDE.md P0.3, risk #8).

Patching is impossible without three capabilities on the real model:

  1. FREEZE the vision-language backbone and run the action expert alone.
  2. FEED the expert a chosen conditioning ``z`` (custom or oracle).
  3. READ and PATCH the intermediate backbone→expert activation (the conditioning
     representation handed from backbone to expert).

These hook points MUST be discovered INTERACTIVELY with the human (not autonomously
overnight): Claude reads SmolVLA's LeRobot implementation, proposes the exact module
names + tensor shapes, and the human confirms them before anything downstream is
trusted. Getting a hook point wrong silently corrupts every number. See CLAUDE.md §4
hard-stop #2.

Until the hook points are confirmed and written down here, these functions raise
rather than guess — a wrong guess is worse than no implementation.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Iterator

# Filled in during hook discovery (P0.3), then version-controlled here so every run
# uses the confirmed points. Example shape: {"read": "vlm.encoder.norm_out", ...}.
HOOK_POINTS: dict[str, str] = {}


def freeze_backbone(model: Any) -> None:
    """Freeze the vision-language backbone so only the action expert runs/updates.

    Confirm against the real module tree during P0.3 before relying on this.
    """
    raise NotImplementedError("freeze_backbone: confirm backbone module(s) in P0.3")


@contextmanager
def read_activation(model: Any, hook_point: str) -> Iterator[dict[str, Any]]:
    """Context manager that captures the activation at ``hook_point`` into a dict.

    Yields a holder dict; after the forward pass, ``holder["value"]`` is the captured
    tensor. Used to grab a clean-run donor activation for patching.
    """
    raise NotImplementedError("read_activation: register a forward hook at the confirmed point")


@contextmanager
def patch_activation(model: Any, hook_point: str, donor: Any) -> Iterator[None]:
    """Context manager that overwrites the activation at ``hook_point`` with ``donor``.

    This is the core surgical move: run the corrupted input but splice in the clean
    backbone activation, then measure recovery (see patching/activation_patch.py).
    """
    raise NotImplementedError("patch_activation: register a forward hook that replaces the tensor")
