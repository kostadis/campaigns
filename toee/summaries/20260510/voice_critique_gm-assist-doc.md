# Voice Critique — gm-assist-doc.md (Chapter 26: Attrition)

**Narration:** `summaries/20260510/gm-assist-doc.md` (single assembled doc, 7 narrator blocks)
**Voice specs:** `voice/zephyr_voice.md`, `voice/zinnia_voice.md`, `voice/sequoia_voice.md`, `voice/calmer_voice.md` — all present
**Per-char examples:** none (`examples/` holds only thematic/global files — `combat_and_consequences.md`, etc. — no `<narrator>.md` routing files). All suggestions are grounded in the voice specs.

This is one assembled file rather than per-scene `.scrubbed.md` files, so this is a single consolidated report with one section per `## <Name>` block. Block numbers below are positional (the doc has no scene numbers / frontmatter).

Overall fidelity is high — the verbatim dialogue, the signature lines (`This again`, `One does not simply take bribes to defect`, `Who's the man?`, `Come and get it`, `They attack. They die.`), and the per-narrator combat registers all land. The flags below are spot-edits, not re-narration triggers. Two systemic issues cut across blocks: pervasive em-dashes and a recurring "filed"/"He doesn't need to know" convergence between Zinnia and Sequoia.

---

## Mechanical scan A — em-dashes (systemic, all blocks)

The narration contains **~60 narration-level em-dashes** (excluding the `## Heading —` lines, and excluding the truncated-speech dash inside `"or I could kill you—"` at line 51, which is verbatim and must stay). This is the dominant LLM punctuation tell in the document. I am **not** enumerating all 60 as individual flags — the pattern is systemic and best fixed with a single global pass (or a re-narration with an em-dash instruction), not 60 hand edits. Representative conversions so the user can see the shape of the fix:

> Feasting. Not hunting — feasting, which is a distinction that mattered to my continued good health. (line 13)

**Suggested:** `Not hunting: feasting. A distinction that mattered to my continued good health.`

> Which — given the state of the second level — was a reasonable assessment. (line 135)

**Suggested:** `Which, given the state of the second level, was a reasonable assessment.`

> the muffled boom of something two levels below — or in a corridor we weren't in — settled into the stone (line 167)

**Suggested:** `the muffled boom of something two levels below, or in a corridor we weren't in, settled into the stone`

> A small man caught in a big machine, reaching for the only lever he understood: someone else's authority. (line 287 — the colon here is already correct; the earlier dash on `that wasn't his — ours —` is the one to convert)

**Suggested for line 287's interruption:** `pinned the name to it that wasn't his (ours) so that when the Blades died…` or recast as two sentences.

Keep em-dashes that fall inside `"..."` dialogue or `*...*` italic VTT spans. Everything in plain narration prose is a candidate.

---

## Block 1 — Zephyr: The Sealed Greater Temple

### [1] Register-wrong vocabulary (mechanical scan B)

> I let the geometry of it settle. We were inside. The door was sealed.

**Why:** Zephyr's spec is explicit — he "reads people, not counts them," his assessments are "about what they need, what they want to believe, what lever moves them — not arithmetic." `geometry` is exactly the analytical register the spec rules out.
**Suggested rewrite:** `I let it settle. We were inside. The door was sealed.` (or `I let the math of it settle` only if you want the economic-Zephyr flavor — but plain is truer here).

### [2] Generic atmospheric prose

> Cold. From behind the door Calmer had been hammering. Everything went still.

**Why:** "Everything went still" is a stock fantasy beat that could sit in any narrator's section; Zephyr's voice notices *what* the stillness means (who reacted, what lever it moved), not the stillness itself.
**Suggested rewrite:** `Cold. From behind the door Calmer had been hammering. The wraith stopped laughing, which told me more than the voice did.`

---

## Block 2 — Zinnia: Return to the Earth Temple

### [1] Voice-bleed — Sequoia's signature line in Zinnia's head

> *Filed. He doesn't need to know what we built this on.*

**Why:** "He doesn't need to know" / "There is no need for him to know" is Sequoia's catchphrase (his spec lists it under *Things He'd Say*). Putting it in Zinnia's interior monologue blurs the two narrators. Zinnia withholds too, but his register is perception-as-currency, not Sequoia's flat dismissal.
**Suggested rewrite:** `Information he doesn't get to have. We built this; he inherited it.`

### [2] Register-wrong / convergence — "filed"

> The leader absorbed it, filed it somewhere between "acceptable" and "later," and redirected us. (line 151) — and again *Filed.* (177), *I filed that.* (191)

**Why:** "filed" is a paperwork metaphor flagged by mechanical scan B, and it recurs across both Zinnia blocks and the Sequoia blocks (see Block 4). Zinnia's spec says he tracks details "the way a monk keeps track of breath… He doesn't write this down. He doesn't need to." Filing is the opposite image — clerical, deliberate.
**Suggested rewrite:** `The leader took it, set it somewhere between "acceptable" and "later," and redirected us.` Reserve at most one "I noted that" across the whole document; vary the rest to perception verbs (*I read it / I caught it / it landed*).

---

## Block 3 — Sequoia: War Council and Hartsch's Blunder

### [1] Aesthetic scene-setting (off-register for Sequoia)

> The war room smelled like men who hadn't slept. Brown marble veined with black, the bronze sconces burning low, and Hartsch in the middle of it…

