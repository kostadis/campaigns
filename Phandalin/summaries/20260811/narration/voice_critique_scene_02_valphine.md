# Voice Critique — Valphine, scene 02: Bullying Through the Loan

**Narration:** `session_doc_scene_02_bullying_through_the_loan.md`
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | match | recomputed `sha256(stripped)[:12]` identical |
| HARD BANS | `base.md` | 4221 chars |
| Voice spec | `valphine_new_pipeline.md` | rule (c) — unique key beginning `valphine_` |
| Per-char examples | `valphine.md` | stem == first name; 12750 chars |
| Global examples | none | — |
| Party doc | `docs/party.md` | roster 4/4 PCs |
| voice_lint | ran | 0 errors, 0 warns, 1 skipped check |

## Budget ledger

**Scope: single scene — doc-level budgets NOT evaluable here.** See `voice_critique_summary.md`.

Scene-local: 12 em-dashes, **all inside verbatim dialogue**, 0 in narration prose. First-person present throughout.

## Flags

### [1] Rulebook conflict — behavioral taxonomy (`base.md` HARD BAN)

> He looks up at Brewbarry the way novices look at altars.

**Why:** `base.md` bans explaining an observed behaviour by generalising it to a class of people "whatever shell it arrives in", and lists `"the way X do/does/say/says … "` explicitly; the rulebook restates it as "one Claude narrator wearing five hats." *Novices* is the class doing the explaining here, and it replaces whatever Valphine actually saw the man's face and body do.
**Suggested rewrite:** `He looks up at Brewbarry and does not blink, and his hands go still at his sides.` — spec: "Her body is present in the prose"; "She narrates with cool precision, as if cataloging a specimen."

### [2] Rulebook conflict — behavioral taxonomy (profession as explanation)

> Spectacle is an instrument, and Brewbarry has played it whether he meant to or not; a banker will sign in public what he would delay in private.

**Why:** Same HARD BAN, second shell — `base.md` names "class, or profession as the explanation for what one person just did." The maxim about bankers-in-general is supplying the reason Aurelan Vance signs, in place of the specific pressure the scene has already built.
**Suggested rewrite:** `Spectacle is an instrument, and Brewbarry has played it whether he meant to or not; the man who spent an hour building a refusal out of arithmetic signs it away with forty people watching him do it.` — spec: "Her observations are sharp, and her conclusions arrive several steps ahead of everyone else's. She does not bother to explain the gap."

## Not flagged — spec-licensed

> He holds both and cannot reconcile them. Surface dwellers are so easily surprised by the obvious.

This sentence is **verbatim from `valphine_new_pipeline.md` line 50**, where it is listed as an exemplar of her elevated, aristocratic vocabulary. Structurally it is adjacent to flags [1] and [2], but the render is executing an explicit instruction and the spec outranks the inference. Not a finding.

Also cleared: `Lathander's light does not petition the skin for permission; it takes what it illuminates` and its closing reprise `Lathander's light reaches even into ledgers. It takes what it illuminates.` — the repetition is a deliberate bookend, and both land the spec's "radiant, indifferent, inexhaustible" register rather than warmth.

## Reclassified table speech

One hatch, two spans:

> `"There's a bit of a crowd surrounding you at this point in time."` | `"I just ignore him."`

Both are GM/player second-person table speech; the beats survive as narration (`By now a crowd has collected around the desk`, `Brewbarry turns his back and gives the man nothing at all`). **GM: accept or reject.**

## Verdict

Two instances of the same banned move — the *class-of-people* explanation — in a section that is otherwise precisely in spec; both are single-sentence spot edits, not a re-render signal.
