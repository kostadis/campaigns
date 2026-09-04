# Test narration — mechanical residue removed upstream

**This is an experiment, not the session document.** The shipping narration is
`../narration/`. Nothing here assembles; `assemble.py` is never pointed at this
directory.

## The question it answers

By the time `/scrub` finished, **no mechanical residue had reached the narration
in any of the eight scenes** — a scan for DC/roll/check/initiative/quest-log
language across all of `../narration/` returns zero. Scenes 06 and 08 were
nonetheless built from extractions that are largely (06: entirely) the table
operating the game rather than roleplay. `sd_narrate` converted that to prose
successfully.

So: if the mechanical quotes are removed **upstream** instead, does the narration
get better, or merely equal?

## What was done

Non-destructive. The smoothed extractions were copied to a sandbox, edited, and
narrated to a separate output directory. `scene_extractions_smoothed/` in the
repo is unchanged for both scenes.

| Scene | Edit | Quotes |
|---|---|---|
| 06 Journey Along the Triboar Trail | whole `## Voiced moments` cut — **not one of the 47 quotes is in-character speech**; all GM map operation and out-of-character exposition | 47 -> 0 |
| 08 Scouting Wyvern Tor | selective: roll/table mechanics cut, read-aloud description and the two Veyra beats kept | 28 -> 8 |

The exact extractions used are in `scene_extractions_used/`, so the run is
reproducible. Command as run (from the campaign root):

```
sd_narrate summaries/010-20260821/session_2026_08_21_chapter_10_the_wizard_of_the_old_owl_well.md \
  --plan summaries/010-20260821/plan.md \
  --scene-extractions <sandbox with the edited extractions> \
  --per-scene-output <sandbox out> \
  --scene 6 8 \
  --party docs/party.md --party-config config/party.yaml --players-config config/players.yaml \
  --voice-dir voice --examples examples --prose-mode --reflections --narrate-tokens 3200 \
  --backend codex-cli --model gpt-5.6-sol --codex-reasoning-effort medium
```

## Result

| | current (`../narration/`) | test |
|---|---|---|
| 06 | 667 words, 0 quoted lines, hatch present | 764 words, 0 quoted lines, **no hatch** |
| 08 | 710 words, 2 quoted lines, hatch present | 687 words, 4 quoted lines, hatch present |

**The finding is not correctness — both versions are already clean. It is room.**
With the die rolls gone from its input, the narrator stopped spending budget
converting mechanics into prose and spent it on character instead. Scene 06
surfaces the party's darkvision split for the first time in narration ("Veyra and
Sister Maela could see into darkness better than Pip and me... Leadership is
sometimes a grand word for deciding where everyone sleeps" — the standing
constraint recorded in `docs/party.md`). Scene 08 recovers the being-lost comedy
that the roll sequence had flattened, and lands the wordless beat as
"There are silences that ask questions. His asked whether I intended to revise my
published findings in light of new evidence."

That is an argument for cutting at the extraction layer **even when the narration
already looks clean**.

## Known defects in this output — do not promote as-is

1. **Scene 08 opens with `"So we kept going."`** — the narrator sometimes begins a
   scene by echoing the previous scene's closing line, and here it rendered that
   echo as **quoted dialogue**. Veyra appears to say Zenvon's closing narration
   aloud. Same mechanism as the duplicated *"I managed not to laugh until his back
   was turned."* at the 03->04 seam in `../narration/`. Must be fixed before this
   version ships.
2. **Scene 08 lost its distances.** The read-aloud says "fifty yards away... twenty
   yards outside the cave"; the test renders "across a broad stretch of broken
   ground." Better prose, but those two numbers are the tactical facts
   `notes/session_prep/20260904_chapter_10_the_wizard_of_the_old_owl_well.md` is
   built on.
3. **Scene 06 has no reclassification hatch** in this version. Expected — nothing
   was left to reclassify — but it means the audit trail moved from the pipeline's
   own record into the cut note in the extraction.
