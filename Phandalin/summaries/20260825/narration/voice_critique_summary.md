# Voice Critique — Chapter 50 (session 20260825), all 8 scenes

**Input shape:** per-scene (directory of `session_doc_scene_*.md`)
**Narration read:** `.scrubbed.md` for scenes 01, 02, 04, 05, 06, 07, 08; raw `.md` for scene 03 (no scrubbed variant exists — the scrub run produced none).
**Review-only artifact.** No narration file was modified by the critique.

> **Applied 2026-08-31.** The GM triaged all nine findings as *Act on it*; **24 edits were applied**
> across six scenes and are recorded in `voice_fixes_20260825.md` — which also carries the warning that a
> future `/scrub` run would wipe them. Two corrections to this report: **finding [2]'s ordering claim was
> wrong** (the scene 06 block was already in its correct source position — the tense and the false `Earlier`
> frame were the real defects, and both are fixed), and the prose totals below are corrected from 6,704 to
> **5,704** — the per-scene figures sum to 5,704 and were themselves correct; the total was a transcription slip.
>
> **Amended 2026-08-31.** Scene 01 has since been **re-narrated on `claude-fable-5` and re-scrubbed** on the GM's instruction, which resolves finding [3] below. The prose table, finding [3] and finding [6] are updated; the codex-cli render and its critique are preserved as `*.codex-cli.bak`. See `voice_critique_scene_01_brewbarry.md` for the targeted re-critique and `scrub_manifest_20260825.md` for the re-render record.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | `paths.genre_file` in `config/session_doc.yaml`, confirmed by all 8 run records; 61 lines, 7,595 chars |
| Rulebook vs run record | **match** | every `*.knobs.json` carries `narration_genre_sha: 6e67c59f94b4`; recomputing `sha256(text.strip())[:12]` today gives `6e67c59f94b4`. The rulebook has not been edited since these scenes rendered (last commit `eae13bed`, 2026-08-12). Post-#276 shape — delivered as a delimited block, not a flattened `GENRE:` label. |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec — Brewbarry | `voice/brewbarry_new_pipeline.md` | **declared** `voice:` in `config/party.yaml` |
| Voice spec — Valphine Sotorra | `voice/valphine_new_pipeline.md` | declared |
| Voice spec — Soma | `voice/soma_new_pipeline.md` | declared |
| Voice spec — Vukradin | `voice/vukradin_new_pipeline.md` | declared |
| Per-char examples | `examples/{brewbarry,valphine,soma,vukradin}.md` | declared `examples:` in `config/party.yaml`, one each |
| Global examples | **none** | `config/party.yaml` declares no `shared_examples:` — nothing reached every narrator |
| Orphans | `voice/v1/` | not globbed by `voice/*.md`, declared by nobody — reaching no prompt |
| voice_lint | ran (`0` exit) | 0 errors, 0 warnings, 1 skipped check per file |

All four narrators resolved. Every register category below is live.

### Note on this skill's Phase 2 — it is describing a pipeline that no longer exists

The skill instructs the critic to mirror a three-rule voice lookup (exact name → first name → unique `<first>_` prefix). **That rule was deleted from the pipeline.** `session_doc/voice.py` and `session_doc/examples.py` now resolve by *declaration* — `config/party.yaml` names each character's `voice:` and `examples:` path, `get_voice_note` does an exact-name lookup with no prefix or similarity matching, and `sd_narrate` refuses to start when a declared spec is missing (feature 009; campaigns#175, #247, #300, #301). The first-name fall-through that used to build a GLOBAL examples block is gone too. Following the skill as written would have resolved Brewbarry to `voice/brewbarry.md` — a file that does not exist — via a rule the render does not use. Flagging so the skill can be corrected; the resolution above uses the live mechanism.

## Budget ledger

**Scope:** whole document, 8 scenes, 5,704 words of narration prose (verbatim `"…"`, `*…*` italics and `<!-- … -->` hatches excluded from every count below).
**Budgets from:** `voice/_genre.md` @ `6e67c59f94b4` and `base.md`.

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| connective em-dash | **0** | rulebook: never — interruption only | ok |
| `the shape of` | 0 | ≤1 doc-wide | ok |
| portable portrait (`with the X of a man who`) | 0 | ≤1 doc-wide | ok |
| behavioral taxonomy — `the way X <verb>s when/and …` | **8** across all 4 narrators | 0 | **BREACH** |
| behavioral taxonomy — class-as-explanation | **2** (both Valphine, scene 06) | 0 | **BREACH** |
| first-person present tense | 7 of 8 sections | always | **BREACH** (scene 06) |
| event ordering follows the extraction | 7 of 8 sections | always | **BREACH** (scene 06) |
| POV — one per section, no narrator third person | 8 of 8 | always | ok |
| recap framing | 0 | 0 | ok |
| generic fantasy reach / symmetrical description | 0 | 0 | ok |
| mock-archaic register | 0 | 0 | ok |
| bookkeeping / filing caps | — | — | *not checked — `voice/_genre.md` declares no ```yaml voice_lint``` block* |

