# Real-world name flags — session 20260830, Chapter 34

Cues in this session's tape carry the real-world first names of people at the table. **They stay
raw in the transcript and in the correction record** — a player's name is not a misspelling, and
silently replacing it would be a name change made by inference. They are listed here so the
downstream `/scrub` pass catches them before anything is published or shared with players.

GM rulings: 2026-09-05 via the Stage 2 review ledger (the three scene-level flags then known), and
2026-09-05 via the `/voice-smooth` review ledger (card S01, adding **George**).

## Surfacing in `scene_extractions/` — these reach narration

| Cue | Speaker label | Line | Real person | Character |
|---|---|---|---|---|
| 200 | Kostadis Roussos | "**Nick**, you're the completionist." | Nicholas Roussos | Sequoia |
| 750 | Kostadis Roussos | "Alright, **Nick**, good for avoiding the surprise round." | Nicholas Roussos | Sequoia |
| 1023 | Kostadis Roussos | "**George**." (calling the player for a Wisdom save) | George | Zinnia |
| 1265 | Kostadis Roussos | "…what did we say about the Minotaur? Sorry, **Thomas**, I forgot." | Thomas Kolivakis | Zephyr |

Cue 1265 formerly appeared in **both** scene 04 and scene 06. The Stage 2 X01 ruling moved the
departure-orders exchange to scene 06, so it now surfaces **once** (verified 2026-09-05).

## In the tape but not in any scene extraction

Recorded for completeness — the `/scrub` pass operates on the transcript, so these matter if the
tape itself is ever shared, even though no scene file carries them.

| Cue | Line | Where |
|---|---|---|
| 4 | "When's **George**?" | pre-session, before the 00:11:25 recap boundary |
| 10 | "Is, **Thomas** not… is **George** on the call?" | pre-session |
| 74 | "They won, what did they win, **Nick**? 15, 20, 23?" | pre-session frisbee chatter |
| 94 | "So, like, what did you tell me, **Nick**?" | pre-session frisbee chatter |
| 416 | "Unless you really enjoy watching me, butts with it. **Nick**?" | mid-session table talk, not extracted |
| 1088 | "**Nick**." | mid-session, not extracted |
| 1307 | "Okay, go, why don't you go eat, **Nick**? Your food's here, right?" | post-session |

**Tape-level total: 11 cues, 12 occurrences — Nick ×7, George ×3, Thomas ×2.** All spoken by
Kostadis Roussos except cue 4 (Nicholas Roussos).

> Census corrected 2026-09-05 during `/voice-smooth`. This file previously said "three cues", which
> was true of the scene extractions as they then stood but not of the tape. The scene-level list
> above is what the earlier count described.

## Why these are flags and not corrections

`notes/vtt_transcription_corrections.md` keeps a "Players (real-world names — never replace, just
flagged as known)" section for exactly this reason — and **George** was already listed there before
this session; it had simply never surfaced in a scene extraction. Replacing "Nick" with "Sequoia" in
the record would assert that the GM addressed the character when he addressed the player, which is
false and loses the table's texture. The scrub pass is where publication-facing anonymisation
belongs.

## Standing question for this campaign

`toee/` has no `notes/scrub_register_policy.md`. Real-world names recur — **11 cues in this session
alone** — so that file is where the standing ruling belongs: whether this campaign scrubs player
first names before sharing, and to what (initials, character names, or removal). Tracked as CF20.
