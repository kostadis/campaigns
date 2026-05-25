---
name: gm-session-prep
description: Generate a co-GM session prep document for the active campaign in the style of toee/notes/phase3_endgame.md — win condition, default trajectory, branches, scene staging, anticipated player questions. Invoke when the user says "prep the next session", "co-gm me", "help me run the next session", "/gm-session-prep", or asks for help thinking through what happens at the next table. The output is a working doc for the GM to read at the table, not a player-facing handout. This is the foundational co-GM prep skill; other skills (gm-faction-network, gm-strategy-doc, gm-handout, gm-npc-build) are narrower specializations.
---

# gm-session-prep

The co-GM prep workflow that produced `toee/notes/phase3_endgame.md`. The output is a **working doc the GM reads before and during the session** — not narrative prose, not a player handout.

## When to invoke

Trigger phrases:
- "prep the next session"
- "co-gm me"
- "help me prep/run the next session"
- "/gm-session-prep"
- Any "help me think through what happens when [event]"

Refuse politely if the working directory is not inside one of the campaign subdirs (`Phandalin/`, `out-of-the-abyss/`, `Hillsfar/`, `toee/`, or a future sibling). The skill is campaign-scoped — see `campaigns/CLAUDE.md` for the isolation rule.

## Inputs to confirm (one at a time, via AskUserQuestion)

Only ask for things you can't infer. If the user already supplied an answer in the invocation, skip that question.

1. **The beat.** What does the user want this session to *do*? One sentence. ("The party arrives in Kelno's quarters", "the cult attacks the wedding", "the merchant prince tests the party's loyalty.")
2. **Genre/tone.** Political thriller? Dungeon crawl? Heist? Comedy of errors? Horror? This is the single most useful framing the user can give — it determines pacing, NPC density, and which moves to pull from the style sheet. Default if pressed: "whatever fits the current campaign state."
3. **Player level.** Numeric. Affects which threats are existential vs trivial. The user's own recipe was "the players were 15."
4. **Anything else load-bearing the docs won't tell you.** E.g., "one player is missing this week", "we're running short — needs to wrap in 90 minutes", "I want to introduce X NPC."

## Required context (read in this order)

Read from the current campaign's `docs/` and `summaries/`. If a path doesn't exist in this campaign, skip it and note the gap rather than failing.

1. `docs/campaign_state.md` — current state of the campaign
2. `docs/world_state.md` — the world's current state (factions, weather, calendar)
3. `docs/party_state.md` or `docs/party.md` — who the PCs are right now
4. `docs/background/` — campaign background lore (read selectively if large; prioritize files matching the beat)
5. The **last two session summaries** under `summaries/YYYYMMDD/` — most recent first. These are the *authoritative* record of what just happened.
6. `docs/npcs/` — selective. Read dossiers for any NPC the user named in the beat, plus their lieutenants.
7. If a `mempalace` is configured (`.mcp.json` lists it), assume the user can also retrieve scene-level detail via search — but don't depend on it.

Do **not** read other campaigns' directories. Do **not** invent canon — if a fact isn't in the docs, mark it as a decision the user needs to make.

## Style notes for this output

Co-GM prep docs in this workspace follow a recognizable shape. The user has corrected explicitly: **this is fanfic-narrative GMing, not lit-RPG.** That means:

- **Strategic clarity over mechanical exhaustion.** State the win condition plainly. State the default trajectory if the party does nothing. State the optimal play. Don't drown the GM in stat blocks — they have those elsewhere.
- **Branches, not rails.** For every choice point, sketch ≥2 paths. The party *will* go off-script; pre-stage the off-script.
- **Antagonists get interiority.** Even one-scene NPCs need a stake, a worry, a small goal. The party may never learn it; the GM needs to know it to play the NPC right.
- **Failure is comedic and material.** If a roll fails, what does the party *lose*? (A bow. A reputation. An ally's trust. Not "you take damage.")
- **In-fiction vs GM-only is explicit.** Mark which information the players can pick up and which is GM-only. Use quoted-block (`>`) for GM-only.
- **Theatrical timing matters.** When to be silent. When to escalate. When to let an NPC interrupt. Call these out as stage directions.
- **Modern register is fine.** Contemporary jokes, management-speak, references — all in bounds. Don't force "thou."
- **The Tenday calendar is real.** Use FR date stamps when relevant.

## Output shape

Use `toee/notes/phase3_endgame.md` as the template. The headings vary by session shape, but the canonical structure is:

```
# {Session title — evocative, not functional}

Co-GM working doc. Not canon yet — staging for {what session}.

## The Win Condition (state plainly to yourself)
{One paragraph. What state must obtain for this session to count as "landed"?}

## The Default Trajectory (what happens if the party does nothing)
{Bulleted. The fates of each major NPC/faction if the party is passive.}

## The Clever Play (what the optimal party would do — the GM should know this)
{Numbered. Not because the party must do this, but so the GM knows when to nudge.}

---

## {Scene 1 — name}

### Setup
- Time and place in-fiction.
- Who's present, who's offstage.
- Map/area references if applicable.

### Approach — {sub-area or first beat}
{Prose + dialogue snippets the GM can lift verbatim if the moment lands.}

### Branch — if the party {does X}
{Consequence + how the next scene shifts.}

### Branch — if the party {does Y}
{Consequence + how the next scene shifts.}

### NPC notes
- **{NPC}** — one-line current motivation, one-line voice tic, what they want from this scene.

---

## {Scene 2 — name}
...

---

## Anticipated player questions
- **"What about {X}?"** → answer the GM should give, plus what's *not* answered.
- **"Can we just {bypass plan}?"** → the path-of-least-resistance the GM should leave open or close.

## Stage directions (timing/silence cues)
- When the party reads {handout}, leave a beat before reacting.
- If {NPC} is killed, don't fill the silence.
- {Other moments where pacing carries the weight.}

## Open decisions (for the user — don't decide for them)
- {Things the canon-and-state docs don't answer that the GM needs to pick before play.}
```

## Steps

1. Read the docs in the order above. Take ~5 minutes of clock time max — don't try to absorb everything; scan for what matters for this beat.
2. Ask the 1-4 inputs the user hasn't supplied, one at a time.
3. Draft the doc to `notes/session_prep/{YYYYMMDD}_{slug}.md` if that path exists, else to `notes/{slug}.md`. The user can move it.
4. Open with a 2-3 sentence summary of what you understood from the docs so the user can catch you if you misread.
5. Produce the working doc.
6. End with **Open decisions** explicitly. Don't decide things the user should decide.

## What this skill is NOT for

- Writing player handouts (use `gm-handout`)
- Building a faction operational map (use `gm-faction-network`)
- Per-NPC strategic dossier (use `gm-strategy-doc`)
- Designing a single NPC (use `gm-npc-build`)
- Mid-session improv (use `gm-improv`)
- Writing up what happened *after* the session (that's CampaignGenerator's job, not this skill)
