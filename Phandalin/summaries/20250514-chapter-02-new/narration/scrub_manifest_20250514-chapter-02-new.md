# Scrub manifest — 20250514-chapter-02-new

Run date: 2026-09-02. Skill: `/scrub` (propose → GM review → deterministic apply).
Scenes reviewed: 8. Scenes changed: 5 (04–08). Decisions applied: 17/17, no skips.

Scanner (`find_residue.py`) produced **6** candidates across 8 scenes. The Phase 1b
reading pass produced the rest — including both classes the scanner is structurally
incapable of matching (anachronism, character-level/sheet talk).

## GM-authored divergences

Every row is a deliberate departure from the tape, approved per-candidate by the GM.
A fidelity check against the VTT will flag all of these. **They are not transcription
errors. Do not "fix" them back.**

| Scene | Line | Tape text | Scrubbed text | Class |
|---|---|---|---|---|
| 04 | 71 | `“One of those bangers. Play Freebird.”` | `“One of those bangers. Play The Roc's Lament.”` | anachronism — named real-world song |
| 04 | 73 | `“Yeah, totally. Freebird.”` | `“Yeah, totally. The Roc's Lament.”` | anachronism — named real-world song |
| 05 | 19 | `"Yeah, standard MMO. The quest marker?"` | `"Yeah, standard. The quest marker?"` | anachronism — modern technology |
| 05 | 43 | `"Wow, 50 GP. …"` | `"Wow, fifty gold. …"` | table shorthand |
| 05 | 109 | `"Well, we just do that to troll the GM. Totally."` | *(excised)* | table speech — out-of-fiction "GM" |
| 06 | 17 | `"Can you [inaudible] and scavenge food on our way?"` | `"Can you forage and scavenge food on our way?"` | transcript artifact |
| 06 | 81 | `"We are not going to get our 50 GP."` | `"We are not going to get our fifty gold."` | table shorthand |
| 07 | 45 | `“We're level one.”` | `“We're new at this.”` | character level |
| 07 | 201 | `“We're level one.”` | `“We've never done this before.”` | character level |
| 07 | 231 | `“We're all level one,” Vukradin says.` | `“None of us has ever done this,” Vukradin says.` | character level |
| 08 | 9 | `"…Does anybody have a passive perception of 15? … Let's go with this as the. Wait, passive perception."` | `"…Does anybody here actually notice things? … Wait — who has the sharpest eyes?"` | sheet talk |
| 08 | 15 | `"Valphine has 15. Oh, she does?"` | `"Valphine does. Oh, she does?"` | sheet talk |
| 08 | 17 | `"Wait, are you kidding me? Passive perception 15? …"` | `"Wait, are you kidding me? Valphine? …"` | sheet talk |
| 08 | 21 | `"…how could one of my characters not have high perception?"` | `"…how could she not notice things?"` | player-level speech ("my characters") |
| 08 | 23 | `"Well, you know, she's just got high wisdom."` | `"Well, you know, she's just wise."` | ability score |
| 08 | 43 | `"Okay. Give me a save 13, I'll be fine."` | `"Okay. Let me ward myself first, I'll be fine."` | saving throw |
| 08 | 53 | `"Regular. Yeah, we see a little hallway with like a door here at the end of it, I think."` | *(excised)* | table speech — DM narration in a player's mouth |

Scene 08 lines 9–23 were applied as **one coupled decision**: the surrounding narration
("But toughness does not help with hidden doors." / "Valphine studies the foyer…" /
"The hidden panel is there.") carries the beat, so the five rewrites had to agree.
Line 43's rewrite was constrained by the following narration line, "Apparently defenses
are more useful when announced" — the replacement had to keep a defence being announced.

## New canon (`provenance: on_the_fly`)

- **The Roc's Lament** — a Sword Coast tavern standard; the song patrons shout for and
  musicians dread. Authored in narration during this scrub run, not played and not
  prepped. It exists solely to replace "Freebird" while preserving Toblen's wince
  ("Toblen’s mouth tightens. There it is: the first honest reaction of the evening.").
  It is a **song title**, not an entity alias.

Nothing else was invented. No mishearings were registered as aliases in this run.

## GM rulings on what is NOT residue

