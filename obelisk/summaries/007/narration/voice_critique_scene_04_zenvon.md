# Voice Critique — Zenvon, scene 04: Rescue and Pursuit

**Narration:** `summaries/007/narration/session_doc_scene_04_rescue_and_pursuit.md` (re-run 19:12)
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

## Flags

### [1] Mechanical scan A — em-dashes in narration prose (8)

| Line | Fragment | Suggested |
|---|---|---|
| 9 | `at the same time — he had decided that, on balance` | `at the same time. He had decided that, on balance` |
| 31 | `somewhere down the corridor — a solid hit` | `somewhere down the corridor: a solid hit` |
| 37 | `the work was routine — pressure, a turn, done` | `the work was routine: pressure, a turn, done` |
| 39 | `His whole face did it — the thing a face does` | `His whole face did it: the thing a face does` |
| 41 | `clipped the runner — a graze, enough to sting` | `clipped the runner: a graze, enough to sting` |
| 49 | `from up the corridor — a wrong sound` | `from up the corridor, a wrong sound` |
| 53 | `All right, wait — you're gonna just leave us here?` | *(leave — this is reported speech, see below)* |
| 55 | `do not read faces — they read cloaks` | `do not read faces. They read cloaks` |

Line 53 is the freed prisoners' line rendered as unquoted reported speech. The em-dash there reproduces the smoothed source's own punctuation, so it is dialogue texture rather than narration prose — **do not convert it.** The scan flagged it because the line carries no quotation marks; this is the one case in the session where the mask heuristic needs a human eye.

### [2] Borderline — one figure doing a lot of work

> Pip went after him like money owed.

**Why:** Not a defect, flagged for your call. The simile is on-voice (debt imagery) and compressed, but *money owed* chases someone slowly and inevitably, whereas Pip is described everywhere else as fast and direct. The vehicle and the tenor pull opposite ways.
**Suggested rewrite:** `Pip went after him like a man collecting.`

## Verified, not flagged

- `Pip looked at me. Are we chasing him, boss, or not?` — the source has this inside a GM line (*"Alright, Pip turns to you. Are we chasing him, boss, or not?"*). Correctly unwrapped, correctly attributed to Pip, and correctly rendered as unquoted reported speech so it is not passed off as a verbatim Pip quote. Good handling.
- `"You're the guy with the fingers who knows how to open the locks. I'm the guy with the sword that knows how to."` — now tracks the **smoothed** layer; the previous run carried the raw `"You're the, you're the guy…"` stutter.
- `"So, you and Veyra can go behind the Redbrand Ruffian, and Sister Maela will help."` — **Redbrand** singular, correct. The previous run pluralised it to *Redbrands*.
- `All right, wait — you're gonna just leave us here?` — now matches the smoothed text; the previous run carried the raw `"you're, you're"` stutter.
- `"Yay! I've been saved!"`, `"Wait, where did he run away? Like, which way?"`, `"Okay."`, `"Not yet"`, `"Quite possible. Okay, yeah, yeah…"`, `"Interesting."`, `"Shit, okay, he ran again."`, `"I see, I hear some footstep."`, `"I'm gonna… my job here is done"`, `"Just stay here until I come back"` — all verbatim.
- **Mechanical scan B: one hit, dismissed as a false positive.** *"the shrinking shape of the runner"* (line 63) is ordinary physical description — a silhouette at distance — not the analytical/architectural sense the scan targets. No register defect in this scene.
- *"I carry a whip, which is a rope with opinions"* — invented and excellent.
- *"That is a line of credit I try not to overdraw"* — the freed prisoners' trust priced as credit. On-spec.

## Verdict

No verbatim defects and no register defects — the only genuinely clean scene of the eight on both counts. All three quotes that tracked the raw layer in the first run now track the smoothed layer, which is the clearest per-scene evidence that the input-path fix took. Eight em-dashes to convert and one optional simile; nothing else.
