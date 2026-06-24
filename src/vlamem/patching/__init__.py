"""★ The crown jewel — activation patching + causal mediation.

The headline number (``BackboneShare``) comes from here. A silent bug in this package
is the single most dangerous failure in the whole project: it would hand a confident,
wrong attribution to a human who then builds a thesis on it. Hence the mandatory sanity
checks (clean→clean ≈ 100%, corrupted→corrupted still broken) before any sweep is
trusted (CLAUDE.md §4 hard-stop #3), and full test coverage in tests/test_patching.py.
"""
