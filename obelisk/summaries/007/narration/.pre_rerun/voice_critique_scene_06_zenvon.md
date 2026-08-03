# Voice Critique — Zenvon, scene 06: Deception in the Barracks

**Narration:** `summaries/007/narration/session_doc_scene_06_deception_in_the_barracks.md`
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

> ⚠️ **Session-wide issue, see summary:** narrated from `scene_extractions/` (unsmoothed). This scene shows the consequence most clearly — see flag [2] and `voice_critique_summary.md` §1.

## Flags

### [1] Register-wrong vocabulary

> The trick was the sightlines.

**Why:** Mechanical scan B hit. *Sightlines* is staging/technical vocabulary. What he is actually reasoning about is **witnesses** — who watches whom do what, and whose story survives. That is his native frame (the whole scene is about owning the room's version of events), and the next two sentences already say it better.
**Suggested rewrite:** `The trick was who would be watching.`

### [2] Verbatim drift — disfluencies re-added to a line the smoothing pass had cleaned

> "We — we are one of you guys, like, come on, we have — we all have the same dress. And look — look at this guy, this guy has turned a traitor. He was trying to — I saw him letting in, letting someone in, so that's why I wanted to catch him and, you know, eliminate him."

Smoothed source: `"We — we are one of you guys. Like, come on, we all have the same dress. And look at this guy — this guy has turned a traitor. He was trying to — I saw him letting someone in. So that's why I wanted to catch him…"`

**Why:** The narration adds three hesitations that are not in the smoothed layer — `we have — we all have`, `And look — look at this guy`, `letting in, letting someone in`. This is the single most important line Zenvon speaks all session (the spec quotes it twice as definitive), and it is the clearest evidence that the run read the unsmoothed extraction: the smoothing pass adjudicated exactly these hesitations one by one, and the narrator put a different set back.
**Suggested rewrite:** Use the smoothed line as written. The preserved `"eliminate him"` at the end is correct and must stay — the spec forbids trading it down to *"kill him."*

### [3] Mechanical scan A — em-dashes in narration prose (7)

| Line | Fragment | Suggested |
|---|---|---|
| 12 | `Several voices behind it, murmuring — the low, uneven kind` | `Several voices behind it, murmuring: the low, uneven kind` |
| 32 | `an extremely good argument — his own wounds were my evidence` | `an extremely good argument. His own wounds were my evidence` |
| 34 | `One of them — Dosa Rook, I would learn — was fully bought` | `One of them, Dosa Rook, I would learn, was fully bought` |
| 50 | *(covered by flag [1] rewrite)* | — |
| 52 | `Hard — but not hard enough` | `Hard. But not hard enough` |
| 56 | `faster than I would have liked. "I told you…"` *(dash precedes quote)* | `…faster than I would have liked.` |
| 62 | `who had started all of this — the one I had named a traitor` | `who had started all of this: the one I had named a traitor` |

## Verified, not flagged

- **Dosa Rook** — genuine. Named in the source extraction (*"Dosa Rook immediately believes the story…"*) and in `session-summary.md`. Not an invention.
- `"Wait! You're one of us!"`, `"Do I look like I'm the kind of person who would lie? That is a killing machine! Kill him!"`, `"Hmm, traitor."`, `"Funny."`, `"Nobody sent word down…"`, `"About time somebody cleaned house…"`, `"I told you these guys weren't to be trusted!"`, `"Step back"` — all verbatim.
- *"So. The barracks."* — the `"So,"` opener the spec logs at 4.5%. On-voice.
- *"I had decided to backstab them. I do not dispute the characterization. I dispute the timing."* — invented, but it is case-building rather than moral self-justification, which the spec endorses. Keep.

## Verdict

Flag [2] is the one to act on, and it is diagnostic rather than cosmetic: Zenvon's signature line of the session was rebuilt from the pre-smoothing text with invented hesitations. That is a re-run concern, not a spot-edit concern — but the cheapest fix is to paste the smoothed line back in. The rest of the scene is the strongest characterisation work in the set; the deception logic reads exactly like the spec's *"repricing the transaction."*
