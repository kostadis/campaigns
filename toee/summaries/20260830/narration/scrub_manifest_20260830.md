# /scrub manifest — session 20260830, Chapter 34 "The Sleeper in the Iron Coffin"

Run 2026-09-05, first `/scrub` for this campaign. Six narration scenes reviewed;
two produced a `.scrubbed.md`. The originals are untouched.

## Scanner vs reading pass

`find_residue.py` returned **1 candidate across all six scenes** (`dice_verb`,
"I rolled", scene 02 line 213). The reading pass found **three more classes**, one of
which was a 12-span block the scanner saw one line of. As the skill says: a
zero-candidate scan is not a clean scene.

**`--party-md` loaded ZERO of four player names.** `load_player_names` matches a
literal `Player:` prefix; `docs/party.md` writes `**Player:** Kostadis Roussos`, and the
`**` defeats the regex. So `player_name` detection was entirely inactive this run. It
did not matter here — a manual census confirmed no real-world player name reached any
narration prose — but it will matter on a session where one does. Same tooling gap the
skill documents for Phandalin's roster format.

## GM-authored divergences

| Scene | Line | Tape / narrated text | Scrubbed text | Class |
|---|---|---|---|---|
| 02 | 191 | "Oh, I can roll off crit damage." | "It's wide open. This is over." | dice talk |
| 02 | 195 | "Oh, I need to still roll another 5— HOLY DICE!" | "Come on— COME ON!" | dice talk |
| 02 | 205 | "The di— SHIT!" | "The blade— SHIT!" | orphaned fragment |
| 02 | 209 | "Effective damage in total on my critical." | "That's all of it. That's everything it had." | dice talk |
| 02 | 213 | "36, sorry. You wanna know how many dice I rolled?" | "Sorry. You want to know the worst part?" | dice talk |
| 02 | 215 | "12!" | *(removed)* | dice count |
| 02 | 217 | "12 of that damage!" | *(removed)* | dice count |
| 02 | 221 | "You want the total amount of damage I dealt with?" | *(removed)* | dice talk |
| 02 | 225 | "Average of bloody two, bro!" | "Bloody two, bro. Every one of them." | dice talk |
| 03 | 29 | "Wait— yes. In the classic fashion, I look at the ceiling to see if there's any answers." | *(removed)* | OOC action declaration |

Every row is a **deliberate divergence from the tape**, GM-approved. A fidelity check
will flag all nine as transcription errors; they are not. Do not "fix" them back.

**How the scene-02 block arose is worth recording.** The GM ruled Sequoia's dice
meltdown KEEP during `/no-mech`, so it survived into the narration input — and fable
rendered it literally, as a player reading dice results aloud mid-combat. The ruling
was made at the extraction layer about *whether the beat stays*; nobody had ruled on
*how it should read as prose*. Those are two different decisions and this run is where
the second one got made: keep the fury, drop the numbers. The narrator prose around it
("I stared at the result." / "I counted twice." / "It was insulting.") was already
carrying the beat.

Whitespace note: `apply_scrub.py` has no line-removal path, so `"new": ""` leaves an
empty line. The three removals left runs of 3–5 blank lines, collapsed afterwards with
a word-preserving normalisation (asserted `before.split() == after.split()`, zero words
changed).

## New canon (`provenance: on_the_fly`)

**None.** No proper noun, item, proverb or institution was invented this run. Every
rewrite was a register change to an existing line; no replacement introduced a named
entity, so nothing here needs registering and nothing is an alias.

## GM rulings on what is NOT residue

- **The modern administrative register is IN CANON** — `supply chain` (5 spans, 3
  scenes), `logistics` (4 spans, 2 scenes), `inventory control`, `procurement`,
  `operating costs`, `org chart`, `security apparatus`, `meal plan`, `government`,
  `managerial`. Settled once as a policy rather than span by span. Grounded in
  `calmer_voice.md` §The Org Chart, `zephyr_voice.md` §accounting vocabulary, and
  `_genre.md` §cover-identity drift. **This is the campaign's premise, not its
  residue.**
- **"friendly neighborhood necromancer" is KEPT** (scene 01 line 41). A Spider-Man
  echo in narrator prose, but it is the GM's own phrase from the tape and reads as
  Zephyr's dryness.
- Spell and item names were never candidates, per the skill's hard invariant:
  `Hold Monster`, `Toll the Dead`, `Spirit Guardians`, `Word of Radiance`,
  `Chill Touch`, `Meteor Swarm`, `Frostbrand`, `Mace of Smiting`, `Black Scarab`,
  `Orb of Golden Death`.
- `Earth God` (scene 03) is canon by ruling G27 in the `/voice-smooth` pass, not a
  garble.
- Dren's supply figures ("food for 3 days", "pay for 4") are in-fiction logistics, not
  mechanics. Not flagged, not changed.

## Notes

- **Scenes 01, 04, 05 and 06 were reviewed and produced no `.scrubbed.md`.** That is
  correct, not an omission — `assemble.py` prefers `.scrubbed.md` per scene and falls
  back to the raw file, so the mixed directory assembles correctly.
- All six scenes are marked `processed`. The two Phase-5 findings on scene 02 were ruled
  before it was recorded, so nothing outstanding was buried.
- The `/no-mech` pass upstream is visible in the result: five of six scenes contain no
  mechanical residue at all, and scene 03 renders Stunning Strike entirely in-fiction
  ("the focused strike that could lock a body in place") because the rules lecture was
  cut before narration rather than after.

### Phase-5 findings — surfaced, then ruled

Both were found by reading the seams **after a clean re-scan**, and both were taken back
to the GM as their own decisions rather than folded in.

1. **`"The di— SHIT!"`** → **`"The blade— SHIT!"`** (applied). The truncated word was
   *"dice"*, answering the GM's *"How much damage did you roll?"*. Redirected to
   Frostbrand, which is what the beat is actually about and what he addresses four lines
   later ("You had one job.").
2. **`"No, no."`** → **kept** (no change). On the tape it contradicted the GM's guess of
   "30 points." In its current position it reads as Sequoia waving off sympathy before
   delivering the worst part. Different from the tape, and it works.

### Correction — how those two lines were orphaned

An earlier draft of this manifest said reclassification had removed the GM's questions.
**That was wrong**, and the distinction matters.

Both GM lines — `"How much damage did you roll?"` (cue 544) and `"30 points."` (cue 548)
— **were present in `scene_extractions_smoothed/`** and were handed to `sd_narrate`.
They appear in neither the narration prose **nor the reclassification hatch**.

So fable did not reclassify them; it **dropped them silently, with no hatch record**, and
kept the answers. Reclassification writes an audit comment. This left nothing.

That is a general finding worth carrying: **fable can drop a line without leaving a hatch
record, and when the line it drops is a question whose answer it keeps, nothing
downstream flags it.** `find_residue.py` will not — an orphaned answer is not mechanical
residue. Only the Phase-5 reading pass catches it. Both of this run's Phase-5 findings
were instances of exactly this, and neither was caused by the scrub.
