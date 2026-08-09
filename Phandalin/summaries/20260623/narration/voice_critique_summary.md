# Voice Critique Summary — session 20260623 (Chapter 46)

**Target:** `summaries/20260623/narration/*.scrubbed.md` (6 scenes, ~11,000 words)
**Specs:** `voice/<char>_new_pipeline.md` — authoritative, per `config/session_doc.yaml: voice_dir: voice`
**Supplementary:** `voice/v1/<char>_voice.md`, `voice/_genre.md`
**Examples:** `examples/{brewbarry,soma,valphine,vukradin}.md`

> ## ⚠ Second pass, 2026-08-09 — scenes 01 and 03 superseded
>
> Scenes **01** and **03** were re-rendered and re-scrubbed after this summary was written. Their rows in the table below and their entries under "Where to spend re-narration budget" are **stale** — see the current per-scene reports.
>
> **Scene 03's two structural findings are resolved.** The POV collapse (≈60 lines with no narrator) and the unattributed dialogue are both fixed; the re-render recovered speakers I had said a re-run could not recover. 1986 → 2661 words, em-dashes 30 → 20.
>
> **Scene 01 regressed on tics.** The banned taxonomising family did not go away, it changed surface form — `with the [X] of a man who…` became `that look X gets when…` and `had a way of X-ing`, now **7 occurrences in 1285 words**. It also newly introduced `the shape of it` (line 39).
>
> **New, and the priority item:** scene 03 line 139 calls Brewbarry "all five and a half feet." He is a **Goliath** (`docs/party.md:46`, `characters/brewbarry.md:5`), Path of the Giant — seven to eight feet — and scene 01 line 57 of this same session calls him "a giant of a man."
>
> Scenes 02, 04, 05 and 06 below are unchanged and still current.

| Scene | Narrator | Flags | Recommendation |
|---|---|---:|---|
| 01 Return to Phandalin | Brewbarry | 4 | Spot-edit |
| 02 A Hero's Welcome at Stonehill Inn | Valphine | 8 | **Blocked** — fix extraction first |
| 03 The Universal Basic Treasure Proclamation | Vukradin | 6 | **Re-narrate** — after attribution recovery |
| 04 Cheese, Business Plans, and Departure Preparations | Soma | 6 | Spot-edit |
| 05 Arrival in Neverwinter | Vukradin | 6 | Spot-edit |
| 06 The Exotic Armorer of Neverwinter | Brewbarry | 6 | Spot-edit (by deletion) |
| | | **36** | |

## Strongest recurring issue: GM table-narration locked inside character dialogue

**Nine occurrences — seven in scene 02, two in scene 06.** GM stage directions are sitting inside quotation marks as though characters spoke them:

> "Then he looks at Valphine and notices that she has the golden eyes. And is, for a moment, startled. Is that a condition?" *(02:87)*

> "And you immediately remember that that's exactly where you had gone to train to be a cleric of Lathander?" *(02:111)*

> "So he says: but Valphine, as much as I would like to do this for free and gratis…" *(06:51)*

The worst instance is `02:135`, where Valphine refers to herself in the third person *inside her own first-person narration*, because the GM's framing was assigned to her as speech.

**This is architectural, not a model failure.** Every `voice/<char>_new_pipeline.md` opens with eight constraints amounting to: *treat every substring between quotation marks as immutable*. That rule exists to protect player dialogue, and it works. But the upstream extraction quoted the GM's narration too — so the voice pass was **prohibited** from converting it, and faithfully passed it through. At `06:45` the model went further and invented a justification (`The proprietor did not hear it. Or pretended not to.`) for a line the GM said out-of-character.

Re-running `session_doc.py` will not fix these. The fix belongs in the extraction layer: GM stage directions must not arrive as quoted text. Until then, every voice pass will reproduce this.

## Second: banned tics from `voice/_genre.md` recurring at scale

Two constructions the genre doc bans **by name** account for 10 flags:

- **"the shape of X"** — 4 occurrences (`02:63`, `02:105`, `05:145`, `06:119`). Genre doc line 43: *"Never use. If you find yourself reaching for it, name the actual thing instead."*
- **"with the [Adj] [Noun] of someone who…"** — 6 occurrences (`02:43`, `02:47`, `02:63`, `04:37`, `04:95`, `04:161`). Genre doc line 44 calls it *"one Claude narrator wearing five hats"* — which is precisely how it presents: three in Valphine's scene, three in Soma's.

The costliest is `04:161`, where `the hunger of a woman who wanted something strange enough to be dangerous` replaces the physical tell that would have made Soma's suspicion of Linene land.

## Third: 102 narration-level em-dashes

| Scene | 01 | 02 | 03 | 04 | 05 | 06 | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Count | 8 | 13 | 30 | 10 | 30 | 11 | **102** |

