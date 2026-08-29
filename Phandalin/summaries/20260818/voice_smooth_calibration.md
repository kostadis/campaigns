# voice-smooth — calibration register (Ch. 48, 2026-08-18)

**Status:** ✅ **REGISTER APPROVED** by the GM 2026-08-24. All five scenes rendered to
`scene_extractions_smoothed/`, speaker parity verified identical on every one. Originally paused
at step 4 (calibration gate), 2026-08-24. **Round 2 of
`/session-summary-consistency` is DONE (2026-08-24 22:51 UTC) — §B is resolved; see §D for the
nine scene-01 blocks that are now stale and must be re-smoothed.** Scene 01 drafted to
`scene_extractions_smoothed/`; scenes 02–05 not yet smoothed. Review mode chosen for
this run: **artifact**. Resume by re-reading this file, not by re-deriving the register.

**Resume order (decided with the GM):** run `/session-summary-consistency` round 2 on the
queue in §B first, then come back, **re-smooth the affected scene-01 blocks against the
corrected verbatim**, get this register approved, then smooth 02–05 and build the artifact.

> The re-smooth is not optional. Scene 01's smoothed lines were rendered on top of the
> garbles in §B. If the verbatim changes underneath them, the derived layer is stale.

---

## A. The register — how hard scene 01 was smoothed

Presented to the GM 2026-08-24 and **APPROVED unchanged**. Eight decision classes; applied to
all five scenes. Because §A was approved without revision, scene 01's already-smoothed blocks
did not need re-rendering — only the nine whose verbatim moved in round 2 were patched.

### A1. Multi-cue merge — structural, applied everywhere
The one-line-per-`> "…"` split is a VTT cue boundary, not a speech pattern. Merged into
continuous prose inside a single quote block. Speaker labels and their order untouched.
Scene 01: 151 quote lines → 110, across an **identical 115-block speaker sequence**.

### A2. Filler and false starts — the main dial
Cut `you know / like / I mean / sort of` where they are breath; kept where they carry a
beat. Collapsed stutters and self-interruptions (`is… is… is…`, `he's, he's…`).

- V: "a Drow cleric of Lathander who… I mean, you could go ask, I'm just telling you, you notice that they're skeptic… they're looking at you with a certain amount of skepticism."
- S: "A drow cleric of Lathander who… I mean, you could go ask. I'm just telling you, you notice that they're looking at you with a certain amount of skepticism."

### A3. `(truncated)` markers → ellipsis
Marker dropped, sentence left genuinely unfinished with `…`. **No endings invented.**
Alternative on the table: keep `(truncated)` so the narrator knows the tape cut out.

### A4. Grammar repaired only where a second source confirms the meaning

| Verbatim | Smoothed | Confirming source |
|---|---|---|
| "the fact that Vukradin intends to announce **is** the name of his latest band" | "**what** Vukradin intends to announce is the name…" | scene summary |
| "you can walk in, like, **have** an avatar" | "walk in **like** an avatar" | GM repeats it correctly ~20 lines later |
| "**I** was so excited about you showing up that **he** produced… he showed up" | "**He** was so excited…" | referent is the armorsmith |
| "**Your** brother Aldric is waiting for you" | "**Brother** Aldric is waiting for you" | prep: "Brother Aldric Sunmantle" — not her sibling |

### A5. GM-as-NPC — speech tag split out, interloper tagged inline, label NOT re-attributed

- V: "Yes, yeah. I mean, he looks at that and goes, there's a private receiving chamber, right?" / "You weren't supposed to do that. He kind of goes like this and ponders…"
- S: "Yes. He looks at that and goes, there's a private receiving chamber. **[Aldric]** 'You weren't supposed to do that.' He kind of goes like this and ponders all the liturgical and ceremonial elements that you have forgotten, and wonders. But he's in a good mood."

NPC voices sourced from `notes/session_prep/20260818_spire_of_the_morninglord.md`, which
carries explicit **Voice:** specs for Brother Aldric Sunmantle (gentle, certain;
*mercy/warmth/hope* are load-bearing words), Perrin Alagondar (formal, apologetic,
overcorrects), Cullen Sharpe (warm, never raised, addresses everyone by name), the Fixer
(silent), Lord Neverember (controlled, not hostile), Aldus (two reactions layered),
Lord Cassian Meliamne. Applied at 4 blocks in scene 01 (Aldric ×3, scarred sun priest ×1).

