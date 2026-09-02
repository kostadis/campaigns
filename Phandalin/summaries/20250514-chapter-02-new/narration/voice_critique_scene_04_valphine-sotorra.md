# Voice Critique (run 2) — Valphine Sotorra, scene 04: Ale and Rumors at Stonehill

**Run:** 2026-09-02, **second critique** · **Input shape:** per-scene · **Source read:** `session_doc_scene_04_ale_and_rumors_at_stonehill.scrubbed.md`

**Supersedes** the earlier critique of this scene, which read a stale `.scrubbed.md` fork of an older render.

## Inputs resolved

| Input | Resolved to | State |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `0a3d011c5f27`, 105 lines | **resolved — and now matches the run record.** The 10:39–10:44 re-render moved this scene onto the current rulebook |
| HARD BANS | `narrate/base.md` | resolved |
| Voice spec | `voice/valphine_new_pipeline.md` | resolved (declared in `config/party.yaml`) |
| Examples | `examples/valphine.md` | resolved |
| Global examples | none (`shared_examples:` absent) | ok |
| `voice_lint` | 0 errors / 0 warnings, per-scene **and** on an assembled proxy | clean; bookkeeping checks confirmed to have run on the proxy |
| Scan A — em-dashes | **0** in narration prose | ok |
| Scan A2 — trailing-dash provenance | **0** reaching narration | ok |

## Measure, this render vs the previous one

| | now | previous render | |
|---|---|---|---|
| Prose words / total | 564 / 1798 — **31.4% prose** | 576 / 1586 — 36.3% | **worse** |
| Orphan quote runs | **12**, longest 8 | 12, longest 9 | |
| Epigrammatic closers | **~7** | 4 | |
| Behavioral taxonomy | 2 | 2 | |

## Resolved since the last critique

- **The cross-narrator convergence is gone.** *"Delight in a proprietor is merely appetite wearing clean clothes"* — which paired with Vukradin's *"a retirement fund wearing the hat of an orphaned-property office"* (02:143) — is not in this render. That finding is closed.
- *"Surface dwellers are so easily surprised by the obvious"* is gone.
- The rulebook digest now matches the current working copy, so every register finding below is authorship, not delivery.

## Flags

### [1] Unattributed dialogue — 12 runs, unchanged, and the prose share fell

Runs at 15–20, 23–30, 37–42, **61–72 (6)**, **75–90 (8)**, **99–110 (6)**, **119–134 (8)**, **137–152 (8)**, 171–180, 183–192, 197–202, 205–214.

The re-render did not touch this. It also removed narration: prose is down from 576 words to 564 while total length grew from 1586 to 1798, so the scene is now **31.4% prose** — the thinnest section in the chapter by either measure.

Lines 119–134 are sixteen lines of Toblen-and-party economics with two tags. Lines 205–214 remain a four-voice wash:

> “The problem with the small, or the dragon?”
>
> “Do we get paid if we kill the dragon?”
>
> “I'm told the dragons have hoards.”
>
> “People just don't understand.”

**This is now the third render with this defect.** Spot-tagging from `scene_extractions_smoothed/04_arrival_at_the_stonehill_inn.md` is the reliable fix; a fourth re-render without an explicit attribution directive is unlikely to behave differently.

### [2] Epigrammatic closers rose from 4 to ~7

- 53 *"…civilized discomfort is rarely free…"*
- 91 *"Music is useful for worship, manipulation, and the imposition of order. Music performed for ale has less procedural weight."*
- 135 *"Surface politics remains committed to disguising paralysis as procedure."* — also flag [3]
- 153 *"Recovery, apparently, means rebuilding in the same place without acquiring the force necessary to prevent repetition. My sisters would consider this an invitation."*
- 165 *"It is an inventive defense and wholly disconnected from any recognizable standard of proof."*
- 181 *"Surface morality can be remarkably efficient when no actual restitution is required."* — also flag [3]
- 193 *"The exchange has been disproportionate, but not without entertainment."*

**Keep one, and it should be 153** — the *"My sisters would consider this an invitation"* clause is the only one that lands in a specific Valphine reference rather than a general maxim.

Not counted, and worth protecting: **59** *"Toblen pauses. The pause is important. He has acquired a bard and does not yet know whether this is good fortune or a punishment."* That is observation of one man, not a category. It is the best sentence in the scene.

### [3] Behavioral taxonomy ×2 — same count, new instances

> “Surface politics remains committed to disguising paralysis as procedure.” *(135)*
> “Surface morality can be remarkably efficient when no actual restitution is required.” *(181)*

**Why:** both name a class ("surface politics", "surface morality") and assert a general habit of it, which is the banned move with the class noun swapped. The previous render's two instances used *"surface dwellers"* and *"proprietors"*. **The specific wordings changed and the count did not** — the re-render rotated the costume, exactly as the rulebook's own ch40–48 sweep predicted.

**Suggested rewrites:** 135 → *"Harbin has not decided. That is the whole of it."* · 181 → *"Brewbarry said nothing and was forgiven anyway. Nobody asked him for anything."*

## Verdict

Thinnest section in the chapter at 31.4% prose, twelve unattributed runs across three consecutive renders, and a closer count that went up rather than down. Fix the attribution by hand from the smoothed layer; do not re-render again expecting it to resolve itself.

---
*Review only. Nothing applied. Cross-scene ledger in `voice_critique_summary.md`.*

