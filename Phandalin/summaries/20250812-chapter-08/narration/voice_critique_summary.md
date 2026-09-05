# Voice Critique — Chapter 8, all six scenes (smoothed-input re-render)

**Narration:** `summaries/20250812-chapter-08/narration/` — 6 scenes, 4,151 prose words
**Input shape:** per-scene (directory)
**Render under review:** codex-cli `gpt-5.6-sol`, medium reasoning, `--scene-extractions scene_extractions_smoothed`
**Baseline for comparison:** the same invocation against `scene_extractions/` (verbatim), preserved from commit `62b17185`

---

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `7a848f23adda` | `--narration-genre-file` on the command line; also `paths.genre_file` in `config/session_doc.yaml`. Resolved, not unset. |
| Rulebook vs run record | **no run record** — no `.knobs.json` written | cannot verify the digest the render actually used; config and CLI agree |
| HARD BANS | `config/agents/session_doc/narrate/base.md` (4,221 chars) | CampaignGenerator checkout |
| Voice specs | all 4 resolved: `brewbarry_`/`soma_`/`valphine_`/`vukradin_new_pipeline.md` | declared in `config/party.yaml`; exact-name match |
| Per-char examples | `examples/{brewbarry,soma,valphine,vukradin}.md` | declared |
| Global examples | none | `shared_examples` not set |
| Party doc | `docs/party.md` | roster block partial — 3 of 5 `Player:` lines |
| `voice_lint` | **ran**, exit 0 | 0 errors, 0 warns, **1 config note** |

### Checks that did NOT run

**`extra_tics` — four campaign-authored patterns, dropped.** `voice_lint` emitted
`note [config] unrecognised voice_lint key 'extra_tics' — ignored`. These are the campaign's
own behavioral-taxonomy shells, derived by scanning ch40–48. **Run by hand for this report:
0 hits across all six scenes.** Filed upstream as CampaignGenerator#376.

## Budget ledger

Scope: whole document (6 scenes, 4,151 prose words). Budgets from `voice/_genre.md` @ `7a848f23adda` and `base.md`.

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| `the shape of` | 0 | ≤1 doc-wide | ok |
| portable portrait (`with the X of a man who`) | 0 | ≤1 doc-wide | ok |
| behavioral taxonomy (all shells) | 0 | 0 | ok |
| `extra_tics` — 4 patterns, each cap 0 | 0 | 0 | ok *(checked by hand; voice_lint dropped them)* |
| connective em-dashes in prose | 0 | rulebook: never as connective | ok |
| bookkeeping / filing register | 0 errors | per rulebook block | ok |
| **POV lexicon** (`_genre.md` L15, L38) | **1** | 0 cross-narrator signature use | **BREACH** |
| first-person present tense | 6 of 6 | all | ok |

---

## Flags

### [1] Rulebook conflict — Soma's signature phrase in Valphine's POV — **BREACH**

Scene 04 (`Valphine Sotorra`), line 29 of the prose:

> The tactical merit remains. The harpy now faces a giant spider at close quarters, Brewbarry's halberd within reach, and **my bale** arranged around every useful escape.

**Why:** `voice/_genre.md` L15 states *"Use the POV character's vocabulary for everything…
Soma calls the party 'my bale' and Vukradin 'shell sprout.' Valphine calls the surface 'the
Overbright.'"* L38 lists `my bale` among the **signatures** to use verbatim. It is Soma's,
and it is in Valphine's mouth. `soma_new_pipeline.md` L43 confirms it as hers.

**This is a regression introduced by this render.** In the baseline, `bale` appears only in
Soma's two scenes (02, 06). Here it also appears in Valphine's.

**Suggested rewrite:** Valphine's register is hierarchical and tactical, not familial —
*"…and my companions arranged around every useful escape"*, or in her own idiom, *"…and the
others placed across every useful escape."* She catalogues positions; she does not adopt a
herd noun for the party.

### [2] Unattributed dialogue — 16 orphan quote runs, and the render carries *less* narration than the baseline

| | baseline (verbatim input) | new (smoothed input) |
|---|---|---|
| orphan quote runs (3+ consecutive, unattributed) | 11 | **16** |
| quoted spans | 165 | **186** |
| **prose words** | 4,318 | **4,151** |

Worst case, scene 04 lines 67–74 — four consecutive quotes, two speakers, no tags and no
action beat:

> "You want me to drop the silence spell?"
> "Well, I mean, I'm in melee now."
> "Yeah, but would you be better off with a spell attack?"
> "Probably."

Scene 04 carries 7 of the 16 runs; scene 06 has 5; scenes 02 and 05 have 2 each.

