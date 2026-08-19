# Voice Critique — Summary, Chapter 3 (20250528), scenes 01–10

**Input shape:** per-scene, directory run over `narration/`. Scrubbed variants used for scenes 01, 02, 03, 07, 08 (mirroring `collect_scene_files`); raw `.md` for 04, 05, 06, 09, 10 (no scrubbed variant exists).
**Narrators:** Brewbarry (01, 07) · Soma (02, 05, 08) · Vukradin (03, 09) · Valphine Sotorra (04, 06, 10).

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` — 61 lines, ~7.5K chars | run record: all ten `.knobs.json` files, post-#276 shape, identical digest |
| Rulebook vs run record | **match** — the current file's digest equals the render-time digest for every scene | verified with the pipeline's own normalization, `sha256(text.strip())[:12]` (a raw-byte sha comparison false-alarms; the knobs digest is of stripped text) |
| Rulebook vs next render | `paths.genre_file: voice/_genre.md` in `config/session_doc.yaml` — same file | no divergence between "what these renders used" and "what the next render will use" |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` (4.1K) | read at critique time |
| Voice specs | `brewbarry_new_pipeline.md`, `soma_new_pipeline.md`, `vukradin_new_pipeline.md`, `valphine_new_pipeline.md` | all four via rule (c) — unique `<first>_…` key; no ambiguity |
| Per-char examples | `examples/{brewbarry,soma,vukradin,valphine}.md` | stem equals first name; one file each, no global examples |
| Party doc | `docs/party.md` | roster **3/4** — Brewbarry's block carries no `Player:` line (campaigns#144 silent-partial hazard); his spec + examples still resolved |
| voice_lint | ran on all 10 files | **0 errors, 0 warnings**; bookkeeping checks **skipped** on every file — the rulebook has no ` ```yaml voice_lint ` block, i.e. this campaign declares no filing register (a config fact, not a run failure) |

## Budget ledger

Scope: whole directory, scenes 01–10.
Budgets from: `voice/_genre.md` @ `6e67c59f94b4` + `base.md` HARD BANS.

| Budget / rule | Observed | Budget | Verdict |
|---|---|---|---|
| "the shape of X" | 0 | never (rulebook) | ok |
| portable portrait ("with the X of someone who…") | 0 confirmed; 1 borderline judged licensed (06 L41, deliberate mask-composition) | never | ok — GM may overrule the borderline |
| behavioral taxonomy ("the way X does … when …" and shells) | **1** (07 L21) | 0 — banned as a move | **BREACH** (borderline: body-lens content, banned shell) |
| connective em-dash in narration prose | **0** (all 36 remaining em-dashes sit inside locked quotes) | never as connective (rulebook) | ok |
| quote-final interruption dashes vs the tape (Scan A2) | 32 in narration; raw extractions **0**, smoothed **58** | must match tape | **1 false assertion** (09 L57, narrator-authored); the other 31 adjudicated genuine or fiction-effective renderings of cue-splits — see below |
| first-person present tense | 10/10 scenes | required, always | ok |
| POV bleed / recap framing / mock-archaic / narrator editorializing | 0 | never | ok |
| bookkeeping / filing caps | — | — | *not checked — rulebook declares none (no voice_lint block)* |

## Scan A2 — trailing-dash provenance (the systemic finding)

Raw `scene_extractions/` carry **0** quote-final `—"` and **91** `(truncated)` markers; `scene_extractions_smoothed/` (what the narrator read) carry **58** and **0**. Same mechanism as the ch48 case: smoothing merges split VTT cues and renders every residual trail-off as an interruption. 32 reached narration. Adjudicated each against the raw tape:

- **1 confirmed false** — scene 09 L57: `"Yeah, moments ago. Hours, even."` is one complete line on *both* extraction layers; the narration split it and gave "even" to Soma. Flagged (also a quoted-line-split spec breach).
- **31 check out** — real cut-ins, real completion devices (the finish-each-other's-sentences move the rulebook endorses), or same-speaker cue-splits the narration renders as a dramatic beat (01 L49's tape completion was mechanical residue; 04 L23 reattributes a Vukradin cue-front to Valphine as mockery — tape-divergent but covered by the mock-quote device; both noted in their scene reports).
- **None is a scene-final line** — the load-bearing-by-position case does not occur here.

## Flags across the directory (4)

| # | Scene | Line | Category | The problem |
|---|---|---|---|---|
| 1 | 03 (Vukradin) | 49 | canon/timeline via example-bleed | "I learned at a pool in the Whispering Wood what I think about fans" — the pool is a **Chapter 11** event; this is Chapter 3. The model read `examples/vukradin.md`'s ch11 passage as memory canon. |
| 2 | 09 (Vukradin) | 57–59 | quoted-line split + false interruption | "Hours—" / "even," splits the tape's complete `"Yeah, moments ago. Hours, even."` across two speakers. |
| 3 | 07 (Brewbarry) | 21 | HARD BAN, behavioral-taxonomy shell (borderline) | "the way an arm hangs when the body is spending more than it has" — banned shell, licensed content. |
| 4 | 10 (Valphine) | 69 | cliché simile | "pulled taut as a bowstring" — the one generic figure in an otherwise exact scene. |

