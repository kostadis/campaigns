# Registry alias rulings

Adjudicated by the GM during the `/registry-cleanup` pass of **2026-08-03**.

## The rule

**An alias in `docs/entity_registry.yaml` is an APPROVED CANONICAL ALTERNATE
NAME — never a transcription garbling.** Earlier registry-building passes
treated aliases as a dumping ground for surface forms seen in the wild, which
was a mistake: every alias reads as a "known, correctly-spelled name" to
downstream consumers, so a garbling parked there silently suppresses the
correction `notes/vtt_transcription_corrections.md` would otherwise make.

Garblings belong in the VTT corrections glossary. Nothing else.

## What was removed (2026-08-03)

| Count | Category |
|---|---|
| 22 | aliases that were also glossary wrong-forms (`Glabagool`, `Zuggtomy`, `Zentarim`, `Strongbench`, `Elvara`, `Callan`, `Kessler`, `Varath`, `Varith`, `Buhammad`, `Melfire`, `Elred`, `Eliana`, `Kelvir`, `Hightower`, `Stroudian`, `Ebonheir`, `Ebonir`, `Princess Ebonheir`, `Globagool`, `Globul`, `Gate Warden`) |
| 37 | near-miss garblings of their own canonical (incl. five manglings of *Themberchaud*, two of *Blingdenstone*, `Pliinki`, `Suushar The Awakened`, `Myrkhul`, `Myrtul`, `zurkwhood`, `Tinmmasks`, `EntemochBoon`) |
| 5 | final adjudicated batch (`Ilian`, `Halls of Sacred Stones`, `Circle of Sowers`-as-alias, `Spiral of the Great Horned King`, `Spiral of the Horned Lord`) |

**Totals: 434 → 370 aliases, 1013 → 1010 entities.**

Structural fixes in the same pass:

- `House Turan` merged into **House T'sarran** (duplicate faction)
- `Plinky` merged into **Plinki** (journal-authorship note hand-carried across —
  `registry merge` drops the folded entity's note)
- `Whirlstone Caverns` merged into **Whorlstone Tunnels** (books note carried across)
- `Lothheism` renamed to **Lolthism** — the *canonical* was the garbling;
  confirmed against `docs/TheUnderdark.md` ("converted to Lolthism")
- `Circle of Sporers` renamed to **Circle of Sowers** — same inversion; the
  published module names Sowers among the seven Neverlight Grove circles

## KEEP — 12 legitimate aliases (reviewed, not missed)

A future `audit_aliases.py` run will surface these in bucket B. They have
already been ruled on; do not re-litigate without a reason.

| Alias | Entity | Why it's legitimate |
|---|---|---|
| `bridesmaids of Zuggtmoy` | Bridesmaid of Zuggtmoy | plural |
| `chamberlains of Zuggtmoy` | Chamberlain of Zuggtmoy | plural |
| `Stone Guards` | The Stone Guard | plural / article |
| `Christopher Perkins` | Chris Perkins | real-world full vs short name |
| `Entemoch` | Entémoch | diacritic-free rendering |
| `Ogremoch` | Ogrémoch | diacritic-free rendering |
| `Faerun` | Faerûn | diacritic-free rendering |
| `Gromph's grimoire` | Gromph Baenre's grimoire | short form |
| `Missing Dragon Egg` | Missing Red Dragon Egg | short form |
| `the missing dragon egg` | Missing Red Dragon Egg | short form / case |
| `Whorlstone Area 14b (Zubriska's Barracks)` | …(Zubriska's Barracks / Hideout) | short form |
| `Keepers of the Flame Barracks` | Keepers of the Flame Headquarters | same location; `gracklstugh-revised-inventory.md` groups HQ / Barracks / Themberchaud's Lair as one |

## Tooling gaps found

`registry.py` has **no `unalias`** and **no `rename`** — it assumes aliases are
only ever added. Removals require editing `entity_registry.yaml` directly; use
`~/.claude/skills/registry-cleanup/strip_aliases.py`.

`registry merge` has two silent behaviours that work against this rule:

1. it **re-adds the folded entity's name as an alias** of the target, recreating
   the garbling you just removed — always re-strip after a merge;
2. it **discards the folded entity's `note`** — read both notes first and
   hand-carry anything unique.

Worth filing against CampaignGenerator.