**Why this matters, and why it is the headline.** `/no-mech`'s stated benefit is that a
cleaner input lets the narrator *"stop spending its budget on conversion and spend it on
character."* The measurement says the opposite happened. Smoothing merged fragmentary cues
into clean, readable quotes — which made them **more** attractive to reproduce verbatim, so
the narrator quoted more and narrated less. The result reads closer to a transcript than the
baseline did.

**The fix is cheap and non-destructive.** Attribution already exists upstream:
`scene_extractions_smoothed/NN_*.md` labels every quote with its speaker. Add speaker tags
and action beats *around* the quotes; never touch a word inside them. Leave any line the
smoothed layer marks `UNKNOWN` untagged.

### [3] Trailing em-dash provenance — false interruption assertions I introduced at /voice-smooth

Scan A2 diff:

| layer | quotes ending `—"` |
|---|---|
| `scene_extractions/` (verbatim) | **0** |
| `scene_extractions_smoothed/` | **3** |
| narration | 1 |

All three were a period or an ellipsis in the raw capture and became em-dashes during
smoothing — punctuation changes, so they were covered by the calibration approval and my
word-level delta audit could not see them. **A trailing em-dash asserts that the speaker was
interrupted**, which is a factual claim about the tape.

Adjudicated against the independent Descript reading:

| Scene | Line | Raw capture | Tape says | Verdict |
|---|---|---|---|---|
| 03 | GM, *"So let me just —"* | `.` | `kostadis: Um, so let me just- **wade:** Disadvantage on all saving throws` — Wade **does** speak over him | **em-dash CORRECT** — improves on the raw |
| 04 | *"…Really? I could have —"* | `.` | `kostadis: I, I could have- Well, give her, give her the mace` — **same speaker continues** | **WRONG** — self-correction, not interruption |
| 06 | Soma, *"…any sort of —"* | `…` | no anchor hit | **WRONG** — raw ellipsis is the pre-smoothing capture; prefer it |

Only the scene 04 one reached the narration. Two edits needed in
`scene_extractions_smoothed/`: restore `.` in scene 04, restore `…` in scene 06, keep scene 03.

---

## Per-scene grid

| Scene | Narrator | Prose words | Quoted spans | Orphan runs |
|---|---|---|---|---|
| 01 Silence at the Tower | Vukradin | 751 | 36 | 0 |
| 02 Battle of the Parapet | Soma | 647 | 31 | 2 |
| 03 Harpies Continue | Brewbarry | 661 | 4 | 0 |
| 04 The Harpy's End | Valphine Sotorra | 759 | 41 | **7** |
| 05 Exploring the Tower | Vukradin | 650 | 45 | 2 |
| 06 Showdown with Moesko | Soma | 683 | 29 | 5 |

Scene 03 is the outlier in the other direction — 4 quoted spans from 1,972 source words. It
renders almost everything as narration. Given Brewbarry's spec (*short, declarative, acts
rather than argues*) that is defensible, and it carries zero orphan runs as a result.

**Measurement caveat:** codex emits **curly** quotes in scene 06 and straight quotes
elsewhere. A first pass of this report counted scene 06 as having zero dialogue and 11 orphan
runs document-wide. Both were wrong; every count above matches `"…"` and `“…”`.

## Locked-dialogue anachronisms — the GM's scope call

**None found.** The `napalm` line is gone (established as a retranscription-only fabrication
during `/voice-smooth`; the render carries *"it smells like nature"*). The DHCP/Santorini
and internet-outage material was cut at `/voice-smooth` and does not appear.

## Reclassified table speech

Five hatches, up from four in the baseline. **This is not a regression** — the increase is
the pipeline correctly recording conversions it previously made silently, and the skill's
"expect the hatch to disappear" prediction assumes the mechanics were *cut*, which this
campaign explicitly ruled against.

| Scene | Spans | Assessment |
|---|---|---|
| 01 | several | routine — Roll20 screen reference, table chatter |
| 02 | several | routine |
| 03 | 2+ | includes *"Vukradin with three hit points and silence concentration"* — **correct**: the player names his own character in third person inside that character's quote. Content survives in the prose. |
| 04 | several | routine |
| 05 | several | includes the GM's **boxed text**. Correct handling — it became scene description (*"The rough-hewn stairs climb the eastern face of the rock…"*) rather than a quoted GM line. Verified present. |

## Verdict

The strongest issue is **[2]**: this render carries more dialogue and less narration than the
baseline it was supposed to improve on, producing 16 orphan quote runs against 11 — so the
smoothing bought readability in the input and spent it on transcript-shaped output. That is a
tagging-and-beats edit, not a re-render; scene 04 alone accounts for 7 runs and is where to
start. **[1]** is a one-word fix. **[3]** is two edits in the smoothed layer, and it is mine.

Mechanically the render is clean: zero on every doc-level budget including the four
`extra_tics` patterns `voice_lint` silently dropped.
