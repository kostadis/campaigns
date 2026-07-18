#!/usr/bin/env bash
# Stage 2b/2c — aggregate known-entity facts into per-entity state dossiers.
# Local Spark (122B, thinking off), --known-only, resumable (existing dossiers skipped).
set -euo pipefail
cd "$(dirname "$0")/../.."   # campaign root (Hillsfar/Hillsfar)

DGX_NO_THINKING=1 ~/.venvs/main/bin/python ~/src/CampaignGenerator/facts_to_state.py \
  --corpus 'docs/ensemble/per_chapter/*/merged.json' \
  --aliases docs/ensemble/aliases.json \
  --known-names docs/background/ddex34-its-all-in-the-blood-inventory.md \
                docs/ensemble/known_names.md \
  --known-only \
  --min-facts 3 \
  --out-dir docs/ensemble/state_dossiers \
  --endpoints http://192.168.1.147:8001/v1 \
  --entity-parallel 8 \
  --model Qwen/Qwen3.5-122B-A10B-FP8

echo "[run_stage2_aggregate] exit status: $?"
