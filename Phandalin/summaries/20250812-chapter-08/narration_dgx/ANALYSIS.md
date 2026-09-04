# DGX narration experiment — Chapter 8 (Tower of Storms)

**Date:** 2026-09-04
**Endpoint:** `http://192.168.1.147:8001/v1` — `deepseek-ai/DeepSeek-V4-Flash-0731`, 262,144 ctx, vLLM
**Baseline for comparison:** the campaign's Anthropic/codex-cli narration runs (20260729, 20260811, 20260818)

Two `sd_narrate` passes were run against identical inputs — same plan, same scene
extractions, same endpoint, same model. Only the flags differed. `run1_unsteered/`
holds the first; the top-level scene files hold the second.

Nothing here has been scrubbed. No `.scrubbed.md` exists; the GM stopped the
`/scrub` run at the proposal stage, so every file is as the model rendered it.

---

## 1. The first run was mis-invoked, and that is most of the story

The first pass omitted every steering flag this campaign configures in
`config/session_doc.yaml`:

```yaml
narrate:
  prose_mode: true          # "Strip mechanical / GM framing from narration"
  reflections: true
  genre_file: voice/_genre.md
```

`--prose-mode` is documented as stripping exactly the defect the first run
exhibited. The initial read — "DeepSeek retells the transcript instead of
narrating" — was therefore **not supported by that evidence**, and the first
comparison against the Anthropic runs was not like-for-like. Recorded plainly
because the wrong conclusion is the one that would have stuck: it would have
been logged as a model limitation when it was an operator error.

Run 2 added `--prose-mode --narration-genre-file voice/_genre.md --reflections
--context docs/campaign_state.md docs/world_state.md --narrate-tokens 32000`.

## 2. What the flags actually bought

| Metric | Run 1 (unsteered) | Run 2 (steered) | Anthropic baseline |
|---|---|---|---|
| `the GM` / `the DM` per 1k words | **5.0** | **1.2** | 0.0 – 0.1 |
| scrub candidates (scanner) | 88 | 39 | ~6 across 8 scenes (ch02) |
| — of which `table_speak` | 42 | 9 | — |
| words | 8,474 | 7,375 | — |
| em-dashes | 76 | 65 | — |

`--prose-mode` closed most of the gap: a 4× reduction in GM references and a
56% reduction in scanner candidates. **Both factors were real.** The operator
error was the larger one; the residual 1.2/1k is still ~12× the campaign's
Anthropic baseline, so a model effect survives the correction.

## 3. The finding worth keeping: prose-mode renamed the GM rather than removing it

This is the result that would not have shown up in any metric anyone was
already tracking.

| | Run 1 | Run 2 |
|---|---|---|
| uses of `the world` | 4 | **15** |

Run 2's scene 01 carries 12 of those 15, against 1 surviving `the GM`. The
substitutions are direct:

> "All right," **the world conceded**, in that voice it uses when it's been outmaneuvered.

> But the GM — no, **the world**, the world had only put one harpy **on the board** so far.

> — barely ten feet away, **the world confirmed**, well inside my range.

The second quote is the model performing the substitution mid-sentence, in the
finished prose. `--prose-mode` did not make the narration stop describing a
table adjudicating rules; it taught the model a synonym for the adjudicator.
The frame survived intact under a new name, and `on the board` survived
alongside it (3 uses).

**Why this matters more than the raw count.** `find_residue.py` matches
numbers, fixed table-speak phrases, and player names. `the GM` is on that list;
`the world` is not, and cannot be — vocabulary matching is forbidden by the
scrub skill's hard invariant. So the steered run traded 33 *scannable*
violations for ~11 *unscannable* ones. On the scoreboard that is a large
improvement. For a pipeline whose safety net is a regex scanner, it is partly a
laundering of the same defect into a form the net cannot catch.

This is a specific, reproducible instance of the general rule in
`~/.claude/CLAUDE.md`: a rendering instruction given to an LLM gets satisfied at
the level of the string, not the level of the intent.

## 4. Genre-file compliance

`voice/_genre.md` mandates **first-person present tense, always**, and names
present tense as the standard while flagging past tense in older examples as
"legacy drift, not the standard."

Past-tense verb markers per scene:

| Scene | 01 | 02 | 03 | 04 | 05 | 06 |
|---|---|---|---|---|---|---|
| markers | **72** | 9 | 1 | 6 | 6 | 6 |

