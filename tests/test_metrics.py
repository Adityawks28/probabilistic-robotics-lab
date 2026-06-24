"""★ Protect the headline number. BackboneShare is unit-tested on hand-checked cases.

A silent bug here is fatal (CLAUDE.md §4): it produces a confident, wrong attribution.
These cases are computed by hand from the formula:

    BackboneShare = (perf_patched − perf_corrupted) / (perf_clean − perf_corrupted)
"""

import numpy as np
import pytest

from vlamem.metrics.backbone_share import backbone_share
from vlamem.metrics.bootstrap import bootstrap_ci
from vlamem.metrics.mem_score import action_distribution_shift, mem_score


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


# ── action_distribution_shift (energy distance) ────────────────────────────────────


def test_shift_is_zero_for_identical_distributions():
    rng = np.random.default_rng(0)
    x = rng.normal(size=(200, 3))
    assert action_distribution_shift(x, x) == pytest.approx(0.0, abs=1e-9)


def test_shift_grows_with_mean_separation():
    rng = np.random.default_rng(0)
    base = rng.normal(size=(200, 2))
    near = base + 0.5
    far = base + 5.0
    d_near = action_distribution_shift(base, near)
    d_far = action_distribution_shift(base, far)
    assert 0.0 < d_near < d_far


def test_shift_is_symmetric():
    rng = np.random.default_rng(1)
    a = rng.normal(size=(150, 2))
    b = rng.normal(loc=2.0, size=(150, 2))
    assert action_distribution_shift(a, b) == pytest.approx(action_distribution_shift(b, a), rel=1e-9)


def test_shift_rejects_mismatched_dims():
    with pytest.raises(ValueError):
        action_distribution_shift(np.zeros((4, 2)), np.zeros((4, 3)))


# ── mem_score (default sensitivity gap) ─────────────────────────────────────────────


def test_mem_score_default_is_sensitivity_gap():
    # robust: responds to meaning (high), ignores nuisance (low) → large positive.
    assert mem_score(meaning_shift=1.0, nuisance_shift=0.1) == pytest.approx(0.9)
    # memorized: barely responds to meaning → near zero / negative.
    assert mem_score(meaning_shift=0.1, nuisance_shift=0.1) == pytest.approx(0.0)
    assert mem_score(meaning_shift=0.05, nuisance_shift=0.2) < 0.0


# ── bootstrap_ci (seeded percentile bootstrap) ──────────────────────────────────────


def test_bootstrap_point_is_observed_mean():
    samples = [0.2, 0.4, 0.6, 0.8, 1.0]
    point, lo, hi = bootstrap_ci(samples, n_resamples=2000, seed=0)
    assert point == pytest.approx(np.mean(samples))
    assert lo <= point <= hi


def test_bootstrap_is_reproducible_under_seed():
    samples = [0.1, 0.3, 0.5, 0.7, 0.9, 0.2, 0.8]
    a = bootstrap_ci(samples, n_resamples=3000, seed=42)
    b = bootstrap_ci(samples, n_resamples=3000, seed=42)
    assert a == b


def test_bootstrap_zero_variance_collapses_interval():
    point, lo, hi = bootstrap_ci([0.5, 0.5, 0.5], n_resamples=500, seed=0)
    assert point == pytest.approx(0.5)
    assert lo == pytest.approx(0.5)
    assert hi == pytest.approx(0.5)


def test_bootstrap_rejects_empty():
    with pytest.raises(ValueError):
        bootstrap_ci([], n_resamples=100)
