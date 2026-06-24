"""Meaning-changing vs nuisance behave as labeled — and the registry keeps them separate.

The registry's class assignment is the construct-validity backbone (risk #2): an axis
in the wrong class would silently invalidate the memorization metric. Those mappings
are pure data, so they are tested for real here. The behavioral checks (does the edit
actually drop success?) stay skipped until the perturbation fns are implemented.
"""

import pytest

from vlamem.perturbations import registry


def test_meaning_changing_axes_are_classified_correctly():
    for name in ["object_identity", "object_pose", "instruction_semantics"]:
        assert registry.class_of(name) == "meaning_changing"


def test_nuisance_axes_are_classified_correctly():
    for name in ["background", "lighting", "texture", "camera_pose", "distractors"]:
        assert registry.class_of(name) == "nuisance"


def test_classes_are_disjoint():
    mc = set(registry.axes("meaning_changing"))
    nu = set(registry.axes("nuisance"))
    assert mc.isdisjoint(nu)
    assert set(registry.axes()) == mc | nu


def test_unknown_axis_raises():
    with pytest.raises(KeyError):
        registry.class_of("does_not_exist")


def test_get_returns_callable_and_class():
    fn, cls = registry.get("object_identity")
    assert callable(fn)
    assert cls == "meaning_changing"


@pytest.mark.skip(reason="behavioral: implement perturbation fns, then confirm success drops (P0.2)")
def test_meaning_changing_edit_drops_success():
    raise NotImplementedError


@pytest.mark.skip(reason="behavioral: nuisance edit should NOT drop success (Phase 1)")
def test_nuisance_edit_preserves_success():
    raise NotImplementedError
