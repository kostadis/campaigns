# Voice Critique Summary — gm-assist-doc.md (2026-05-18 session)

**Doc:** `summaries/20260518/gm-assist-doc.md`
**Scenes critiqued:** 7 (Grygum ×2, Thorin ×2, Daz ×2, Zalthir ×1)
**Per-scene reports:** `voice_critique_scene_0{1..7}_*.md`

## Flag counts

| Scene | Narrator | Flags | Verdict |
|---|---|---|---|
| 01 | Grygum (Immortal Chambers) | 4 | spot-edit |
| 02 | Thorin (Refectory dinner) | 5 | spot-edit |
| 03 | Daz (Grim Awakening) | 3 | strongest scene — minor edits |
| 04 | Zalthir (Tour of the Bastion) | 2 | highest voice fidelity in doc |
| 05 | Grygum (Council of Twelve) | 3 | strongest Grygum scene |
| 06 | Daz (Crime Scene) | 3 | one systemic pattern issue |
| 07 | Thorin (Keeper's Chambers) | 2 | cleanest of the seven |

**Total:** 22 flags across 7 scenes. None of the scenes need re-narration; all are spot-edit candidates.

## Strongest recurring theme — **the "with the particular X of someone who..." construction**

This single workshop construction shows up across **all four narrators**:

- Scene 1 (Grygum): "navigating institutional gravity for forty-one years and knows which way to lean into it" (variant)
- Scene 2 (Thorin): "the particular noise of people who were important and knew it"
- Scene 2 (Thorin): "the particular gray of someone who had pushed through several days of bad sleep and hadn't yet admitted it to themselves"
- Scene 2 (Thorin): "the particular kind of tired that isn't about sleep"
- Scene 5 (Grygum): "the particular weight of a building that takes itself seriously"
- Scene 5 (Grygum): "the particular expression of people who have never, in their professional lives, been asked to pay for something..."
- Scene 6 (Daz): "the particular economy of a creature that has decided it need not move for anyone"
- Scene 6 (Daz): "the practiced delicacy of someone who had done this many times and preferred not to think about why"
- Scene 6 (Daz): "the particular embarrassment of someone who had suddenly understood..."
- Scene 7 (Thorin): "holding himself the way people do when they're trying to look like they're not rattled"

**Why this matters:** the construction is plausibly on-voice for *Daz* (his spec endorses "measured, categorical" observation with relative-clause portraits) — but it shows up identically in Thorin's and Grygum's scenes, where the voice specs explicitly call for shorter, more concrete, more paratactic constructions. The convergence is the strongest signal in the doc that the narration model has a default sentence-mold it falls into when it needs to attribute behavior to a *kind* of person.

**Recommendation:** If you want to fix this systemically rather than per-line, add a negative example to each voice spec — something like:

> Avoid: "with the particular [X] of someone who [does Y]" relative-clause portraits.
> Prefer: a concrete noun + a short follow-up.

## Second recurring theme — **wrong-narrator bookkeeping verbs**

The verbs *filed it / filing / categorized* leak from Grygum (notes) and Daz (auditing) into **Thorin's** scenes:

- Scene 2 (Thorin): "categorized and discarded" — Daz vocabulary
- Scene 2 (Thorin): "filing it the same way I was filing it" — Daz/Grygum
- Scene 7 (Thorin): "I filed it" (then "I clocked that and kept moving" two paragraphs later — the correct register)

And **Daz's** noun *ledger* shows up in **Grygum's** voice in scene 5 — a direct violation of Daz's own spec, which warns against letting *ledger* dominate.

**Recommendation:** Thorin's bookkeeping verbs are *noted, worth noting, kept it, clocked*. Grygum's are *notes, filed, took notes*. Daz's are *audit, tally, account, column, balance, sorting columns* — and the spec explicitly says to rotate them. Keeping these separated would also help the model distinguish three otherwise-similar "I observe and record" registers.

## Per-narrator summary

- **Zalthir** (1 scene, 2 flags): highest fidelity. The Brother-[NAME]/[OTHER-NAME] uncertain-monk pattern, the tactical inventories, and *"Fembris's legs were done. Mine were not"* all read as model that has fully internalised the spec.
- **Daz** (2 scenes, 6 flags): strong on the auditing voice; the convergence pattern lives mostly in his scenes because his spec is the one that *invites* relative-clause portraits — but the model is overfitting it.
- **Grygum** (2 scenes, 7 flags): voice is largely right, but the model reaches for literary similes (lonely firekeeper, window-unlocked) that Ben/Grygum wouldn't reach for. His spec emphasizes applied-vocabulary deadpan over invented imagery.
- **Thorin** (2 scenes, 7 flags): the second-most flagged. Voice is right when Joe's actual table tics show up ("I mean...you know," "like," "first thing on a Tuesday"). It drifts when the model substitutes Daz/Grygum's "filed/categorized" verbs or when it reaches for emotional-naming flourishes ("the particular kind of tired that isn't about sleep") instead of letting concrete objects do the feeling-work.

## Recommended action

1. Spot-edit the highest-priority flags per scene (the per-scene reports rank them).
2. Before next narration run, consider adding to each voice spec an explicit *anti-example* for the relative-clause portrait construction — that pattern is producing more friction than any single sentence-level issue.
3. The Daz/Grygum/Thorin bookkeeping verbs are worth a one-line cheat sheet in the genre prompt: *Thorin notes / Grygum files / Daz audits.*

No re-narration recommended. The voice work is broadly successful — the gap to "clean" is a few dozen spot edits and one model-tic fix.
