"""Structured run logging → the experiment log (sheet / CSV / W&B).

Tracks the experiment grid: model × intervention × perturbation axis × seed. Kept
deliberately small; the backend is config-driven (configs/base.yaml: logging.backend).
"""

from __future__ import annotations

import logging
from typing import Any

_LOGGER_NAME = "vlamem"


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a configured module logger (idempotent)."""
    logger = logging.getLogger(name or _LOGGER_NAME)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("[%(asctime)s] %(name)s %(levelname)s: %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


def log_run(record: dict[str, Any], *, backend: str = "none") -> None:
    """Record one run's metadata + metrics to the configured experiment log.

    Args:
        record: Flat dict including model, intervention, axis, seed, and metrics.
        backend: One of "none" | "csv" | "wandb" (from configs/base.yaml).
    """
    if backend == "none":
        get_logger().info("run: %s", record)
        return
    raise NotImplementedError(f"log_run backend {backend!r} not implemented yet")
