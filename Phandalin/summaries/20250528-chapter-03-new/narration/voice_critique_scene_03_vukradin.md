# Voice Critique — Vukradin, scene 03: Archaeologists and Altars

**Narration:** `session_doc_scene_03_archaeologists_and_altars.scrubbed.md`
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
| voice_lint | ran on `session_doc_scene_03_archaeologists_and_altars.scrubbed.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

### [1] canon/timeline breach — example-bleed from Chapter 11

> Two dwarves in a haunted temple are an audience, and an audience is fans, and I learned at a pool in the Whispering Wood what I think about fans, and I will not unlearn it to spite a prospector.

**Why:** The pool in the Whispering Wood — and Vukradin's realization about playing for fans — is a **Chapter 11** event ("The Stag, the Brambles, the Wolves, and the Pool"; see `examples/vukradin.md`). This scene is Chapter 3. The narrator model read the ch11 example passage as *memory canon* rather than voice reference and backdated the event eight chapters. At Chapter 3, per the ch11 passage itself, Vukradin still believes it is about the music, not the fans — so the clause is wrong twice: the event has not happened yet and the conclusion is not his yet.
**Suggested rewrite:** "Two dwarves in a haunted temple are an audience, and I have never in my life turned down an audience." *(grounded in spec — cheerleader-conductor energy, sincere professional; timeline-safe)*

## Notes

- Scan A2: the single quote-final dash (line 57) matches a real cue handoff — Soma answers over him on the tape.

## Reclassified table speech

- `"Okay, so what you do find is you find a bunch of secret doors."`
- `"16 perception, if that helps."`
- `"All right, you find a set of secret doors. Actually, to be precise, the cleric finds a set of secret doors. I'm assuming the cleric, having learned from the Morning Lord, who shared that information, is not keeping it secret for her advantage. I don't know what advantage it would have, but sure."`
- `"Isn't that what, like, drow — that's like an information-is-power kind of thing?"`
- `"Yeah, we'll figure it out. So — is this before or after the long rest? This is before the long rest."`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

One flag, and it is a one-clause spot edit in the `.scrubbed.md`, not a re-render — everything around it is the strongest ledger-register scene in the document ("the danger has been fully amortized by other people," "New clauses, sprouting the moment payment comes due. Scandalous.").
