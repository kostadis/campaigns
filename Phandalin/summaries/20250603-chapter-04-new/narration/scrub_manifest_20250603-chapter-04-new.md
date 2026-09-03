# Scrub manifest — Phandalin ch04 (20250603-chapter-04-new)

Run date: 2026-09-02 · 5 narration scenes reviewed · 15 candidates · 15 GM verdicts, all APPROVE
(10 were text changes; 5 were approvals of a *keep* recommendation).

Review vehicle: an Approve/Reject/Discuss artifact, one card per candidate, downloaded and
read back — https://claude.ai/code/artifact/f77aeb9c-2c12-4a95-8404-edef1db92e66

Candidate sources: **5 from the scanner** (one a false positive), **10 from the Phase 1b
reading pass**. The 2:1 split is the expected shape, not an anomaly — every reading-pass
find sat in a documented scanner blind spot (bare number+skill, dice notation, named
real-world entity, modern-register vocabulary).

---

## GM-authored divergences from the tape

Every row below is a deliberate rewrite approved by the GM. **A fidelity check against the
VTT will flag all of them as transcription errors. They are not.** Do not "fix" them back.

| Scene | Line | Tape text | Scrubbed text | Class |
|---|---|---|---|---|
| 01 | 13 | `"Oh, Jesus."` | `"Oh, gods."` | named real-world entity |
| 01 | 89 | `All right, so I have nine hit points.` | `All right — I can stand.` | hp_number |
| 01 | 115 | `shrug off 5 damage worth of it` | `shrug off most of it` | damage_number |
| 03 | 67 | `but I only got a 10 on my performance, so it wasn't so good` | `but it wasn't so good` | number+skill |
| 03 | 77 | `rolling for initiative now. 21.` | `going first.` | roll callout |
| 03 | 95 | `The range is 60 feet, so I can definitely head back over here.` | `It reaches far enough that I can head back over here.` | foot_count |
| 03 | 103 | `Guess I'll take the five points of damage.` | `Guess I'll take it.` | damage_number |
| 03 | 109 | `That's a hit, right? He's 11. Yeah.` | `That's a hit. Yeah.` | AC talk |
| 03 | 113 | `I don't have anything that does 1d12.` | `I don't have anything that hits that hard.` | dice notation |
| 05 | 115 | `You can just roll cantrip damage if you want to make it easy.` | `Treat it like any other cantrip if you want to make it easy.` | resolution talk |

**Note on line numbers:** these index the *narration* files, which were themselves
hand-corrected earlier the same day (see the `hand-fixed after narration` audit comments in
each scene). They do not index the VTT.

## New canon (`provenance: on_the_fly`)

**None.** No proper noun, item, institution or proverb was invented in this run. Every
approved change was a removal or a plain-language restatement; no anachronism required an
in-world replacement, so the "replacement is a lore opportunity" path was never taken.

`"Oh, gods."` is a generic polytheistic oath, not a reference to any named deity — it is
deliberately *not* a claim that Vukradin invoked Tymora or anyone else. A more specific
option was offered on the card and the GM took the generic one.

## GM rulings on what is NOT residue

These are invisible to the scanner and will be re-proposed forever unless recorded. Also
appended to `notes/scrub_register_policy.md`.

| Ruling | Spans | Verdict |
|---|---|---|
| **Modern physics/scientific register is IN CANON**, on the same footing as imported economics | `potential energy` (05:127), `terminal velocity` (05:131), `broadcast` (02:13) | keep — new class, settled this run |
| Unattributed pop-culture *idiom* that names no entity | `"Technically correct. The best kind of correct."` (05:31, Futurama) | keep — consistent with the existing "modern idiom that is neither tech nor a named entity" row |
| Spell vocabulary, including the word *cantrip* | `cantrip` (03:109, 03:115, 05:115), `Poison Spray`, `Starry Wisp`, `Sacred Flame`, `Command`, `Mold Earth` | keep — the hard invariant; never a candidate |
| Faerûnian place names authored during the narration fix | `a Baldur's Gate standby` (05:191), `the Cloaktower` (05:127) | keep — already in-world |

### One policy conflict, resolved in favour of fidelity

Card **C1** — `"Got 11 insight on — do I think he's a surface ogre?"` (03:47).

Scrub policy calls a bare number+skill residue. But this exact wording had been ruled
**correct-to-tape** hours earlier in the same session's `/voice-smooth` pass: it was never a
garble, only a missing sentence boundary, and both transcripts carry those words. The two
policies genuinely conflicted. **The GM ruled the fidelity decision governs**, so scrub stood
down and the line is unchanged.

Recorded here so a future scrub run does not re-open it, and so the divergence between "this
looks like residue" and "this is what was said" is visible rather than mysterious.

## Notes

- **Scenes 02 and 04 were reviewed and produced no `.scrubbed.md`.** That is correct, not an
  omission: `collect_scene_files` in `assemble.py` prefers `.scrubbed.md` per scene and falls
  back to the raw `.md`, so the mixed directory assembles correctly. Both scenes were marked
  `processed` because they were reviewed, not because they produced a file.
- **The narration directory is now a mixed set** — 3 scenes have a scrubbed fork (01, 03, 05)
  and 2 do not (02, 04). Any downstream pass editing these scenes must resolve the effective
  file per scene and default to editing **both** copies where the pair exists.
- **Scanner false positive deliberately NOT persisted to `ignore`:** 04:195
  `"No, no, no — I have one."` matched `roll_result_dialogue`. `"I have one"` is far too
  generic to retire permanently — writing it to state would suppress genuine roll-result
  detection campaign-wide from here on. Recorded as a per-instance rejection only.
- **Tooling gap — `--party-md` loaded 3 of 4 player names.** `load_player_names` matches the
  literal prefix `Player: X`; Phandalin's roster lines are formatted
  `**Barbarian 7 | Goliath | Stéphane Bourdeaud**`, so Stéphane is invisible to `player_name`
  detection. No player names appeared in this chapter's narration, so nothing was missed
  here — but the gap is real and will matter in a session where one does.
- **`sd_narrate`'s reclassifier did most of the work before this pass ran.** Scenes 02 and 04
  were clean because their dice talk (the plus-five exchange, `"my DMG"`,
  `"Jesus Christ, guys"`) was dropped into the `<!-- table-speech reclassified -->` hatch at
  narration time. Phase 1 masks comment spans, so none of it generated candidates. That hatch
  is an audit record: never scrub it, never forge one.
- No durable `state.py rule` was added this run — every change was scene-local, and none of
  the matched phrases is repeated boilerplate.
