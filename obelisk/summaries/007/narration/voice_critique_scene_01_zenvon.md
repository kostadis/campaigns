# Voice Critique — Zenvon, scene 01: Battle in the Tresendar Crypts

**Narration:** `summaries/007/narration/session_doc_scene_01_battle_in_the_tresendar_crypts.md` (re-run 19:10, smoothed source, registry disabled)
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

## Flags

### [1] Verbatim alteration — `--prose-mode` stripped mechanics *inside* a quotation

> "Wait, that does nothing?"

Source (smoothed extraction **and** all three VTT transcripts): `"Wait, 8 points of damage does nothing?"`

**Why:** `--prose-mode` is documented as "Strip mechanical / GM framing from **narration**." It reached inside quotation marks. The number is the whole point of the line — 8 damage landing on a skeleton and doing nothing is what triggers Zenvon's repricing of the fight two sentences later. Same defect class as the registry bug: a legitimate transform applied to dialogue.
**Suggested rewrite:** `"Wait, 8 points of damage does nothing?"`

### [2] Verbatim alteration — same cause, and this one changes the information

> "I'm gonna move back. I'm just about out, so…"

Source and VTT (`Nikhil:`): `"I'm gonna move back. I'm just at 4 points of damage, so…"`

**Why:** More serious than [1]. *"I'm just at 4 points of damage"* is a specific HP state; *"I'm just about out"* is a paraphrase that asserts something the player did not say. This is a quoted line carrying altered fact. Note the retranscribed VTT renders it *"I'm just at four points of damage so..."* — the number is stable across all three transcripts, so there is no transcription ambiguity to hide behind.
**Suggested rewrite:** `"I'm gonna move back. I'm just at 4 points of damage, so…"`

### [3] Register-wrong vocabulary

> "So it's gone." Two exits had just become a problem for later. I filed it.

**Why:** Mechanical scan B hit, and it recurs in scene 02 (*"I filed that away without comment"*). *Filed* is clerical; Zenvon's idiom is transactional — he prices, totals, and enters things in a ledger. The narration establishes the ledger metaphor well elsewhere in this scene (*"one more entry like that would close the account"*), which makes the filing cabinet an intrusion from a different office.
**Suggested rewrite:** `"So it's gone." Two exits had just become a problem for later. I put it on the list.`

### [4] Cliché / over-built simile

> The second was the cleanest strike I have made in years — I felt it before it landed, the way you feel a deal closing, the axe finding the seam between the ribs like the seam had been drawn on a map for me.

**Why:** *The way you feel a deal closing* is excellent and exactly on-spec. The second simile then re-explains the same swing with a map image, and two similes on one axe stroke is one more than the spec's terse narrator would spend. Cut the weaker one.
**Suggested rewrite:** `The second was the cleanest strike I have made in years — I felt it before it landed, the way you feel a deal closing. The axe found the seam between the ribs. Bone cracked.`

### [5] Mechanical scan A — em-dashes in narration prose (16, joint-highest of the session)

| Line | Fragment | Suggested |
|---|---|---|
| 9 | `two doors — one behind us` | `two doors: one behind us` |
| 13 | `shouted at my back — if you have a mace` | `shouted at my back: if you have a mace` |
| 17 | *(covered by flag [4])* | — |
| 27 | `walked forward — walked, in front of all of them … lectern — and planted herself` | `walked forward. Walked, in front of all of them … lectern. And planted herself` |
| 31 | `went out of them — whatever passes for nerve … no flesh — and they backed off` | `went out of them, whatever passes for nerve … no flesh, and they backed off` |
| 39 | `went deep — deeper than anything` | `went deep. Deeper than anything` |
| 41 | `pausing for breath — good value, Pip, always` | `pausing for breath. Good value, Pip, always` |
| 43 | `Strike and step away — the blade is built` | `Strike and step away: the blade is built` |
| 47 | `caught him — a bruise through the armor` | `caught him: a bruise through the armor` |
| 49 | `Sound allocation — Pip was the line` | `Sound allocation. Pip was the line` |
| 53 | `threw fire at it — a sound like the end of the world` | `threw fire at it: a sound like the end of the world` |
| 55 | `within arm's reach — no way around that — so I closed` | `within arm's reach, no way around that, so I closed` |
| 57 | `came drifting back — and stopped` | `came drifting back. And stopped` |

## Verified, not flagged

- `"Turn on bed."` — **genuine**, and correctly attributed to Zenvon in the source. The mishearing of "Turn Undead" is preserved with the narrator's own gloss (*"which was not what she had said"*). Exactly the right handling of an ESL-adjacent moment: rendered, not corrected.
- `"No damage, just frightening."` — source speaker is **Zenvon**, not the GM. Attribution correct.
- `"BE GONE! In the name of my dwarven god."` — **dwarven** now correct (the previous run had "Dwarvish").
- `"Nick, Nick is possible with the scimitar. Yes."` — genuine; Nick is the scimitar's mastery property. Doubled word preserved per the ESL ruling.
- `"Yay."`, `"Shit."`, `"So it's gone."`, `"The ones that ran away?"`, `"I'll use the axe."` — verbatim.

## Verdict

Two quoted lines have had their mechanics stripped by `--prose-mode`, and flag [2] alters what the player actually said about his own hit points. That is the defect to fix, and it is a pipeline setting, not a wording choice. The prose itself is a clear improvement on the first run — the ledger voice is calibrated rather than saturated, and the "Turn on bed" handling is exemplary. Spot-edit the two quotes; do not re-narrate.
