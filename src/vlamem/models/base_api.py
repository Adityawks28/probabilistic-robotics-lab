"""Uniform VLA interface — every model speaks this so the pipeline is model-agnostic.

A concrete wrapper (SmolVLA, TinyVLA) implements this Protocol/ABC. The three methods
below are exactly what the patching/probing code needs:

  * ``predict``  — run the policy on an observation, return an action.
  * ``get_repr`` — read the backbone→expert conditioning representation (for M1, donors).
  * ``set_cond`` — feed the expert a chosen conditioning z (for M2 oracle-conditioning,
                   and for patching a donor activation into a corrupted run).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class VLA(ABC):
    """Abstract base for an efficient VLA (vision-language backbone + action expert)."""

    @abstractmethod
    def predict(self, observation: Any, instruction: str) -> Any:
        """Return the action(s) the policy takes for ``observation`` under ``instruction``."""
        raise NotImplementedError

    @abstractmethod
    def get_repr(self, observation: Any, instruction: str) -> Any:
        """Return the backbone→expert conditioning representation (the patch target)."""
        raise NotImplementedError

    @abstractmethod
    def set_cond(self, conditioning: Any) -> None:
        """Override the conditioning fed to the action expert on the next ``predict``.

        Pass ``None`` to clear the override and restore normal backbone conditioning.
        Used for oracle-conditioning (M2) and for patching donor activations.
        """
        raise NotImplementedError
