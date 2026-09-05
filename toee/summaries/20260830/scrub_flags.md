# Real-world name flags — session 20260830, Chapter 34

Three cues carry the real-world first names of people at the table. **They stay raw in the
transcript and in the correction record** — a player's name is not a misspelling, and silently
replacing it would be a name change made by inference. They are listed here so the downstream
`/scrub` pass catches them before anything is published or shared with players.

GM ruling 2026-09-05, via the Stage 2 review ledger (all three accepted).

| Cue | Speaker label | Line | Real person | Character |
|---|---|---|---|---|
| 200 | Kostadis Roussos | "**Nick**, you're the completionist." | Nicholas Roussos | Sequoia |
| 750 | Kostadis Roussos | "Alright, **Nick**, good for avoiding the surprise round." | Nicholas Roussos | Sequoia |
| 1265 | Kostadis Roussos | "…what did we say about the Minotaur? Sorry, **Thomas**, I forgot." | Thomas Kolivakis | Zephyr |

Cue 1265 sits inside the departure-orders exchange that appears in **both** scene 04 and scene 06,
so it will surface twice in any scene-level pass until that overlap is resolved.

## Why these are flags and not corrections

`notes/vtt_transcription_corrections.md` keeps a "Players (real-world names — never replace, just
flagged as known)" section for exactly this reason. Replacing "Nick" with "Sequoia" in the record
would assert that the GM addressed the character when he addressed the player, which is false and
loses the table's texture. The scrub pass is where publication-facing anonymisation belongs.

## Standing question for this campaign

`toee/` has no `notes/scrub_register_policy.md`. If real-world names recur — and on this evidence
they do, three times in one session — that file is where the standing ruling belongs: whether this
campaign scrubs player first names before sharing, and to what (initials, character names, or
removal).
