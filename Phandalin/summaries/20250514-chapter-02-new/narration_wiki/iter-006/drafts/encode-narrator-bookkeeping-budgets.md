---
slug: encode-narrator-bookkeeping-budgets
title: Encode narrator-specific bookkeeping budgets
evidence:
  - narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md
  - narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md
  - narration/voice_critique_summary.md
  - narration/voice_fixes_20250514.md
conflict_ids: []
proposed_tier: campaign
mentions_campaign_identity: true
---

# Encode narrator-specific bookkeeping budgets

## Problem

Ledger, filing, cataloguing, and auditing language crossed from Vukradin's argumentative voice into Valphine's POV, blurring two narrator lenses while the mechanical bookkeeping check remained skipped.

## Root Cause

The prose rulebook names character vocabularies but has no structured `voice_lint` configuration that converts those distinctions into narrator-specific bookkeeping and filing limits.

## Corrective Strategy

Add a structured campaign lint block that permits a narrow bookkeeping budget for Vukradin and sets zero or stricter budgets for narrators whose lenses are not administrative. Keep unconfigured categories visibly skipped, and use the lint result as review evidence rather than as an automatic Gate decision.

## Evidence

- `narration/voice_critique_summary.md` — The review found three uses of “ledger” across Vukradin and Valphine plus filing-family terms in Valphine, and records that the missing `voice_lint` block prevented mechanical detection.
- `narration/voice_fixes_20250514.md` — The approved repair retained one “ledger” use in Vukradin, removed the crossings from Valphine, and verified that bookkeeping remained skipped because the configuration was still absent.
- `narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md` — The retained Vukradin usage demonstrates the campaign-specific allowance the future budget should preserve.
- `narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md` — The revised Valphine section demonstrates the intended zero-crossing result without flattening her motive-systems voice.
