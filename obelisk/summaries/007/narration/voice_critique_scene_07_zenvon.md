# Voice Critique — Zenvon, scene 07: The Bandit's Gambit

**Narration:** `summaries/007/narration/session_doc_scene_07_the_bandit_s_gambit.md` (re-run 19:14, **registry disabled**)
**Voice spec:** `voice/zenvon_voice.md`
**Per-char examples:** `examples/zenvon.md`
**Party doc:** `docs/party.md`

> This is the scene that carried the registry name-leak in the first run. **All four instances are gone.** See "Verified" below.

## Flags

### [1] Borderline register — *shape* used abstractly

> He gave me nothing but the shape of his fear: "Look, dude, I just carry crates, alright?…"

**Why:** Mechanical scan B hit, and a marginal one — *shape* here is metaphorical rather than architectural, and "the shape of his fear" is a defensible image. Flagged because it is the one place in this scene where an abstract noun stands in for something he would normally quantify. Zenvon reads people as amounts: what a man knows, what he will sell it for, how long he will hold.
**Suggested rewrite:** `He gave me nothing but the size of his fear` — or, closer to his idiom: `He gave me nothing but what his fear was worth.`

### [2] Tell-not-show — a refusal to describe, described

> Nobody argued. It did not take long, and I am not going to describe it, because there is nothing in it worth describing.

**Why:** Same pattern as scene 05 flag [2]. The spec is emphatic that the silence after violence *is* the characterisation (*"He kills and moves on; the silence is the point"* / *"Moral self-justification after violence"* is listed under **Things They'd Never Say**). Announcing the refusal converts a silence into a statement about a silence — and the sentence immediately after it (*"He was a man who would run. Now he is a man who will not"*) already does the job perfectly, flatly, and without comment.
**Suggested rewrite:** Cut the middle clause. `Nobody argued. It did not take long. He was a man who would run. Now he is a man who will not.`

### [3] Mechanical scan A — em-dashes in narration prose (6)

| Line | Fragment | Suggested |
|---|---|---|
| 31 | `He knew nothing about it — I believed that part — but the name had weight` | `He knew nothing about it, I believed that part, but the name had weight` |
| 39 | `I was reading him — the eyes, the hands, the too-quick agreement — and the reading was clean` | `I was reading him: the eyes, the hands, the too-quick agreement. And the reading was clean` |
| 57 | `hung a waterproof satchel — a potion of healing and a potion of invisibility` | `hung a waterproof satchel: a potion of healing and a potion of invisibility` |
| 59 | `two garnets on the third — ten gold each, by my eye` | `two garnets on the third, ten gold each, by my eye` |

## Verified, not flagged — the first-run defects are all repaired

| First run | This run | Source |
|---|---|---|
| `"Tell me more about Iarno and Nezznar the Spider…"` | `"Tell me more about Glasstaff and Spider…"` | ✅ verbatim |
| `"The Black Spider. Nezznar."` | `"Black Spider," I said.` | ✅ verbatim |
| Wick: `"I — Iarno? Man, he's like some scary shit…"` | Wick: `"I didn't — Glasstaff? Man, he's like some scary shit…"` | ✅ verbatim |
| prose: *"Iarno answers to somebody"* | prose: *"Glasstaff answers to somebody"* | ✅ |

**"Nezznar" now appears zero times in the narration.** Per `campaign_state.md:65` the Black Spider is *"confirmed real… No name, no face, no location"* — the party does not have that name, and it is no longer in a PC's mouth. `--reflections` cannot reintroduce it: the string appears zero times in both `campaign_state.md` and `world_state.md`.

Also repaired:

- **`"Yeah, I mean, I would prefer to attack him at this point instead of letting him run away,"`** — now the actual session line. The first run substituted the *examples file's* wording (*"I would prefer to eliminate him…"*), pulling a sentence out of `examples/zenvon.md` and presenting it as spoken. Correct now.
- `"There's a little bit of fairness in what you're saying, but—"`, `"Be a nice guy with us"`, `"I cannot guarantee anything, or you can join us"`, `"Okay… Are you really interested to join us?"`, `"Of course I'm with you, boss"`, `"In order to trust you…"`, `"Like, what's upstairs?"`, `"Did we get anything here? There are so many crates and barrels."` — all verbatim.
- Wick's long plea (line 11) is merged from the gm-assist summary bullet, which the extraction marks *"(from gm-assist, verbatim)"*. Legitimate source.
- `"Be a nice guy with us"` — preserved unchanged per the ESL ruling; not normalised to idiomatic English.
- Wick's third-to-first-person slip is rendered as narration (*"He said *Wick's only ever been sent* and then caught himself"*) rather than silently smoothed. Good handling of a detail the extraction explicitly flagged.
- The coin tally (16s/7g, 12s/5g, 20c/11e, 2 garnets @ 10g) matches the source exactly.

## Verdict

The registry leak is fully closed and the examples-file substitution is gone — the two most serious defects in the first run, both fixed, both verified against source rather than assumed. What remains is one abstract noun and one narrated silence, and the narrated silence is the more interesting note because it recurs in scene 05. Spot-edit.
