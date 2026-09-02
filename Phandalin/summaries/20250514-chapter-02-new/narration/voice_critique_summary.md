# Voice Critique — Chapter 02 (20250514-chapter-02-new), all 8 scenes

**Input shape:** per-scene (8 files; `.scrubbed.md` used for 04–08, raw `.md` for 01–03 — no scrubbed variant exists)
**Run date:** 2026-09-02
**Supersedes:** the 2026-09-01 22:42 critique set and `voice_critique_scene_04_valphine-sotorra.md` (09-02 09:39). **Every one of those was written against a narration that has since been re-rendered.** All eight `.md` files were regenerated between 07:50 and 09:59 on 2026-09-02.

---

## HEADLINE: the eight scenes were not rendered against one rulebook

Three different genre-rulebook versions reached Pass 5 across this one document:

| Digest | Lines | Scenes rendered under it | Provenance |
|---|---|---|---|
| `6e67c59f94b4` | 61 | **01** | = `HEAD:voice/_genre.md` (committed) |
| `5f211a965c9f` | ? | **02, 07** | an uncommitted intermediate — **not reconstructable** |
| `0a3d011c5f27` | 105 | **03, 04, 05, 06, 08** | = current working copy |

`voice/_genre.md` is dirty in git (+44 lines vs HEAD) and was edited *during* the render run — between 07:57 (scene 02) and 08:00 (scene 03). The 44 added lines are the ones that matter most to this critique: the **epigrammatic-closer ration**, the **`I file` ban**, the **three extra taxonomy shells**, and the **`yaml voice_lint` block**. Scene 01 certainly never saw them; scenes 02 and 07 may not have.

**This does not excuse the findings below.** Scene 04 — the worst offender for closers — rendered under the *current* rulebook and breached the ration anyway. But it does mean scenes 01/02/07 have not actually been checked against the rules you now intend to enforce.

**Fix before acting on anything else:** commit `voice/_genre.md`, then re-render 01, 02 and 07 so the whole document is rendered against one digest.

---

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `0a3d011c5f27`, 105 lines, 11,618 chars | `paths.genre_file` (config) — matches the run record for 03/04/05/06/08 only |
| Rulebook vs run record | **DIVERGENT — three digests across eight scenes; file dirty in git** | sha comparison, see above |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | read |
| Voice specs | `voice/{brewbarry,valphine,soma,vukradin}_new_pipeline.md` — all 4 resolved | `config/party.yaml` declarations |
| Per-char examples | `examples/{brewbarry,valphine,soma,vukradin}.md` — all 4 resolved | declared |
| Global examples | none — `shared_examples:` absent | correct; no cross-narrator bleed vector |
| Orphan voice/example files | **none** | every file in `voice/` and `examples/` is declared |
| Party doc | `docs/party.md` (37 KB) | `paths.party` |
| `voice_lint` | ran, **0 errors, 0 warnings, 0 notes** on both per-scene files and an assembled proxy | see caveat below |

### `voice_lint` caveat — a check that silently did not run

`voice_lint` segments a document on `## <Name> — <Scene>` headings. **Per-scene narration files have no such headings**, so its `bookkeeping` / convergence checks match nothing and it prints **zero notes** — indistinguishable from a pass. Verified with a canary: `### Soma` headings → bookkeeping silently skipped; `## Soma — A` headings → 3 errors fired.

Worked around here by assembling a proxy document with synthetic `## <narrator> — <scene_name>` headings from the frontmatter and linting that. **Result: genuinely clean, 0 errors.** No `I file`, no `the shape of`, no portable-tic hits anywhere in the document.

This is a `voice_lint` bug, not a Phandalin one: per-scene input should emit a `[skipped]` note rather than nothing.

---

## Budget ledger

