# Voice Critique — Chapter 8, DGX narration (6 scenes)

**Narration:** `summaries/20250812-chapter-08/narration_dgx/session_doc_scene_*.md`
**Input shape:** per-scene (directory). No `.scrubbed.md` exists for any scene — the
`/scrub` run was stopped at the proposal stage — so every critique target is the raw
`.md`, which is correct fallback behaviour, not a miss.
**Render:** `sd_narrate --backend dgx`, `deepseek-ai/DeepSeek-V4-Flash-0731`, 2026-09-04.

---

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `7a848f23addaf266` — 105 lines, 11,681 chars | `paths.genre_file` in `config/session_doc.yaml`. Post-#276 file form. |
| Rulebook vs run record | **no `.knobs.json` written by this run** | Provenance instead comes from the invocation itself: this session ran `--narration-genre-file voice/_genre.md`, so the rulebook was delivered as a delimited block, not a flattened `GENRE:` label. Not the flattening failure mode. |
| Retired `narrate.genre` key | absent | config is migrated |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | read at run time |
| Voice specs | all 4 declared and present — `voice/{vukradin,soma,valphine,brewbarry}_new_pipeline.md` | `config/party.yaml` declarations (feature 009) |
| Per-char examples | all 4 declared and present — `examples/{vukradin,soma,valphine,brewbarry}.md` | roster declarations |
| Global examples | none | `shared_examples:` empty |
| Orphans | `voice/v1/` (a directory nothing declares) | reaches no prompt |
| Party doc | `docs/party.md` | prose roster |
| `voice_lint` | **ran** — 3 ERROR, 0 warn, **1 `[config]` note** | see below |

### The `voice_lint` note is a check that did not run

```
note   [config] unrecognised voice_lint key 'extra_tics' — ignored
```

`voice/_genre.md` declares four campaign-local taxonomy patterns under `extra_tics`,
derived by scanning ch40–48 and documented as having zero false positives on that
corpus. **The installed `voice_lint` does not recognise the key and silently skipped all
four.** That is not a pass — it is four rules the campaign wrote down and the tool did
not evaluate.

I ran them by hand. They found a real breach the tool missed:

> …standing there in his silence **like a man holding up a roof**.
> — scene 03, Brewbarry

`like-a-man-who`, declared `cap: 0`. This is the behavioral-taxonomy family that
`base.md` bans as a *move* — comparing the observed thing to a generic class of person
instead of naming what was seen.

**This is a tooling finding, not a campaign one, and it affects every `/voice-critic`
run in this workspace until `voice_lint` learns the key.**

---

## Budget ledger

**Scope:** whole directory, 6 scenes, 5,277 prose words (dialogue excluded).
**Budgets from:** `voice/_genre.md` @ `7a848f23addaf266`

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| `the shape of` | **3** (s01 ×2, s04 ×1) | 0 doc-wide | **BREACH** |
| `with the X of a man who` | 0 | 0 | ok |
| `the way X do … when …` | 0 | 0 | ok |
| `like-a-man-who` | **1** (s03) | 0 | **BREACH** — *found by hand; `voice_lint` skipped it* |
| `X-of-a-man (no who)` | 0 | 0 | ok — *by hand* |
| `that-particular-X-she-gets-when` | 0 | 0 | ok — *by hand* |
| `the-kind-of-person-who` | 0 | 0 | ok — *by hand* |
| bookkeeping `I file / I filed` | 0 | banned outright for all 4 narrators | ok |
| connective em-dashes | **62** of 63 total | rulebook: **never** as a connective | **BREACH** |
| first-person **present** tense | 5 of 6 scenes | all scenes | **BREACH** (scene 01) |
| epigrammatic closers | not counted | ≤1 per POV per session | *not checked — requires whole-session scope; this is one chapter* |
| recap framing | 0 | banned | ok |

---

## Flags

### [1] Rulebook conflict — scene 01 is in the wrong tense (whole-scene)

`voice/_genre.md`: *"**First-person present tense, always** ("I", "we") — the scene
unfolds as it happens... Never drift into third person... If in doubt, first person,
present tense."* It explicitly names past tense in older examples as *"legacy drift, not
the standard."*

