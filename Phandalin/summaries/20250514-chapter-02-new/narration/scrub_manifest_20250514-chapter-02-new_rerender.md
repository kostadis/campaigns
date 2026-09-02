# Scrub manifest — 20250514-chapter-02-new, RE-RENDER PASS (scenes 04, 07, 08)

Run date: 2026-09-02 (second run). Skill: `/scrub` (propose → GM review → deterministic apply).
Scenes reviewed: 3. Scenes changed: 3. Decisions applied: **15/15, no skips.**

**This run supersedes the scene 04 / 07 / 08 rows of `scrub_manifest_20250514-chapter-02-new.md`.**
Scenes 01, 02, 03, 05 and 06 are untouched by this pass and the first manifest still governs them.

## Why a second run was needed

`sd_narrate` re-rendered scenes 02–08 on 2026-09-02 between 07:50 and 09:59. The first
scrub run wrote `.scrubbed.md` for 04–08 at 10:11 **from a stale preview** — the text it
scrubbed was the *previous* render, not the one now sitting in the raw `.md`. The two files
had diverged by ~52 modified lines in scene 04 alone, which is not the shape a scrub
produces.

Consequences, both confirmed by grep against the raws before this run:

- Every anachronism and level-talk rewrite from run 1 was **absent from the raw** and
  present only in the orphaned `.scrubbed.md`. `Freebird` ×2 and `We're level one` ×3 were
  live again in the file that assembly would fall back to if the scrubbed copy were removed.
- Scene 08's re-render had independently dropped the entire passive-perception / ability-score
  block that run 1 scrubbed by hand — seven of that run's rows no longer had a referent.

The prior `.scrubbed.md` files were the **only** surviving copy of that earlier render, so
they were preserved before being overwritten:

| Backup | Contents |
|---|---|
| `session_doc_scene_04_ale_and_rumors_at_stonehill.prior-render.md.bak` | pre-re-render narration + run-1 scrub |
| `session_doc_scene_07_the_dwarves_don_t_believe_her.prior-render.md.bak` | same |
| `session_doc_scene_08_secrets_of_the_buried_temple.prior-render.md.bak` | same |

These are **not** pipeline artifacts and nothing reads them. They exist only so the earlier
render is recoverable; delete them once you are satisfied with the current text.

## Scanner vs reading pass

`find_residue.py` returned **0 candidates across all three scenes.** Every one of the 15
changes below came from the Phase 1b reading pass. Both classes the scanner is structurally
incapable of matching were present (anachronism, character-level / sheet talk), plus a
six-line raw dice-roll exchange sitting between two narration paragraphs.

Zero candidates is a floor, not a clean bill. This run is the clearest measurement of that
the campaign has: 0 scanned, 15 accepted.

## GM-authored divergences

Deliberate departures from the tape, approved per-candidate. A fidelity check against the
VTT will flag all of these. **They are not transcription errors. Do not "fix" them back.**

Line numbers are against the current raw `session_doc_scene_*.md`.

| Scene | Line | Tape text | Scrubbed text | Class |
|---|---|---|---|---|
| 04 | 69 | `“One of those bangers. Play Freebird.”` | `“One of those bangers. Play The Roc's Lament.”` | anachronism — named real-world entity |
| 04 | 71 | `“Yeah, totally. Freebird.”` | `“Yeah, totally. The Roc's Lament.”` | anachronism — named real-world entity |
| 07 | 43 | `“We're level one.”` | `“We're new at this.”` | character level |
| 07 | 51 | `“…I'll rush up to talk to them. I have a high charisma.”` | `“…I'll rush up to talk to them. They'll like me.”` | ability score |
| 07 | 97 | `“Anybody do better than that?”` | *(excised)* | table speech — roll canvass |
| 07 | 99 | `“Four.”` | *(excised)* | table speech — raw roll result |
| 07 | 103 | `“Any more roles, guys.”` | *(excised)* | table speech — roll call (note tape typo *roles*) |
| 07 | 105 | `“I said 14.”` | *(excised)* | table speech — raw roll result |
| 07 | 107 | `“Oh, 14. Nice.”` | *(excised)* | table speech — raw roll result |
| 07 | 175 | `“We also get the 50 gold pieces.”` | `“We also get the fifty gold pieces.”` | table shorthand — digits in dialogue |
| 07 | 177 | `“…get the 50 gold pieces… we can get the 50 gold pieces.”` | `“…fifty gold pieces…”` (3 occurrences) | table shorthand — digits in dialogue |
| 07 | 219 | `“We're level one.”` | `“We've never done this before.”` | character level |
| 07 | 245 | `“We're all level one.”` | `“None of us has ever done this.”` | character level |
| 08 | 23 | `"Regular. Yeah, we see a little hallway with like a door here at the end of it, I think."` | *(excised)* | table speech — DM narration in a player's mouth |
| 08 | 33 | `"Hit the door."` | *(excised)* | table speech — player instruction to the GM |

