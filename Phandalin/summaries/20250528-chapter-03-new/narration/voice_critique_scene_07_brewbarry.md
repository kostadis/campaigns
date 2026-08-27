# Voice Critique — Brewbarry, scene 07: Ambush Behind the Altar

**Narration:** `session_doc_scene_07_ambush_behind_the_altar.scrubbed.md`
**Input shape:** per-scene (directory run; scrubbed variant preferred where it exists)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `Phandalin/voice/_genre.md` @ `6e67c59f94b4` | run record (`.knobs.json`, post-#276); 61 lines, ~7.5K chars |
| Rulebook vs run record | **match** — current file digest equals render-time digest (verified with the pipeline's own `sha256(text.strip())[:12]`) | sha comparison |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/brewbarry_new_pipeline.md` | rule (c): unique key `brewbarry_new_pipeline` for first name `brewbarry` |
| Per-char examples | `examples/brewbarry.md` | stem equals first name; single file, no concatenation |
| Global examples | none | all four example files route per-character |
| Party doc | `docs/party.md` | roster **3/4** PCs carry `Player:` lines — Brewbarry's block lacks one (campaigns#144 silent-partial hazard) |
| voice_lint | ran on `session_doc_scene_07_ambush_behind_the_altar.scrubbed.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

### [1] rulebook conflict — behavioral-taxonomy shell (HARD BAN, borderline)

> I have watched her carry the mace low all day, the way an arm hangs when the body is spending more than it has.

**Why:** `base.md` bans the move "the way X do/does … when …" in every shell — explaining an observed behaviour by generalising it. The content is Brewbarry's licensed body-lens, but the shell is literally the banned construction, generalising Valphine's arm to how bodies-in-general behave. Borderline — flagged because the ban is explicit that rotating the shell does not clear the move.
**Suggested rewrite:** "I have watched her carry the mace low all day, the head of it near dragging. She is spending more than she has." *(renders the specific observed thing; keeps his short declaratives)*

## Notes

- **Dialogue anachronisms, GM scope calls, neither surfaced by the scrub pass:** "He's dead, Jim" (line 69, Soma, verbatim quote — Star Trek); "tank" (lines 55–57 — table gamer-slang, and the narration already launders it: "I do not know tanks. But if it means the thing that stands in front of Vukradin and takes the hit, then yes"). Both are locked player speech; the laundering means neither compounds into future narration as established register.
- Scan A2: both quote-final dashes check out (line 55's matches a raw `(truncated)` marker with Soma supplying "tank" — rendered via the hatch).

## Reclassified table speech

- `"tank. Wade, you're up. Oh, sorry — I'm still stuck in the back. Not getting to the other side, so just one more Ice Knife. Sorry, I'm still not used to hearing Soma."`
- `"Moral guilt? No. In a drow? Nah. She's enjoying the pain and the light."`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

One borderline flag, a one-clause spot edit. Otherwise this is Brewbarry's best scene — "Rage turns axes. Rage turns teeth. Rage does not turn burning. I did not know that until now. I do not like knowing it" is the strongest run of sentences in the document.
