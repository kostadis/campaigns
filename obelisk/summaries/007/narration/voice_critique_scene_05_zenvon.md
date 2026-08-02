# Voice Critique — Zenvon, scene 05: The Pit Trap and the Cellar

**Narration:** `summaries/007/narration/session_doc_scene_05_the_pit_trap_and_the_cellar.md` (re-run 19:13)
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

## Flags

### [1] Register-wrong figure — a verb from the wrong world

> Behind me, Veyra's fire went past the both of us and married the far wall.

**Why:** *Married* is a lyrical, faintly whimsical verb — the kind of choice the spec rules out (*"Anything florid or lyrical about a landscape, a ruin, or his own emotional state"*). The first run's version of this beat was better and blunter: *"The wall did not deserve it."* Zenvon reports a miss as a wasted expenditure, not as a union.
**Suggested rewrite:** `Behind me, Veyra's fire went past the both of us and spent itself on the far wall.`

### [2] Tell-not-show — an emotional claim the scene has not earned in his register

> That woman's hands are worth more than everything in my pockets, and I have never told her so, and I will not start now.

**Why:** The first two clauses are excellent — Maela's healing valued in his own currency, which is exactly right. The third clause narrates his own reticence rather than performing it, and the spec is specific that his silences are the characterisation (*"He has never once justified any of it out loud, and nobody has asked… That silence is characterization"*). Announcing that you will not say a thing is a way of saying it.
**Suggested rewrite:** `That woman's hands are worth more than everything in my pockets. I have never told her so.`

### [3] Mechanical scan A — em-dashes in narration prose (4 — second-lowest of the session)

| Line | Fragment | Suggested |
|---|---|---|
| 15 | `should cost more than it did — he was bruised and annoyed` | `should cost more than it did. He was bruised and annoyed` |
| 21 | `the arithmetic worked out — his weight against my footing` | `the arithmetic worked out: his weight against my footing` |
| 35 | `opened onto a landing — a small one, fifteen feet above` | `opened onto a landing: a small one, fifteen feet above` |
| 41 | `looked for him — scuff marks, a door still moving, anything` | `looked for him: scuff marks, a door still moving, anything` |

**Mechanical scan B:** clean. (The previous run's apparent *file* hit was *single file*, a false positive; that phrasing is gone from this draft.)

## Verified, not flagged

- **`"I have a whip, okay, so I'm gonna use the whip as a rope,"` is correctly attributed to Zenvon.** In the smoothed source this sits inside a **GM** block that I tagged inline during the voice-smooth pass: `> "Well, actually, you can… [Zenvon] I have a whip, okay, so I'm gonna use the whip as a rope to…"`. The narration resolved the `[Zenvon]` tag and assigned the speech correctly rather than voicing the GM. This is direct evidence that the inline mixed-attribution tagging did its job — worth knowing before deciding whether to re-attribute those blocks upstream.
- `"And I try to help him"`, `"So that I can pull it off"`, `"So, so we carefully move past the trap"`, `"Around it, yes, yes, and being more careful"`, `"Avoid any other traps"`, `"Yes, yes, I don't see anything where it's leading, but yes"`, `"So, there is, like, a water…"`, `"And I see some barrels, okay. The front door onto the west."`, `"Okay, let's follow this guy"`, `"This guy has told everybody"`, `"There's no choice"`, `"He leaves us no choice other than to attack"` — all verbatim.
- ESL markers intact: doubled acknowledgement (*"yes, yes"*, *"Got it, got it"* woven into prose at line 35), the `"So,"` opener, and `"like,"` as a mid-sentence marker in *"So, there is, like, a water…"*.
- `"I'm just at 4 points of damage"`-class mechanics — **no equivalent stripping occurred in this scene.** The scene-01 defect did not generalise.
- *"a hole twenty feet deep with Pip in it, looking up at me with the expression of a man who has been overcharged"* — invented, on-voice, and funnier than the first run's version.
- *"I noted it and did not look inside it, which is the kind of decision you remember later"* — a genuinely good piece of foreshadowing for the scene-07 cistern, built from what the party actually did (noted the cistern, did not search it).

## Verdict

Two soft spots — one lyrical verb, one narrated silence — and the fewest em-dashes of any combat-adjacent scene. The `[Zenvon]` tag resolving correctly is the most useful finding here, because it tells you the inline tagging approach works and the seven mixed-attribution blocks do not urgently need upstream re-attribution. Spot-edit.
