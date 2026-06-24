"""Config / result IO — load YAML configs, save metrics and figures.

Real (not stubbed) for config loading since experiments need it immediately and it
carries no fabrication risk. Result-writing helpers are kept minimal and explicit.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML config file into a dict. Raises if the file is missing."""
    import yaml

    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"config not found: {p}")
    with p.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"config {p} did not parse to a mapping (got {type(data)!r})")
    return data


def save_json(obj: Any, path: str | Path) -> Path:
    """Serialize results to JSON, creating parent dirs. Returns the written path."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, sort_keys=True)
    return p