**Scope:** whole document, 8 scenes, **4,943 prose words** (9,148 total; 54.0% prose).
**Budgets from:** `voice/_genre.md` @ `0a3d011c5f27`.

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| `the shape of` | 0 | ≤1 doc-wide | ok |
| `with the X of a man who` portrait | 0 | 0 | ok |
| `the way X do … when` | 0 | 0 | ok |
| `like-a-man-who` / `X-of-a-man` / `that-particular-X` / `the-kind-of-person-who` | 0 | 0 each | ok |
| `I file / I filed` — sections containing | 0 of 8 | ≤1 | ok |
| **Connective em-dashes in narration prose** | **0** | rulebook: never | **ok** |
| Trailing `—"` interruption assertions reaching narration | **0** | provenance-true only | ok (raw 2 → smoothed 3; **none propagated**) |
| **Epigrammatic closers — Valphine** | **~10** | ≤1 per narrator per session | **BREACH** |
| **Epigrammatic closers — Vukradin** | **~6** | ≤1 | **BREACH** |
| **Epigrammatic closers — Soma** | **~4** | ≤1 | **BREACH** |
| Epigrammatic closers — Brewbarry | 0 | ≤1 | ok |
| **Behavioral taxonomy (prose shells, read not scanned)** | **4** | 0 | **BREACH** |
| First-person present tense, all sections | 8 of 8 | all | ok |
| POV bleed | 0 | 0 | ok |
| Mock-archaic register | 0 | 0 | ok |

Two mechanical categories the rulebook is silent on and that are therefore *not checked*: adverb-heavy combat (no combat in this chapter) and symmetrical description (nothing matched by eye).

---

## Flags

### [1] Unattributed dialogue — 37 orphan quote runs, and scene 04 is unreadable

**Severity: highest. This is the chapter's dominant defect and it survived the 09-02 re-render.**

Scan C finds 37 runs of ≥3 consecutive quote-only paragraphs with no attribution and no action beat. After clearing legitimate tagged two-handers and one deliberate chorus, **at least 24 are real.** Distribution:

| Scene | Runs | Longest | Worst |
|---|---|---|---|
| 01 | 1 | 3 | cleared (framed two-hander) |
| 02 | 6 | 5 | **65–74** (5 lines, ≥4 speakers) |
| 04 | **12** | **9** | **125–142** (9 lines), **145–160** (8), **77–90** (7) |
| 05 | 2 | 3 | 67–72 |
| 06 | 1 | 3 | cleared |
| 07 | 8 | 6 | **197–208**, **233–244** (6 each) |
| 08 | 7 | 5 | **21–30**, **105–114**, **145–154** (5 each) |

Scene 04 lines 63–89 run 14 lines with a single tag, across at least three speakers (Toblen, Vukradin, and a third voice supplying *"One of those bangers. Play The Roc's Lament."*). Lines 211–219 are a four-voice wash with no tags at all. **This is the "incomprehensible" report from the last pass, unfixed.**

> “The problem with the small, or the dragon?”
>
> “Do we get paid if we kill the dragon?”
>
> “I'm told the dragons have hoards.”
>
> “People just don't understand.”
>
> “Yeah, you guys are all a little too materialistic, just robbing from each other. You know, boiled water is cheap.”

**Why:** four or more speakers with strict alternation broken and no beat between them; the reader cannot recover who is talking. It is a narration failure, not a dialogue one.
**Fix:** the attribution already exists in `scene_extractions_smoothed/NN_*.md`. Add speaker tags and action beats *around* the quotes; never change a word inside them. Where the smoothed layer says `UNKNOWN`, leave the line untagged — the narration already does this correctly in three places (*"Someone behind me admits,"* 02:25; *"someone says,"* 02:165; *"someone behind me says,"* 07:217) and those should stay.
**Recommendation:** scene 04 warrants a re-render with an explicit attribution directive; 02, 07 and 08 can be spot-tagged.

---

### [2] Epigrammatic closers — the ration is breached by every narrator except Brewbarry

The rule (added to the rulebook mid-run): *at most one abstract, balanced, thesis-like closer per POV narrator per session.* Observed ~20 across three narrators.

**Valphine (~10 — worst).** A doc-level cap breach is not ten defects, so here is the ranking:

**Keep one:**
> “Convenient. The dead lose their rights when their theology becomes distasteful.” *(07:87)*

It is the sharpest, most beat-specific, and it is exactly the "archivist of motive" verdict her spec licenses (`valphine_new_pipeline.md`: *"Long sentences must land in a clear verdict"*).

**Cut or render concrete — ranked most-generic first:**
- 04:143 *"This is government reduced to its essential components."* — abstract civics, no Valphine in it
- 04:161 *"Surface dwellers are so easily surprised by the obvious."*
- 07:117 *"Surface dwellers become exquisitely protective of differences once the similarities are spoken aloud."* — **this and the line above are the same generalization twice**; at most one survives
- 04:53 *"...surface economies often depend upon giving an ordinary act a ceremonial name."*
- 07:125 *"The accusation costs Norbus nothing. That is its elegance."*
- 07:187 *"A standard surface moral taxonomy: weapons become harmless when carried by agreeable strangers."* — also flag [3]
- 07:247 *"He weighs starvation against acid and reaches the conclusion hunger always purchases."*
- 04:31 *"Delight in a proprietor is merely appetite wearing clean clothes."* — also flag [3] and flag [4]

