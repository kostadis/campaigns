# Voice Critique — Brewbarry, scene 07: Wandering the Blue Lake District

**Narration:** `session_doc_scene_07_wandering_the_blue_lake_district.scrubbed.md`
**Input shape:** per-scene
**Doc-level budgets:** evaluated across the whole document in `voice_critique_summary.md` — a single-scene critique cannot evaluate them.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record + config; 61 lines |
| Rulebook vs run record | match — not edited since this render | sha comparison |
| HARD BANS | `base.md` | 4.1K |
| Voice spec | `voice/brewbarry_new_pipeline.md` | declared `voice:` in `config/party.yaml` |
| Per-char examples | `examples/brewbarry.md` | declared `examples:` |
| Global examples | none | no `shared_examples:` declared |
| voice_lint | ran | 0 errors, 0 warnings, 1 skipped check (no ```yaml voice_lint``` block) |

## Flags

### [1] Cross-narrator convergence — the same sentence as Vukradin's, noun swapped — CONFIRMED

> The argument lands. I feel it land, clean, the way a good swing lands and nothing gets back up.
> — L103

Against scene 08 L129, **Vukradin**:

> I lean in with everything I have, and I feel it land clean, the way a phrase lands when the room stops chewing to listen.

**Why:** `base.md`'s HARD BANS name `"the way X do/does/say/says … when …"` as a banned variant of behavioral taxonomy, and the rulebook's gloss on the family is exact — "one Claude narrator wearing five hats." Here the hat-swap is visible in the diff: `I feel it land, clean, the way a ___ lands ___`, with `good swing` for the goliath and `phrase` for the bard. Neither character reached for this; the narrator did, twice, and dressed it per POV. This is the fable portable-tic mode — a construction that fits any narrator equally well is for that reason wrong for all of them.

It is also against his own spec in a second way: Brewbarry "does not build arguments, justify himself, or hedge," and a simile is a small argument. The three sentences immediately after it are the correct move and need no help:

> Fabric is threads. Soft fabric is soft threads. A robe is only as kind as its smallest part.

**Suggested rewrite:** cut the simile and let the flat statement carry it — *The argument lands. Nothing gets back up.*

## Not flagged

Strong section. The Yoko beat is the model case of an anachronism the narration absorbs rather than launders:

> "Call him Yoko and move on," Soma says. … I do not know who Yoko is. Probably somebody else who wrote about soup. (L57, L63)

Self-covering — **keep**. The joke is better for the gloss, and it is exactly his spec's "asks honest questions that reveal how much he does not know, without embarrassment."

Also his and nobody else's:

> A woman locks a door behind her. Then she locks it again. It was already locked. My neck knows before my head does. (L65)
> I love him. He is wrong. (L91)
> We do not buy the thread. Decorative thread is a lie a robe tells. (L111)
> Nobody agreed to this. I would remember. I remember every deal I make now. (L113)

L65 is the rulebook's "somatic-first" instruction executed properly — the body registers the wrongness before the narration names it.

`"Let's add it to the quest list!"` (L117) and `"Definitely be there in 2 days."` (L133) are locked verbatim dialogue. The first is metagame tooling and the second a numeral where the narration says "Two days" — both inside quotes, so neither is a narration flag.

## Reclassified table speech

**One hatch, 8 spans:** `"…in Discord"` ×2, `"Where's Bayard with his natural 20…"`, `"Wedding dress making when you need them, right?"`. Correct calls — Discord and the natural 20 are out-of-fiction by construction.

## Verdict

One flag, and it is half of the document's strongest finding: this sentence and Vukradin's in scene 08 are the same sentence with the noun changed, which is the ban stated as a move rather than a wording.