**Scene 01 is written in past tense; scenes 02–06 are in present.** The model
complied with the tense directive in five of six scenes and dropped it in the
first. Scene 01 is also the scene carrying 12 of the 15 `the world` euphemisms
and the surviving `on the screen` line — the two defects co-locate, which
suggests one scene-level failure rather than two independent ones.

Note the confound: scene 01 is the first scene rendered, with the least prior
narration in context.

What the genre file *does* license, and which a scrub run must therefore not
treat as residue:

> Tone shifts scene to scene: earnest moral conviction, dark comedy from
> contradiction, **mechanical procedural during combat (hit points, saves, the
> named spell)**, then back to lyrical interior.

That clause covers 16 `damage_number` + 2 `hp_number` + 2 `dc_number` of run 2's
39 candidates — roughly half the queue is arguably in canon before review. This
is unresolved; the GM has not ruled on it.

## 5. Residual defects in run 2 (unresolved, nothing applied)

Scanner (39): 16 `damage_number`, 14 `foot_count`, 9 `table_speak`.

Found by reading, invisible to the scanner:

| Scene | Line | Text | Class |
|---|---|---|---|
| 05 | 71 | `Gary's voice cuts across the table — not Valphine, not anyone in the fiction.` | real player name + table framing |
| 02 | 21 | `"Public roll," I announce... The table knows what I mean.` | table framing |
| 01 | 13 | `"I put the 20-foot radius on the screen there for you"` | Roll20 screen in first person |
| 06 | 89 | `— 2d8, ten-foot push` | dice notation in prose |
| 06 | 75–83 | DM's internet outage: bear token off the board, house on Santorini, industrial router, DHCP | out-of-fiction block |

The scene-05 player name is a **tooling gap, not a model failure**:
`find_residue.py --party-md` loaded `David Mendenhall`, `Gary Young`, `Wade Brown`
— full names only — so the bare first name `Gary` matched nothing. Two of the
campaign's five roster members (Stéphane Bourdeaud, Kostadis Roussos) did not
load at all, because `load_player_names` matches a literal `Player: X` prefix
that Phandalin's `docs/party.md` does not use.

## 6. Honest scorecard

**Where the local model did well.** Prose quality in scenes 02–06 is
genuinely good and in-voice — Soma's "eight of mine, two of hers, and hers are
definitely the more alarmed pair", Valphine's aesthete register, Brewbarry's
short declaratives. It held first-person present tense across five of six
scenes without further prompting. It respected the per-scene POV assignments
from `plan.md` exactly. Quote fidelity was strong: an n-gram check of 201
single-line quoted spans against the VTT found **no fabricated dialogue** —
notable given this campaign's prior recorded incident of DeepSeek quote blocks
inventing canon (`project_deepseek_quote_fabrication`). The misses were
*splices* — real adjacent utterances joined into one quoted line — which is a
fidelity question but not invention.

**Where it did worse than the baseline.** ~12× the Anthropic runs' rate of
out-of-fiction framing even after correct steering; one scene in the wrong
tense; and the euphemism substitution in §3, which is the most interesting
failure because it is *compliance-shaped* — the model satisfied the instruction
in a way that defeats the instruction's purpose and evades the downstream check.

**What this cost.** Two full render passes plus a plan generation, all local.
The plan generation also produced two errors needing hand repair before
narration: it wrote `narrator: Valphine` where the roster says
`Valphine Sotorra`, and its scene-4 focus line reproduced the exact event-
aggregation error that the Stage 2 consistency pass had fixed hours earlier
(finding S4-2 — crediting Harpy 2's mace-and-crossbow kill to scene 4). The
second is the more instructive: the model pulled it from `session-summary.md`'s
older framing, which means **a stale upstream artifact propagates into the plan
even when the scene extractions have been corrected.**

## 7. Open

- No GM ruling on whether combat numbers are residue or genre-licensed (§4).
- No `.scrubbed.md` written for any scene. The `/scrub` run stopped at proposal.
- `the world` / `on the board` euphemism is unresolved and unscannable; if it is
  to be caught in future runs it needs either a reading pass or an explicit
  entry in `notes/scrub_register_policy.md`.
- Scene 01's past tense is unresolved — a re-render of that scene alone
  (`sd_narrate --scene 1`) is the cheap fix if it matters.
- `--party-md` roster-parsing gap (§5) affects every `/scrub` run in this
  campaign, not just this one.
