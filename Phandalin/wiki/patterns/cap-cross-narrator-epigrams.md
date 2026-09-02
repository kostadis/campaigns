---
baseline_sha256: 87e6fa1ce3af1c97ec957d5fdb76d4fde595b1ad495dbffd2f07145e12fa1f6e
conflict_ruling_refs: []
evidence:
- narration/session_doc_scene_03_first_sight_of_phandalin.md
- narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md
- narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md
- narration/voice_critique_summary.md
- narration/voice_fixes_20250514.md
gate1:
  iteration_id: iter-006
  ruling: accepted
slug: cap-cross-narrator-epigrams
status: confirmed
tier: campaign
title: Cap cross-narrator epigrammatic closers
---

# Cap cross-narrator epigrammatic closers

## Problem
Abstract, balanced sentences repeatedly close paragraphs across several Phandalin POV voices, making otherwise distinct narrators share the same essay-like cadence.

## Root Cause
The guidance distinguishes vocabulary and sentence rhythm by character but gives no corpus-level budget for thesis-like closers, so a model-wide rhetorical habit can pass every local voice check.

## Corrective Strategy
Audit paragraph closers across the whole session and keep only those produced by a narrator's defined reasoning style. For this campaign, cap the move at one strong instance per narrator per session; turn surplus closers into concrete observation, bodily reaction, or action in that narrator's lens.

## Evidence
- narration/session_doc_scene_03_first_sight_of_phandalin.md
- narration/session_doc_scene_05_grave_robbers_on_the_quest_board.md
- narration/session_doc_scene_07_the_dwarves_don_t_believe_her.md
- narration/voice_critique_summary.md
- narration/voice_fixes_20250514.md
