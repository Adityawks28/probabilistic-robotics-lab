"""Model wrappers behind a uniform VLA API, plus the critical activation hooks.

Every model (SmolVLA now, TinyVLA in Phase 4) is exposed through ``base_api.VLA`` so
the rest of the package is model-agnostic. ``hooks.py`` is the ★ critical surface that
makes patching possible: freeze the backbone, feed a chosen conditioning z, and
read/patch the backbone→expert activation.
"""
