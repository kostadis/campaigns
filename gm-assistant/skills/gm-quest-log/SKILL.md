---
name: gm-quest-log
description: Build a player-facing quest log for the active campaign — every open promise, contract, errand, and personal thread the party currently knows about, reconstructed from session summaries rather than the grounding docs. Written in the voice of a party member who keeps notes, so it can be handed straight to players. Invoke when the user says "what quests do the players have open", "make a quest list", "player-facing quest log", "what are the party's open threads", "/gm-quest-log". Output goes to notes/handouts/quest_log.md. Player-knowledge only — never module trackers, dossiers, or GM secrets.
---

# gm-quest-log

Produces the list of open business the *party* believes it has. Not the list the GM is tracking — the list the players would write down if one of them kept a notebook, which is a strictly smaller and more interesting document.

The value is in the gap. What the party thinks it owes, who it thinks it owes it to, and which threads it has noticed but nobody has paid it to pursue.

## When to invoke

- "what quests do the players have open"
- "make me a player-facing quest list"
- "what's the party actually chasing right now"
- "give the players a quest log"
- "/gm-quest-log"

## The rule that matters most: rebuild from summaries, not grounding docs

**The grounding docs will be stale, and they will be confidently stale.**

`docs/campaign_state.md`, `docs/world_state.md`, `docs/planning.md`, and `docs/party.md` are pipeline outputs regenerated on a cadence that does not match play. In the obelisk campaign they were four chapters behind: `campaign_state.md` listed Glasstaff as "not yet confronted" when the party had already fought him, wounded him, and watched him teleport away — and listed Halia as "unvisited" three sessions after she was interrogated at the Sleeping Giant.

A quest log built from those docs would have handed the players quests they had already finished.

So:

1. **Session summaries are the source of truth.** Read every one, oldest to newest.
2. **Grounding docs are a cross-check only** — useful for catching a thread you missed, never for setting status.
3. **When a summary and a grounding doc disagree, the summary wins.** Say so in the report-back.

## Required context (read in this order)

