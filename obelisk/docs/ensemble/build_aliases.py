#!/usr/bin/env python3
"""Generate docs/ensemble/aliases.json from the canonical corrections glossary.

Single source of truth for transcription garbles:
    notes/vtt_transcription_corrections.md   (wrong -> **right** rows)

Plus BUNDLING_ALIASES below — entity short-forms, titles, and player->character
mappings that must NOT be substituted into transcript text (the word-boundary
applier would double-expand them, e.g. "Sildar Hallwinter" -> "Sildar Hallwinter
Hallwinter"), so they cannot live in the corrections glossary. This dict is the
ONLY hand-maintained source of bundling aliases; edit it here.

Output: aliases.json mapping {canonical: [variant, ...]} for
facts_to_state.py --aliases. DO NOT hand-edit aliases.json — re-run this script.
"""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]          # campaign dir
CORRECTIONS = ROOT / "notes" / "vtt_transcription_corrections.md"
OUT = ROOT / "docs" / "ensemble" / "aliases.json"

# variant -> canonical. Bundling only (never applied to transcript text).
BUNDLING_ALIASES = {
    "Sildar": "Sildar Hallwinter",
    "Toblen": "Toblen Stonehill",
    "Professor Orryn Voss": "Orryn Voss",
    "Maela": "Sister Maela",
    "Sister Maela Dawnforge": "Sister Maela",
    "Zenvon Foreput": "Zenvon",
    "Nikhil Reddy": "Zenvon",          # player -> character
    "Nikhil": "Zenvon",                # player (bare first name) -> character
}

row_re = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$")
bold_re = re.compile(r"\*\*(.+?)\*\*")

# 1) collect every variant -> canonical edge from both sources
edges = {}  # variant(lower-preserving original) -> canonical


def add_edge(variant: str, canonical: str):
    variant, canonical = variant.strip(), canonical.strip()
    if variant and canonical and variant.lower() != canonical.lower():
        edges[variant] = canonical


for line in CORRECTIONS.read_text(encoding="utf-8").splitlines():
    m = row_re.match(line)
    if not m:
        continue
    wrong, right = m.group(1), m.group(2)
    if wrong.strip().lower() == "wrong" or set(wrong.strip()) <= set("-:| "):
        continue
    bm = bold_re.search(right)
    canonical = bm.group(1) if bm else right
    canonical = re.sub(r"\s*\(.*\)\s*$", "", canonical).strip()   # drop trailing note
    for w in wrong.split(","):
        add_edge(w, canonical)

for variant, canonical in BUNDLING_ALIASES.items():
    add_edge(variant, canonical)


# 2) resolve chains to a terminal canonical (Toblin -> Toblen -> Toblen Stonehill)
def resolve(name: str) -> str:
    seen = set()
    while name in edges and name not in seen:
        seen.add(name)
        name = edges[name]
    return name


canon_to_variants = defaultdict(set)
for variant in edges:
    canon_to_variants[resolve(variant)].add(variant)

out = {c: sorted(v) for c, v in sorted(canon_to_variants.items())}
OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"wrote {OUT} — {len(out)} canonical entries")
for c, v in out.items():
    print(f"  {c}: {v}")