**Target: 2** (one per scene). Render the rest as the physical detail she is actually looking at — her spec's lens is power, leverage and concealed knives, which are *observations*, not maxims.

**Vukradin (~6):** 02:35, 02:95, 02:131, 02:143, 05:41, 05:59. Keep **02:95** (*"Everyone benefits except the dead people whose possessions are sitting in a monster's chest"*) — it is the chapter's moral spine and it is in his voice. Target: 2.

**Soma (~4):** 03:21, 03:61, 08:89, 08:101. Keep **03:61** (*"Some places mistake that for a plan."*) — it closes her survey of the town and earns its position. Target: 1–2.

**Brewbarry: 0.** Correct, and matches `examples/brewbarry.md`. No action.

---

### [3] Behavioral taxonomy — 4 instances, in shells `voice_lint` cannot see

The HARD BAN is on the *move*, not the wording, and all four walk past every regex in the rulebook's `extra_tics` block:

> “A standard surface moral taxonomy: weapons become harmless when carried by agreeable strangers.” *(07:187)*

**Why:** it names a class of people's behavior as a category instead of rendering what Valphine saw. It even calls itself a taxonomy.
**Suggested rewrite:** *"Norbus looks at my mace and decides it is furniture."*

> “Delight in a proprietor is merely appetite wearing clean clothes.” *(04:31)*

**Why:** taxonomizes proprietors as a class. Her lens is *this* innkeeper's motive, not the species.
**Suggested rewrite:** *"Toblen is delighted. He is also already counting."*

> “Surface dwellers are so easily surprised by the obvious.” *(04:161)*
> “Surface dwellers become exquisitely protective of differences once the similarities are spoken aloud.” *(07:117)*

**Why:** same move, twice, on the same class noun. The second also reads as the first one's sequel.

**This is the #245 result reproduced exactly: every mechanical scan returned zero, and the reading pass found the move four times.** The rulebook's `extra_tics` patterns are worth extending with a `<abstract noun>: <generalization about a class>` shell, but that belongs in `voice_lint`, not in a hand-edit here.

---

### [4] Cross-narrator convergence — the same clothing metaphor, two narrators

> **Vukradin (02:143):** “It is also a retirement fund wearing the hat of an orphaned-property office.”
>
> **Valphine (04:31):** “Delight in a proprietor is merely appetite wearing clean clothes.”

**Why:** identical construction — *institution/appetite* **wearing** *garment of respectability* — one narrator's frame reaching two POVs a scene and a half apart. This is the portable-tic family the bans exist for; it is invisible in a per-scene report, which is why both halves are quoted here.
**Fix:** keep Vukradin's (it is the payoff of his whole guard argument), cut Valphine's — which flag [2] and [3] also want gone.

---

### [5] Scene 05 — a reclassified exchange was cut in half

Lines 105–113 leave orphaned fragments of an exchange whose other half was reclassified as table speech in the trailing hatch:

> “Especially when we change the quest.”
>
> *(blank)*
>
> Soma pauses.
>
> “Trying. Yes.”

The hatch reclassifies *"Are you trying to say something?"* — but *"Trying. Yes."* was left in the narration, where it answers a question the reader never sees. Line 97, *“No, that we're his favorite group of players.”*, is real-player table speech that also survived.

**Why:** this is a scrub-boundary defect, not a voice one, but it reads as broken prose.
**Handoff:** `/scrub` — the reclassification needs to take both halves or neither.
**Note:** the surrounding *quest / quest board / quest marker / fetch quest* vocabulary is **canon** per `notes/scrub_register_policy.md` and must not be touched.

---

### [6] Quote typography is inconsistent across the document

| Curly `“ ”` | Mixed | Straight `"` |
|---|---|---|
| 01, 02, 04, 07 | 03 (6 curly / 10 straight) | 05, 06, 08 |

**Why:** these assemble into one chapter. Scene 03 changes style mid-scene.
**Fix:** normalize at assembly, not by hand-editing eight files. Also: scenes 05 and 08 each carry a stray triple-newline (05:109, 08:53).

---

### [7] Scene 08 is largely un-narrated table speech