### A6. Kept because it may be voice, not error
`skepticals` (Brewbarry) — he is *simple, not dim*, and still learning surface norms.
False start and "like" dropped, the word kept.

### A7. Garbles left strictly alone → see §B

### A8. Silent typography
Spell names capitalised (*Daylight*, *Light*, *Hold Person*), "Whispers"→"whispers",
"spire"→"Spire", "Natural One"→"Natural one".

### A9. Note on the voice files
`voice/*_new_pipeline.md` are **narration prompts**; their first rule is "Do not modify
any characters inside quotation marks." That rule is correct *downstream* of voice-smooth —
this skill produces the quotes those prompts then lock. Only their *voice specification*
sections were used, never their constraint sections. Looks like a conflict; isn't one.

---

## B. Queue for `/session-summary-consistency` round 2 (scene 01 only) — ✅ RESOLVED

Residual transcription errors found while smoothing. Per the skill these are **upstream** —
they were not fixed in the smoothed layer, because fixing them here means fluently
rendering a mistake. All are in
`scene_extractions/01_arrival_at_the_spire_of_the_morninglord.md`.

| Speaker | Verbatim | Suspected | Confidence |
|---|---|---|---|
| Brewbarry | "What are we **ruling** perception?" | "rolling" | high |
| Brewbarry | "I'm **casting so much energy** on myself" | *thaumaturgy* — phonetic; scene summary says Thaumaturgy | high |
| Brewbarry | "I'll whisper **and I hear**" | "in her ear" | high |
| GM | "the followers of **Love**, who are the gods of pain" | Loviatar | high |
| GM | "are you trying to be **cannot**…" | "canon" | high |
| GM | "so that she gets another **role**" | "roll" (homophone) | high |
| Vukradin | "**Bourd**, of course!" | Brewbarry | medium |
| Vukradin | "So, **Phoenix**. Old person?" | *Phoenix* unexplained; *Old person* = Hold Person, already annotated | low |
| Valphine | "We're done for a minute there." | not reconstructable | low |
| GM | "**He** rolled a natural 20" (of Valphine) | GM using the player's pronoun; cf. the `he's`→`she's a cleric` fix already applied at stage 1 | ruling needed |

**Two player real names still sitting in quote *content* in scene 05** — allowed by
`/session-summary-consistency` (leave-but-flag), but they reach narration through the
smoothed layer, so voice-smooth needs a ruling on them:

- `05:107` Brewbarry — "Remember, I asked you to find the gnome's name for me, **as David**." (tail annotated as garbled)
- `05:812` GM — "Does that, does that capture, of, **stephane**?" (GM checking the read with the player)

---

## C. Inventory at pause time

| Scene | Verbatim | Smoothed |
|---|---|---|
| 01 arrival_at_the_spire_of_the_morninglord | 418 lines, 115 blocks, 151 quote lines | **drafted** — 115 blocks, 110 quote lines |
| 02 the_sermon_of_searing_light | 76 quote lines | not started |
| 03 lathander_s_death_performance_and_the_shakedown | 260 quote lines | not started |
| 04 the_alagondar_inheritance | 127 quote lines | not started |
| 05 information_gathering_cullen_sharpe_and_the_counting_house | 305 quote lines | not started |

The verbatim `scene_extractions/` and the VTT were not written to and must not be —
voice-smooth's only output is `scene_extractions_smoothed/`.

---

## D. Round 2 outcome (2026-08-24) — what changed under the scene-01 draft

Adjudicated in the **Chapter 48 Quote Rulings** artifact,
`https://claude.ai/code/artifact/1a7e4c04-d314-4626-8a05-56daf42976bb`, saved 22:51 UTC
and **revised at 22:56 UTC** — the second save reopened four scene-01 items (see the
amendment at the end of this section).
15 rulings: 13 approve, 2 reject. 13 further corrections were auto-applied (two
independent transcripts, or glossary + unambiguous context) and are listed in the
artifact footer.

### The nine scene-01 quote blocks whose verbatim moved — **re-smooth these**

| Speaker | Was | Now |
|---|---|---|
| Brewbarry | "What are we ruling perception?" | "What are we rolling? Perception?" |
| GM | "the followers of Love" | "the followers of Loviatar" |
| Brewbarry | "I'll whisper and I hear" | "I'll whisper in her ear" |
| GM | "so that she gets another role?" | "…another roll?" |
| Vukradin | "Bourd, of course!" | "Brewbarry, of course!" |
| Brewbarry | "casting so much energy on myself" | "casting thaumaturgy on myself" |
| GM | "Are you trying to be cannot…" | "Are you trying to be canon…" |
| Vukradin | "So, Phoenix. Old person?" | "So, Valphine. Hold person?" |
| Valphine | "We're done for a minute there." | "[inaudible]" |

