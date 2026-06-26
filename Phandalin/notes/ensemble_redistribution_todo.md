# Ensemble: Redistribution Pass TODO

After the alias review pass (`/ensemble-alias-review`) is complete, a second pass is needed for rejected generic-label dossiers.

## The Problem

The cross-chapter merge in `docs/ensemble/run.py` uses entity name as its only key. This correctly merges "Cryovain" across chapters, but incorrectly conflates "boar" in ch 41 with "boar" in ch 44 — different animals, same label.

The alias review (this pass) works at the **entity name** level and can only merge or reject whole dossiers. It cannot split a dossier whose facts came from different encounters.

## What the Redistribution Pass Needs

A **fact-level tool** that:

1. Takes a rejected dossier (e.g., "boar", "bandit", "Anchorite", "Speaker", "twig blights")
2. Shows each fact with its `source_chapter` field (already present in `merged.json`)
3. Lets the user assign each fact to a specific entity:
   - An existing named dossier (e.g., assign "boar" ch40 facts → "Anchorite of Talos" because that's the anchorite shapeshifted)
   - A new per-encounter label (e.g., "talking boar ch22", "Woodland Manse Boar")
   - Discard (if the fact is genuinely spurious)

## Dossiers to redistribute (from alias review pass)

- `Narrator` / `The narrator` — VTT speaker labels
- `Speaker` / `the speaker` — VTT speaker labels, facts span many NPCs
- `boar` / `boars` — multiple distinct encounters (ch 22 talking boar ≠ ch 41-44 Woodland Manse boars)
- `bandit` / `bandits` / `bandit count` — aggregated across many unrelated bandit encounters
- `twig blights` / `vine blights` / `blights` — facts from different encounter locations
- `Anchorite` / `anchorite of Talos` (monster type) — multiple distinct anchorite encounters
- `dragon count` — meta-fact artifact
- `Talos` (as npc) — deity invocations mislabeled as NPC facts
- `Bard` → already resolved as Vukradin alias

## Skill to build

Name: `ensemble-fact-redistribute`
Input: a rejected dossier name or list of names
Working data: `docs/ensemble/merged.json` (has `source_chapter` per fact)
Output: reassignment map → feeds back into a new merge or directly into per-entity dossiers

## Pipeline improvement: split chapters by narrator section before extraction

**Problem:** Session docs have per-narrator sections (one POV per section, e.g. "## Soma — The Cursed Clearing").
The current `run.py` passes the full chapter to the extractor, so self-referential facts get labeled
subject="Narrator" instead of subject="Soma". This creates the 119-fact redistribution problem above.

**Fix:** In `run.py`, split each chapter doc on narrator section headers before extraction.
Run one extraction call per section, injecting `narrator_name` as context so the LLM can attribute
self-referential facts correctly.

**Trade-off:** N calls per chapter (one per narrator) instead of 1. Each call is smaller and cleaner.

**Prerequisite:** Check that section headers are consistently machine-parseable across chapter docs.
Pull 2–3 docs and assess format consistency before implementing.

**Impact:** Would eliminate the Narrator/Speaker redistribution problem for all future chapters.
The current 119 facts remain a one-time manual cleanup.
