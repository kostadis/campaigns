# Voice Critique — Gyrgum, scene 04: The Spectral Silver Dragon's Trial

**Narration:** `session_doc_scene_04_the_spectral_silver_dragon_s_trial.scrubbed.md`
**Voice spec:** `voice/gyrgum_voice.md`
**Per-char examples:** `examples/gyrgum.md`

## Flags

### [1] Narrator name drift (metadata) — line 4

> narrator: Gyrgum

**Why:** Every other mention in the session spells him **Grygum** (35 occurrences in prose); his own voice file is titled "# Grygum — Voice Notes". This frontmatter is the only "Gyrgum" anywhere, and `assemble.py` reads it to build the section heading.
**Suggested rewrite:** narrator: Grygum

### [2] Stock phrase — line 200

> We were trading the lock on the exits for the silence inside. We made the trade with our eyes open.

**Why:** "with our eyes open" is a stock idiom doing the work Grygum normally does with a concrete price. His register names the cost out loud (cf. "The precedent is thin. It is not zero.").
**Suggested rewrite:** We were trading the lock on the exits for the silence inside. We knew what we were paying and we paid it.

### [3] Kind-of-person attribution — line 88

> The words had gone out of my mouth and the stairs had not eaten us afterward, which is the kind of correlation a working priest learns to respect.

**Why:** Adjacent to the banned "with the particular [noun] of [someone who…]" portrait — it attributes the habit to a *category* of person. Grygum can simply own it in first person.
**Suggested rewrite:** The words had gone out of my mouth and the stairs had not eaten us afterward. I have learned to respect a correlation like that.

## Verdict
The frontmatter misspells the narrator as Gyrgum, which will propagate into the assembled section heading; fix that before assembly regardless of the prose flags. The prose itself is the strongest in the session — "an orc with a mace and a loud opinion" and the Protanther chessboard both land — with only one stock idiom worth touching.