1. `ls summaries/*/` — enumerate every session directory. Sessions are numbered dirs; the session doc inside is titled, not named `session-summary.md`, so glob for `summaries/*/*.md` rather than guessing a filename.
2. Every session doc, **oldest first**. The `## Scenes` and `## NPCs` sections carry quest offers; `## Summary` carries the outcome.
3. Any session dir with no session doc — check for `gm-assist.md` instead. A missing summary does not mean a missing session, and quests get handed out in exactly those gaps. (obelisk session 004 had no summary and contained two of the campaign's four paid contracts.)
4. The campaign's opening doc if present (`notes/open.md`, `notes/session1_*.md`) — the founding job usually lives there and nowhere else.
5. The four grounding docs, last, as a cross-check.

## Method: walk the timeline, log offers, then close them

For each session in order, record two things:

- **Promises opened.** An NPC offered work, named a price, asked a favour, or extracted an agreement. Capture *who asked*, *the terms*, and *what the party was told*.
- **Promises closed.** The party did the thing, or the thing became moot on-screen.

A quest is open if it was offered on-screen and never closed on-screen. Anything else is inference — and inference goes in the report-back to the GM, not in the handout.

**Partial closure is the most common state and the most interesting one.** "Find Iarno Albrek" was not open, and not closed — the party found him, identified him, wounded him, and lost him. That is a third thing, and the log should say so in the party's own terms.

## The leak checklist — run this before writing a line

Player-facing means the document contains only what the party has seen, been told, or reasonably inferred at the table. Before including any item, ask: *when did a player learn this?* If there's no answer, it doesn't go in.

**Never include, under any circumstances:**

- **Module trackers.** Files like `docs/oblesik_tracking.md` are the full published-adventure checklist across every chapter — future villains, unrevealed identities, the ending. Do not read from it for this skill. It will hand you the campaign's biggest reveals in a bulleted list.
- **`docs/npcs/` dossiers and `notes/*_strategy.md`** — these are the NPC viewed from inside their own head.
- **The `## DM Notes` section of `planning.md`** and anything under a "Hidden:" label in a dossier.
- **Secrets held by friendly NPCs.** Daran Edermath being a 500-year-old drow is in `world_state.md`; no player has been told.
- **Extractions.** `distill_extractions/`, `planning_extractions/` are search accelerators over GM material.
- **Mechanical GM state.** Threat-arc scores, encounter CRs, "the party is meant to go here next."

**Do include, because the party genuinely knows it:**

- What NPCs said out loud, including lies the party has not yet caught.
- Reveals extracted under interrogation or exposed by a monster. If a Nothic broadcast Pip's secret to the whole party telepathically, it is player knowledge now, however much Pip wishes otherwise.
- The party's own suspicions, framed as suspicion. "She is not what she pretends to be" is player-facing. "She is Zhentarim" is not.

## Voice: the party's notekeeper, not the GM

Write it as one specific party member's notebook. Pick whoever canonically takes notes — check `docs/party.md` and the voice files for a character who writes things down (Veyra of the Blue Candle, in obelisk, because she was established rereading her notes by candlelight).

This is not decoration. A named narrator solves three problems at once:

- **It bounds knowledge naturally.** A character can only write what they witnessed, so the leak checklist enforces itself.
- **It lets suspicion be stated as suspicion.** "The invitation stands anyway" carries the party's read on Halia without asserting a fact they don't have.
- **It makes the document readable at the table** instead of an administrative list players skim.

Read the narrator's voice file under `voice/` before writing. Match their register — dry, breathless, sardonic. Keep entries short; this is a working notebook, not prose.

If no character plausibly keeps notes, use a plain neutral log and say why in the report-back.

## Output shape

Write to `notes/handouts/quest_log.md`. Create `notes/handouts/` if absent.

```
# Quest Log

*Kept by {narrator}, {one clause establishing why they're the one writing}.*
*Current as of {the last on-screen event, in the party's words}.*

---

## {The founding job — the one that started the campaign}

### {Quest name in the party's words}
**Who's asking:** {or "Nobody had to ask" if it's personal}
**What we know:** {2-4 lines, only what was said on-screen}
**Where/why:** {the operative unknown}
**Status:** {Open / Urgent / etc, in plain speech}

---

## Paid Work
{Contracts with named patrons and stated terms. Include the actual gold figure
and who negotiated it — players remember the haggling. Note partial progress
explicitly: found-but-escaped, started-but-abandoned.}

## Unfinished Business at {current location}
{Things the party walked away from mid-solve. Barricaded doors, unexplored
levels, monsters left alive behind them. This section is usually the most
actionable and is almost never in the grounding docs.}

## Errands and Offers
{Undelivered goods, standing invitations, quests offered but not accepted,
NPCs owed a follow-up.}

## Our Own Business
{Per-character personal threads. One block per character with a live thread.}

## Things Nobody Has Hired Us For, Which We Notice Anyway
{Unexplained events, unanswered questions, names with no referent. Short
bullets. This is where foreshadowing lives without becoming a quest.}

---

*{One closing line the narrator would write — the pattern they've spotted but
can't name yet. Only if the threads genuinely converge; skip it if they don't.}*
```

Section names should bend to the campaign. The shape is: **the spine, the paid work, the immediate mess, the small stuff, the personal, the unexplained.**

## Steps

1. Enumerate `summaries/*/` and read every session doc oldest-first. Check gap sessions for `gm-assist.md`.
2. Read the opening doc for the founding job.
3. Build the offer/closure ledger. Note every disagreement with the grounding docs.
4. Run the leak checklist over the candidate list.
5. Pick the narrator; read their voice file.
6. Write `notes/handouts/quest_log.md`.
7. **Report back to the GM separately** — see below. This part does not go in the file.

## The report-back is not optional

The handout is a rendering of state; the GM is the only one who can confirm the state is right. End every run with a short list, in chat and not in the file, covering:

- **Contradictions found** — where a grounding doc disagreed with a summary, and which one the log followed.
- **Genuine uncertainties** — things the summaries left ambiguous. The obelisk run surfaced barricaded bugbears that session 006 shut behind a door and session 007 never mentioned again; the log listed them as alive, flagged for the GM to overrule. State the assumption, don't silently pick.
- **Anything omitted as a GM secret** that the GM might have intended the players to have.
- **Continuity noise** — names spelled two ways across summaries ("Forepot" / "Foreput"), NPCs merged or split by transcription error. These belong in the spell-pass glossary.

Do not fold these into the handout as caveats. The players get a clean document; the GM gets the diff.

## What this skill is NOT for

- GM-side thread tracking or "what should happen next" (use `gm-session-prep`)
- An in-world artifact the party *finds* — a letter, notice, ledger (use `gm-handout`)
- Faction intel and who-really-runs-this-town (use `gm-faction-network`)
- Regenerating `campaign_state.md` — that's the CampaignGenerator pipeline, not this skill. This skill never writes to `docs/`.
</content>
