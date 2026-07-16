# Ensemble cleanup worklist — derived from `facts_to_state.py --list` (registry + min-facts 3)

Generated from the 440-entity census in `output` (2026-07-13). These are **candidates for review**, not
decisions — run them through the two human-checkpoint skills below. Fact counts shown as `[type N]`.

- **Part A → `/ensemble-alias-review`** (name variants of the *same* entity)
- **Part B → `/entity-triage`** (not-an-entity noise)

The registry already caught many aliases (e.g. `Sarith` → `Sarith Kzekarit`, the `Jorlan` merge); these are
the ones it **missed**.

---

## Part A — Alias candidates (`/ensemble-alias-review`)

### A1. Clear short ↔ long (same person; canonical = the fuller name)
| Alias (fewer facts) | → Canonical | Note |
|---|---|---|
| `Kalan` [npc 14] | **Kalan Strongbranch** [npc 38] | First Reader / Head of the Avowed |
| `Sylvira` [npc 25] | **Sylvira Savikas** [npc 15] | Candlekeep Great Reader |
| `A'lai` [npc 13] | **A'lai Aivenmore** [npc 18] | the protected drow evoker's contact |
| `Fembris` [npc 21] | **Fembris Lancer** [npc 12] | |
| `Daral` [npc 40] | **Daral Yashenti** [npc 9] | (canonical is the higher-fact `Daral`; confirm which) |
| `Fheminor` [npc 3] | **Fheminor Scrivenbark** [npc 10] | |
| `Teles` [npc 4] | **Teles Ahvoste** [npc 10] | |
| `Brother Vareth` [npc 7] | **Vareth** [npc 16] | "Brother" is a title; canonical likely `Vareth` |
| `Quartermaster Senni Diggermattock` [npc 4] | **Senni Diggermattock** [npc 19] | title prefix |
| `Chief Chipgrin` [npc 5] | **Chipgrin Goldwhisker** [npc 12] | chief of the Gold Whisker clan |
| `Thorin Giantfriend` [npc 8] | **Thorin** [npc 420] | PC's earned epithet |

### A2. Spelling / transcription variants (typos — same entity)
| Variant | → Canonical | Note |
|---|---|---|
| `Gyrgum` [npc 15, ch1] | **Grygum** [npc 484] | early-chapter misspelling of the PC — **high value** |
| `Dasco Pickshine` [npc 11] | **Dazco Pickshine** (in registry) | `s`/`z` variant; deep-gnome Pickshine-mines overseer |
| `Borough Warden Jadger` [npc 3] + `Uth-Jadger` [npc 3] | **Jadgar** [npc 11] | "Borough"="Burrow" Warden ghost; `Jadger`/`Jadgar` spelling |

### A3. "The X" / article variants
| Variant | → Canonical |
|---|---|
| `The Flumph` [npc 5] | **Flumph** [npc 11] |
| `The Underdark` [location 12] | **Underdark** [location 29] |

### A4. Epithet → real entity (alias points at a *different* canonical name)
| Epithet | → Canonical | Note |
|---|---|---|
| `Dark Lady` [npc 3] + `The Dark Lady` [npc 3] | **Zuggtmoy** | "the Dark Lady" is Zuggtmoy's cult epithet — confirm before merging |

### A5. Verify (real judgment call — let review decide)
- `Elian` [npc 6] / `Ellen` [npc 3] / **Elin** — the mute girl Dawnbringer cured; the registry already
  flagged an `Elin`/`Ellen` transcript-vs-doc spelling split. Same person? Likely, but confirm.
- `Topsy` [npc 14] / `Turvy` [npc 8] / `Topsy and Turvy` [npc 7] — the two-headed troll: one entity with a
  paired name, or two? Decide the canonical.
- `Chief Diggermattock` [npc 3] → `Dorbo Diggermattock` [npc 30]? (registry lists `Chief Dorbo` as a Dorbo
  alias, so probably — but `Senni` is also a Diggermattock, so don't blind-merge on surname.)
- Role-titles that may be **Kalan**: `The First Reader` [npc 4], `Gate Warden` [npc 4]. Both are roles
  Kalan held — alias to Kalan, or keep as role labels? (Could instead be Part B.)
- `Priest of Bahamut` [npc 4] / `Gorg'Bahamut` [npc 3] → **Grygum** (cleric of Bahamut)? Verify — may be
  role-label / narration fusion rather than an entity.

### A6. Do NOT merge (token-share false positives — genuinely distinct)
`Darklake` (the lake) ≠ `Darklake Brewery` ≠ `Darklake District` · `House Mizzrym` ≠ `Ilvara Mizzrym` ·
`Clan Ironhead` ≠ `Grinta Ironhead` · the Duskryns (`Jorlan` / `Kaelira` / `Nym` are separate people) ·
`Kazook Pickshine` ≠ `Dasco Pickshine` · `Stonespeaker Crystal` (object) ≠ `Stonespeaker Hgraam` (person) ·
`the Ember Vanguard` ≠ `The Ember Grapple` · `Garden of Welcome` ≠ `The Garden Shadow` ·
`Stone Guard` ≠ `Stone of Controlling Earth Elementals`.

---

## Part B — Not-an-entity candidates (`/entity-triage`)

### B1. Narrator / first-person cluster (high priority — these are `[known]`, high fact-count, will become dossiers)
| Subject | Facts | Ruling to consider |
|---|---|---|
| `I` | [npc 28] | pronoun captured as an NPC — **not an entity** |
| `Narrator` | [npc 15] | narration device |
| `The Narrator` | [npc 10] | narration device |
| `Narrator (Dragonborn)` | [npc 4] | the dragonborn narrating voice = **Zalthir**? → alias to Zalthir, else not-an-entity |
| `Speaker` | [npc 3] | narration device |

These are the in-fiction narrating voice splintered across labels. Decide once: **alias the whole cluster
to the narrating PC**, or mark **not-an-entity**. (Whichever you pick, do it consistently for all five.)

### B2. Running-tally / measurement artifacts (registry already pushed these to `[location]` scope, but formally kill them)
`chasme count` (44 facts un-scoped!) · `demogorgon count` · `duergar count` · `silver candlestick value`
(×3) · `equipment value` · `faerun danger` · `underdark danger`. These are extraction counters/appraisals,
not entities.

### B3. Bulk note — location-scoped fragments
202 of the 440 rows are `[location]`-scoped anonymous bundles (`chamber (chamber)`, `cavern (bridge)`,
`throne room (throne room)`, `Velkynvelve elevation (…)` …). They're semi-quarantined (won't merge into
named entities), so they're lower priority — but `/entity-triage` can sweep the ones that are real places
worth registering vs. pure scene-noise.

---

## Not covered here (different skill)
Type-collisions still visible in the census (`Glabbagool` npc+monster+object, `Dawnbringer`, `Zuggtmoy`,
`Themberchaud`, `Bag of Holding`, `Bookwyrm`, `Drow`, `Gray Ghosts`, …) are already resolved in
`merged_dossiers/` by `/ensemble-type-merge`. They appear here only because `--list` is the **pre-merge**
view.