**Six of these are verbatim re-applications of run-1 decisions** on identical text (04:69,
04:71, 07:43, 07:219, 07:245, 08:23). The GM re-confirmed them as a block rather than
re-adjudicating each; they are recorded individually here because the line numbers moved.

**Whitespace:** the seven excisions left runs of blank lines. Those were collapsed to a
single paragraph break in 07 and 08. No prose was touched by that step.

## New canon (`provenance: on_the_fly`)

**Nothing new was invented in this run.** `The Roc's Lament` was authored in run 1 and is
already recorded in `notes/scrub_register_policy.md`; re-applying it to the re-rendered
lines does not mint a second coinage. It remains a **song title, not an entity alias**.

No mishearings were registered as aliases.

## GM rulings on what is NOT residue

No new class rulings this run — every candidate resolved against the standing policy in
`notes/scrub_register_policy.md`, which is what that file is for. Applied without re-asking:

- **"Talking is a free action, right?"** (07:165) — in canon, already ruled ch02.
- **The Princess Bride exchange** (08:87–91) — in canon, already ruled ch02. Note the
  re-render now sets `Mostly dead.` as Soma's *narration* rather than dialogue, which reads
  better than the version run 1 saw.
- **`quest` / `quest board`** (07:69) — in canon.
- **"a couple hundred gold pieces"** (07:253) — spelled out, in-fiction, not shorthand.

One ambiguity was ruled *residue* rather than kept: **08:33 `"Hit the door."`** The
recommendation was to leave it as plausible in-fiction; the GM ruled it a player
instruction to the GM and excised it. Recorded here because the recommendation and the
ruling diverged, and because the class — a bare imperative with no number and no fixed
phrase — is invisible to every scanner pattern.

## Notes

- **The `.scrubbed.md` fork is now correct for 04, 07 and 08** — each is the current raw
  render plus this run's 15 approved spans. Scenes 01–03 still have no `.scrubbed.md`
  (correct; `collect_scene_files` falls back to the raw). Scenes 05 and 06 still carry
  run-1 `.scrubbed.md` files built from their current raws.
- **Scenes 05 and 06 were checked for the same staleness and are CLEAN.** Both were
  re-rendered on 2026-09-02 (09:59 and 08:02), inside the same window that produced this
  run's problem, so both were verified rather than assumed: each `.scrubbed.md` differs from
  its current raw by only a handful of targeted spans (the shape a scrub produces, not a
  re-render), and the run-1 residue is present in the raws and absent from the scrubbed
  copies — `MMO` / `50 GP` / `troll the GM` in 05, `[inaudible]` / `50 GP` in 06. Run 1's
  scrub of 05 and 06 stands. **No action needed on either.**
- **Scenes 02 and 03 were re-rendered on 2026-09-02 and have never been scrubbed against
  the current text.** Run 1 reviewed them and correctly produced no `.scrubbed.md`, but that
  review was of the earlier render. Scene 03 in particular now carries `"How long have we
  been walking?"`, which reads as player-to-GM table speech. Worth a pass before assembly.
- **Scanner false positives:** none fired. The scene 06 `foot_count` false positives from
  run 1 (`eighty feet`, `twenty feet`) were not in scope and remain un-persisted to
  `ignore`, deliberately — the strings are too generic to retire campaign-wide.