Counts exclude em-dashes inside `"..."` and `*...*` (VTT-captured speech, correctly verbatim). The convention is also inconsistent within one pipeline run: scenes 02 and 04 use unspaced `word—word`, scenes 01, 03, 05 and 06 use spaced ` — `.

## Fourth: POV headings — ~~finding withdrawn~~, resolved in the opposite direction

> **Correction (2026-08-09).** The original finding said four scenes were missing a `### <Character Name>` heading per `voice/_genre.md` line 11, and that `assemble.py` used it to mark POV boundaries. **That was wrong.** `session_doc/assemble.py` lines 165–167 build the section header from frontmatter:
> ```python
> narrator = meta.get("narrator", "")
> header = f"## {narrator} — {scene_name}" if narrator else f"## {scene_name}"
> parts.append("---\n\n" + header + "\n\n" + body)
> ```
> The in-body heading is never read. The `narrator:` frontmatter field is correct in all six scenes, so assembly was never affected. The scenes that *had* the heading were the anomaly — they produced the narrator's name twice in the assembled output.
>
> Per GM ruling, `### Vukradin` (scenes 03 and 05) and `### Soma` (scene 04) were removed from their `.scrubbed.md` files. All six scenes now assemble identically. Reintroduce the in-body heading only if a scene ever carries more than one POV.

## Fifth: Vukradin's signature verdict register is absent from both his scenes

Spec: *"Verdict words: 'Foolish!' / 'Scandalous.' / 'Phonies!' / 'Nope.' / 'Done.'"*, and failure-prevention rule 9 names the verdict register as one of three things that **must** be present. A mechanical scan finds **none of them** in scene 03 or scene 05. Both scenes have long building sentences that drift into abstraction instead of landing — rule 8's exact failure mode.

## Two findings about the inputs themselves

**1. `"ever the X"` is inherited from the corpus, not drift.** It appears 8 times in this session's narration (`02:13`, `02:65`, `02:121`, `03:99`, `04:35`, `04:103`, `04:157`, `05:67`) — and in **three of the four example files**: `valphine.md:92` ("Vukradin, ever the pedant"), `soma.md:130` ("Vukradin, ever the loose pebble"), `vukradin.md:34` ("Brewbarry, ever the eager companion"). The pipeline is copying its own reference material. Note `ever the showman` is used of Vukradin in `02:13` and of Brewbarry in `05:67`, and `ever the pragmatist` of Brewbarry in `02:65` and of Valphine in `04:157` — the same epithets rotating across characters.

**Recommendation:** add `"X, ever the Y"` to the banned-tics list in `voice/_genre.md`. It will keep returning otherwise, because the examples teach it.

**2. `examples/soma.md` contradicts `voice/soma_new_pipeline.md`.** The Chapter 03, 04 and 14 passages are terse and dry — the spec's Soma. The Chapter 08 and 11 passages are lush and literary (*"its subtle shimmer hinting at its significance"*, *"impossible geometries"*, *"a hypnotic dance"*), which the spec forbids in failure-prevention rules 1, 5 and 10. The pipeline receives both and splits the difference. When Soma's narration drifts literary, it is obeying half its own inputs.

## Where to spend re-narration budget

1. **Do not re-run scene 02 yet.** Seven of its eight flags trace to quoted GM narration; a re-run reproduces them.
2. **Scene 03 is the one worth re-narrating** — roughly 60 lines carry no narrator at all. But lines 95–135 contain unattributed dialogue whose speakers are not recoverable from the narration, and a re-run will invent attribution rather than recover it. Pull speakers from the VTT first.
3. **Scenes 01, 04, 05 and 06 are spot-edits.** Scene 06's flags mostly resolve by *deleting* explanatory tails rather than rewriting.
4. **Cheapest high-leverage change:** add the two recurring tics to `voice/_genre.md`'s banned list and fix the em-dash convention. That is one file edit against 10 flags plus 102 em-dashes across future sessions.

## Also flagged for GM adjudication (not voice issues)

- `01:29` — *sheetment*, almost certainly a VTT garble of **impeachment**. Inside italics, correctly untouched.
- `04:127` — **"the Consumers' League"** referenced as an established body; not in `docs/` or the entity registry. Possible invented institutional detail.
- `05:117` — `"I'm gonna write that down on the quest tracker."` Table vocabulary inside locked dialogue. Today's scrub pass could not match it and the immutable-quote rule blocks the voice pass.
- `05:65` — `"Sam Club has found us."` Probable garble of *Sam's Club*.
- `02:105` — `"Well, yes, that's our next [stop]."` Bracketed reconstruction from the smoothed layer leaked into narration.

---

**These reports are review-only.** Nothing in the narration was modified. Where you accept a suggestion, apply it to the `.scrubbed.md` file, not the raw `.md`, so `assemble.py` picks it up.