**Why:** Sequoia's spec: "His observations are always practical, never aesthetic… greased hinges, not 'ominous portents.'" Marble veining and low-burning sconces are mood-lighting, not the load-bearing detail Sequoia would clock. (The "smelled like men who hadn't slept" opening *is* in voice — practical, bodily — keep that.)
**Suggested rewrite:** `The war room smelled like men who hadn't slept. Hartsch was in the middle of it, asking what to do next like a man who'd never once had to answer that question himself.`

### [2] Cliché / flourish metaphor

> He brought up Romag — what Romag would have wanted, what Romag built, all of it in the voice of a man trying to borrow a dead man's spine.

**Why:** "borrow a dead man's spine" is a workshopped image; Sequoia's spec lists "Flowery description of anything" and "A long speech" under *Things He'd Never Say* — his metaphors are flat and functional, not literary.
**Suggested rewrite:** `He brought up Romag — what Romag would have wanted, what Romag built. Borrowing authority off a man we'd killed. He didn't know that part.`

### [3] Register-wrong vocabulary

> There it was. The whole shape of the man in one stroke.

**Why:** `shape` is on the mechanical scan B list, and "the whole shape of the man in one stroke" is a flourish Sequoia's deadpan, declarative voice wouldn't reach for.
**Suggested rewrite:** `There it was. The whole man, in one move.`

---

## Block 4 — Zinnia: The Failed Raid and Rescuing the Broken Blades

### [1] Anachronistic / modern-tech idiom

> Something behind Dren's eyes came back online.

**Why:** "came back online" is a contemporary technology metaphor in the mouth of a fantasy elf monk-spy. Zinnia's spec renders his reads as perception ("came back," "landed," "I knew"), not as a system rebooting.
**Suggested rewrite:** `Something behind Dren's eyes came back.`

### [2] Convergence — "filed" again

> I filed that. A wraith with a grudge against the faction we wear the badges of is leverage…

**Why:** Third+ use of "filed" across the document (see Block 2). The surrounding read is strong and in-voice — only the verb repeats.
**Suggested rewrite:** `I marked it. A wraith with a grudge against the faction we wear the badges of is leverage…` (or drop the tag entirely — the read stands on its own).

*Note:* "everyone is running an angle" (line 307) and "I watched it calculate the whole way through" (line 311) read as in-voice spy idiom, not the geometric/analytical register — not flagged.

---

## Block 5 — Calmer: Battle with the Wraith and Specters

No substantive voice flags. This block is the strongest in the document — clerical vocabulary for the undead ("a weapon of conjured light," "a thing of judgment," "the rite of turning"), the genuine-celebration-as-casing register, and the verbatim payoff (`"It worked! It worked!… Who's the man? Who is the man?"`) all match the spec exactly. The only edits here are the systemic em-dashes (lines 345, 349, 359, 361, 363, 365, 369, 371, 377, 381, 383, 385).

---

## Block 6 — Sequoia: The Defector's End

No substantive voice flags. Signature lines land verbatim (`"I think he's okay."`, `"One does not simply take bribes to defect."`, `"Good thing I am small. He never clocked me coming."`, the `*That's odd.* / *That's not good.*` two-beat). One minor note:

### [1] Minor — mixed register for the same object

> One of the bugbears who was supposed to be standing between us and the things that wanted us dead… (line 399, "*Our* perimeter") vs. "a man who used to guard our wall" (line 433)

**Why:** `perimeter` (mechanical scan B — military/clinical) and `wall` describe the same thing two paragraphs apart. Sequoia's plainer instinct is "wall" (line 413: "the wall he's standing on"). Not wrong, just pick one.
**Suggested rewrite:** Use `wall` in both spots for consistency with his plain register.

---

## Block 7 — Zephyr: Ambush of the Air Temple Gnolls

Strong block — the Tiefling tax lands verbatim (`"Tiefling flesh!"` → `"Come and get it."`), the Abyss/`or whatever you are` callbacks are spec-accurate, and "The world charging me for existing again" is core-Zephyr. Two small notes:

### [1] Clinical-measurement insert in combat

> Dagger high, dagger low, and then the third strike from the blind side with everything stacked behind it. Thud. Thirty pounds of pressure in a six-inch line.

**Why:** Zephyr's combat register is staccato and total ("Thud. One gone."), not forensic. "Thirty pounds of pressure in a six-inch line" reads like a coroner's note dropped into an assassin's beat — closer to analytical measurement than his "They attack. They die." rhythm.
**Suggested rewrite:** `Dagger high, dagger low, then the third from the blind side with everything behind it. Thud. The gnoll didn't so much die as stop.`

### [2] Clarity — garbled line

> There is no longer eulogy than they earn.

**Why:** Reads as a transcription/generation garble (missing article / inverted construction). The intended sense is "that's the whole eulogy they earn" — clarity issue, not voice.
**Suggested rewrite:** `That's the only eulogy they earn.`

---

## Verdict

The dominant fixable issue is the ~60 narration-level em-dashes — a single global pass is cheaper than hand edits and will lift the whole document off the LLM-default rhythm. The one genuine voice problem worth a deliberate fix is the **Zinnia/Sequoia convergence**: the recurring "filed" verb plus Sequoia's "He doesn't need to know" surfacing in Zinnia's head (Block 2 [1]) makes the two spies bleed together — vary the perception verbs and keep that catchphrase with Sequoia. Everything else is spot-editable; Blocks 5 and 6 are clean enough to leave as-is apart from the em-dashes. No block warrants re-narration.
