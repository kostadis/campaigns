# Voice Critique — Vukradin, scene 08: Return to the Common Chord

**Narration:** `session_doc_scene_08_return_to_the_common_chord.scrubbed.md`
**Input shape:** per-scene
**Doc-level budgets:** evaluated across the whole document in `voice_critique_summary.md` — a single-scene critique cannot evaluate them.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record + config; 61 lines |
| Rulebook vs run record | match — not edited since this render | sha comparison |
| HARD BANS | `base.md` | 4.1K |
| Voice spec | `voice/vukradin_new_pipeline.md` | declared `voice:` in `config/party.yaml` |
| Per-char examples | `examples/vukradin.md` | declared `examples:` |
| Global examples | none | no `shared_examples:` declared |
| voice_lint | ran | 0 errors, 0 warnings, 1 skipped check (no ```yaml voice_lint``` block) |

## Flags

### [1] Cross-narrator convergence — the same sentence as Brewbarry's, noun swapped — CONFIRMED

> I lean in with everything I have, and I feel it land clean, the way a phrase lands when the room stops chewing to listen.
> — L129

Against scene 07 L103, **Brewbarry**:

> The argument lands. I feel it land, clean, the way a good swing lands and nothing gets back up.

**Why:** `base.md`'s HARD BANS name `"the way X do/does/say/says … when …"` as a banned variant of behavioral taxonomy, and the rulebook's gloss is exact — "one Claude narrator wearing five hats." The frame `I feel it land, clean, the way a ___ lands ___` is filled with `phrase` here and `good swing` there. The music noun is correctly his; the sentence is not.

**Suggested rewrite:** keep the register, drop the frame — *I lean in with everything I have, and the room stops chewing to listen.*

### [2] Music metaphor density against his own spec — PLAUSIBLE

Five in narration prose:

> the way a phrase lands when the room stops chewing to listen (L129)
> it sits in my ear like a chord voiced one note wrong, and I cannot immediately say which note (L151)
> A pause exactly the length of a rest. (L167)
> a screech so far outside the key that the key files a complaint (L205)
> Her Bless settles over us like tuning (L301)

**Why:** his spec is explicit — "Music is his native organizing metaphor… but he uses it sparingly, where it earns its place, **not in every paragraph**."

**Why only PLAUSIBLE:** the scene is set on a stage during a performance, which is precisely where it earns its place, and L151 and L301 are both excellent. The real objection is narrower: L129 and L151 do the same job — a phrase landing, a chord sitting wrong — within 22 lines. Fixing flag [1] resolves this on its own.

## Not flagged

The longest section in the session (2,478 words, 55% narration prose) and it holds voice throughout. His spec's "he reaches for the ledger — coin returned, paperwork filed, receipts mailed — when he renders moral judgment" is executed almost literally and correctly:

> Not a coin changes hands, and the ledger balances anyway: the past infringement valued, squared by one exclusive night; the license running forward with disclosure stitched into it. Clean paper. Conflict-free. This is how it is done. (L189)

Also his:

> A performance you cannot call perfect is a performance you should not be charged for. That is fair trade. (L21)
> Nobody at the door recognizes me, which proves nothing except that I was ahead of my time, and I say as much. (L31)
> It should ring like a compliment. She means it as one, I think, or as half of one. (L151)
> Twenty-five gold pieces, twice, like naming it two times makes it smaller. (L223)
> Twenty-five gold, earned by my own name in my own hand. Fair-trade gold, and nobody bled for it. (L229)
> And here is the thing: I keep the spells in their case. I offered, sincerely, but nobody's mind gets altered tonight except the honest way, by a song standing on its own legs. (L293)

L293 is the section's real work — the party votes for mind-alteration and he quietly does not do it, without a speech about it. The rulebook's "the narrator never editorializes" held under pressure.

**Third-person check cleared:** `the great Vukradin` (L31) and `this was not the real Vukradin` (L163) are Vukradin naming himself as a public brand, which the scene is about. Not POV slips.

`cosplaying` in narration prose (L53) — GM-ruled in-canon during the scrub. The economics vocabulary at L131–L189 (`front-end points`, `Revenue share`, net/gross, `image and likeness`, `Perpetuity`) is the campaign's premise. No action on either.

Locked-dialogue anachronisms — `"A, B, C." / "Always be closing,"` (L43–45), `"more cowbell"` (L309), `"heavy metal"` (L313) — are surfaced as GM scope calls in `voice_critique_summary.md`. Note that the cowbell reference is partly self-covering already: Soma's `"the Nine Hells Chorale did not need more cowbell"` (L311) does the in-world work for free.

## Reclassified table speech

**One hatch, 2 spans:** `"So her response is: your usual fee."` and `"I start towering over her, and I'm like: are you trying to rip off my friend?"` — both third-person self-description inside quotation marks, which is the documented tell. Correct calls, and both beats survive in the narration at L87 and L167.

## Verdict

Half of the document's strongest finding sits at L129; the rest of the section is the most sustained voice work in the session and needs nothing.
