"""Central seeding — one place to make every run deterministic.

Determinism is a hard requirement (CLAUDE.md §2): every run takes a seed, applied
here so torch/numpy/python all agree. This is a real (not stubbed) implementation
because it carries no fabrication risk and the rest of the package depends on it.
"""

from __future__ import annotations

import os
import random


def set_seed(seed: int, *, deterministic_torch: bool = True) -> int:
    """Seed Python, NumPy, and (if installed) PyTorch from a single integer.

    Args:
        seed: The seed to apply across all RNGs.
        deterministic_torch: If True, also request deterministic cuDNN behavior.

    Returns:
        The seed that was applied (echoed for logging).
    """
    if not isinstance(seed, int):
        raise TypeError(f"seed must be an int, got {type(seed)!r}")

    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)

    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        if deterministic_torch:
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    return seed
