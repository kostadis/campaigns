# Voice Critique — Summary (session 20260618)

Directory critique of `narration/session_doc_scene_NN_*.scrubbed.md` against each
narrator's `voice/<name>_voice.md` spec and `examples/<name>.md`. Review-only —
no narration files were modified. One report per scene:
`voice_critique_scene_NN_<narrator>.md`.

> **Refresh note (scenes 05–07, Thorin):** these three scenes were re-narrated
> after the original pass, so their reports and table rows below were regenerated
> against the current scrubbed text. The earlier findings for 05–07 (the
> "triplicated room-opening", "The flatness is the feeling", "It costs me
> something to learn it") no longer match the narration and have been replaced.
> Rows 01, 02, 04, 08, 09 were **not** re-checked this pass and may be stale.

## Flag counts

| Scene | Narrator | Flags | Em-dash | Other | Strongest issue |
|---|---|---|---|---|---|
| 01 | Grygum | ~8 | 6 | tell-not-show, lyrical drift | "He was glowing"; "footnotes of a vial" |
| 02 | Daz | 5 | 3 | 2 cliché simile | "tip of a tongue" stock simile over an audit beat |
| 03 | Thorin | 6 | 2 | cliché, register, convergence, tell | self-annotating tag "because I like to know the ground before I cross it" |
| 04 | Zalthir | 7 | 3 | register "structure", 2 simile, 1 tell | "drawn the board… where every piece lands"; "last line of a poem he'd written" |
| 05 | Thorin | 3 | 2 | register "photons", writerly simile | mostly in voice; 2 em-dashes + "Photons don't care about lead" |
| 06 | Thorin | 3 | 9 | convergence (×2), mild idiom | nine narration em-dashes; "Daz/Zalthir would've…" device used twice |
| 07 | Thorin | 3 | 8 | **convergence (×4)**, mixed simile | **proxy-deduction peaks** — 4 Daz/Zalthir attributions in one scene |
| 08 | Daz | 4 | 2 | cliché, borderline tell | "packed like that squirrel out of Ice Age" pop-culture allusion |
| 09 | Zalthir | 7 | 4 | tell, 2 over-written | "I was not going to say out loud that I found the partnership easy" — says the quiet part |

**Total: ~57 flags across 9 scenes. ~28 are mechanical em-dash conversions.**

## Verdict

Voice fidelity is **high across all four narrators** — the in-voice cores
(Grygum's late-arc precision, Daz's audit/column idiom, Thorin's terrain logic,
Zalthir's cold mark-and-file) all land. The drift is concentrated in three
recurring patterns, in priority order:

1. **Em-dash overuse (mechanical, ~28 hits).** Prose em-dashes used as
   parenthetical asides in nearly every paragraph of every scene. Pure
   find-and-convert (comma / colon / period). Highest volume, lowest risk.

2. **Naming what the spec wants left implicit (cross-narrator, ~10 hits).** The
   model keeps *stating* the feeling or the device instead of rendering it —
   most starkly where it prints a voice spec's own stage-direction as narration
   ("The flatness is the feeling," scene 05) or announces a cost the character
   must leave hanging ("It costs me something to learn it," scene 07; "I was not
   going to say out loud that I found the partnership easy," scene 09). These are
   one-line deletions/edits, but they're the real voice slips, not the em-dashes.

3. **Thorin's proxy-deduction device (the cross-scene Thorin issue).** The
   re-narrated 05/06/07 no longer share an opening — that template problem is
   gone — but the "[Daz/Zalthir] would've done Y, so I did Y" device has *grown*:
   twice in scene 06 and **four times in scene 07**, plus two appearances in 05.
   It turns Thorin into a clearing-house for absent teammates' thinking, against a
   spec whose Thorin reads terrain directly and commits without narrating whose
   method he borrowed. Keep one nod per scene; let him own the rest.

## Where to spend the re-narration budget

- **Spot-edit (cheapest, covers most of it):** the em-dash sweep + the ~10
  named-feeling/stage-direction lines + the per-scene clichéd similes. None of
  these need a re-run.
- **Re-narrate candidate (scenes 05–07):** the **proxy-deduction device**. It
  fires 8 times across the three refreshed Thorin scenes and can't be cleanly
  hand-stripped without rewriting the surrounding logic each time. It traces to
  the presence-correction reflection blocks in the extractions; if you re-run
  `session_doc.py --scene 6` / `--scene 7`, tell the prompt to let Thorin own the
  deduction in his own terrain-first frame rather than attribute it to an absent
  teammate. Spot-editing is viable if you'd rather — keep one attribution per
  scene and convert the others.
