# Voice Critique — Valphine Sotorra, scene 04: Dining with Lim and Interrogating Bellows

**Narration:** `session_doc_scene_04_dining_with_lim_and_interrogating_bellows.scrubbed.md`
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

### [1] The aphorism frame, twice in one section — PLAUSIBLE

> A tortle who counts what leaves a building is a tortle worth listening to. I file it.
> — L25

> "What would you like me to elaborate? When they arrive, how they arrive? …" A witness who drafts his own cross-examination. I could weep.
> — L59

**Why:** `A [noun] who [does X] is [verdict]`, twice, plus a third in scene 06 (`A merchant whose costs do not twitch when the artery is severed was never drinking from the artery`). Her spec licenses the content — "her conclusions arrive several steps ahead of everyone else's; she does not bother to explain the gap" — but not one frame carrying all of it.

**Why only PLAUSIBLE:** both are good sentences, and "I could weep" is the exact deadpan-menace-by-removing-affect her spec asks for. The tic is the repetition, not the instance.

**Suggested rewrite (L25):** her lens is motive-systems, so name the motive rather than the type — *She counts what leaves a building. Somebody taught her to, or something did.*

### [2] `I file it` — flat register against the spec — PLAUSIBLE

> …and "came out with nothing." A tortle who counts what leaves a building is a tortle worth listening to. **I file it.**
> — L25

**Why:** the *register* is squarely on-spec — she is "an archivist of motive" who narrates "as if cataloging a specimen," so ledger and filing imagery belongs to her. The objection is narrower: her spec says "elevated, aristocratic, with no modern slack," and `I file it` is flat office-English. It also recurs verbatim as `I file the observation as accurate` in scene 06 L15 — 2 of her 2 sections. Note that **nothing checked this**: `voice_lint`'s bookkeeping/filing caps are skipped because `voice/_genre.md` declares no ```yaml voice_lint``` block.

**Suggested rewrite:** *I set it beside the rest.* — or let the verdict stand alone and cut the filing verb entirely.

### [3] `the way X …` simile frame — contributes to a doc-level breach

> I hold the fact the way one holds a hot coal by choice, and it is very fine.
> — L81

**Why:** member of the eight-instance doc-level set (`voice_critique_summary.md`, flag [4]). Distinct from the others in that it is genuinely hers — "she finds beauty in pain… pain is concentration, devotion, proof of contact" — and the "by choice" is doing the spec's work. Flagged as a member of the set; low priority to change.

## Not flagged

The analytical spine of this section is the strongest character work in the document:

> Wrong prices are not generosity. Wrong prices are a subsidy, and a subsidy is a leash, and the interesting question is always who holds the far end. (L31)
> There it is. The restaurant is not the customer; the restaurant is the cover. (L81)
> In my mother's house such a servant would be priceless, and would not survive a tenday. (L37)
> How deliciously literal. (L43)

`"a cosplaying Brewbarry…"` / `"He's not cosplaying, either,"` (L27–29) — `cosplaying` is GM-ruled an in-canon word. No action.

The clock reads `the third hour after midnight` at L61 and L85, consistent with scenes 06 and the rest of the document. The scrub's clock-notation normalisation is holding.

## Reclassified table speech

**None.** No hatch in this scene.

## Verdict

Her best section and the document's; the flags are register polish on top of work that is doing exactly what the spec asks.
