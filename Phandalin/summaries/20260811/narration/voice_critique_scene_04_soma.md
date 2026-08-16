# Voice Critique — Soma, scene 04: Naming the Margaster Sabotage

**Narration:** `session_doc_scene_04_naming_the_margaster_sabotage.md`
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | match | recomputed `sha256(stripped)[:12]` identical |
| HARD BANS | `base.md` | 4221 chars |
| Voice spec | `soma_new_pipeline.md` | rule (c) — unique key beginning `soma_` |
| Per-char examples | `soma.md` | stem == first name; 7066 chars |
| Global examples | none | — |
| Party doc | `docs/party.md` | roster 4/4 PCs |
| voice_lint | ran | 0 errors, 0 warns, 1 skipped check |

## Budget ledger

**Scope: single scene — doc-level budgets NOT evaluable here.** See `voice_critique_summary.md`.

Scene-local: 2 em-dashes, **both inside verbatim dialogue**, 0 in narration prose. First-person present throughout.

## Flags

None.

The weather motif — `He hands them out on weather sometimes.` / `A bad feeling is weather.` / `Weather frays a rope ragged. This rope looks cut.` — is built from `soma_new_pipeline.md` line 45 ("her wisdom comes from a long coastal life — weather, hospitality, fishing, mending"), and it delivers the sabotage inference as a verdict rather than a lecture, which is spec line 39 and failure-prevention rule 9. `my bale` and the hatchling frame are spec stock phrases used correctly. `Somewhere behind my beak I smile.` renders the reaction physically instead of naming it (spec line 49).

`Vukradin opens it for Brewbarry the way I used to open clams for hatchlings` was checked against the behavioral-taxonomy ban and **cleared** — it draws on the narrator's own history, not a class of people.

## Watch — adjacent to the ban, not flagged

> We witnessed it. A banker would say that was one bad apple. Bankers are paid to say that.

This generalises a profession, which is the family `base.md` bans. It is **not** flagged because no banker in the scene did the thing being explained — it is a hypothetical Soma raises and then dismisses, not a substitute for an observed behaviour. Recorded so the pattern is visible if it recurs; the same author move produced confirmed breaches in scenes 02, 05 and 08.

## Reclassified table speech

One hatch, nine spans:

> `"Were they Cambions?"` | `"They are Moriarty, you mean?"` | `"Moriarty, yeah. Okay."` | `"Moriarty had class, though."` | `"Oh, they don't? No."` | `"Caribbean stew."` | `"Okay, that's a nice story, GM, but you haven't answered my question. What's the connection with Linene's supply chain issue?"` | `"Yeah, they're, they're, they're Cambions."` | `"Exactly."`

Correctly pulled — one span addresses the GM directly, and the Cambion exchange is player knowledge that no character holds (`docs/Margaster.md` is explicit that no PC knows the cambion connection). The prose keeps the in-fiction residue (`Nobody has answered his actual question yet, so he keeps asking it`). **GM: accept or reject.**

**Un-hatched, same class — GM decision:** `"Okay, what are… we're level 7?"` and `"We're about to be level dead, that's fine. Okay."` The second reads as an in-fiction joke and may be worth keeping; the first is character-sheet talk.

## Verdict

No voice findings. The scene's inference chain — manifold failed, house rose, woman died — lands as three flat sentences, which is the register the spec asks for.