Suggested rewrites are in the per-scene reports. All four are one-clause spot edits; **none is a re-render signal.** Fixes for 03/07 go in the existing `.scrubbed.md`; scenes 09 and 10 have no `.scrubbed.md` yet — create one for each so `assemble.py` picks the fix up.

## Doc-level convergence (the strongest recurring issue)

**The "X the way Y [verbs] Z" analogy shell appears 10 times, in all four narrators, across 7 of 10 scenes:**

- Soma: "polls us the way he polls a crowd before a set" (08 L9), "the way I look at a low cupboard" (05 L45), "the way such digs end" (08 L91)
- Valphine: "the way I spend pain" (04 L117), "the way I read a redacted ledger" (06 L9), "the way I savor a well-placed burn" (06 L45), "the way one feels a missing tooth" (10 L13), "the way a mill runs on water" (10 L43)
- Brewbarry: "the way an arm hangs when…" (07 L21 — the flagged one)
- Vukradin: "the way you sketch a verse before you have earned it" (09 L73)

Each instance is individually well-chosen and in-lexicon — that is what makes it invisible per scene. Collectively it is one narrator's connective rhythm wearing four hats (the fable portable-tic profile). Not a per-sentence purge: fixing flag #3 and trimming one or two of Valphine's five (she carries half the total) breaks the pattern.

**Accounting-register spread (mild):** the ledger/invoice/amortized field is Vukradin's signature and he uses it heavily and correctly (13 hits across scenes 03/09). Valphine carries 9 hits across 04/06/10 ("redacted ledger," "our own ledger," "arithmetic," "economy") — partially licensed by her power-as-currency spec, but "ledger" specifically is his word; her own is catalog/archive. Soma has exactly one: "joints are **filing** their usual complaints" (05 L11). Worth a trim only if you want the registers fully separated; noted, not flagged.

## Notes for the GM (not flags)

- **Dialogue anachronisms the scrub pass never surfaced** — all inside verbatim quotes (locked player speech; removal = authorial rewrite, GM scope call): "Scooby-Doo style" (04 L25), "He's dead, Jim" (07 L69), "tank/tanking" (07 L55–57, 10 L61 — narration already launders it via "I do not know tanks"), "Archeology for Dummies" (09 L59), "the other players" (10 L53 — defensible as bard troupe-speak). The 1.4/10.1 keep precedents apply if you want a blanket ruling.
- **Canon check:** "I trained him in interrogation" (06 L37, Valphine re: Brewbarry) — unverifiable at Chapter 3; the party is weeks old.
- **Reclassified table speech:** every scene except 01 carries a hatch (listed in full in the per-scene reports). Scene 04's holds **16 spans** — the biggest scope-call cluster in the directory; worth a read before assembly since `assemble.py` strips them.
- If you ever want OOTA-style filed/ledger caps enforced mechanically here, add a ` ```yaml voice_lint ` block to `voice/_genre.md`; right now that whole check category does not run.

## Verdict

The pipeline delivered everything it was supposed to — rulebook resolved and digest-matched on all ten renders, all four specs and example files reached the prompts — and the output holds voice unusually well: four spot-edit flags, zero re-render signals. The two real defects are both fidelity, not register: a Chapter 11 memory backdated into Chapter 3 by example-bleed, and one quoted line split against the tape. Fix those two first.

## Applied rulings (2026-08-18)

All twelve artifact rulings executed. Fixes live in `.scrubbed.md` files (raw untouched); scenes 04, 05, 06, 09, 10 had scrubbed files created for this.

- **f1–f4 accepted as proposed** — scene 03 L49 (Whispering Wood clause removed), scene 09 L57–59 (tape restored: "Hours, even." one speaker), scene 07 L21 (taxonomy shell → "the head of it near dragging"), scene 10 L69 (bowstring → "narrowed to the breath before a verdict").
- **p1 trim** — analogy shell reduced 10 → 5: scene 06 L9 ("I read them the way I read a redacted ledger:" frame cut), scene 06 L45 ("the way I savor" → "like"), scene 10 L13 ("the way one feels" → "like"), plus f3.
- **p2 trim** — scene 10 L13 "our own ledger" → "our own arithmetic"; scene 05 L11 "filing" → "lodging"; scene 06 L9 ledger gone via p1. Zero ledger/filing outside Vukradin's scenes.
- **n6 cut** — scene 06 L37 training claim removed: "He understands, untaught, that…".
- **n3/n4/n5 keep** — tank/tanking, Archeology for Dummies, "the other players" stay as licensed player speech.
- **n1 replace (GM-approved wording)** — scene 04 L25: "Scooby-Doo style" → "haunted-manor style". **Deliberate GM-authored divergence from the tape inside a verbatim quote** — do not "fix" it back in fidelity checks.
- **n2 annotate (GM-approved)** — scene 07: "He's dead, Jim," and "I do not know Jim. Dead is dead." stay verbatim; a sage's marginal note follows, inventing **Jimble the Unmoved** (registered in `docs/entity_registry.yaml`, `provenance: on_the_fly`). First use of the sage's-marginal-note convention (Kostadinious the Sage), now codified in the scrub and voice-critic skills. **The note is apparatus, not narration — GM-authored, not on the tape.**
