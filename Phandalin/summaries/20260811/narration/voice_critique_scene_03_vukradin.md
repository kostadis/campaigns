# Voice Critique — Vukradin, scene 03: Rimardo Audits the Moral Economy

**Narration:** `session_doc_scene_03_rimardo_audits_the_moral_economy.md`
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | match | recomputed `sha256(stripped)[:12]` identical |
| HARD BANS | `base.md` | 4221 chars |
| Voice spec | `vukradin_new_pipeline.md` | rule (c) — unique key beginning `vukradin_` |
| Per-char examples | `vukradin.md` | stem == first name; 15936 chars |
| Global examples | none | — |
| Party doc | `docs/party.md` | roster 4/4 PCs |
| voice_lint | ran | 0 errors, 0 warns, 1 skipped check |

## Budget ledger

**Scope: single scene — doc-level budgets NOT evaluable here.** See `voice_critique_summary.md`.

Scene-local: 10 em-dashes, **all inside verbatim dialogue**, 0 in narration prose. First-person present throughout.

## Flags

None.

The ledger reflex is `vukradin_new_pipeline.md` line 51 ("He reaches for the ledger — coin returned, paperwork filed, receipts mailed — when he renders moral judgment"), so `The good column of the ledger`, `My mind is already sorting it into columns and finding no column that fits`, and `The audit closes. The columns balance.` are the spec firing, not bookkeeping-noun convergence. The rulebook declares no per-section bookkeeping cap for Phandalin, so that category is *not checked* rather than passed — but nothing here reads as another narrator's register.

`*Laundered.* The word goes in under the ribs.` renders the injury somatically instead of naming the feeling; `From the stage to the spreadsheet.` and `The floor of the Counting House does not move, but something under my accounting does.` are specific rather than portable. The single-word verdict landings (`A dividend. Fine.` / `Done. Entered, witnessed, clean.`) match spec line 42.

No behavioral-taxonomy shell, no editorializing frame, no recap framing.

## Reclassified table speech

None. No hatch is present in this file, and the reading pass found no un-hatched table speech in the prose either — the scene's dialogue is all in-fiction.

## Render defect

**Line 119 — a clause is emitted twice with no separator:**

> "The employees were paid," Valphine says, counting it"The employees were paid," Valphine says, counting it off on her fingers.

This is a generation/assembly defect rather than a voice finding, and it needs a manual fix regardless of what is decided about anything else in this critique. Intended text is almost certainly the second, complete copy.

## Out of scope — flagged for `/consistency-check`

Line 67: `the fairest income distribution scheme in the Dessarin Valley`. Phandalin sits in the Sword Coast North; the Dessarin Valley is the Red Larch / Triboar region. Geography is a canon question, not a voice question — noted here only because it surfaced during the read.

## Verdict

No voice findings; the section is the strongest match to its spec in the session. The blocking item is mechanical — the duplicated clause at line 119.
