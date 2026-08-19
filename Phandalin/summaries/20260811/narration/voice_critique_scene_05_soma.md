# Voice Critique — Soma, scene 05: Perrin Claims the Necklace

**Narration:** `session_doc_scene_05_perrin_claims_the_necklace.md`
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

Scene-local: 16 em-dashes, 14 inside verbatim dialogue, **2 in narration prose** — a matched parenthetical pair (`…his agent — he points at the man dangling from Brewbarry's grip — can provide…`). The rulebook permits the em-dash for interrupted thought and forbids it only as a connective joining two clauses; this is an interruption, so **no breach**. These are the only two prose em-dashes in the entire session.

## Flags

### [1] Rulebook conflict — behavioral taxonomy (`base.md` HARD BAN)

> "This is fine, he's with us," I tell Perrin and the fixer, who are both staring at the skeletal horse the way people do the first time.

**Why:** `base.md` lists this construction directly, with a near-identical example ("everyone looked at me the way they do when they want someone else to decide"), and forbids "every other appeal to a group's … class … as the explanation for what one person just did." *The way people do* stands in for the two specific reactions Soma is looking at — and her spec's whole lens is that she "notices the physical world first: wounds, posture, hands, breath."
**Suggested rewrite:** `…who are both staring at the skeletal horse, Perrin's mouth open, the fixer's weight already going back onto his heels.` — the scene's own opening establishes she reads this man by his boots and his weight shifts, so the material is already on the page.

## Cleared on inspection

Three further `the way X` constructions were checked and **cleared**, because each compares against the narrator's own experience rather than generalising a class:

- `holding still at the alley mouth the way nothing honest holds still` — an abstraction, not a class of people; and it is a genuinely Soma-shaped verdict.
- `Brewbarry takes the fixer by the neck, one hand, the way you lift a hatchling out of the surf.` — her own coastal history, spec line 45.
- The hatchling frame throughout (`I have raised hatchlings. I know what a bad idea sounds like when it is still small and warm.`) is spec line 43.

`Old joints. One trip matters.` executes spec line 44's bodily age. `Nobody laughs but me, on the inside, where it counts.` is the spec's dry, internal humour.

## Reclassified table speech

One hatch, eighteen spans — including `"The camera zooms in."`, `"Very dramatic zoom right then."`, `"Yawn very loudly."`, `"Algorithm has saved him from ban… from demonetization."`, `"Unalived is used to avoid demonetization, that's all."`, `"Stephane?"`, and the full elven-chainmail inventory exchange (`"Add to your character elven chain mail."` … `"to equipment…"`).

Correctly pulled — real player names, second-person instruction, and character-sheet bookkeeping. The in-fiction residue survives properly (`Brewbarry yawns. Loudly. A yawn you could stable a horse in.`, and Valphine `makes Brewbarry trade his scale mail for the elven chain before we move`). **GM: accept or reject.**

**Un-hatched residue — GM decision, not an error.** Three modern/pop-culture jokes stayed in the fiction: `"this isn't Houston, Texas. This is Neverwinter in the Forgotten Realms"`, `"as they say on Mandalore, this is the way"`, and `"Yeah, Boney's a Zoomer"` (plus the narration line `And it adds 15 pounds`). The rulebook explicitly licenses absurdist comedy and the session keeps `Oral B. Vance` and `SystemD of Neverwinter`, so these are plausibly intentional — but they sit in the same class as the demonetization asides that *were* pulled, so the line is currently inconsistent within one scene.

## Verdict

One instance of the banned class-generalisation move, in a section whose own opening paragraph demonstrates the correct alternative; a single-sentence spot edit.