- **Tooling gap unchanged — `--party-md` loaded 3 of 4 players.** Stéphane Bourdeaud's
  roster line in `docs/party.md` has no `Player: X` prefix, so he is invisible to
  `player_name` detection. No `player_name` candidates fired either way.
- **`voice_lint` bug worth filing:** it segments on `## <Name> — <Scene>` headings, which
  per-scene narration files do not have, so its bookkeeping and convergence checks match
  nothing and print **zero notes** — indistinguishable from a pass. Found during the
  `/voice-critic` run immediately before this scrub. Per-scene input should emit a
  `[skipped]` note.
- **The voice critique of 04, 07 and 08 was written against the stale `.scrubbed.md`** and
  is partly obsolete for those three scenes — see the "Effect on the voice critique" note in
  the reply and in `voice_critique_summary.md`'s scope line.

---

# Addendum — scenes 01, 02, 03 reviewed against current text (2026-09-02, run 3)

The run-2 notes flagged that scenes 02 and 03 had never been scrubbed against their current
render, and that all three of 01/02/03 were marked `processed` by run 1 — which would make
Phase 0 skip them permanently. Reviewed properly here.

**Scanner: 0 candidates across all three.** As in run 2, everything came from reading.

## Result

| Scene | Outcome |
|---|---|
| 01 | **Clean.** No candidates. No `.scrubbed.md` — correct. |
| 02 | **Clean.** No candidates. No `.scrubbed.md` — correct. |
| 03 | **1 accepted change** → `session_doc_scene_03_first_sight_of_phandalin.scrubbed.md` created. |

## GM-authored divergence

| Scene | Line | Tape text | Scrubbed text | Class |
|---|---|---|---|---|
| 03 | 49 | `“How long have we been walking?”` | *(excised)* | table speech — player-to-GM question in the narrator's own mouth |

The smoothed layer attributes the line to **Soma, who narrates this scene**: she asks the GM how
long they have walked, and her own narration answers it two lines later. GM ruled: excise the
question, keep the answer.

### Second-order edit, decided separately

Excising the question stranded the answer — the preceding paragraph ends *“That answers one
question about how a town without soldiers continues to exist,”* so *“Several days, I decide”*
could be misread as answering **that**, and `I decide` lost its prompt. Per the skill's Phase 5
rule this was taken back as its own decision rather than folded in.

| Line | Before | After |
|---|---|---|
| 03:49 | `Several days, I decide, though my knees have been arguing for more.` | `We have been walking several days, I decide, though my knees have been arguing for more.` |

**This one alters narration prose, not table speech.** It is a deliberate divergence from the
tape like any other row above.

## Classes checked and found absent

Not present in the narration of 01, 02 or 03 — verified rather than assumed:

- **`Gygax`** and **`1099`** (named real-world entities, both in scene 02's tape) — the
  reclassification hatch caught both; neither reached the narration.
- **`COVID`, `tariffs`, `memes`** (scene 03's tape) — the render dropped all three; they are not
  even in the hatch.
- **`interdimensional`** (the Lionshield Coster) — present only inside scene 03's hatch, already
  out of the narration.
- Level talk, sheet talk, roll residue, digit money, `the GM` / `the DM`: none.

## Notes

- **`processed` was already set for all three by run 1**, against text that may not have been
  current — the same stale-preview window that caused run 2. That flag is now retroactively true:
  all three have been reviewed against the render on disk. No `state.py` change was needed, but
  the hazard is real and worth naming: `processed` records *that a review happened*, not *which
  text was reviewed*. It should carry the reviewed file's digest.
- Scenes 01 and 02 correctly have **no `.scrubbed.md`**. The directory is now mixed 4-and-4;
  `collect_scene_files` handles that, preferring `.scrubbed.md` and falling back to the raw.
- **Scenes 02 and 03 also carry hand voice-fixes in their raw `.md`** (see
  `voice_fixes_20250514.md`), because at the time those scenes had no scrubbed variant. Scene 03
  now has one, built from the already-fixed raw, so both layers agree. Scene 02 still has fixes in
  the raw only, which is correct while it has no scrubbed variant.
