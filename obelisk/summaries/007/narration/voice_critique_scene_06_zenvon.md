# Voice Critique — Zenvon, scene 06: Deception in the Barracks

**Narration:** `summaries/007/narration/session_doc_scene_06_deception_in_the_barracks.md` (re-run 19:14)
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

## Flags

### [1] Mechanical scan A — em-dashes in narration prose (10)

| Line | Fragment | Suggested |
|---|---|---|
| 9 | `murmuring, low — men waiting for something` | `murmuring, low. Men waiting for something` |
| 13 | `One I could not — south side, tucked out of the light` | `One I could not: south side, tucked out of the light` |
| 23 | `put him at a disadvantage — the truth was all he had` | `put him at a disadvantage. The truth was all he had` |
| 35 | `tried to defend his honor — loudly, badly` | `tried to defend his honor, loudly, badly` |
| 49 | `not attacking him myself — the room could still see me` | `not attacking him myself. The room could still see me` |
| 51 | `out of the dark and hit him — hard, real, but the man stayed up` | `out of the dark and hit him. Hard, real, but the man stayed up` |
| 61 | `Pip was fastest — he finished the man he had struck` | `Pip was fastest. He finished the man he had struck` |
| 67 | `the wounded ruffian beside him — the honest one` | `the wounded ruffian beside him: the honest one` |
| 71 | `cut the ruffian down himself — his own man … never lied — and then he threw up his hands` | `cut the ruffian down himself, his own man … never lied, and then he threw up his hands` |

### [2] Borderline — a stated rule where a shown one would land harder

> There is a moment in every negotiation when the other side stops weighing your offer and starts weighing each other, and I watched that moment cross four faces at once.

**Why:** Flagged for your call, not as a defect. The aphorism-then-instance structure is on-voice for a man who argues from precedent, and *"cross four faces at once"* is a real observation. But the scene already demonstrates the principle through action, and the generalisation slightly pre-empts its own evidence. Keep it if you want Zenvon explicitly theorising his craft; cut the first clause if you want him only ever counting.

## Verified, not flagged

- **The signature deception line is now correct.** It matches the smoothed source word for word:
  > `"We — we are one of you guys. Like, come on, we all have the same dress. And look at this guy — this guy has turned a traitor. He was trying to — I saw him letting someone in. So that's why I wanted to catch him and, you know, eliminate him."`

  The previous run rebuilt it from the raw extraction with three hesitations the smoothing pass had deliberately removed (*"we have — we all have"*, *"And look — look at this guy"*, *"letting in, letting someone in"*). This was the single most damaged line in the first run and it is fully repaired.
- `"eliminate him"` preserved — the spec forbids trading it down to *"kill him"*, and it survived.
- `"Alright, I'll — I'll join with you. Let's go check. Let's confirm your suspicions."` — verbatim. Note this contains the `"Alright"` opener the spec lists under *Things They'd Never Say*; because it is **verbatim** and the spec allows that Nikhil does say it rarely (6× across 1,513 lines), it ships as spoken. Not a defect — flagging only so the apparent conflict does not get "fixed" later.
- `"Wait! You're one of us!"`, `"What do you mean they attacked you, man?…"`, `"Do I look like I'm the kind of person who would lie?…"`, `"Hmm, traitor."`, `"Funny."`, `"Nobody sent word down…"`, `"I'm gonna have to go check this story, see if it's real."`, `"About time somebody cleaned house…"`, `"I told you these guys weren't to be trusted."`, `"So, he's the bad guy."`, `"Step back."` — all verbatim, all correctly attributed.
- **Dosa Rook** — genuine, named in both the extraction and `session-summary.md`.
- **Mechanical scan B: clean.** The previous run's *"The trick was the sightlines"* is gone, replaced by *"The route to checking ran past the stairs"* — concrete, spatial, no staging vocabulary.
- *"I have negotiated with many kinds of men. I had not, until then, watched one open the bidding with a corpse."* — invented, and the strongest closing line of the session. It also hands scene 07 its opening.

## Verdict

No verbatim defects, no register defects, and the line that was worst-damaged in the first run is now exact. The only mechanical work is ten em-dashes. This is the best-calibrated scene of the eight — the deception reads as repricing rather than lying, which is precisely the spec's core thesis.
