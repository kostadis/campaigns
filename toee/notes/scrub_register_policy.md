# Scrub / cut register — Temple of Elemental Evil

Standing rulings shared by `/scrub`, `/no-mech` and `/voice-smooth`. **Read this before any of
those three runs.** Nothing in here is scannable — no pattern finds it — so without this file the
next run re-proposes settled questions, and re-asking a settled question puts a settled ruling
back at risk.

Created 2026-09-05 (GM ruling, `/no-mech` on session 20260830). Closes CF20, open since Stage 2.

---

## 1. Player real-world names — FLAG, never replace

Cues where the GM addresses a player by their real first name stay **raw** in the tape, in
`transcript_corrections.yaml`, and in the smoothed layer. A player's name is not a misspelling, and
substituting the character's name would assert that the GM addressed the character when he
addressed the player — false, and it loses the table's texture.

`notes/vtt_transcription_corrections.md` carries them under "Players (real-world names — never
replace, just flagged as known)": **Kostadis Roussos, Nicholas Roussos, Thomas Kolivakis, George**.

Per-session registers live in `summaries/<date>/scrub_flags.md`. That file's scope is the **tape**,
not the scene extractions — count accordingly. (Session 20260830: 11 cues, 12 occurrences at tape
level; only 4 reached the scene extractions, and 2 of those 4 were later removed by `/no-mech`.)

**Still open:** whether this campaign anonymises player first names before anything is shared with
players or published, and to what — initials, character names, or removal. Not yet ruled. Until it
is, the flags exist so a publication-facing pass can act on them.

## 2. Table/tooling logistics — CUT, do not smooth

*(GM ruling C6, `/voice-smooth` on 20260830. Standing.)*

Content where the table is operating the software rather than playing the game is **deleted** from
`scene_extractions_smoothed/`, not lightly smoothed. It carries no narratable content.

In scope: Roll20 token and map handling ("let me just put them here", "let me just pull up this arm
as a blah blah blah", "Let me just mark them as surprised"), client questions ("are you guys on the
Roll 20?"), character-sheet reading aloud ("You should see a number there"), and off-mic real-world
asides to someone not at the table.

Each affected file carries an italic note naming what was cut, so the omission is auditable rather
than silent. Deleting is distinct from marking `[unclear]`, which is reserved for lost *meaningful*
content.

## 3. Table mechanics — CUT, by scene, with the GM ruling each scene

*(GM rulings, `/no-mech` on 20260830.)*

The classifier is **who is being spoken to**, not "is this mechanical":

| | Ruling |
|---|---|
| In-character speech (PC or `*as <NPC>*`) | **KEEP** |
| GM read-aloud / scene description / boxed text | **KEEP** |
| GM-to-player-as-player (rolls, AC, turn calls, rules Q&A) | **CUT** |

Settled sub-rulings for this campaign:

- **Player reactions to dice are KEEP when they are about the fiction.** Sequoia's meltdown over
  rolling 36 on 12 dice was kept, because it runs into his curse at Frostbrand — his intelligent
  sword. Pure table speech by the classifier; kept anyway. Do not re-propose cutting it.
- **Rules lectures are CUT** even when the GM is teaching a real feature (the Stunning Strike
  explanation in scene 03).
- **GM characterisation of a PC is KEEP** even mid-combat — "Calmer does the usual thing he does in
  these situations", "Calmer's really into the whole Spirit Guardians thing".
- **Combat-resolution lines that describe the fiction are KEEP** — "It furiously attacks with all
  five of its limbs", "misses all five times". Lines that only move numbers are CUT.
- Whether to cut category-2 GM world-building exposition has **not** arisen in this campaign yet and
  is not settled.

## 4. Two campaign-specific traps for these skills

**The NPC-label triage signal is permanently dead here.** toee's extractor never breaks NPCs into
their own speaker label — every NPC line is `**GM** — *as Varek Solain, …*`. `scan_quotes.py` will
therefore triage every scene as "no NPC speaker labels; may be all-mechanical", on every future run,
regardless of content. **Classify on the italic stage direction instead.**

**`**GM**` is not only the GM.** Kostadis is both the GM and Calmer's player, and since
`config/players.yaml` gained `gm: true`, every one of his lines carries the GM label — including
Calmer's. A PC's entire performance sits under `*as Calmer,*` directions inside GM-labelled blocks.
Never cut on the `GM` label alone.
