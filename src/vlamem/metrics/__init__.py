"""★ The numbers the thesis depends on: BackboneShare, MemScore, bootstrap CIs.

``backbone_share`` is the headline ratio and is implemented as a pure, unit-tested
function (no model, no IO) so its correctness is provable in isolation — a hand-checked
case lives in tests/test_metrics.py. MemScore and bootstrap follow once the harness
feeds them real performance numbers.
"""
