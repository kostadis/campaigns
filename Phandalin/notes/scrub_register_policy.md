# Phandalin — scrub register policy

**Campaign-scoped rulings on what is NOT mechanical residue.** Read this BEFORE walking
candidates in a `/scrub` run (Phase 2), and append to it in Phase 6 whenever the GM rules
on a new class.

**Why this file exists:** none of what follows is scannable. `find_residue.py` matches
numbers, fixed table-speak phrases, and player names — it cannot match vocabulary at all,
by design (see the skill's hard invariant). So nothing but this document stops the next
run re-proposing every ruling below, one instance at a time.

It lives in `notes/` because it is a cleanup-pass reference, not campaign canon — do not
mine it into the mempalace.

---

## The register line

**Metagame *adventuring* vocabulary is in canon. The class to police is modern
technology.**

> "I am thinking the meta-game gaming MMO language is the kind of language adventurers
> would use. I mean 'you have quests' — pretending you don't is weird. Where we need to be
> careful is when the language refers to modern technology like computers etc."
> — GM, 2026-09-02 (ch02 scrub)

This is a *single policy*, not N independent rulings. Settle it once at the top of a run
and let it collapse the queue. Ch50 is the cautionary case: several rounds went by
proposing economics terms one at a time before the GM explained they were the campaign's
premise.

## Ruled IN CANON — never propose these

| Class | Examples | Ruled |
|---|---|---|
| Quest / adventuring vocabulary | quest, quest board, quest marker, exclamation mark, "the yellow bang", fetch quest | ch02 |
| Alignment talk | "What do you like? Lawful, super lawful?" | ch02 |
| Action economy as wry aside | "Talking is a free action, right?" | ch02 |
| Class names as professions | "they've been rogues and clerics. And rangers" | ch02 |
| A caster naming prepared spells | Goodberry / Longstrider / Ice Knife; swapping what is held ready | ch02 |
| Imported real-world economics | tax-free income; "fair-trade, conflict-free gold"; supply chain; revenue share; marketing; perpetuity; image and likeness | ch50, reaffirmed ch02 |
| Modern idiom that is neither tech nor a named entity | "bangers", "fat shaming" | ch02 |
| Self-covering real-world reference | the Princess Bride "mostly dead… / …is still alive" exchange | ch02 |
| Specific words ruled in canon outright | **cosplaying** | ch50 |

Rationale on two of these, in the GM's words:

- **Quest markers:** *"It's a map with markers. Maps have markers. So why not an
  exclamation point? A yellow bang?"*
- **Spell talk:** *"Of course a druid talks about their spells. Soldiers talk about their
  blades."*
- **Economics:** Vukradin importing real-world economics into Faerûn is the campaign's
  central conceit — KP's planar-efficiency project is the same premise from the other
  side. Chapter 07's title is literally "Conflict Free Gold".

## Ruled RESIDUE — still propose these

| Class | Examples | Ruled |
|---|---|---|
| Modern technology | **MMO** (scrubbed while "the quest marker" in the same line was kept) | ch02 |
| Named real-world entity | Freebird; Bud Light, Hollywood, Kickstarter, Blue Oyster Cult, Houston; SystemD; Zoomer; meth lab; Chinese wall | ch02, ch48, ch50 |
| Character level | "we're level one", "we're level 7?" | ch02, ch48 |
| Character-sheet talk | passive perception, ability scores ("she's got high wisdom"), saves ("give me a save 13") | ch02 |
| Player-level speech | "one of my characters" | ch02 |
| Out-of-fiction table reference | "the GM", "troll the GM" | ch02 |
| DM narration in a player's mouth | "Yeah, we see a little hallway with like a door at the end of it" | ch02 |
| Table shorthand for money | "50 GP" where the surrounding prose says "fifty gold pieces" | ch02 |
| Raw transcript artifact | a literal `[inaudible]` left in finished narration | ch02 |

## Coinages authored during scrub runs (`provenance: on_the_fly`)

These were invented in narration to replace an anachronism. They are canon now, and a
consistency pass must not read them as fabrications.

| Coinage | Replaced | Chapter | Note |
|---|---|---|---|
| **The Roc's Lament** | Freebird | ch02 | A Sword Coast tavern standard — the song patrons shout for and musicians dread. A *song title*, not an entity alias. |
| **Aurum Bee Vance** | Oral B. Vance | ch48 | A **mishearing**, NOT an alias. Belongs in the canonical entity's note; never register it as an alternate name. |
| Menzoberranzan **cadet house** | Chinese wall | ch48 | A drow institution for laundered agency. |
| **dreamlily** | meth lab | ch48 | A named narcotic. |
| "talks like a **shell-sprout**" | Zoomer | ch48 | Soma's idiom for the young. |
| **Jimble the Unmoved** | — | ch03 | Marginal-note coinage; a cleric of the old coastal sagas who pronounced companions dead rather than spend the prayer. Glosses "He's dead, Jim." |

## Ruled RESIDUE — additions from the ch02 re-render pass (2026-09-02, run 2)

| Class | Examples | Ruled |
|---|---|---|
| Raw roll results / roll canvass in dialogue | "Anybody do better than that?", "Four.", "Any more roles, guys.", "I said 14.", "Oh, 14. Nice." | ch02 r2 |
| Digits in dialogue for money | "the 50 gold pieces" -> "the fifty gold pieces" (same class as "50 GP") | ch02 r2 |
| Bare imperative addressed to the GM | **"Hit the door."** | ch02 r2 |

The last row is worth its own note. It carries no number and no fixed table-speak phrase,
so **no scanner pattern can ever reach it** — and it is genuinely ambiguous as in-fiction
dialogue. The `/scrub` recommendation was to keep it; the GM ruled it out. Ambiguous bare
imperatives go to the GM rather than being resolved by the reading pass.

Also reaffirmed unchanged in that run: **"Talking is a free action, right?"**, the
**Princess Bride** exchange, **quest / quest board**, and spelled-out money
("a couple hundred gold pieces") are all in canon.

**No new coinages.** `The Roc's Lament` was re-applied to re-rendered lines; it is still the
single ch02 coinage, still a song title and not an entity alias.

## In-world scholar persona

Phandalin's marginal-note persona is **Kostadinious the Sage**, the campaign's in-world
biographer. Never mint a new sage per note.
