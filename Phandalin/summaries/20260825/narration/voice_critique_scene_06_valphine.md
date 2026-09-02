# Voice Critique — Valphine Sotorra, scene 06: Planning the Stakeout

**Narration:** `session_doc_scene_06_planning_the_stakeout.scrubbed.md`
**Input shape:** per-scene
**Doc-level budgets:** evaluated across the whole document in `voice_critique_summary.md` — a single-scene critique cannot evaluate them.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record + config; 61 lines |
| Rulebook vs run record | match — not edited since this render | sha comparison |
| HARD BANS | `base.md` | 4.1K |
| Voice spec | `voice/valphine_new_pipeline.md` | declared `voice:` in `config/party.yaml` |
| Per-char examples | `examples/valphine.md` | declared `examples:` |
| Global examples | none | no `shared_examples:` declared |
| voice_lint | ran | 0 errors, 0 warnings, 1 skipped check (no ```yaml voice_lint``` block) |

## Flags

### [1] Event reordering, an invented chronology, and a tense break — CONFIRMED

L87–L111 lifts eleven lines out of sequence, relabels them as a flashback, and renders them in past tense:

> Earlier, while we still pressed Lim, the calendar had been weighed. "We have a lot of stuff we have to do today, right? Tonight, we're supposed to have dinner with…" Vukradin had begun, and the name slid toward the wrong house before it was caught.

Three separate rules, one passage:

1. **Ordering.** `base.md`: *"CRITICAL: The actual events of the session must appear in the order they occur in the extracted moments. Do not reorder, move, or restructure session events — only the narrator's internal thoughts and memories may be non-linear."* This is external dialogue, not interior thought. In `scene_extractions_smoothed/06_planning_the_stakeout.md` the calendar/tea material sits at **lines 254–296** — *after* the stakeout planning at lines 105–141. The narration moves it ahead of material that in the source came first.
2. **A temporal claim the tape does not support.** "Earlier, while we still pressed Lim" places the exchange inside scene 05, in Lim's kitchen. The source has it in scene 06's own street conversation. The narrator authored a "when" that did not happen — and it is the kind of assertion a later consistency pass will read as canon.
3. **Tense.** The rulebook: *"First-person present tense, always… If in doubt, first person, present tense."* Eleven lines of `said` / `asked` / `offered` / `I supplied` / `had been weighed`. `base.md` does ALLOW flashbacks — but for *the narrator's inner life*, which this is not.

**Suggested fix:** not a sentence edit. Restore the block to its source position (after the rat-familiar planning at L85, before L113's `The delivery does not move until the third hour after midnight`), drop the "Earlier, while we still pressed Lim" frame, and put it back in present tense. Her verdicts inside the block are strong and survive the move unchanged: *The distinction is not trivial; one lord wants to discuss our circulation of wealth, the other's house forges writs.* and *One learns, in the noble houses, to deliver assurance in exactly the tone that guarantees nothing.*

### [2] Behavioral taxonomy — class as the explanation — PLAUSIBLE

> "We are still looking for the missing gnome, right?" I ask, because a party of surface dwellers will chase whatever glitters most recently, and someone must hold the thread.
> — L17

> The surface dwellers perform this ritual of completing each other's jokes; I understand it as bonding, the way a house understands shared poisonings.
> — L71

**Why:** `base.md` bans "every other appeal to a group's age, sex, class, or profession as the explanation for what one person just did." Both sentences explain what these four specific people are doing by what surface dwellers do in general.

**Why only PLAUSIBLE:** the rulebook pulls the other way — "use the POV character's vocabulary for everything," "the POV character's frame is the only frame in their section" — and drow-vs-surface is her lexicon. The line I would hold: the *vocabulary* is licensed, the *causation* is not. Calling them surface dwellers is hers; using "surface dwellers do this" as the reason a thing happened is the banned move. GM's call.

**Suggested rewrite (L17):** name who, not what class — *…because Vukradin has already moved on to the next bright thing and Brewbarry follows Vukradin, and someone must hold the thread.*

### [3] `the way X …` simile frame — two more instances, contributing to a doc-level breach

> …and were-rats keep each other's acquaintance the way noble houses keep each other's secrets. (L59)
> …I understand it as bonding, the way a house understands shared poisonings. (L71)

**Why:** two of the eight-instance doc-level set (`voice_critique_summary.md`, flag [4]), and they sit twelve lines apart doing the same job — both reach for *noble houses* as the comparison term. One of the two should go.

**Not flagged:** L21, `the way my mother taught me to assemble a rival house's supply lines before recommending which one to cut` — names a specific person and a specific lesson, which is what the rulebook asks for. Keep.

### [4] `I file the observation as accurate` — flat register — PLAUSIBLE

> "Introduce them to Vukradin, and we will," Soma says. **I file the observation as accurate.**
> — L15

Same objection as scene 04 L25 and the same defence: the ledger register is her spec ("an archivist of motive… as if cataloging a specimen"), the flat modern verb is not ("elevated, aristocratic, with no modern slack"). `I file` now appears in 2 of her 2 sections. Nothing checked this — `voice_lint`'s filing caps are skipped for want of a ```yaml voice_lint``` block in the rulebook.

## Not flagged

The highest narration-prose ratio in the session (67%), and the analytical set-piece at L21 and L29 is the best structural work in the document:

> A merchant whose costs do not twitch when the artery is severed was never drinking from the artery. (L21)
> Menzoberranzan is nothing but third routes; the official commerce of the city exists so the real commerce has something to hide behind. (L29)
> In my house you let another voice carry your conclusion; the conclusion still belongs to you. (L31)

L31 is doing something rare — she withholds the deduction on-page and tells you why, which is the spec's "she does not bother to explain the gap" turned into plot.

`"Hashtag,"` (L67) and `"100%,"` (L65) are locked verbatim dialogue — surfaced as GM scope calls in `voice_critique_summary.md`, not flagged here.

## Reclassified table speech

**None.** No hatch in this scene.

## Verdict

Flag [1] is the one thing in this session that changes what the document asserts happened, and it is a re-render or a structural edit, not a sentence fix; everything else here is polish on the strongest analytical section in the run.
