---
slug: cap-cross-narrator-epigrams
title: Cap cross-narrator epigrammatic closers
evidence:
  - narration/session_doc_scene_03_first_sight_of_phandalin.md
  - narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md
  - narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md
  - narration/voice_critique_summary.md
  - narration/voice_fixes_20250514.md
conflict_ids: []
proposed_tier: campaign
mentions_campaign_identity: true
---

# Cap cross-narrator epigrammatic closers

## Problem

Abstract, balanced sentences repeatedly close paragraphs across several Phandalin POV voices, making otherwise distinct narrators share the same essay-like cadence.

## Root Cause

The guidance distinguishes vocabulary and sentence rhythm by character but gives no corpus-level budget for thesis-like closers, so a model-wide rhetorical habit can pass every local voice check.

## Corrective Strategy

Audit paragraph closers across the whole session and keep only those produced by a narrator's defined reasoning style. For this campaign, cap the move at one strong instance per narrator per session; turn surplus closers into concrete observation, bodily reaction, or action in that narrator's lens.

## Evidence

- `narration/voice_critique_summary.md` — The review identifies eleven epigrammatic closers across three narrators and none in Brewbarry, demonstrating cross-narrator convergence rather than a universal campaign voice.
- `narration/voice_fixes_20250514.md` — The approved repair reduced eleven instances to three, one per affected narrator, while preserving voice-lint cleanliness and distinct phrasing.
- `narration/session_doc_scene_03_first_sight_of_phandalin.md` — Soma's retained wager contrast shows the move working when it follows her patient physical reasoning.
- `narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md` — Vukradin's retained self-argument shows the move working inside his moral distinction-making.
- `narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md` — Valphine's retained motive-first maxim shows the move working inside her motive-systems lens.
