# Voice Critique — Vukradin, scene 09: Amateur Archaeologists

**Narration:** `session_doc_scene_09_amateur_archaeologists.md`
**Input shape:** per-scene (directory run; scrubbed variant preferred where it exists)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `Phandalin/voice/_genre.md` @ `6e67c59f94b4` | run record (`.knobs.json`, post-#276); 61 lines, ~7.5K chars |
| Rulebook vs run record | **match** — current file digest equals render-time digest (verified with the pipeline's own `sha256(text.strip())[:12]`) | sha comparison |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/vukradin_new_pipeline.md` | rule (c): unique key `vukradin_new_pipeline` for first name `vukradin` |
| Per-char examples | `examples/vukradin.md` | stem equals first name; single file, no concatenation |
| Global examples | none | all four example files route per-character |
| Party doc | `docs/party.md` | roster **3/4** PCs carry `Player:` lines — Brewbarry's block lacks one (campaigns#144 silent-partial hazard) |
| voice_lint | ran on `session_doc_scene_09_amateur_archaeologists.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

### [1] quoted-line split + false interruption (narrator-authored)

> "Yeah, moments ago. Hours—"
>
> "even," Soma finishes. "Do we still see, like, an Archeology for Dummies book under their arm or something?"

**Why:** Both extraction layers — raw *and* smoothed — carry this as one complete line by one speaker: `"Yeah, moments ago. Hours, even."` The narration split the quote, handed the tail to Soma, and asserted an interruption that never happened. This breaches the voice spec's non-negotiable constraint 5 (never split or reorder quoted lines) and is the one confirmed-false interruption dash of the 32 in this directory — every other one traces to the smoothing layer or a real cut-in.
**Suggested rewrite:** restore the tape — `"Yeah, moments ago. Hours, even."` then `"Do we still see, like, an Archeology for Dummies book under their arm or something?" Soma asks.` *(Scene 9 has no `.scrubbed.md` yet; the fix belongs in a new one so `assemble.py` picks it up.)*

## Notes

- **Dialogue anachronism, GM scope call:** "Archeology for Dummies" (line 59, Soma, verbatim) — a modern book-brand joke the scrub pass never surfaced. Locked player speech; keep/replace is a GM ruling.
- The interrogation of the dwarves ("playing the instrument backwards") is spec-perfect Vukradin — words-as-connection wounded, not cynical.

## Reclassified table speech

- `"Insight. Not very good."`
- `"can tell they're lying — that they're lying?"`
- `"saying. Well, then I would be very upset—"`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

One flag: restore "Hours, even." to a single speaker per the tape. Everything else is Vukradin at full spec — the enthusiasts verdict and "The ledger balances" close the scene exactly in register.
