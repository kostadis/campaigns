# Voice Critique (run 2) — Valphine Sotorra, scene 07: The Dwarves Don't Believe Her

**Run:** 2026-09-02, **second critique** · **Input shape:** per-scene · **Source read:** `session_doc_scene_07_the_dwarves_don_t_believe_her.scrubbed.md`

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
| Prose words / total | 613 / 1965 — **31.2% prose** | 787 / 1863 — 42.2% | **much worse** |
| Orphan quote runs | **10**, longest **16** | 8, longest 6 | |
| Epigrammatic closers | **~12** | 6 | |
| Behavioral taxonomy | 2 | 2 | |

## This render is worse than the one it replaced, on every measure

This is the headline for scene 07 and it should be read before anything else.

| | previous | now |
|---|---|---|
| Prose words | 787 | **613** (−22%) |
| Prose share | 42.2% | **31.2%** |
| Orphan runs | 8 | **10** |
| Longest run | 6 lines | **16 lines** |
| Epigrammatic closers | 6 | **~12** |

**The one line the previous critique said to keep is gone.** *"Convenient. The dead lose their rights when their theology becomes distasteful."* — named as the single closer Valphine should have kept for the whole session — is not in this render. What replaced it is twelve weaker ones.

## Flags

### [1] Unattributed dialogue — a 16-line run and a 14-line run

Runs at 13–20, **33–44 (6)**, **55–72 (9)**, 81–88, 137–142, **147–178 (16)**, **181–192 (6)**, 195–204, **207–220 (7)**, **225–252 (14)**.

Lines 147–178 are sixteen consecutive quote-only paragraphs — the business negotiation over the sending stones, across at least four speakers (Norbus, Vukradin, Soma, Brewbarry) with not one attribution. Lines 225–252 are fourteen more.

> “Well, if you were willing to go in there and deal with any nasties and beasties, we would be willing to give you two sending stones.”
>
> “Oh, those were, uh — messages, was it?”
>
> “Are those valuable?”
>
> “I'm not sure about that.”
>
> “We also get the fifty gold pieces.”

**Why:** the previous render tagged this passage (*"Norbus offers payment."*, *"Soma finds the leverage that will move Vukradin."*, *"Brewbarry looks interested."*). Those beats were removed. This is the largest single regression in the chapter.

**Fix:** restore attribution from `scene_extractions_smoothed/07_meeting_the_prospectors.md`. **Leave line 221's *"Still, we did ask"* alone** — the previous render's *"We did ask," someone behind me says* was a correct unassignable, and folding it into narration was the right call.

### [2] Epigrammatic closers doubled, 6 → ~12

11, 31, 53, 73, 89, 109, 113, 121, 129, 143, 193, 221. Ranked, worst first:

1. 73 *"Their subsequent dissatisfaction is not our contractual concern."*
2. 193 *"Norbus's moral test is magnificently useless. I almost admire it."*
3. 89 *"…the dwarves claim cultural authority while denying any specific mandate."*
4. 221 *"Fairness arrives late, after agreement, which is when disclosures are least likely to destroy a bargain."*
5. 31 *"Soma's judgment is cleaner than archaeology's preferred vocabulary."*
6. 121 *"…but apparently the distinction matters deeply if one is a dwarf."*
7. 109 *"A rationed sacrifice insults power by pretending tribute is negotiation."*
8. 143 *"Expert manipulation, though he persists in calling it sincerity."*
9. 53 *"…which tells me that possession has already preceded legitimacy."*
10. 113 *"Menzoberranzan would consider the sequence elementary."*

**Keep 53** — it is anchored to Dazlyn guarding the dig before asking why the party came, which is an observation with a maxim attached rather than a maxim alone. Target 1 for this scene.

Protect, and do not count against the ration: **21** *"Sensible masonry."* (three words, dry, entirely hers) and **135** *"Lolth hides below and rations favor through priestesses. Lathander crosses the world every morning without permission. My sisters never completed the calculation."* — the conversion passage survived the re-render and is still the best writing in the chapter.

### [3] Behavioral taxonomy ×2 — same count, new instances

> “Prudence and fear are often confused in the Overbright, largely by those who possess too much of one and insufficient quantities of the other.” *(11)*

**Why:** *"those who possess too much of one"* is a class of person defined by a habit — the taxonomy move with `who` intact, in a shell none of the rulebook's four `extra_tics` patterns matches.
**Suggested rewrite:** *"Soma walks in without looking at the doorways. I look at the doorways."*

> “The ignorant merely hate what they recognize. Those who recognize every component separately must protect themselves by declaring the whole fraudulent.” *(129)*

**Why:** two classes of person taxonomized in consecutive sentences to explain one dwarf's reaction.
**Suggested rewrite:** *"Norbus can name every part of me and still refuses the sum."*

As in scene 04, the previous render's two instances were different sentences. **The move survives re-rendering at a stable rate of two per Valphine section.**

## Verdict

A 22% loss of narration, a sixteen-line unattributed run where the previous render had speaker beats, and twice the closers — including the loss of the one line the last critique asked you to keep. **Of the three re-rendered scenes this is the one to roll back rather than re-render**: `session_doc_scene_07_the_dwarves_don_t_believe_her.prior-render.md.bak` is better on every measure, and its residue is already documented and re-scrubbable.

---
*Review only. Nothing applied. Cross-scene ledger in `voice_critique_summary.md`.*