The last row is `voice_lint`'s only output on this run, on every file: `[skipped] bookkeeping/filing checks — no ```yaml voice_lint block```. That is the "this campaign declares no filing register" cause, not a delivery failure — but it means the doc-level filing caps that catch fable's bookkeeping-repetition mode were **not evaluated by anything**. The manual count is in flag [4].

## Flags, doc-level, strongest first

### [1] Cross-narrator convergence — CONFIRMED

Two different narrators, two different scenes, the same sentence frame with the domain noun swapped:

> The argument lands. I feel it land, clean, the way a good swing lands and nothing gets back up.
> — scene 07 L103, **Brewbarry**

> I lean in with everything I have, and I feel it land clean, the way a phrase lands when the room stops chewing to listen.
> — scene 08 L129, **Vukradin**

**Why:** `base.md`'s HARD BANS name `"the way X do/does/say/says … when …"` as a banned *variant* of behavioral taxonomy, and the rulebook's gloss on the family is exact — "one Claude narrator wearing five hats." Here the hat-swap is visible in the diff: `I feel it land, clean, the way a ___ lands ___`, with `good swing` for the goliath and `phrase` for the bard. Neither character reached for this; the narrator did, twice, and dressed it per POV. This is also the fable "portable tic" mode — a construction that fits any narrator equally well is for that reason wrong for all of them.

**Suggested rewrite (scene 07, Brewbarry):** his spec is "short, declarative… very little space between feeling and acting," and the next three sentences already do the work perfectly ("Fabric is threads. Soft fabric is soft threads."). Cut the simile and let the flat statement carry it — *The argument lands. Nothing gets back up.*
**Suggested rewrite (scene 08, Vukradin):** keep the music register, drop the frame — *I lean in with everything I have, and the room stops chewing to listen.*

### [2] Rulebook conflict — scene 06 reorders session events, invents a chronology, and breaks tense — CONFIRMED

Scene 06 L87–L111 lifts eleven lines out of sequence, relabels them as a flashback, and renders them in past tense:

> Earlier, while we still pressed Lim, the calendar had been weighed. "We have a lot of stuff we have to do today, right? Tonight, we're supposed to have dinner with…" Vukradin had begun, and the name slid toward the wrong house before it was caught.

**Why — three separate rules, one passage:**

1. **Ordering.** `base.md`: *"CRITICAL: The actual events of the session must appear in the order they occur in the extracted moments. Do not reorder, move, or restructure session events — only the narrator's internal thoughts and memories may be non-linear."* This is external dialogue, not interior thought. In `scene_extractions_smoothed/06_planning_the_stakeout.md` the calendar/tea material sits at **lines 254–296** — *after* the stakeout planning at lines 105–141. The narration moves it to L87, ahead of material that in the source came first.
2. **A temporal claim the tape does not support.** "Earlier, while we still pressed Lim" places the exchange inside scene 05, in Lim's kitchen. The source has it in scene 06's own street conversation. The narrator authored a "when" that did not happen.
3. **Tense.** The rulebook: *"First-person present tense, always… If in doubt, first person, present tense."* Eleven lines of `said` / `asked` / `offered` / `I supplied` / `had been weighed`. `base.md` does ALLOW flashbacks — but for *the narrator's inner life*, which this is not.

