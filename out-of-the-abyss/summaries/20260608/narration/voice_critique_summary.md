# Voice Critique Summary — Session 20260608

6 scenes / 4 narrators / 22 flags total

| Scene | Narrator | Flag count | Strongest flag |
|---|---|---|---|
| 01 — Reporting to Bookwyrm | Daz | 4 | Maritime "rudder" metaphor — wrong geographic frame |
| 02 — Investigation Strategy | Thorin | 3 + meta | Card-game idiom; frontmatter `narrator: Throin` typo |
| 03 — Secret Meeting with Kalan | Zalthir | 4 + meta | Over-elaborated aphorism sounds like Grygum; `Brookworm` typo |
| 04 — Research in the Flora Theca | Grygum | 3 + meta | Inverted Stroud reference; `teleportat` typo |
| 05 — Interrogating Daral at the Hearth | Daz | 3 | `grammar` wrong vocab register for bookkeeping-frame character |
| 06 — Glabbagool's Trial | Zalthir | 3 | `column` bleeds Daz's vocabulary into Zalthir's narration |

## Strongest recurring theme

**Vocabulary bleed between narrators.** Three of six scenes contain an idiom or term that belongs to a different narrator:

- sc02 Thorin uses `everybody's holding a card they won't show` — card-game language from Daz's information-currency frame
- sc05 Daz uses `grammar` — linguistic/structural term outside his bookkeeping vocabulary set
- sc06 Zalthir uses `a clean column for` — directly from Daz's ledger vocabulary, used three times in sc01/sc05

The model appears to be reaching for "analytical-sounding" language without distinguishing which character's specific analytical vocabulary is being invoked. Daz's frame is financial/bookkeeping; Thorin's is terrain/stone; Zalthir's is tactical-categorical with monastery callbacks; Grygum's is paratactic witness-notation. Crossing these registers is the most consistent failure mode.

## Second theme

**Generic similes in opening character descriptions.** Four of six scenes have a stock simile in the first or second paragraph describing another character or entering a room:

- sc01: "like a loose tooth" (Grygum worrying at a word)
- sc03: "the way a man looks at someone explaining how he came to run the gate of Candlekeep" (elaborate Kalan look)
- sc04: "like the books are sleeping and might wake" (Fembris walking)
- sc06: "the way the surface of deep water is still, the way a thing is still when nothing inside it is wasted" (Glabbagool's stillness)

The pattern is consistent: the model reaches for atmospheric imagery at the scene-entry moment instead of the character's specific observation mode.

## Mechanical fixes (highest priority, not voice flags)

These are consistency errors that should be applied to the `.scrubbed.md` files before `assemble.py` runs:

| File | Error | Fix |
|---|---|---|
| sc02 frontmatter | `narrator: Throin` | `narrator: Thorin` |
| sc03 line ~10 | Kalan says "Brookworm" | "Bookwyrm" |
| sc04 line ~58 | "teleportat" | "teleport it" |

## Per-narrator summary

**Daz (sc01, sc05):** 7 flags across two scenes. Strongest issue: wrong-register metaphors (scalpel, rudder in sc01; grammar in sc05). Bookkeeping vocabulary is otherwise well-deployed. The sc05 close ("The dead poisoner is the innocent one") is the best single sentence in the session.

**Thorin (sc02):** 3 flags. Largely on-voice — "The heart is a fact" and the solo-conversation close are excellent. Card-game idiom is the primary miss; frontmatter typo is the urgent mechanical fix.

**Zalthir (sc03, sc06):** 7 flags across two scenes. Strongest systemic issue: over-articulation in sc03 (philosophical elaborations that Zalthir would compress), and "column" bleed from Daz in sc06. The monastery callbacks and declarative-full-stop rhythm are right when the model doesn't interrupt them.

**Grygum (sc04):** 3 flags, cleanest narration in the set. The priestly training thought source, the chess reference (wrong spin but correct story), and "I had pages of it now. It's what I do." are all in character. Flags are genuine spot-edits.

## Recommendation

The narration is largely voice-faithful. This is not a re-run situation — targeted spot-edits on the 22 flagged sentences are the efficient path. Start with:

1. **Mechanical fixes** (frontmatter typo, Brookworm, teleportat) — these affect assembly and downstream tools.
2. **Vocabulary bleed** (sc02 card idiom, sc05 grammar, sc06 column) — these are the clearest narrator-crossing errors.
3. **Similes** (sc01 rudder, sc04 sleeping books, sc06 double water simile) — secondary priority, editorial preference.

If a systemic voice problem surfaces on re-read after spot-edits, the efficient fix is to add explicit negative-vocabulary notes to each narrator's voice spec ("Daz: never use 'grammar' or 'rudder'; Zalthir: never use 'column'") and re-run the relevant scenes.
