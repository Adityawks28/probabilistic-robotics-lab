"""★ Protect the headline number. BackboneShare is unit-tested on hand-checked cases.

A silent bug here is fatal (CLAUDE.md §4): it produces a confident, wrong attribution.
These cases are computed by hand from the formula:

    BackboneShare = (perf_patched − perf_corrupted) / (perf_clean − perf_corrupted)
"""

import pytest

from vlamem.metrics.backbone_share import backbone_share


def test_full_recovery_is_one():
    # clean=1.0, corrupted=0.0, patched recovers fully → 1.0 (backbone-localized).
    assert backbone_share(perf_clean=1.0, perf_corrupted=0.0, perf_patched=1.0) == 1.0


def test_no_recovery_is_zero():
    # patch does nothing → 0.0 (expert-localized).
    assert backbone_share(perf_clean=1.0, perf_corrupted=0.0, perf_patched=0.0) == 0.0


def test_half_recovery_is_half():
    # hand-checked: (0.6 − 0.2) / (1.0 − 0.2) = 0.4 / 0.8 = 0.5 (entangled / GATE-0 fail).
    assert backbone_share(perf_clean=1.0, perf_corrupted=0.2, perf_patched=0.6) == pytest.approx(0.5)


def test_no_cliff_raises():
    # No measurable perturbation cliff → the ratio is undefined; fail loud.
    with pytest.raises(ValueError):
        backbone_share(perf_clean=0.9, perf_corrupted=0.9, perf_patched=0.9)


@pytest.mark.skip(reason="MemScore: implement after action_distribution_shift is validated (Phase 1)")
def test_mem_score_sensitivity_gap():
    raise NotImplementedError


@pytest.mark.skip(reason="bootstrap CI: implement with seeded resampling (Phase 1)")
def test_bootstrap_ci_coverage():
    raise NotImplementedError