**Suggested fix:** this one is not a sentence edit. Restore the block to its source position (after the rat-familiar planning at L85, before L113's "The delivery does not move until the third hour after midnight"), drop the "Earlier, while we still pressed Lim" frame, and put it back in present tense. Valphine's closing verdicts on it ("The distinction is not trivial…", "One learns, in the noble houses, to deliver assurance in exactly the tone that guarantees nothing") are strong and should survive the move unchanged.

### [3] Scene 01 is a transcript, not a narration — CONFIRMED, and it correlated with the backend — **RESOLVED 2026-08-31**

Scene 01 is **27% narration prose**. Every other scene is 52–67%.

| scene | narrator | total words | quoted | prose | prose % | backend |
|---|---|---|---|---|---|---|
| 01 | Brewbarry | ~~910~~ 1001 | ~~549~~ 469 | ~~**244**~~ **477** | ~~**27%**~~ **48%** | ~~`codex-cli`~~ `claude-code` / fable |
| 02 | Soma | 726 | 306 | 418 | 58% | `claude-code` |
| 03 | Vukradin | 1238 | 436 | 801 | 65% | `claude-code` |
| 04 | Valphine | 1245 | 546 | 700 | 56% | `claude-code` |
| 05 | Soma | 1336 | 638 | 695 | 52% | `claude-code` |
| 06 | Valphine | 1375 | 459 | 916 | 67% | `claude-code` |
| 07 | Brewbarry | 905 | 331 | 573 | 63% | `claude-code` |
| 08 | Vukradin | 2478 | 1116 | 1357 | 55% | `claude-code` |

`session_doc_scene_01_a_banker_s_revelation.knobs.json` records `"backend": "codex-cli"`. **All seven others record `"claude-code"`.** The one scene rendered by a different model is the one that did not narrate.

**Why it is a voice finding and not just a length one:** lines 61–149 run about forty consecutive quoted lines with no attribution and no interior at all. The rulebook licenses minimal tag lines ("often just a thought between the speech beats") — but there is no thought between these beats. Brewbarry's spec ("he feels something and then he acts… he notices fear in people the rest of the party misses… he notices loyalty at a level that surprises people") is invisible across the whole Bimble/Bimbo exchange. Where the section *does* narrate it is genuinely good and unmistakably him — "Bankers have armor too", "Friends do not rush friends", "He says my name like the contract was mine. Like I should feel the cut of it. / I do." — which is the evidence that the spec was delivered and the render did not use it.

**Suggested fix:** re-render scene 01 with `backend: claude-code` rather than editing it. This is not spot-editable — the missing material is the narration itself.

**Outcome.** Done on 2026-08-31 with `--backend claude-code --model claude-fable-5`, the scene-02 invocation with scene 01's parameters and identical in every other argument. Narration prose **244 → 477 words (31% → 48%)**, quoted lines 66 → 52, **attributed quoted lines 0 → 26**. The forty-line untagged block is gone. The run logs also confirm the cause: the GM tried codex-cli on scenes 01, 02 and 03, switched to fable, re-ran 02–08, and never went back for 01 — the file was a leftover from the abandoned attempt, not a considered render.

### [4] `the way X …` as a doc-wide simile frame — BREACH of the ledger row

Eight instances, in all four narrators' sections:

| scene | narrator | text |
|---|---|---|
| 02 L33 | Soma | the way you square up to a magistrate |
| 03 L37 | Vukradin | Still the way a lute peg is still |
| 04 L81 | Valphine | the way one holds a hot coal by choice |
| 06 L59 | Valphine | the way noble houses keep each other's secrets |
| 06 L71 | Valphine | the way a house understands shared poisonings |
| 07 L103 | Brewbarry | the way a good swing lands and nothing gets back up |
| 08 L129 | Vukradin | the way a phrase lands when the room stops chewing to listen |

(Scene 06 L21, "the way my mother taught me to assemble a rival house's supply lines," is **not** in this count — it names a specific person and a specific lesson, which is what the rulebook asks for. Keep it.)

**Why:** individually most are defensible; as a set they are the ban. `base.md` is explicit that the test is the move, not the wording, and that rotating the phrasing does not clear it. A frame that appears in every POV is by definition not any POV's.

**Suggested fix:** this is a cap breach, so it wants a budget, not seven rewrites. Keep the two strongest — 03 L37 (the lute peg is Vukradin's own instrument and does real work on the warforged) and 06 L21 — and convert the rest to direct statement.

### [5] Behavioral taxonomy — class as the explanation — PLAUSIBLE

> …because a party of surface dwellers will chase whatever glitters most recently, and someone must hold the thread.
> — scene 06 L17

> The surface dwellers perform this ritual of completing each other's jokes; I understand it as bonding, the way a house understands shared poisonings.
> — scene 06 L71

**Why:** `base.md` bans "every other appeal to a group's age, sex, class, or profession as the explanation for what one person just did." Both sentences explain what these four specific people are doing by what surface dwellers do.

**Why only PLAUSIBLE:** the rulebook pulls the other way — "Use the POV character's vocabulary for everything," "Valphine calls the surface 'the Overbright,'" "the POV character's frame is the only frame in their section" — and her spec makes her an "archivist of motive" who "reads people as systems." Drow-vs-surface *is* her lexicon. The line I would actually hold is that vocabulary is licensed but causation is not: calling them surface dwellers is hers; using "surface dwellers do this" as the reason a thing happened is the banned move. GM's call.

### [6] The `A [class] [verb]s [general truth]` aphorism frame — **CONFIRMED, cross-narrator** (upgraded 2026-08-31)

> A tortle who counts what leaves a building is a tortle worth listening to. (04 L25)
> A witness who drafts his own cross-examination. I could weep. (04 L59)
> A merchant whose costs do not twitch when the artery is severed was never drinking from the artery. (06 L21)

Originally logged as PLAUSIBLE and confined to Valphine. The fable re-render of scene 01 added two more instances in **Brewbarry's** voice, which makes it the same shape as flag [4]: one frame, every POV, the noun swapped. Six clear instances across three narrators:

| scene | narrator | text |
|---|---|---|
| 01 L31 | Brewbarry | A warrior checks his straps before battle. |
| 01 L139 | Brewbarry | A small-business woman knows how food moves in a city. |
| 03 L13 | Vukradin | A performer knows the difference between a joke that failed and a room that wasn't listening. |
| 03 L83 | Vukradin | A being who counts your days deserves to be addressed properly. |
| 04 L25 | Valphine | A tortle who counts what leaves a building is a tortle worth listening to. |
| 06 L21 | Valphine | A merchant whose costs do not twitch when the artery is severed was never drinking from the artery. |

**Why:** each narrator's spec licenses the *content* — Valphine's conclusions "arrive several steps ahead", Vukradin reframes for a living, Brewbarry maps the unfamiliar onto what he knows. None of them licenses one frame carrying all of it in three different mouths.

**The sharpest evidence is Brewbarry's**, because his examples file settles the register outright: when he generalises about a class of people he writes *"Order is bullies. They bully barbarians."* A fluent English aphorism is not his sentence, whoever else it might suit. 01 L139 is the one to cut; 01 L31 and 06 L21 are the two to keep.

### Not flagged, and why

- **Filing / ledger register.** `I file it` (04 L25), `I file the observation as accurate` (06 L15), `running the accounts` / `on the ledger` (06 L9), `adds an errand to his ledger` (06 L57), `I mark the day` (04 L23), `I tuck that away` (03 L45), `the ledger balances anyway` (08 L189), `the key files a complaint` (08 L205). This is fable's bookkeeping-repetition mode and nothing checked it — but both specs license it explicitly. Valphine is "an archivist of motive" who narrates "as if cataloging a specimen"; Vukradin "reaches for the ledger — coin returned, paperwork filed, receipts mailed — when he renders moral judgment." The register is right. The only thing I would touch is the literal verb `I file` twice, in 2 of Valphine's 2 sections — and "I file it" is flat office-English against a spec that says "elevated, aristocratic, with no modern slack."
- **Vukradin's music metaphors, scene 08** — five in narration prose (L129, L151, L167, L205, L301). His spec says "sparingly… not in every paragraph," but the scene is set on a stage during a performance, which is where it earns its place. L129 and L151 do the same job (a phrase landing / a chord sitting wrong) within 22 lines; if [1] is fixed, this resolves itself.
- **Prose that echoes the examples** — matching the writer's established voice is the goal.
- **Everything inside `"…"`** — verbatim, load-bearing.

## Scan A2 — trailing em-dash provenance

```
scene_extractions_new:      quote endings —"  0     (truncated) markers  111
scene_extractions_smoothed: quote endings —"  2     (truncated) markers  111
```

**Delta = 2**, both in `04_dining_with_lim_and_interrogating_bellows.md`:

| line | raw (`scene_extractions_new`) | smoothed (what the narrator read) |
|---|---|---|
| 173/174 | `"She goes, I… I just, I just, I just run… I just run a restaurant. I've got...` | `"She goes: I just— I just run a restaurant. I've got good suppliers, and—"` |
| 326/327 | `"She laughs in that way, turtles laugh, and says."` | `"She laughs in that way turtles laugh, and says—"` |

The second is a smoothing artifact worth naming: the raw capture ends in a **full stop**, and the smoothed layer converted it to an assertion that the speaker was cut off. Nobody speaks over her.

**Neither reached the narration** — `grep` for both strings in `session_doc_scene_04_*.md` returns nothing. Finding closed at the extraction layer; no adjudication needed against the tape, and nothing to fix in the narration.

Worth noting for contrast with ch48: this smoothing run left all 111 `(truncated)` markers in place, where ch48's stripped 57 down to 1. Different behaviour, much smaller blast radius.

## Locked-dialogue anachronisms — GM scope calls, not flags

Player speech the critique must not rewrite. Three dispositions each: **keep**, **replace in-world**, **annotate** (`*Marginal note in a later hand: … — Kostadinious the Sage*`). The scrub run already ruled on the economics vocabulary and on `cosplaying`; these are what remains.

| scene | line | text | note |
|---|---|---|---|
| 06 | 67, 71 | `"Hashtag,"` … `"Not all were-rats,"` | a Twitter construction, and the only one in the doc that nothing in-fiction absorbs. Strongest annotate candidate. |
| 08 | 43, 45 | `"A, B, C." / "Always be closing,"` | Glengarry Glen Ross. Sits inside the licensed economics register, which argues for keep. |
| 08 | 309 | `"That's the great thing about more cowbell." / "Works on any song. Universally."` | SNL. **Partly self-covering already** — Soma's next line, "the Nine Hells Chorale did not need more cowbell," does the in-world work for free. |
| 08 | 313 | `"I thought we were heavy metal."` | genre name; replace-in-world is cheap here if wanted. |
| 06 | 65 | `"100%,"` | modern idiom rather than a reference. |
| 07 | 57, 63 | `"Call him Yoko and move on,"` → `I do not know who Yoko is. Probably somebody else who wrote about soup.` | **self-covering — keep.** The narration has already absorbed it in Brewbarry's voice, and the joke is better for it. |

Per the scrub run's standing rulings, **no action**: `fair trade` / `organic` / `supply chain` / `marketing` / `revenue share` / `front-end points` / `net`/`gross` / `image and likeness` / `perpetuity` (the campaign's premise, not residue), and `cosplaying` (ruled in-canon).

## Reclassified table speech

Six hatches, one per scene, in scenes 01, 02, 03, 05, 07, 08. Scenes 04 and 06 have none. `assemble.py` strips these at assembly, so this is the last review point.

| scene | spans | what was pulled |
|---|---|---|
| 01 | ~25 | the largest by far — GM second-person address, the `"I mean, literally, you intimidated him with an intimidation check."` mechanic, the B-I-M-B-L-E spelling bit, and the GM's own aside about names that cannot be twisted |
| 02 | 1 | `"21 Insight."` — a bare roll result; correctly out |
| 03 | 12 | `"Kmart!"`, `"…putting these on YouTube"`, `"sending him to Claude to transcribe"`, `"It's an Airbnb."` ×2 — every hard real-world anachronism in scene 03 left through this hatch rather than the scrub |
| 05 | 1 | a GM restatement of Brewbarry's approach to Lim |
| 07 | 8 | `"…in Discord"` ×2, `"Where's Bayard with his natural 20…"` |
| 08 | 2 | `"So her response is: your usual fee."`, `"I start towering over her, and I'm like:…"` — both third-person self-description inside quotes |

Two of these are worth an explicit GM eye rather than a rubber stamp: **scene 01's**, because 25 spans is a large scope call made by the model on the one scene that also under-narrated, and **scene 03's**, because it is doing anachronism removal that the scrub pass never saw.

## Verdict

~~Scene 01 is not narration — 27% prose against a 52–67% band, forty consecutive untagged quoted lines, and it is the only scene in the run with `"backend": "codex-cli"` in its run record; re-render it on `claude-code` rather than editing it.~~ **Done — scene 01 was re-narrated on fable and re-scrubbed on 2026-08-31; prose 31% → 48%, attributed quoted lines 0 → 26.** With that resolved, the two remaining defects are doc-level and not spot-editable: the `I feel it land, clean, the way a ___ lands` frame appears in both Brewbarry's and Vukradin's sections with only the noun changed, and scene 06 frames eleven lines of its own conversation as a flashback to Lim's kitchen and shifts to past tense to do it. (An earlier version of this line also claimed the block had been reordered; it had not — see `voice_fixes_20260825.md`.) The rulebook reached the model intact and undrifted, all four specs resolved, and the narration's cleanest result is the one the rulebook is strictest about: zero connective em-dashes in 5,704 words of prose.
