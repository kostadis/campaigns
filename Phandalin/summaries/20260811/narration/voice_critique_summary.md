# Voice Critique Summary — Session 20260811 (ch48), scenes 01–08

**Narration dir:** `/home/kroussos/campaigns/Phandalin/summaries/20260811/narration/`
**Input shape:** per-scene (8 files, no `.scrubbed.md` variants exist — raw `.md` used for every scene)
**Scenes:** 01 Brewbarry · 02 Valphine · 03 Vukradin · 04 Soma · 05 Soma · 06 Vukradin · 07 Brewbarry · 08 Valphine

---

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record (`*.knobs.json`, post-#276); 61 lines, 7547 chars |
| Rulebook vs run record | **match** | recomputed `sha256(text.strip())[:12]` = `6e67c59f94b4`; all 8 scenes carry the identical digest — the rulebook has not been edited since this render, and no scene diverges from its siblings |
| Config vs run record | **match** | `config/session_doc.yaml → paths.genre_file: voice/_genre.md`; no retired `narrate.genre` key present |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4221 chars |
| Voice specs | `brewbarry_new_pipeline.md`, `soma_new_pipeline.md`, `valphine_new_pipeline.md`, `vukradin_new_pipeline.md` | rule (c) — unique key beginning `<first>_`; all four resolved, none ambiguous |
| Per-char examples | `brewbarry.md`, `soma.md`, `valphine.md`, `vukradin.md` | stem == first name; one file per character |
| Global examples | none | every file in `examples/` routes to a narrator |
| Party doc | `docs/party.md` | roster 4/4 PCs parsed (+ Boney as NPC companion) |
| voice_lint | ran (exit 0) | 0 errors, 0 warnings, **1 skipped check per file** |

**voice_lint skip, verbatim:** `[skipped] bookkeeping/filing checks — voice/_genre.md has no \`\`\`yaml voice_lint block. Not the same as clean: nothing was checked.` This is skip-cause (3): the rulebook genuinely declares no filing register for Phandalin. It is a real *not-checked*, not a pass, but it is not a finding about the run.

---

## Budget ledger

**Scope:** whole session, scenes 01–08 (all 8 per-scene files)
**Budgets from:** `voice/_genre.md` @ `6e67c59f94b4` + `base.md` HARD BANS

Phandalin's rulebook states **absolute prohibitions**, not numeric caps — "Never use", "only … never as a connective". The ledger reflects that: the budget for a banned move is 0, not ≤1.

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| `the shape of X` | 0 | rulebook: never | ok |
| `with the [Adj] [Noun] of someone who…` | 0 | rulebook: never | ok |
| `ever the X` / `had a way of X-ing` / `that look X gets` | 0 | base.md: never | ok |
| **Behavioral taxonomy — all shells** | **4** | base.md HARD BAN: 0 | **BREACH** — *resolved, see Resolution* |
| Connective em-dashes (prose) | 0 | rulebook: never as a connective | ok |
| First-person present tense | 8 of 8 sections | rulebook: always | ok |
| Third-person drift | 0 | base.md: hard failure | ok |
| Narrator editorializing / recap framing | 0 | rulebook + base.md: never | ok |
| Generic fantasy reach | 0 | rulebook: never | ok |
| Symmetrical description / mock-archaic register | 0 | rulebook: never | ok |
| Bookkeeping / filing caps | — | — | *not checked — rulebook declares no `yaml voice_lint` block* |

### Em-dash detail (Scan A)

68 em-dashes in the eight files; **66 sit inside verbatim `"…"` dialogue** — VTT-captured interruption, which is exactly the licensed use and is not flaggable regardless. Only **2 occur in narration prose**, and they are a matched parenthetical pair in scene 05 (`…his agent — he points at the man dangling from Brewbarry's grip — can provide…`), which is interrupted thought, not a connective joining two complete clauses. **No breach.** This is a clean result on the axis that usually fails.

---

## The one systemic finding

**Behavioral taxonomy — 4 instances, all in the `the way X do/does Y` shell.** This is `base.md`'s HARD BAN ("banned as MOVES, not as wordings … every other appeal to a group's age, sex, class, or profession as the explanation for what one person just did"), and Phandalin's own rulebook restates it as *"one Claude narrator wearing five hats."*

| Scene | Narrator | Sentence fragment |
|---|---|---|
| 02 | Valphine | `He looks up at Brewbarry the way novices look at altars.` |
| 02 | Valphine | `a banker will sign in public what he would delay in private` |
| 05 | Soma | `staring at the skeletal horse the way people do the first time` |
| 08 | Valphine | `Cullen is enjoying himself, the way a fencing master enjoys an enthusiastic student.` |

**Three of the four are Valphine's**, which is where the re-narration budget should go. Her spec licenses aristocratic generalisation ("She reads people as systems of motive") and that pull is visible — but the ban is on the move regardless of who makes it, and the fix is local: name the observed thing (the hands, the pause, the word chosen) and stop.

**voice_lint returned 0 errors on all four.** Its regex for this family requires a trailing `when …` clause, which none of these have. This is the skill's "scans are a floor, not a ceiling" case, confirmed on live output — the reading pass found what the mechanical pass could not.

Six comparable `the way X` constructions were checked and **cleared**, because they compare against the *narrator's own* experience rather than generalising a class: `he carries it the way I carry the halberd` (01), `the way I used to open clams for hatchlings` (04), `the way you lift a hatchling out of the surf` (05), `the way nothing honest holds still` (05), `the way other people distrust dark alleys` (06), `the way a vintner knows a corked bottle` (08).

---

## Not flagged — and why

Two sentences that a naive pass would flag are **spec-licensed and correct**:

- Scene 02, `Surface dwellers are so easily surprised by the obvious.` — appears **verbatim** in `valphine_new_pipeline.md` line 50 as an exemplar of her vocabulary. The render is obeying its spec.
- Scene 06, `I own a fourth-level slot that can turn a man into a different man` — `base.md` AVOIDs mechanical detail, but the campaign rulebook explicitly overrides ("Drop hit points, distances, spell names directly into prose") and `vukradin_new_pipeline.md` line 44 makes procedural mechanics his precision register. Correct as written.

---

## Table-speech reclassification — review queue

| Scene | Hatch present | Assessment |
|---|---|---|
| 01 | yes (3 spans) | ok |
| 02 | yes (2 spans) | ok |
| 03 | **none** | ok — no table speech detected in the prose |
| 04 | yes (9 spans) | ok — Cambion/Moriarty table debate correctly pulled |
| 05 | yes (18 spans) | ok, with residue — see below |
| 06 | **none** | **MISS — see below** |
| 07 | **none** | ok — no table speech detected in the prose |
| 08 | yes (28 spans) | ok — all roll-calling correctly pulled |

**Scene 06 is the miss.** It carries no reclassification hatch at all, and six lines of pure dice-mechanics table talk are live in the narration as in-fiction dialogue (`"You know, 13 investigations…"`, `"20 insights, and then…"`, `"20… wait, what? I think double rolls."`, `"You got a 9 perception?"`, `"Looks like I had a 9 perception."`, plus the narration line `"We're going with the Insight roll." That's not favoritism, that's methodology.`). Scene 08 correctly hatched exactly this class of line. **GM decision required** — this is a scope call the pass failed to make, and it is the last point at which it is visible, because `assemble.py` strips hatches.

**Scene 04, minor:** `"Okay, what are… we're level 7?"` and `"We're about to be level dead, that's fine."` are the same class, un-hatched. The second reads as an in-fiction joke; the first does not.

**Scene 05, GM's call:** `"this isn't Houston, Texas"`, `"as they say on Mandalore"`, `"Boney's a Zoomer"` survived the hatch that correctly caught the camera-zoom and demonetization asides. Given the rulebook's explicit licence for absurdist comedy — and that the campaign keeps `Oral B. Vance`, `SystemD of Neverwinter` and `Chinese wall` — these are plausibly intentional. Flagged for a decision, not as an error.

---

## Render defects (not voice findings)

1. **Scene 03, line 119 — duplicated span.** `"The employees were paid," Valphine says, counting it"The employees were paid," Valphine says, counting it off on her fingers.` A clause is emitted twice with no separator. Needs a manual fix regardless of any voice decision.
2. **Scene 01, line 77** — `"Okay. Alright, this is Brewbarry'smoment. Go for it."` missing space (inside verbatim dialogue).
3. **Scene 08, line 79** — `"It's much safer withus."` missing space (inside verbatim dialogue).
4. **Scene 03, line 67** — `the fairest income distribution scheme in the Dessarin Valley`. Phandalin sits in the Sword Coast North, not the Dessarin Valley. Out of scope for this skill — worth a `/consistency-check` pass.

---

## Verdict

The one breach is behavioral taxonomy, four instances, three of them Valphine's — a local sentence-level fix, not a re-render signal. Everything the rulebook prohibits absolutely is otherwise clean, tense and POV are compliant across all eight sections, and the em-dash budget that usually fails is met with two prose dashes, both legitimate interruptions. The higher-priority item is not a voice problem at all: **scene 06 shipped with no table-speech hatch and six lines of dice-roll talk still in the fiction**, and scene 03 carries a duplicated clause.

---

## Resolution

*Appended after the fixes were applied. The findings above are preserved as written at critique time; this section records what was done about them.*

**Behavioral-taxonomy BREACH — cleared.** All four instances rewritten into `.scrubbed.md`, sources untouched:

| Scene | Before | After |
|---|---|---|
| 02 L129 | `He looks up at Brewbarry the way novices look at altars.` | `He looks up at Brewbarry and does not blink, and his hands go still at his sides.` |
| 02 L101 | `…; a banker will sign in public what he would delay in private.` | `…; the man who built his refusal out of arithmetic signs it away with the whole floor watching him do it.` |
| 05 L135 | `…staring at the skeletal horse the way people do the first time.` | `…staring at the skeletal horse, Perrin's mouth open, the fixer gone still in Brewbarry's grip.` |
| 08 L31 | `Cullen is enjoying himself, the way a fencing master enjoys an enthusiastic student.` | `Cullen is enjoying himself; he lets the pat land, and he does not step back from it.` |

**Render defect 1 — fixed.** Scene 03 L119 duplicated clause de-duplicated to `"The employees were paid," Valphine says, counting it off on her fingers.`

**Two corrections to this report's own suggested rewrites**, both caught during application:

1. Scene 02 L101's suggestion said *"spent an hour building a refusal"* and *"forty people watching"*. The scene states neither a duration nor a head-count; both were fabricated detail. The applied text anchors to what the scene does establish — the page of cramped figures, and the crowd already described as "clerks, clients, the idle wealthy."
2. Scene 05 L135's suggestion — *"the fixer's weight already going back onto his heels"* — **is physically impossible at that moment.** Brewbarry takes the fixer by the neck at L111 and L177 has him "dangling from Brewbarry's grip"; the boot-and-weight read at the scene's open is of *Perrin*, not the fixer. The applied text keeps Perrin's mouth open and renders the fixer still inside the grip he is actually held in.

**Verification across the effective assembly set** (scrubbed where present, raw otherwise — scenes 01 and 07 have no scrubbed variant and need none):

- Diffs: 5 lines modified total, **0 added, 0 removed**; no change inside `"…"` dialogue or any `<!-- -->` hatch.
- Banned constructions: 0 hits. The 7 surviving `the way X` constructions are the ones cleared in this report as narrator's-own-experience comparisons.
- `voice_lint`: 8/8 files at 0 errors, 0 warnings (1 expected bookkeeping `[skipped]` note each).
- `find_residue.py`: candidate_count 0 on all 8.
- Em-dash: the sole prose-adjacent dash in a rewritten line is pre-existing verbatim dialogue (`"So, Cullen, my good friend—"`).

**Still open — not addressed here:** render defects 2 and 3 (`Brewbarry'smoment`, `withus`, both inside verbatim dialogue) and the Dessarin Valley geography question, which belongs to `/consistency-check`. Scene 06's table-speech miss was handled separately by `/scrub`.

---

## Per-scene reports

- `voice_critique_scene_01_brewbarry.md` — 0 flags
- `voice_critique_scene_02_valphine.md` — 2 flags
- `voice_critique_scene_03_vukradin.md` — 0 flags (1 render defect)
- `voice_critique_scene_04_soma.md` — 0 flags
- `voice_critique_scene_05_soma.md` — 1 flag
- `voice_critique_scene_06_vukradin.md` — 0 flags (table-speech miss)
- `voice_critique_scene_07_brewbarry.md` — 0 flags
- `voice_critique_scene_08_valphine.md` — 1 flag
