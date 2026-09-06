# Voice Critique — Sequoia, scene 06: Return to Nulb

**Narration:** `session_doc_scene_06_return_to_nulb.md`  
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `9d58d0d40afa`, 80 lines | run record (`.knobs.json`), post-#276 |
| Rulebook vs run record | **match** — all six scenes carry the same digest, and it equals the live file | `sha256(text.strip())[:12]` |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | read |
| Voice spec | resolved via roster declaration | `config/party.yaml` → `voice:` |
| Per-char examples | **NONE — 0 of 6 files declared** | no `examples:` keys, no `shared_examples:` |
| Global examples | none | no `shared_examples:` |
| Party doc | `docs/party.md` | 4/4 PCs |
| voice_lint | ran, exit 0 | 0 errors, 0 warnings, **1 skipped check** |


> **Suggested rewrites are `[grounded in spec only]`.** All six files in `examples/` are
> orphans — no roster entry declares them and there is no `shared_examples:` block, so
> under the post-#301 declared-not-routed rule they reach no prompt. The narrator wrote
> this scene with a voice spec and no examples.

## Budget ledger

Scope: single scene — **doc-level budgets NOT evaluable**; see `voice_critique_summary.md`
Budgets from: `voice/_genre.md` @ `9d58d0d40afa`

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| "the shape of" | 0 | 0 (base.md HARD BAN) | ok |
| portable portrait ("with the X of a man who") | 0 | 0 (base.md HARD BAN) | ok |
| behavioral taxonomy (any shell) | 0 | 0 (base.md HARD BAN) | ok |
| banned tics ("what could only be described as", "the cusp of", "the particular kind of") | 0 | 0 (rulebook) | ok |
| adverb-heavy combat (quickly/swiftly/brutally) | 0 | 0 (rulebook) | ok |
| recap framing | 0 | 0 (rulebook) | ok |
| connective em-dashes | 0 in prose | — | *not checked — rulebook states the permission (interrupted speech/thought) but no prohibition* |
| bookkeeping / filing caps | — | — | *not checked — rulebook declares no `yaml voice_lint` block* |
| doc-level numeric budgets | — | — | *not checked — rulebook declares none* |


## Flags

None. The scene breaches no stated rule, and no sentence read as generic,
register-wrong, or convergent with another narrator.


## Reclassified table speech

none


## Verdict

No findings. 518 prose words, 13.5% of the document.
