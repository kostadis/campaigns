---
baseline_sha256: 87e6fa1ce3af1c97ec957d5fdb76d4fde595b1ad495dbffd2f07145e12fa1f6e
conflict_ruling_refs: []
evidence:
- narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md
- narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md
- narration/voice_critique_summary.md
- narration/voice_fixes_20250514.md
gate1:
  iteration_id: iter-006
  ruling: accepted
slug: encode-narrator-bookkeeping-budgets
status: confirmed
tier: campaign
title: Encode narrator-specific bookkeeping budgets
---

# Encode narrator-specific bookkeeping budgets

## Problem
Ledger, filing, cataloguing, and auditing language crossed from Vukradin's argumentative voice into Valphine's POV, blurring two narrator lenses while the mechanical bookkeeping check remained skipped.

## Root Cause
The prose rulebook names character vocabularies but has no structured `voice_lint` configuration that converts those distinctions into narrator-specific bookkeeping and filing limits.

## Corrective Strategy
Add a structured campaign lint block that permits a narrow bookkeeping budget for Vukradin and sets zero or stricter budgets for narrators whose lenses are not administrative. Keep unconfigured categories visibly skipped, and use the lint result as review evidence rather than as an automatic Gate decision.

## Evidence
- narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md
- narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md
- narration/voice_critique_summary.md
- narration/voice_fixes_20250514.md
