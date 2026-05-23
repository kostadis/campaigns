# Voice Critique Summary — gm-assist-doc.md (session 2026-05-11)

**Source:** `gm-assist-doc.md` — assembled doc, seven `## Narrator — Scene` blocks
**Voice specs loaded:** Thorin, Grygum, Daz, Zalthir (all present in `voice/`)
**Per-char examples loaded:** all four narrators (`examples/<name>_example.md`)

## Flag counts per scene

| # | Narrator  | Scene                                          | Flags |
|---|-----------|------------------------------------------------|-------|
| 1 | Thorin    | Arrival in Daggerford                          | 4     |
| 2 | Grygum    | The Silent Child of Meredith                   | 3     |
| 3 | Daz       | The Burning Wizard Inn                         | 3 (one flag covers two instances) |
| 4 | Zalthir   | Arrival at Candlekeep and the Prisoner Question| 3     |
| 5 | Grygum    | Zalthir's Trial of the Broken Mirror           | 2 (one flag covers two instances) |
| 6 | Thorin    | Therapy for a Sentient Blade                   | 3     |
| 7 | Daz       | The Sealed Records of Menzoberranzan           | 2     |

## Strongest recurring issue

**The "with the particular X of Y who Z" construction has become this doc's house-style tic.** It surfaces in at least six distinct sentences across four scenes (Thorin scene 1, Daz scene 3 twice, Grygum scene 5 twice, and arguably Daz scene 7's *"to keep alive a man she could see was nobody special"*). It's a workshopped construction that flattens all four narrators toward the same observer-voice — the one writing the *assembled doc*, not the four distinct narrators it's pretending to be. This is the highest-leverage place to spot-edit before assembly: searching the doc for `the particular` and `with the particular` will surface most of them.

## Secondary recurring issues

- **Workshop similes opening or punctuating paragraphs** ("like a held breath", "like a change in air pressure", "the way a healer's eyes go straight to a wound", "the way things that have been collecting knowledge for centuries tend to sit"). Four flagged across four narrators. Each individual instance reads fine; the pattern is a fingerprint of the rendering model reaching for the same toolkit regardless of narrator. Thorin and Zalthir are most damaged by this — their specs both call for terrain-first, concrete prose with no atmospheric flourishes.

- **Long subordinate-clause sentences in two paratactic-spec narrators** (Grygum scene 2's medicine-examination sentence, Grygum scene 5's "aggravation and necessity" doubling, Zalthir scene 4's spy-and-the-sociology-of-hierarchy tail). Both Grygum and Zalthir's specs are explicit about short, stacked sentences; both get the same drift toward 40–50-word essayistic sentences.

- **Vocabulary bleed between narrators.** Thorin scene 6 borrows Daz's *recalibrates*; Daz scene 7 lets *ledger* dominate against the spec's explicit author's note to rotate the bookkeeping noun.

## Where to focus the re-edit budget

If you want to spend the minimum: do a single pass searching for `the particular` across the doc, plus the two long-sentence flags in Grygum scene 2 and Zalthir scene 4, plus the *recalibrates* in Thorin scene 6 and the *ledger* over-use in Daz scene 7. That catches roughly 70% of the flagged issues.

If you want to re-narrate any scene from scratch: scene 1 (Thorin in Daggerford) has the largest concentration of off-voice prose and the workshopped opener — it's the only scene where re-running `session_doc.py --scene 1` would arguably be cheaper than spot-edits. The other six are spot-edit territory.

The report is review-only — these are flags, not corrections. The narration file is untouched.
