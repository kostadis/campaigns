# Voice Critique — Valphine Sotorra, scene 04: Ale and Rumors at Stonehill

**Narration:** `narration/session_doc_scene_04_ale_and_rumors_at_stonehill.md`
**Input shape:** per-scene (no `.scrubbed.md` variant exists; raw `.md` critiqued)
**Prose scanned:** 508 words of narration prose (81 quoted spans and 1 italic span excluded)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` — **resolved** | run record `narration_genre_file`; 61 lines, 7547 chars |
| Rulebook vs run record | **match — not edited since this render** | `sha256(text.strip())[:12]` = `6e67c59f94b4`, identical to `.knobs.json`; all 6 sibling scene records carry the same digest |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4221 chars |
| Voice spec | `voice/valphine_new_pipeline.md` — **resolved** | `config/party.yaml` roster declares `Valphine Sotorra` → exact name match |
| Per-char examples | `examples/valphine.md` (12.5K) — **resolved** | roster declaration |
| Global examples | none | `party.yaml` declares no `shared_examples:` — correct, no global bleed (#301) |
| Orphans | none | all 4 `voice/*.md` and all 4 `examples/*.md` are declared |
| Party doc | `docs/party.md` (`paths.party`) | roster 4/4 PCs present — not partial (campaigns#144) |
| Source layer read | **`scene_extractions_smoothed/`**, not the configured `scene_extractions` | verified empirically: 81/81 narration quotes match smoothed exactly; only 40/81 match raw |
| voice_lint | ran (exit 0) | 0 errors, 0 warnings, **1 note — bookkeeping/filing checks SKIPPED** |

**On the source layer.** `session_doc.yaml` sets `scene_extractions_dir: scene_extractions`, but every quoted span
in the narration is an exact match to `scene_extractions_smoothed/`. The pipeline preferred the smoothed layer
(`session_doc/io.py`, `SMOOTHED_DIR_SUFFIX`). This is the ch48 trap and it matters: diffed against the *configured*
raw layer the scene shows 25 apparent verbatim breaches, every one of which is an artifact of the wrong baseline.
Against the layer actually read, verbatim fidelity is perfect.

## Budget ledger

Scope: **single scene — doc-level budgets are not evaluable from one section.** Rows marked *(8-scene)* were
measured across all eight scene files in `narration/` and are reported as a separate observation, not as this
scene's verdict.

Budgets from: `voice/_genre.md` @ `6e67c59f94b4`

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| Verbatim fidelity of quoted spans | 81/81 exact vs smoothed layer | no drift | ok |
| Connective em-dashes in narration prose | **0** (all 10 em-dashes sit inside locked quotes) | rulebook: never as a connective | ok |
| Connective em-dashes in prose *(8-scene)* | **0 across all 8 scenes** | — | ok |
| `the shape of` | 0 | never | ok |
| Portable portrait (`with the X of a man who`) | 0 | never | ok |
| Behavioral taxonomy (any shell, incl. `the way X do … when`) | 0 | 0 | ok |
| First person, present tense | throughout; no third-person slip | always | ok |
| Italics for direct thought | 1 (`*Orcs.*`), single word | "don't overuse" | ok |
| Symmetrical description / mock-archaic / adverb-heavy | 0 | never | ok |
| Cross-narrator convergence *(8-scene)* | 2 shared 4-grams total, both benign proper-noun/signature | — | ok |
| Self-convergence, Valphine ch04 vs ch07 | 0 shared 4-grams | — | ok |
| Dialogue attribution density | **3 tags / 81 quoted spans (3.7%)** | examples baseline ~55% | **BREACH** |
| Narrator first-person presence | **2 markers / 508 prose words (3.9 per 1000)** | same narrator ch07: 29.6 per 1000 | **BREACH** |
| Prose share of section | **35%** — lowest of the 8 scenes (961 quoted words vs 508 prose) | render range 35–91% | **BREACH** |
| Bookkeeping / filing caps | — | — | *not checked — `voice/_genre.md` declares no ```yaml voice_lint``` block* |

## Flags

### [1] Rulebook conflict / craft — the attribution vacuum (line 9 onward, whole section)

> “Where have you been living that meals are free?”
>
> “I don't have any money for the meal. I'll just eat my rations outside. You guys go ahead.”
>
> “Starving artists.”

**Why:** 81 quoted spans carry 3 attribution tags. There are 11 runs of 4+ consecutive untagged quotes; the
longest is 9, the next 8. The smoothed layer the narrator read labels the speaker of all 106 moments, so nothing
was inferred away — the information was given and discarded. The quoted run above is Soma / Vukradin / Soma, but
because Vukradin spoke last before it, a reader assigns line 15 to Vukradin and line 17 to Soma — both wrong.
`examples/valphine.md` tags roughly 55% of its quotes ("explains Gnercli, his voice tense", "insists Gnercli",
"King Gnercli, obviously annoyed, says"), and scene 07 — same narrator, same render — does it correctly:
`"Let's go," says Vukradin.` The rulebook licenses *minimal* tag lines, not absent ones.

**Suggested rewrite:** restore a tag at each speaker change after a run of two, in the examples' idiom —
`“Where have you been living that meals are free?” Soma asks, unimpressed.` / `“Starving artists.”` This is not a
per-line edit job at this density; see the verdict.

### [2] Rulebook conflict — the narrator's own four lines are unattributed (lines 111, 125, 137, 205)

> “The problem with the small, or the dragon?”

**Why:** Valphine speaks four times in this scene — `“Ignorance is bliss.”` (111), `“Yeah, that's right.”` (125),
`“Are you dealing with these orcs on that list?”` (137) and the line above (205). All four are untagged, so the
reader has no way to know the POV character speaks at all. `base.md`: "This is a first-person memoir. The narrator
is always 'I'." The 205 case is the sharpest: it sits *directly* after her own interiority —
`The words settle pleasantly against my skin.` (203) — and the narration still does not connect her thought to
her mouth. Three of these four were human re-attributed upstream ("re-attributed from **GM** on the Zoom text
export"); that precision work is discarded here.

**Suggested rewrite:** `“The problem with the small, or the dragon?” I ask.` — matching ch07 line 25,
`"So, does it look like it was recently destroyed or a long time ago?" I ask.`

### [3] Voice spec conflict — the narrator is barely present in her own section (lines 89, 115)

> Vukradin begins. The performance is accomplished, technically clean, and entirely too long for an exchange whose likely reward is bread. I sit beside Soma’s ten-copper infusion and watch steam rise from the cup while Toblen listens, his eyebrows lifting as the music fills the common room.

**Why:** This is one of only two first-person markers in 508 words of prose. Valphine's *judgment* is everywhere
and it is good; her *body and position* are almost absent, so the section reads as a transcript with margin notes
rather than a memoir. The spec puts her body in the prose ("Burn, sting, pulse, the edge of light on skin"), and
the examples locate her constantly — "I watch as Vukradin attempts to negotiate. And I sigh.", "I stifle a laugh.",
"I now have to insert myself." Scene 07, same narrator and same render, runs 31 markers in 1046 words — 7.5× this
rate — so this is scene-specific, not a model ceiling.

Two calibrations, so the number is not oversold. Scene 03 (Soma) sits at 4.0 markers per 1000 against this
scene's 3.9, so this is *not* meaningfully the lowest in the render on that metric alone — the same-narrator ch07
contrast is the comparison that carries weight. What *is* uniquely low here is prose share: 508 prose words
against 961 quoted, 35%, the lowest of the eight scenes and the reason the two deficits compound.

**Suggested rewrite:** no single-line fix; the density is the problem. See the verdict.

### [4] Tell-not-show — naming the feeling (line 115)

> I am bored. Music is useful as discipline, ceremony, leverage, or the public manifestation of power. This is ale acquisition.

**Why:** The spec is explicit: "She does not confess emotion. She analyzes. If she names a feeling, it is because
the analysis required it." The analysis here is excellent and entirely sufficient on its own — *"This is ale
acquisition."* is the verdict, and it lands. The three-word flat declarative in front of it both states what the
next two sentences demonstrate and borrows a rhythm the rulebook assigns to Brewbarry ("Brewbarry's short
declaratives"). Note the source: the GM's table line *"And I think Valphine was bored with all this display of
music"* — correctly reclassified into the hatch, then rendered as a bald assertion rather than dramatised.

**Suggested rewrite:** drop the first sentence. `Music is useful as discipline, ceremony, leverage, or the public manifestation of power. This is ale acquisition.`

### [5] Voice spec conflict — the read on Vukradin (line 103)

> Vukradin studies him, fails to penetrate even this modest veil, and arrives at certainty by the simpler route.

**Why:** The spec: "She reads Vukradin's sincere moral optimism as expert manipulation, because in her grammar
there is no other category for it. She admires the maneuver while misidentifying the motive." The examples bear
this out — "Vukradin begins to amuse me", "he twists the knife expertly", "I smile as the Bard spins a tale of his
expertise and training, fictional no doubt." Here she reads him as *incapable*, which is contempt rather than
amused admiration, and it is the one register the spec rules out. The underlying event is faithful (he did roll a
4 on Insight and fail), so this is a framing flag, not a factual one — the event survives either framing.

**Suggested rewrite:** `Vukradin studies him, finds nothing, and takes the shorter road to certainty. I am almost impressed; it is the same move I would make with worse motives.`

## Locked-dialogue anachronisms — GM scope call

Not flags. These are player speech inside locked quotes; the critique must not rewrite them. Three dispositions:
**keep** (licensed table joke), **replace in-world** (authorial rewrite of player speech), or **annotate** with a
Kostadinious the Sage marginal note (precedent: Jimble the Unmoved, ch3 scene 07, GM-approved 2026-08-18).

| Line | Quote | Speaker (per extraction) | Note |
|---|---|---|---|
| 69, 71 | “One of those bangers. Play Freebird.” / “Yeah, totally. Freebird.” | Soma / Vukradin | Real-world song title and modern slang. **The narration already launders it** — `Toblen’s mouth tightens. His rag stops moving.` renders the innkeeper not recognising it, the same move as "I do not know Jim. Dead is dead." A **keep** is well supported. |
| 49 | “Oh, we're getting to the fat shaming now.” | Soma | Out-of-fiction meta about the GM describing Toblen sizing up the tortle, and **not laundered** — the surrounding narration doesn't absorb it. The extraction did not mark it `*table commentary*` (it does mark Soma's "hashtag" line that way), so the narrator had no signal. This is the one that most wants a disposition. |

## Reclassified table speech

7 spans logged in the `<!-- table-speech reclassified: … -->` hatch, all GM out-of-fiction narration (destination
confirmation, roadhouse boxed text, "he's very glad to see you. Your business.", the 10cp price as GM report, two
insight-roll rulings, and the GM's "Valphine was bored / she's not a music lover"). **All seven are correct calls
and worth rubber-stamping.**

One completeness gap for the GM: the hatch logs *GM* table speech only. Three PC table lines were dropped without
being logged — Valphine's own `"With a four, you probably believe him."` and `"Yeah, actually, no, that's true."`,
and Soma's `"He's following a hashtag not all barbarians."` (which the extraction explicitly marks
`*table commentary*`). Dropping them is correct — `base.md` bans mechanical detail — but the audit trail
understates what was reclassified, and two of the three are the narrator's own lines.

## Provenance note — em-dashes in locked speech (Scan A2)

Trailing-em-dash interruption assertions in this narration: **0**. Clean; no false interruptions shipped.

But the layers diverge on mid-quote dashes: `scene_extractions/` carries **1** em-dash inside its quotes,
`scene_extractions_smoothed/` carries **12**. The `/voice-smooth` pass substituted em-dashes for commas in ~11
locked lines — e.g. raw `"…in the past, I don't know, 200 years."` → smoothed `"…in the past — I don't know, 200
years."`; raw `"Yes, well, in that case…"` → smoothed `"Yes — well, in that case…"`. Those reached the narration
verbatim, so the narrator is not at fault, and the rulebook's em-dash rule governs narration prose (which is
clean). Flagging it because the smoothed file's own calibration header states *"grammar repair REJECTED (spoken
grammar left as said)"* — punctuation substitution inside speech sits uneasily against that ruling, and it puts
the campaign's banned connective dash into characters' mouths. GM's call whether to tighten `/voice-smooth`.

## Verdict

The scene's prose is clean against every rule the rulebook states — zero connective em-dashes, zero banned
constructions, correct first-person present throughout, no convergence with any other section — and its verbatim
fidelity is perfect. The defect is structural: 81 quoted spans carry 3 attribution tags, and all four of
Valphine's own lines are among the untagged, so the POV character is inaudible in her own section. Scene 07 proves
the same narrator, spec and rulebook produce correctly attributed dialogue in this render, so this is a re-render
signal for scene 04 rather than a sentence-edit job — the attribution and presence deficits are doc-shaped and
cannot be spot-edited into compliance.