Three speaker-line annotations in scene 01 also changed (Thaumaturgy, Hold Person,
and the ASR note). Scene 02 gained 2 fixes, scene 03 gained 8, scene 05 gained 8;
scene 04 needed nothing. Scenes 02–05 were never smoothed, so only scene 01 is stale.

### The two rejects — the verbatim stands, do not "improve" it while smoothing

- **s01-05.** `"He rolled a natural 20. Wow."` **stays** `He`, even though the Zoom export
  reads `You` and the character is *she*. GM ruling: the GM was talking about the
  *player*. Do not repair this pronoun in the smoothed layer.
- **s01-03.** The cue was **kept**, not dropped — reconstructed as
  `"So, Valphine. Hold person?"` rather than trimmed to the Zoom export's bare
  `"Hold person?"`.

### The two player-name questions §B raised are both settled

- `05:107` **"as David"** — deleted. The Zoom export ends the sentence at "for me."; the
  tail was an ASR artifact, not the player's name. No policy needed.
- `05:812` **"stephane"** — scrubbed to `"Does that capture it?"`. Both transcripts
  carried the real name, so this one was real and the GM ruled it out of the record.
  **Precedent for voice-smooth: player real names do not reach the smoothed layer.**

### Glossary

Two rows added to `notes/vtt_transcription_corrections.md` under a new
*Round 2 (2026-08-24)* subsection, both GM-approved on their cards, both carrying
caveats because neither is a bare non-word: `casting so much energy → casting
thaumaturgy` (multi-word phrase) and `SOBA → SOMA` (*soba* is a real word — logged in
the live-risks list).

### Amendment — the 22:56 UTC re-save (four scene-01 items reopened)

The GM saved a second time and changed four verdicts. Final scene-01 state:

| id | Final ruling | Line now reads |
|---|---|---|
| s01-01 | verdict cleared, then **kept applied** on the GM's word | "I'm casting thaumaturgy on myself" |
| s01-02 | discuss → **"canonical"**, not "canon" | "Are you trying to be canonical…" |
| s01-03 | discuss → note wording followed | "So Valphine, Hold Person?" |
| s01-04 | discuss → GM chose `[inaudible]` after all | "[inaudible]" |

So the **nine stale scene-01 blocks in the table above still stand**, with three of them
now carrying different text than the first save produced: s01-02 is *canonical*, s01-03
is *"So Valphine, Hold Person?"*, s01-04 is *[inaudible]*.

### ⚠ Canon fact supplied by the GM in the s01-02 note — not a quote fix

> "Are you trying to be canonical — in other words is she using the proper forms of the
> ceremony. **She did, it's important for later.**"

**Valphine used the proper liturgical forms at the Spire.** This is GM-authored canon that
arrived through a quote-review note, so nothing downstream has it yet: it is not in
`planning.md`, not in the chapter split, and not in the bible. The GM flagged it as
load-bearing for a later beat. Promote it deliberately — it does not belong to this skill,
and grounding docs are CampaignGenerator outputs that must be fixed at source.

---

## E. Completion (2026-08-24) — all five scenes rendered

| Scene | Blocks | Verbatim quote lines | Smoothed |
|---|---|---|---|
| 01 arrival_at_the_spire_of_the_morninglord | 115 | 151 | 112 |
| 02 the_sermon_of_searing_light | 55 | 76 | 59 |
| 03 lathander_s_death_performance_and_the_shakedown | 207 | 260 | 204 |
| 04 the_alagondar_inheritance | 103 | 127 | 101 |
| 05 information_gathering_cullen_sharpe_and_the_counting_house | 239 | 305 | 237 |

Speaker sequence verified **identical to the verbatim on all five** (`diff` of the ordered
`**Speaker**` labels). No player real name appears anywhere in the derived layer, including
editorial annotations. `scene_extractions/` and the VTT were not written to during the pass.

Scene 02's smoothed count is *higher* than a pure merge would give because Valphine's
16-cue sermon was rendered as four rhetorical movements rather than one wall of prose.

### Escalations found while smoothing — these are `/session-summary-consistency` items

Per the skill these were **not** fixed in the derived layer. Four residual transcription
errors surfaced only once the lines were read as prose:

| Scene | Verbatim | Suspected |
|---|---|---|
| 02 | "To the English, I can." | "In English, I can't." — inverts the joke |
| 03 | "Cullen's **preview** conversations" | "private" |
| 03 | "To circulate the **wall**." | "wealth" |
| 05 | "**acting** favors… then I can be Neverwinter's godfather" | "trading" |

### Hand-off

`session_doc` should now read from `scene_extractions_smoothed/`. The verbatim
`scene_extractions/` and the VTT remain the record.

---

## F. Review outcome (2026-08-24 23:43 UTC) — voice-smooth COMPLETE

Artifact **Chapter 48 Smoothed Quotes**,
`https://claude.ai/code/artifact/a13a1681-f82a-4704-8405-25a0cee8fd39`.
**All nine flagged renderings approved, no notes.** Per the verdict mapping, approve means
the rendering already stands in `scene_extractions_smoothed/` — no edits were required.

Approved renderings of note:
- Valphine's sermon stays as **four rhetorical movements**, not one block (s02-q01).
- Aurelan Vance's long speeches stay **merged**, despite the risk that the cue-by-cue
  stammer was the characterisation Brewbarry mocks (s05-q02).
- All three grammar repairs on the rumour line stand (s03-q03), and "520" stays split
  as "5, 20" (s03-q04).

### ⚠ The four transcription repairs are approved **in the derived layer only**

s02-q03, s03-q01, s03-q02 and s05-q01 were repairs of *transcription* errors made inside
the smoothed layer, which the skill normally forbids. The GM approved all four. That
ruling covers the **derived layer**; it is **not** a ruling on the verbatim, which still
reads:

| Scene | Verbatim still says | Smoothed now says |
|---|---|---|
| 02 | "To the English, I can." | "In English, I can't." |
| 03 | "Cullen's **preview** conversations" | "private" |
| 03 | "To circulate the **wall**." | "wealth" |
| 05 | "**acting** favors" | "trading" |

**The two layers now diverge on these four lines by explicit approval.** Closing the gap
means a round 3 of `/session-summary-consistency` on the verbatim — the GM's call to make,
not this skill's.

### Step 5 hand-off — done

`session_doc` should read from `scene_extractions_smoothed/`. The verbatim
`scene_extractions/` and the VTT remain the record and were never written to.

## G. Post-completion repair (2026-08-24) — Valphine misgendered in-character

GM ruling: two players slipped their *player's* gender onto Valphine while speaking
**in character**. Valphine is female; the pronouns are wrong in the fiction, so they are
repaired in the derived layer.

| # | Scene | Speaker | Verbatim still says | Smoothed now says |
|---|---|---|---|---|
| g-01 | 02 | Brewbarry | "all eyes on **him**. **He's** about to illuminate them with **his** divine message." | "all eyes on **her**. **She's** … **her** divine message." |
| g-02 | 02 | Brewbarry | "the way that **he** sets forth" | "the way that **she** sets forth" |
| g-03 | 02 | Brewbarry | "Isn't that what **he** did?" | "Isn't that what **she** did?" |
| g-04 | 02 | Brewbarry | "**He** blessed him with the holy light." | "**She** blessed him with the holy light." |
| g-05 | 05 | Vukradin | "**He** jests. As you know, **he's** a cleric of Lathander." | "**She** jests. As you know, **she's** a cleric of Lathander." |

g-04 and g-05 also occur inside the `## Scene summary (from gm-assist, verbatim)` block of
their scene file and were fixed there too, so the summary and the quote block agree. The
**upstream gm-assist / session-summary still carries the error** and will re-inject it if
those blocks are regenerated.

### Does this conflict with the §D reject (s01-05)?

No. That ruling — `"He rolled a natural 20"` stays `He` — covers the **GM speaking
out-of-fiction about the player Gary**, where the masculine pronoun is correct. §G covers
**PCs speaking in character about the character Valphine**, where it is not. The dividing
line is the frame, not the pronoun.

### Judgment call flagged for the GM

**g-03** is the least certain of the five. Context is DM "Inflicting pain, though, is…" →
Brewbarry "Isn't that what he did?" The read applied is *"isn't inflicting pain what
Valphine just did?"* An alternative read makes "he" the blinded Loviatarite. If the GM
prefers that reading, revert this one line only; the other four are unambiguous.

**The two layers now diverge on five further lines.** As with §F, the verbatim
`scene_extractions/` and the VTT were not written to.