Twenty-two of scene 08's quote lines are procedural table exchange with almost no narration between them — *"Is it a secret door?"*, *"East."*, *"Hit the door."*, *"Did we search in there?" / "Nothing of value." / "No signs of other exits or anything." / "No, no." / "Weird."* Line 83, *"Pile of ochre jellies falls on your heads. No."*, is GM speech rendered as in-fiction dialogue.

Soma's actual narration in this scene is good — the cover-blocks discovery at 155–165 is the chapter's best piece of deduction. It is buried under transcript.
**Recommendation:** re-render scene 08 with instruction to compress the door-by-door procedural into narration and keep only the load-bearing lines.

---

## Locked-dialogue anachronisms — GM scope call

Two, both inside verbatim quotes. **Neither is a defect; both need your ruling.**

**(a) Scene 08:131–135 — *The Princess Bride*.**
> “Okay, so you're trying to — mostly dead...” / “...is still alive.” / “That's right. Slightly alive.”

Dispositions: **keep** (a licensed table joke, and the narration does not launder it) · **replace in-world** · **annotate** with a Kostadinious the Sage marginal note. Precedent: Jimble the Unmoved, ch03 scene 07, GM-approved 2026-08-18.

**(b) Scene 08:25–27 — "everybody's a trope of some kind."**
Modern literary-critical vocabulary. Note that `notes/scrub_register_policy.md` makes *adventuring* metagame vocabulary canon — "trope" is arguably outside that class, arguably inside it. Your call.

---

## Reclassified table speech

Five hatches survive in the per-scene files. `assemble.py` strips them, so this is the last review point.

| Scene | Spans | Look, or rubber-stamp? |
|---|---|---|
| 03 | 5 | rubber-stamp — all clearly GM scene-setting |
| 04 | 2 | rubber-stamp |
| 05 | **10** | **look.** Ten spans is the largest hatch in the chapter, and it is the same scene whose reclassification was cut in half (flag [5]). Verify each half-exchange left the narration cleanly. |
| 07 | 7 | **look** — one span (*"Norbus, however, says — well, before you go any deeper…"*) is narrated back in at 07:215 as prose; confirm that is intended and not a double. |
| 08 | 0 | none — and scene 08 is the scene with the most un-reclassified table speech (flag [7]). The absence is itself the signal. |

Scenes 01, 02, 06: none.

---

## Per-scene grid

| Scene | Narrator | Prose words | Total | Prose share | Rulebook digest |
|---|---|---|---|---|---|
| 01 The Band Comes Together | Brewbarry | 624 | 835 | 74.7% | `6e67c59f` ⚠ |
| 02 The Gray Begins at the Wall | Vukradin | 683 | 1381 | 49.5% | `5f211a96` ⚠ |
| 03 First Sight of Phandalin | Soma | 693 | 883 | 78.5% | `0a3d011c` |
| **04 Ale and Rumors at Stonehill** | Valphine | 576 | 1586 | **36.3%** | `0a3d011c` |
| 05 Grave Robbers on the Quest Board | Vukradin | 639 | 1053 | 60.7% | `0a3d011c` |
| 06 The Hike to the Canyon | Brewbarry | 412 | 600 | 68.7% | `0a3d011c` |
| **07 The Dwarves Don't Believe Her** | Valphine | 787 | 1863 | **42.2%** | `5f211a96` ⚠ |
| 08 Secrets of the Buried Temple | Soma | 529 | 947 | 55.9% | `0a3d011c` |
| **Total** | | **4943** | **9148** | **54.0%** | |

Scenes 04 and 07 are the two thinnest and the two with the most orphan runs — the same defect measured two ways. Both are Valphine's.

---

## Verdict

Scene 04 is 64% raw transcript with twelve unattributed quote runs, one of them nine lines long, and it is the same failure the last critique reported before the 09-02 re-render — the re-render did not fix it. Re-render 04, 07 and 08 with an explicit attribution-and-compression directive rather than spot-editing; the epigrammatic-closer breach (~20 against a budget of 4) is a doc-wide cap and cannot be edited into compliance either. Before any of that, commit `voice/_genre.md` and re-render 01, 02 and 07, which were rendered against rulebook versions that did not contain the rules this report is enforcing.

Mechanically the chapter is genuinely clean: zero portable tics, zero connective em-dashes in narration prose, zero filing verbs, correct first-person present throughout, and zero false interruption assertions inherited from the smoothing layer.
