#!/usr/bin/env python3
"""
Per-chapter ensemble driver for the Phandalin campaign.

For each chapter file in docs/chapters/:
  1. Runs ensemble.py (5-pass extraction → merge) into per_chapter/<stem>/
  2. Skips chapters where merged.json already exists (resumable)

After all chapters:
  3. Concatenates all per-chapter merged.json files into merged.json,
     adding a source_chapter field to each fact for provenance.
"""
import json
import subprocess
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
CAMPAIGN_DIR = SCRIPT_DIR.parent.parent
CHAPTERS_DIR = CAMPAIGN_DIR / "docs" / "chapters"
PLAN = SCRIPT_DIR / "plan.yaml"
PER_CHAPTER_DIR = SCRIPT_DIR / "per_chapter"

PYTHON = Path.home() / ".venvs/main/bin/python"
ENSEMBLE = Path.home() / "src/CampaignGenerator/ensemble.py"

ENDPOINTS = "http://192.168.1.147:8001/v1 http://192.168.1.121:8001/v1"
MODEL = "Qwen/Qwen3-Next-80B-A3B-Instruct-FP8"
EMBED_ENDPOINT = "http://192.168.1.121:8000"
EMBED_MODEL = "Qwen/Qwen3-Embedding-0.6B"

CHAPTER_PARALLEL = 3  # chapters submitted to vLLM concurrently
# Two endpoints (spark1+spark2), chunk-parallel=4 each → 4 chunks distributed
# across 2 boxes = ~2 per box per chapter, × 3 chapters = ~6 concurrent per box.
# Both boxes have --max-num-seqs 8, so this is comfortable.
# unit-timeout=0 disables the per-pass wall-clock cap.

chapters = sorted(CHAPTERS_DIR.glob("chapter_*.md"))

if not chapters:
    print(f"No chapter files found in {CHAPTERS_DIR}", file=sys.stderr)
    sys.exit(1)

PER_CHAPTER_DIR.mkdir(exist_ok=True)
print_lock = threading.Lock()

def run_chapter(chapter: Path) -> tuple[Path, bool]:
    stem = chapter.stem
    chapter_workdir = PER_CHAPTER_DIR / stem
    merged = chapter_workdir / "merged.json"

    if merged.exists():
        with print_lock:
            print(f"[skip]          {stem}")
        return chapter, True

    with print_lock:
        print(f"[extract+merge] {stem}")

    result = subprocess.run([
        str(PYTHON), str(ENSEMBLE),
        str(chapter),
        "--plan", str(PLAN),
        "--workdir", str(chapter_workdir),
        "--endpoints", *ENDPOINTS.split(),
        "--model", MODEL,
        "--chunk-parallel", "4",
        "--unit-timeout", "0",
        "--embed-endpoint", EMBED_ENDPOINT,
        "--embed-model", EMBED_MODEL,
        "--embed-threshold", "0.93",
    ])

    ok = result.returncode == 0
    if not ok:
        with print_lock:
            print(f"  ERROR: ensemble failed for {stem}", file=sys.stderr)
    return chapter, ok

failed = []
with ThreadPoolExecutor(max_workers=CHAPTER_PARALLEL) as pool:
    futures = {pool.submit(run_chapter, ch): ch for ch in chapters}
    for fut in as_completed(futures):
        chapter, ok = fut.result()
        if not ok:
            failed.append(chapter.stem)

if failed:
    print(f"\n{len(failed)} chapter(s) failed: {', '.join(failed)}", file=sys.stderr)
    print("Fix and re-run; completed chapters will be skipped.", file=sys.stderr)
    sys.exit(1)

# Combine
print("\n[combine] Merging per-chapter outputs...")
all_facts = []
missing = []
for chapter in chapters:
    merged = PER_CHAPTER_DIR / chapter.stem / "merged.json"
    if not merged.exists():
        missing.append(chapter.stem)
        continue
    facts = json.loads(merged.read_text())
    for fact in facts:
        fact["source_chapter"] = chapter.stem
    all_facts.extend(facts)

if missing:
    print(f"  WARNING: missing merged.json for: {', '.join(missing)}", file=sys.stderr)

out = SCRIPT_DIR / "merged.json"
out.write_text(json.dumps(all_facts, indent=2, ensure_ascii=False))
print(f"[done] {len(all_facts)} facts → {out}")
