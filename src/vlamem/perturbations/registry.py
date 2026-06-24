"""Name → perturbation function, keeping the two classes strictly separate.

Real (not stubbed): the registry itself carries no fabrication risk and enforces the
meaning-changing / nuisance separation that the whole construct-validity argument rests
on. ``get`` refuses to return a function without telling you which class it belongs to.
"""

from __future__ import annotations

from typing import Callable, Literal

from vlamem.perturbations import meaning_changing as mc
from vlamem.perturbations import nuisance as nu

PerturbClass = Literal["meaning_changing", "nuisance"]

# The single source of truth for which axis is which class. Adding an axis to the
# wrong class here is the one mistake that would invalidate the memorization metric.
_MEANING_CHANGING: dict[str, Callable] = {
    "object_identity": mc.object_identity,
    "object_pose": mc.object_pose,
    "instruction_semantics": mc.instruction_semantics,
}

_NUISANCE: dict[str, Callable] = {
    "background": nu.background,
    "lighting": nu.lighting,
    "texture": nu.texture,
    "camera_pose": nu.camera_pose,
    "distractors": nu.distractors,
}


def class_of(name: str) -> PerturbClass:
    """Return which class an axis belongs to. Raises KeyError if unknown."""
    if name in _MEANING_CHANGING:
        return "meaning_changing"
    if name in _NUISANCE:
        return "nuisance"
    raise KeyError(f"unknown perturbation axis: {name!r}")


def get(name: str) -> tuple[Callable, PerturbClass]:
    """Return ``(fn, class)`` for a named axis, so callers always know the class."""
    cls = class_of(name)
    fn = _MEANING_CHANGING.get(name) or _NUISANCE[name]
    return fn, cls


def axes(perturb_class: PerturbClass | None = None) -> list[str]:
    """List axis names, optionally filtered to one class."""
    if perturb_class == "meaning_changing":
        return list(_MEANING_CHANGING)
    if perturb_class == "nuisance":
        return list(_NUISANCE)
    if perturb_class is None:
        return list(_MEANING_CHANGING) + list(_NUISANCE)
    raise ValueError(f"unknown perturbation class: {perturb_class!r}")
