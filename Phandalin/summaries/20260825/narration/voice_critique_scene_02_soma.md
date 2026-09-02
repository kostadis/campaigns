# Voice Critique — Soma, scene 02: The Skeletal Horse Sighting

**Narration:** `session_doc_scene_02_the_skeletal_horse_sighting.scrubbed.md`
**Input shape:** per-scene
**Doc-level budgets:** evaluated across the whole document in `voice_critique_summary.md` — a single-scene critique cannot evaluate them.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record + config; 61 lines |
| Rulebook vs run record | match — not edited since this render | sha comparison |
| HARD BANS | `base.md` | 4.1K |
| Voice spec | `voice/soma_new_pipeline.md` | declared `voice:` in `config/party.yaml` |
| Per-char examples | `examples/soma.md` | declared `examples:` |
| Global examples | none | no `shared_examples:` declared |
| voice_lint | ran | 0 errors, 0 warnings, 1 skipped check (no ```yaml voice_lint``` block) |

## Flags

### [1] `the way X …` simile frame — contributes to a doc-level breach

> The man squares himself up to the horse the way you square up to a magistrate.
> — L33

**Why:** one of eight instances of this frame across all four narrators (full table in `voice_critique_summary.md`, flag [4]). `base.md` names `"the way X do/does … when …"` as a banned variant of behavioral taxonomy and is explicit that the test is the move, not the wording. In isolation this one is mild and Soma-plausible; it is flagged as a member of the set, not on its own merits.

**Suggested rewrite:** Soma's lens is physical-world-first. Render the posture — *The man squares himself up to the horse, shoulders back, chin out, like he means to be judged.* — or cut to the behaviour and let it stand.

## Not flagged

The section is otherwise strong and on-spec. `shell sprout` and `my bale` used verbatim as the rulebook requires; `A stranger is only a friend the tide hasn't brought in yet` and `Shells don't hurry, and neither do friends` are hers and nobody else's; `He thinks with his whole face` is exactly the specific-over-poetic the rulebook asks for. L43 (`I have hatchlings of my own out there somewhere. You would think I'd have asked the horse by now.`) does real interior work off a throwaway line.

`*Charming cleric.* Valphine will want that carved somewhere.` (L73) — italics for direct thought, used as punctuation. Correct.

## Reclassified table speech

**One hatch, one span:** `"21 Insight."` — a bare roll result. Correctly out of the narration.

## Verdict

One member of a doc-wide simile pattern; nothing wrong with this section on its own terms.