None of the following is scannable, so without this section the next run re-proposes
all of it.

- **Register policy (ch02).** Metagame *adventuring* vocabulary is in-canon: "adventurers
  have quests; pretending they don't is weird." The line to police is **modern
  technology** — computers and the like. This is why "MMO" went and "quest marker" stayed.
- **Quest / quest board / exclamation mark / yellow bang / quest marker / fetch quest** —
  all **in canon**. GM: "It's a map with markers. Maps have markers. So why not an
  exclamation point? A yellow bang?" `quest board` is additionally in-fiction: Toblen
  names it aloud in scene 04.
- **Spell-preparation talk (scene 06)** — in canon. Soma discussing which workings she
  holds ready, and naming Goodberry / Longstrider / Ice Knife, stays. GM: "Of course a
  druid talks about their spells. Soldiers talk about their blades." (Spell names were
  never a candidate category regardless — see the skill's hard invariant.)
- **Alignment talk** — "What do you like? Lawful, super lawful?" (scene 07) — keep.
- **"Talking is a free action, right?"** (scene 07) — keep.
- **"fat shaming"** (scene 04) — keep. Modern idiom, not tech.
- **The Princess Bride exchange** (scene 08, "mostly dead…" / "…is still alive." /
  "That's right. Slightly alive.") — keep.
- **"bangers"** (scene 04) — keep; only the song title was replaced.
- **Imported real-world economics** — "tax-free income" (scene 02), "Fair-trade,
  conflict-free gold" (scene 05) — canon by design, this campaign's central conceit.
  Never proposed. Note chapter 07's title is literally "Conflict Free Gold".
- **Class names as professions** — "rogues and clerics. And rangers" (scene 08) — keep.

## Notes

- **Scenes 01, 02, 03 were reviewed and produced no `.scrubbed.md`.** That is correct,
  not an omission — `collect_scene_files` in `assemble.py` prefers `.scrubbed.md` per
  scene and falls back to the raw `.md`, so the mixed directory assembles correctly.
  Any downstream pass editing this directory is therefore touching **one** file for
  scenes 01–03 and **two** for scenes 04–08.
- **Scanner false positives deliberately NOT persisted to `ignore`:** scene 06
  `foot_count` on "eighty feet" (canyon walls) and "twenty feet" (the black stone wall).
  Both are mundane physical description. The matched strings are too generic to retire
  permanently — persisting them would silently disable the detector for genuine movement
  residue campaign-wide. Rejected per-instance; they will resurface on a re-run.
- **Tooling gap — `--party-md` loaded 3 of 4 players.** `load_player_names` matches only
  the literal `Player: X` prefix. Stéphane Bourdeaud's roster line in `docs/party.md` is
  `**Barbarian 6 (Path of the Giant) | Goliath | Stéphane Bourdeaud**` — no prefix — so
  he is invisible to `player_name` detection. No `player_name` candidates fired in this
  session either way, but the gap is live for future runs.
- **Scene 08 has no `<!-- table-speech reclassified: … -->` hatch**, despite carrying the
  heaviest table speech in the session (scenes 03, 04, 05 and 07 all have one). The two
  excisions there (L53, and none other) were made as explicit per-instance decisions with
  `"new": ""`. **No hatch was fabricated**, per the skill's rule against forging an audit
  record of a decision the pipeline never made.
- The two excisions leave a doubled blank line at 05:109 and 08:53. Cosmetic; markdown
  collapses them.

---

## Post-run: where these rulings now live

The "not residue" rulings above were promoted out of this manifest into
**`Phandalin/notes/scrub_register_policy.md`** — campaign-scoped, git-tracked, and read
by `/scrub` at Phase 0 of every future run regardless of working directory. The skill was
amended in the same pass (`~/.claude/skills/scrub/SKILL.md`, backup
`SKILL.md.bak-20260902`): the register policy is now required input 5, Phase 2 filters
candidates against it before proposing, and Phase 6 appends to it.

This corrected a real defect. Phase 6 previously said "write the durable, campaign-level
rulings to memory… memory serves the next `/scrub`." Claude Code project memory is keyed
to the **working directory**, so a ruling written during this chapter's scrub was already
unreachable from the next chapter's scrub. Flagged by the GM.