> "She can sing," I **said**. "She can sing all she wants." The words **came** out lighter than I meant, almost giddy, because this **was** the whole argument — my entire philosophy, rendered as a tactical fact.

Past-tense verb markers per scene: **s01 = 72**, s02 = 9, s03 = 1, s04 = 6, s05 = 6, s06 = 6.
Scene 01 is past tense throughout; the other five are present.

**Not spot-editable.** This is a whole-scene rewrite — re-render with
`sd_narrate --scene 1`.

### [2] Rulebook conflict — 62 connective em-dashes (doc-wide)

`voice/_genre.md`: *"Em-dash **only** for interrupted speech or interrupted thought —
never as a connective. If a comma, colon, or period would join the two halves, use that
instead. A dash between two complete clauses is the flattening habit, not the device."*

63 em-dashes in narration prose; **62 are connective or appositive**, 1 is an
interruption.

> Soma had put it plainly enough **—** a couple of people had gotten charmed before we even knew what was happening.

> …because the silence cuts both ways **—** it's a wall, and walls have doors only if you build them.

**This is a doc-wide cap breach and it is not 62 defects.** Do not commission 62
rewrites. The parenthetical pairs (`One of the harpies — the singer, the one who'd
started all this — hung there`) are the most defensible and read least like the
flattening habit; the clause-joining ones are the actual breach. **Recommended target:
keep at most 2 doc-wide, convert the rest to comma/colon/period.** That is a re-render
signal, not an edit pass.

### [3] HARD BAN — `the shape of` ×3 (doc-wide, cap 0)

> …and I felt **the shape of** it take hold — the world going soft-edged and muffled beyond the boundary… *(s01)*

> **The shape of** this fight was forming. *(s01)*

> Vukradin decides, Soma describes **the shape of** it *(s04)*

`base.md` bans this as a *move*, not a wording, so rotating the phrasing does not clear
it. **Keep none.** Each is doing work a concrete observation would do better — s01's
second instance in particular is the narrator summarising the tactical situation, which
is adjacent to the recap-framing ban.

### [4] HARD BAN — behavioral taxonomy, scene 03

> He takes it, standing there in his silence **like a man holding up a roof**.

`base.md`: *"If a sentence explains an observed behaviour by generalising it to a class
of people — men, women, they, people, that age, anyone who — that is this ban, whatever
shell it arrives in."*

**Suggested rewrite** *(grounded in `examples/brewbarry.md`, which has him in short
declaratives — "Order is bullies. They bully barbarians.")*:
> He takes it. He does not move. The silence sits on him and he holds.

### [5] Out-of-fiction intrusion — the narrator describes the table (scenes 01, 02, 05, 06)

Not a style flag: the POV character is narrating the game session rather than the
fiction. `voice/_genre.md` requires the POV character's frame to be *"the only frame in
their section."*

| Scene | Text |
|---|---|
| 01 | `"I put the 20-foot radius **on the screen** there for you"` |
| 01 | `And then the number landed and I felt the whole **table** flinch.` |
| 02 | `"Public roll," I announce, to nobody in particular. **The table knows what I mean.**` |
| 05 | `**Gary's voice cuts across the table** — not Valphine, not anyone in the fiction.` |
| 06 | `And then the **DM's internet** dies.` / `The bear **token** vanishes off **the board**.` / `His house on **Santorini**… **industrial router**… **DHCP**` |

The scene-05 instance is the worst — a **real player's name** inside first-person
narration, with the break from fiction stated outright. It is a *tooling* miss as well:
`find_residue.py --party-md` loaded only full names (`Gary Young`), so the bare `Gary`
matched nothing, and two of five roster members did not load at all because
`load_player_names` requires a literal `Player: X` prefix that `docs/party.md` does not
use.

**These belong to `/scrub`, not to a voice fix.** Listed here because that run is
unfinished and this is the record that they exist.

### [6] The GM was renamed, not removed — `the world` ×15 (scene 01: 12)

Downstream of `--prose-mode`. The unsteered run used `the world` 4 times; the steered
run uses it 15.

> "All right," **the world conceded**, in that voice it uses when it's been outmaneuvered.

> But the GM — no, **the world**, the world had only put one harpy **on the board** so far.

> — barely ten feet away, **the world confirmed**, well inside my range.

