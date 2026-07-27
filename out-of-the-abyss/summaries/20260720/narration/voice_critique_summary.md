# Voice Critique Summary — Session 20260720, Scenes 03–08

Six scenes critiqued (narration for scenes 01–02 doesn't exist yet, so they're not covered here). All six read from the raw `session_doc_scene_NN_*.md` files — no `.scrubbed.md` variants exist for this session, since the `/scrub` pass run earlier found zero mechanical-residue candidates in every scene.

| Scene | Narrator | Flags | Strongest issue |
|---|---|---|---|
| 03 — The Aftermath of the Sanctum Attack | Zalthir | 3 | "filed" used twice, spending a rare verb's rarity |
| 04 — The Death of Bookwyrm | Daz | 3 | bookkeeping noun "account" repeats 3× in one section |
| 05 — Racing to the Sea Warden's Tower | Grygum | 2 | generic "something clicked behind his eyes" |
| 06 — The Shortcut to the North Gallery | Thorin | 1 | (cleanest scene in the batch) |
| 07 — Battle in the Domed Rotunda | Zalthir | 2 | "geometry" (Thorin's register, not his) used twice |
| 08 — Aftermath and Strategy | Thorin | 1 | (also very clean) |

## Strongest recurring issue: em-dash overuse, in every single scene

52 narration-level em-dash instances across the six scenes (38 lines), ranging from 3 (scene 08) to 13 (scene 04). This is the one finding that appears in 100% of the scenes regardless of narrator, which makes it a textbook case of the critique's "convergence with house style" category — the em-dash habit is uniform across Zalthir, Daz, Grygum, and Thorin sections alike, which means it isn't any one character's voice, it's the narration pass's default connective tic. Most instances convert cleanly to a colon (explanatory aside), comma (participial clause), or period (simple split); a handful are worth keeping as-is because they do real work — enacted hesitation (scene 06, line 47: "He just — stopped"), emphatic repetition (scene 07, line 45: "one attack in it — one —"), or the genre spec's own sanctioned "em-dash for interrupted speech or thought" (several instances introducing an italicized remembered line).

Given the volume and the uniformity across narrators, this is the one item worth fixing systemically rather than sentence-by-sentence — a single pass across all six `.md` files converting the connective (non-load-bearing) instances would clear the great majority of the 52 flags in one sitting.

## Second theme: bookkeeping-noun cap violations, in 2 of 6 scenes

The genre spec caps recording/bookkeeping vocabulary at one per section for most narrators, with a narrow two-max exception for Daz (different nouns only, never repeated). Both violations found here are the exact failure mode the spec names — not overuse of the *category*, but the same *noun* repeating:
- Scene 03 (Zalthir): "filed" twice, where the spec calls it "rarely written" and gives no exception.
- Scene 04 (Daz): "account" three times plus "column" once — even under Daz's two-noun exception, this is over, and the same noun repeating is precisely what the spec's "never let one noun dominate" line warns against.

Worth checking future scenes for the same pattern, since it's easy to miss in isolation (each individual sentence reads fine; it's only visible reading the section as a whole).

## Everything else

Scenes 06 and 08 (both Thorin) are the cleanest in the batch — no bookkeeping or register-vocabulary issues at all, and the em-dash counts are the lowest. Scene 07's "geometry" flag is worth a second look specifically because it's vocabulary that fits a *different* narrator's established register (Thorin's terrain/position framing) leaking into Zalthir's section — the kind of cross-narrator bleed the genre spec is designed to prevent.

## Reminders

- This report is review-only. Nothing in the narration files has been changed.
- For the em-dash pattern specifically, given how uniform it is across all six scenes, a manual sweep-and-convert pass (or a targeted re-run of the relevant `session_doc.py` phase with an instruction to vary connective punctuation) is likely more efficient than editing each of the 52 instances by hand.
- The two bookkeeping-cap violations and the "geometry" mismatch are small, targeted edits — cheapest done by hand directly in the narration `.md` files (there's no `.scrubbed.md` layer yet for this session to redirect edits to).
