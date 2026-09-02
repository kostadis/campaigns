# Voice Critique — Vukradin, scene 03: Arrival at The Board Laid Bare

**Narration:** `session_doc_scene_03_arrival_at_the_board_laid_bare.md`
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

**Source note:** this is the raw `.md`. Scene 03 is the one scene of the eight with **no `.scrubbed.md`** — the scrub run produced none. Every real-world anachronism in this scene left through the reclassification hatch instead (see below), which is a different mechanism with a different reviewer.

## Flags

### [1] `the way X …` simile frame — contributes to a doc-level breach

> Not still like a bored doorman. Still the way a lute peg is still: holding tension, refusing to move.
> — L37

**Why:** member of the eight-instance doc-level set (`voice_critique_summary.md`, flag [4]).

**Why I would keep this one anyway:** it is the strongest instance in the document. The lute peg is Vukradin's own instrument, it does real work on a warforged, and the colon-clause names the specific quality rather than gesturing at a category. If the budget is cut to two, this is one of the two.

## Not flagged

Structurally the best-behaved section in the session. 65% narration prose, the highest ratio except scene 06. The POV work is genuine and repeatedly does what the rulebook asks:

> Devotion or inventory, I can't tell yet, and both answers interest me. (L75)
> Alone. All those visits, one tortle at a window table with the best view of the tower. That picture isn't mine to say anything about, so I don't. (L49)
> A perfect explanation. I believe it, mostly, the way I believe a song I haven't heard the last verse of. (L123)

L123 is the second `the way` in the section, but it is a first-person qualification of his own belief rather than a taxonomy of someone else's behaviour — different move, not the ban.

`"Organic Fair Trade!"` (L119) and the supply-chain reasoning at L115–125: the campaign's economics premise, ruled in-canon by the GM during the scrub. No action.

`"You haven't been here in 73 days."` (L73) — a number, but Bellows counting is in-fiction characterisation, not mechanical residue. The narration at L75 does the right thing with it.

`"The usual…" I add, as if I have one.` (L109) — the scrub's one scanner false positive (`roll_result_dialogue` matching `I have one`), correctly rejected per-instance and correctly not written to the ignore list.

## Reclassified table speech

**One hatch, 12 spans**, and it is doing anachronism work: `"Kmart!"`, `"it's not like we're putting these on YouTube or anything."`, `"Oh, you're just sending him to Claude to transcribe for you, right?"`, `"It's an Airbnb."` ×2.

Worth an explicit GM eye. Every hard real-world reference in this scene was removed by the model's own scope call, not by the scrub — and this is the scene the scrub never produced an output for. If the GM disagrees with any of these classifications there is currently no other checkpoint that would catch it.

## Verdict

Clean section, one member of a doc-wide simile pattern that I would keep. The thing to review here is the hatch, not the prose.
