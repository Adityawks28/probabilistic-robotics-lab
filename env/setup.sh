#!/usr/bin/env bash
# env/setup.sh — reproducible environment for vla-memorization-localization.
#
# Installs LeRobot v0.5.0 (the SmolVLA stack) and the pinned dependencies, then
# installs this repo's `vlamem` package in editable mode.
#
# VERIFY (human): after this runs, confirm CUDA + a trivial GPU forward pass work
# before trusting any downstream number. See CLAUDE.md §S1 / Phase 0.
#
# Usage:
#   bash env/setup.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEROBOT_VERSION="0.5.0"

echo "[setup] repo root: ${REPO_ROOT}"
echo "[setup] target LeRobot version: ${LEROBOT_VERSION}"

# 1. Pinned Python dependencies.
python -m pip install --upgrade pip
python -m pip install -r "${REPO_ROOT}/env/requirements.txt"

# 2. LeRobot (SmolVLA stack). Pin to the exact version used for the study.
#    If you prefer the prebuilt image, use env/Dockerfile instead of this step.
python -m pip install "lerobot==${LEROBOT_VERSION}"

# 3. The research package itself, editable.
python -m pip install -e "${REPO_ROOT}[dev]"

echo "[setup] done."
echo "[setup] NEXT (human VERIFY): run a trivial GPU forward pass and confirm CUDA is available, e.g.:"
echo "        python -c 'import torch; assert torch.cuda.is_available(); print(torch.randn(8,8,device=\"cuda\").sum())'"
