# Voice Critique — Zenvon, scene 04: Rescue and Pursuit

**Narration:** `summaries/007/narration/session_doc_scene_04_rescue_and_pursuit.md`
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

> ⚠️ **Session-wide issue, see summary:** narrated from `scene_extractions/` (unsmoothed). See `voice_critique_summary.md` §1.

## Flags

### [1] Convergence with the examples file — third of four, and a duplicate of scene 03

> He was very happy. I did not have anything prepared for that. His face when the bars moved was — I was not counting anything, for a moment.
>
> Then I was again.

**Why:** Third firing of the `examples/zenvon.md` formula, and the second on **this same boy** — scene 03 already spent it on him at the bars, eleven lines before the party even reached the lock. The examples file's own instruction is *"only the manner transfers, never the incidents."* This scene has the better claim on the beat (the cell actually opens here), so this is the one to keep and scene 03's is the one to cut. But the sentence itself should still stop being a quotation of the example.
**Suggested rewrite:** `He was very happy. I did not have anything prepared for that. / Then I did, and it was the lock on the second cell.`

### [2] Register-wrong vocabulary

> Free these people. Yes. That was the shape of it.

**Why:** Mechanical scan B hit. *Shape* is the architectural default. He does not perceive plans as forms; he perceives them as **terms** — the division of a job, who pays what, who goes where.
**Suggested rewrite:** `Free these people. Yes. Those were the terms.`

### [3] Register-wrong vocabulary

> Behind us, Veyra shifted for one last angle on the runner and let a second firebolt go.

**Why:** Second scan B hit, same family as scene 03's *geometry*/*angle*. What he registers is that she moved for a **clear shot**.
**Suggested rewrite:** `Behind us, Veyra shifted for one last clear shot at the runner and let a second firebolt go.`

### [4] Verbatim alterations — two quoted lines changed

> "So, you and Veyra can go behind the Redbrands Ruffian, and Sister Maela will help."

Source: `"So, you and Veyra can go behind the Redbrand Ruffian, and Sister Maela will help."` — pluralised inside the quote.

Source (both layers): `"So, you and Veyra can go behind the Redbrand **Ruffian**…"` — pluralised to *Redbrands* inside the quote. A genuine narration-side alteration; not attributable to the input-path bug.

> "Wait, you're, you're gonna just leave us here?"

Raw source: `"Hold on, the, the, the, the people go, all right, wait, you're, you're gonna just leave us here?"`
Smoothed source: `"Hold on — the people go: all right, wait, you're gonna just leave us here?"`

**Why:** The `you're, you're` stutter **was** spoken — it is in the raw extraction, and the voice-smooth pass deliberately removed it. So the narration is faithful to its input; the input was simply the wrong layer (see summary §1). The narrator correctly strips the GM's framing in both cases. Only the *Redbrands* pluralisation is a narration defect.
**Suggested rewrite:** `"…behind the Redbrand Ruffian…"` and, once the smoothed layer is the source, `"Wait, you're gonna just leave us here?"`

### [5] Mechanical scan A — em-dashes in narration prose (9)

| Line | Fragment | Suggested |
|---|---|---|
| 10 | `spent everything he had on distance — one long, careful retreat` | `spent everything he had on distance: one long, careful retreat` |
| 32 | `the way Pip goes after anything — full speed, sword first — and I heard` | `the way Pip goes after anything, full speed, sword first, and I heard` |
| 38 | `Routine work — focus, not effort` | `Routine work. Focus, not effort` |
| 42 | *(covered by flag [1] — rewrite removes it)* | — |
| 46 | `across the back — a scorch, not a stop` | `across the back: a scorch, not a stop` |
| 48 | `pulled away again — another clean retreat` | `pulled away again: another clean retreat` |
| 50 | `a pit, hidden in the hallway … at exactly that speed. By the noise of him at the bottom he had landed soft — annoyed, not broken — but he was out` | `…landed soft, annoyed, not broken, but he was out` |
| 58 | `they saw bodies with no red cloaks — the cloaks are the pass` | `they saw bodies with no red cloaks. The cloaks are the pass` |
| 62 | `The wall took it — a black scorch where a man's back should have been — and the corridor` | `The wall took it, a black scorch where a man's back should have been, and the corridor` |

## Verified, not flagged

- `Pip turned to me. "Are we chasing him, boss, or not?"` — the source has this inside a GM line (*"Alright, Pip turns to you. Are we chasing him, boss, or not?"*). Correctly unwrapped and attributed to Pip.
- `"You're the, you're the guy with the fingers…"` — stutter is in the raw source; faithfully rendered. Same input-layer caveat as flag [4].
- `"Yay! I've been saved!"`, `"Shit, okay, he ran again."`, `"I see, I hear some footstep."`, `"Just stay here until I come back"` — verbatim.
- *"I carry a whip, which is a rope that has made something of itself"* — invented, but squarely on-voice and grounded in the source action. Keep.

## Verdict

Two of this scene's quoted lines carry raw-layer disfluency that the smoothing pass had removed — a symptom of the input-path bug, not of the narrator, which rendered its source faithfully. The narration-side defect is the *Redbrands* pluralisation. Beyond that, this scene shares the cage-boy beat with scene 03 and needs one of the two cut. Spot-edit.