The second quote is the substitution happening mid-sentence in finished prose. This is a
personified game-master with a new name, and `on the board` survived alongside it.

**No scanner can catch this.** `find_residue.py` matches numbers, fixed table-speak
phrases and player names; vocabulary matching is forbidden by the scrub skill's hard
invariant. If it is to be caught in future runs it needs an explicit entry in
`notes/scrub_register_policy.md`.

### [7] Unattributed dialogue — 5 orphan quote runs, 4 of them in scene 05

| Scene | Lines | Run length |
|---|---|---|
| 01 | 93–100 | 4 |
| 05 | 25–30 | 3 |
| 05 | 47–58 | 6 |
| 05 | 73–78 | 3 |
| 05 | 105–114 | 5 |

Scene 05 carries 60 quoted spans against 759 prose words — by far the highest dialogue
density in the chapter, and the prose is not doing enough to say who is speaking. The
s05 47–58 run cycles **three** speakers, so alternation does not identify anyone.

**The fix is cheap and non-destructive: the attribution already exists upstream.**
`scene_extractions/05_exploring_the_tower_of_storms.md` labels every one of these,
including the GM-reattributions and Gary→Valphine/Brewbarry rulings settled in the Stage 2
pass. Add speaker tags and action beats **around** the quotes; never change a word inside
them.

### [8] Tell-not-show — `I felt / I feel the X` (7 instances)

> and **I felt the ledger in my head start to run** — what we had, what they had… *(s01)*

> **I feel for the rage** — the familiar heat, the thing that has carried me… *(s03)*

Low severity, and some are defensible: s02's `I feel her thrash, the strength going out
of her wings` renders rather than names. Flagged as a cluster, not eight rewrites.

---

## Per-scene prose density

| Scene | Narrator | Prose words | Quoted spans | Notes |
|---|---|---|---|---|
| 01 | Vukradin | 1,065 | 65 | past tense; 12× `the world`; 2× `the shape of` |
| 02 | Soma | 1,019 | 41 | strongest scene |
| 03 | Brewbarry | 736 | 10 | `like-a-man-who` breach; thinnest dialogue |
| 04 | Valphine Sotorra | 942 | 34 | 1× `the shape of` |
| 05 | Vukradin | 759 | 60 | 4 orphan runs; player name |
| 06 | Soma | 756 | 31 | DM-outage block |

---

## Locked-dialogue anachronisms — GM scope call

These sit inside verbatim `"…"` and were **not** flagged. They are the GM's decision,
with three dispositions each (keep / replace in-world / annotate per the sage's-marginal-note
convention — Phandalin's persona is **Kostadinious the Sage**).

| Scene | Quote | Note |
|---|---|---|
| 06 | `"Losing you, Kostadis. The tubes are clogged. It's a series of tubes. Switch to the truck, man."` | The Ted Stevens "series of tubes" line. Real-world political reference; the GM's real name also appears. |
| 06 | `"Not the DHL connections, the VPN? No, no. The word was DHCP."` | Modern networking. Partially self-covering — the narration answers it with `I have no idea what a DHCP is.` |

Existing policy (`notes/scrub_register_policy.md`) rules **named real-world entities** as
residue and **self-covering references** as usually keep, so these pull in opposite
directions. Not resolved here.

---

## Reclassified table speech

**None.** No `<!-- table-speech reclassified: … -->` hatch appears in any of the six
scenes. Given the volume of table material that *did* reach the prose (flag [5]), the
absence is worth noting: the reclassification pass either did not fire or did not run
under this backend.

---

## Verdict

Scene 01 is the chapter's problem and it is not spot-editable: wrong tense throughout,
both `the shape of` breaches, and 12 of the 15 `the world` euphemisms — one scene
carrying three separate rulebook failures. Re-render it (`sd_narrate --scene 1`) rather
than editing it. The doc-wide 62-connective-em-dash breach is also a re-render signal,
not an edit pass. Scenes 02–06 are in-voice and largely sound; their remaining problems
are out-of-fiction intrusions that belong to the unfinished `/scrub` run, not to voice.

Separately and independently of the narration: **`voice_lint` silently skipped four rules
this campaign wrote down**, and one of them was breached.
