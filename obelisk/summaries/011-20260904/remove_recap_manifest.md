# remove-recap manifest — Chapter 11 (011-20260904)

Run 2026-09-06. Skill: `/remove-recap`. GM ruling recorded per Phase 3.

## Detection

The recap was inspected directly in the speaker-attributed VTT because this
pass ran at the preferred pre-extraction stage: no `scene_extractions/` or
`scene_extractions_smoothed/` directory exists yet.

For deterministic analysis, transcript cues 45–72 were rendered temporarily in
the scene-extraction quote format expected by `find_recap.py`. The temporary
review file was removed after analysis.

| | |
|---|---|
| Source | `GMT20260904-220136_Recording.transcript (1).cleaned.vtt`, cues 45–72 |
| Score | **4/6 — RECAP, strong** |
| Quotes | 12 (GM share 0.83, longest GM-only run 5) |
| Markers | past-tense **12** vs live-play **0** |
| opening markers | `to remind you`, `quick summary` |
| closing_sting | `so here we are` |

The detector's closing-sting candidate occurs in cue 67:

> “Or was it the same quest? Anyway, so here we are.”

The remaining exchange is still recap correction and table orientation. The GM
confirmed the true boundary in cue 73: cut through **“Sorry, sorry.”** and keep
the immediately following live-play description:

> “The faint smell of smoke hangs in the air as you ascend a rugged ridge…”

Thus the ruled recap span is 00:07:09.560 through the opening words of cue 73 at
00:09:11.970. Live play begins within cue 73 after “Sorry, sorry.”

## Rescue check

`recap_unique.py --against summaries/010-20260821` compared the recap with
61,252 words of Chapter 10 material.

- **GM asides / editorial annotations:** none.
- **This chapter's bookkeeping:** none.
- **Bullets poorly covered upstream:** none. Every recap beat is well covered
  by the previous chapter's documents.

The table's correction that Wyvern Tor was the same marauder assignment rather
than a new third quest is already explicit in Chapter 10: Hamun Kost offered the
Cragmaw Castle location for clearing the Wyvern Tor marauders or questioning
Agatha, and the party chose Wyvern Tor. Nothing needed rescue.

## All three surfaces

| # | Surface | Result |
|---|---|---|
| 1 | `session_summary.md` `## Scenes` | Already clean. The first scene is `Arrival at Wyvern Tor`; no recap scene exists. |
| 2 | `session_summary.md` `## Summary` | Already clean. It opens with the party cresting Wyvern Tor. |
| 3 | Enhanced-summary file used as `sd_narrate` recap context | Not yet created. No recap-bearing copy exists. |

The Stage 0 source `gm-assist.md` is also clean and begins with live play at
Wyvern Tor.

## What was cut

Nothing required editing: `enhance_summary` had already omitted the opening
recap from the derived summary and scene structure. This manifest records the
GM-approved boundary so later extraction must not recreate the recap as a
scene.

The recap duplicates Chapter 10 (`summaries/010-20260821`), whose documents
already record Hamun Kost's offer, the Cragmaw Castle lead, the Agatha option,
and the party's choice of the Wyvern Tor assignment.

## Hard invariant honoured

All VTT files are untouched. No verbatim scene extraction exists yet, and none
was created or edited by this pass.

## Renumbering and downstream rebuild

None. There was no recap scene in the approved scene list, so the seven Chapter
11 scenes retain their existing order. No `plan.md` or narration files exist,
and no re-planning or paid re-narration was run.

## Upstream gaps found

None.

## Standing policy

`notes/scrub_register_policy.md` already records the campaign ruling that
opening recaps and their preceding scheduling chatter are cut by default, with
rescue always performed first. No duplicate policy entry was added.
