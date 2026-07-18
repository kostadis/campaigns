#!/usr/bin/env bash
# Stage 1 ensemble extraction — Hillsfar (DDEX34)
# Source: docs/chapters/chapter_*.md (staged from per-session gm-assist.md).
# Model: live cross-box Qwen3.5-122B (single endpoint), thinking DISABLED
# (registry default thinking_default:false + DGX_NO_THINKING=1 belt-and-suspenders).
# Single endpoint -> --no-speculative. IPs not hostnames (WSL2 hostname-hang gotcha).
set -euo pipefail
cd "$(dirname "$0")"   # docs/ensemble

DGX_NO_THINKING=1 ~/.venvs/main/bin/python ~/src/CampaignGenerator/ensemble_batch.py \
  --chapters '../chapters/chapter_*.md' \
  --per-chapter-dir per_chapter \
  --out merged.json \
  --plan plan.yaml \
  --endpoints http://192.168.1.147:8001/v1 \
  --model Qwen/Qwen3.5-122B-A10B-FP8 \
  --chunk-parallel 4 \
  --no-speculative \
  --unit-timeout 600 \
  --embed-endpoint http://192.168.1.121:8000 \
  --embed-model Qwen/Qwen3-Embedding-0.6B \
  --embed-threshold 0.93 \
  --chapter-parallel 3

echo "[run_stage1] batch exit status: $?"
