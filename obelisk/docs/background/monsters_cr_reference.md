# Monster Challenge Rating (CR) Reference — Phandelver and Below: The Shattered Obelisk

**Purpose:** Source-of-truth CR table for the boss-hierarchy logic in `monsters_phase3_hierarchy.md`.

> **REGENERATED 2026-08-22, deterministically, from the 5etools canonical bestiary.**
> Every CR is read from `~/src/5etools-src/data/bestiary/bestiary-*.json`, keyed on (name, source), with
> 5etools `_copy` variants resolved to the stat block they inherit. **28 of 95 rows were wrong** in the
> hand-built version — see *Corrections applied* at the foot of this file. **Do not hand-edit a CR here.**
> Fix the lookup and regenerate, so `monsters_phase3_hierarchy.md` can never again inherit a number
> nobody checked.

**Boss-tier rule (per GM):**
- CR gap between a tribe's rank-and-file and its boss **< 4** → **NOMINAL** boss (a leader in name).
- CR gap **> 4** → **HARD** boss (genuinely more dangerous than the rank-and-file).
- A gap of exactly **4** → **NOMINAL+ (borderline-hard)**, never silently resolved either way.

**Reading the Stat block column.** Plain `MM`/`PaBTSO` = a direct entry in that book. `X (copy)` = the
creature carries no CR of its own and inherits X's stat block — reading those directly is what produced
several of the old errors. A **bold** source means the row's own label named the wrong book.

**Edition note.** This campaign runs 2014 rules. `XMM` rows exist only in the 2024 *Monster Manual* and are
**not** drop-in for a 2014 table — they need a GM ruling before use.

## Humanoids & goblinoids

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Goblin (MM) | 1/4 | MM |  |
| Goblin Boss (MM) | 1 | MM |  |
| Goblin Boss Archer (PaBTSO) | 1 | Goblin Boss (MM) *(copy)* | Appendix A |
| Goblin Psi Brawler (PaBTSO) | 2 ⚠ *was 1/4* | PaBTSO | Appendix A |
| Goblin Psi Commander (PaBTSO) | 4 ⚠ *was 1/2* | PaBTSO | Appendix A |
| Hobgoblin (MM) | 1/2 | MM |  |
| Bugbear (MM) | 1 | MM |  |
| Orc (MM) | 1/2 | MM |  |
| Ogre (MM) | 2 | MM |  |
| Redbrand Ruffian (PaBTSO) | 1/2 ⚠ *was 1/4* | PaBTSO | Appendix A |
| Cultist (MM) | 1/8 | MM |  |
| Cult Fanatic (MM) | 2 | MM |  |
| Druid (generic, MM) | 2 | MM | varies by build |

## Beasts & companions

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Wolf (MM) | 1/4 | MM |  |
| Dire Wolf (MM) | 1 | MM |  |
| Giant Poisonous Snake (MM) | 1/4 | MM |  |
| Giant Badger (MM) | 1/4 | MM | (Bessie named, skip) |
| Capybara (Violet, named) | — | — | skip named individual — no generic stat block |

## Underdark humanoids

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Duergar (MM) | 1 | MM |  |
| Svirfneblin (MM) | 1/2 | MM | Deep Gnome (Svirfneblin) |
| Grimlock (MM) | 1/4 | MM |  |
| Quaggoth (MM) | 2 ⚠ *was 1* | MM |  |
| Drow (generic, MM) | 1/4 | MM |  |
| Drow Elite Warrior (MM) | 5 ⚠ *was 4* | MM |  |
| Drow Mage (MM) | 7 | MM |  |

## Aberrations

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Mind Flayer (MM) | 7 | MM |  |
| Mind Flayer Clairvoyant (PaBTSO) | 11 ⚠ *was 7* | PaBTSO | fanatics' base stat block |
| Mind Flayer Nothic (PaBTSO) | 2 ⚠ *was 4* | Nothic (MM) *(copy)* | Appendix A |
| Mind Flayer Prophet (PaBTSO) | 8 ⚠ *was 7* | PaBTSO | Appendix A |
| Brain Breaker (PaBTSO) | 12 ⚠ *was 10* | PaBTSO | uses infected elder brain stats, AC 14 |
| Infected Elder Brain (PaBTSO) | 11 ⚠ *was 14* | PaBTSO | elder brain base CR 14 |
| Grell (MM) | 3 | MM |  |
| Grell Psychic (PaBTSO) | 4 ⚠ *was 3* | PaBTSO | Appendix A |
| Nothic (MM) | 2 | MM |  |
| Intellect Devourer (MM) | 2 | MM |  |
| Intellect Snare (PaBTSO) | 8 ⚠ *was 3* | PaBTSO | Appendix A |
| Encephalon Gemmule (PaBTSO) | 3 ⚠ *was 2* | PaBTSO | Appendix A |
| Encephalon Cluster (PaBTSO) | 10 ⚠ *was 5* | PaBTSO | Appendix A |
| Gnawble (PaBTSO) | — ⚠ **UNVERIFIED** | — | Not in Appendix A — a Far Realm rift *feature*, not a creature |
| Aberrant Zealot (PaBTSO) | 8 ⚠ *was 3* | PaBTSO | Appendix A |
| Aberrant Zealot, Tentacled (PaBTSO) | 8 ⚠ *was 5* | Aberrant Zealot (PaBTSO) *(copy)* | Appendix A |
| Flesh Meld (PaBTSO) | 7 ⚠ *was 2* | PaBTSO | Appendix A |
| Oculorb (PaBTSO) | 9 ⚠ *was 13* | PaBTSO | Appendix A (beholder warped) |
| Beholder (MM) | 13 | MM |  |
| Spectator (MM) | 3 | MM |  |
| Aboleth (MM) | 10 | MM |  |
| Githyanki Warrior (MM) | 3 | MM |  |
| Githyanki Knight (MM) | 8 | MM |  |

## Fiends & extraplanar

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Quasit (MM) | 1 | MM | (Zeond named, skip) |
| Chain Devil (MM) | 8 | MM | (Vakketar named, skip) |
| Yochlol (MM) | 10 | MM | (Zuluthl named, skip) |
| Mezzoloth (MM) | 5 | MM |  |
| Nycaloth (MM) | 9 | MM | (Nellik named, skip) |
| Arcanaloth (MM) | 12 | MM | (Ashripask named, skip) |
| Homunculus (MM) | 0 | MM |  |

## Elementals & plants

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Earth Elemental (MM) | 5 | MM |  |
| Galeb Duhr (MM) | 6 | MM | (Fremine/Frowode/Cameren named, skip generic) |
| Water Weird (MM) | 3 | MM | (Kellikilli named, skip) |
| Xorn (MM) | 5 | MM | (Zoklork named, skip) |
| Roper (MM) | 5 | MM |  |
| Shambling Mound (MM) | 5 | MM |  |
| Psionic Shambling Mound (PaBTSO) | 5 | Shambling Mound (MM) *(copy)* | Appendix A |
| Mimic (MM) | 2 | MM |  |
| Gibbering Mouther (MM) | 2 | MM |  |
| Black Pudding (MM) | 4 | MM |  |
| Psychic Gray Ooze (PaBTSO) | 1 ⚠ *was 1/4* | **XMM** | Appendix A |
| Fiendish Auger (PaBTSO) | 5 ⚠ *was 2* | PaBTSO | Appendix A |
| Otyugh (MM) | 5 | MM |  |
| Otyugh Mutate (PaBTSO) | 6 ⚠ *was 5* | PaBTSO | Appendix A |

## Undead & constructs

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Zombie (MM) | 1/4 | MM |  |
| Ash Zombie (PaBTSO) | 1/4 | Zombie (MM) *(copy)* | Appendix A |
| Ghoul (MM) | 1 | MM |  |
| Ghast (MM) | 2 | MM |  |
| Wraith (MM) | 5 | MM | (Mormesk named, skip) |
| Banshee (MM) | 4 | MM | (Agatha named, skip) |
| Dwarf Skeleton (PaBTSO) | 1/2 | PaBTSO | Appendix A |
| Cloaker (MM) | 8 | MM |  |
| Cloaker Mutate (PaBTSO) | 10 ⚠ *was 8* | PaBTSO | Appendix A |
| Infected Townsperson (PaBTSO) | 2 ⚠ *was 1/4* | Berserker (MM) *(copy)* | Appendix A |

## Dragons & great beasts

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Young Green Dragon (MM) | 8 | MM | (Venomfang named, skip) |
| Young Amethyst Dragon (PaBTSO) | 9 ⚠ *was 13* | **FTD** | Confirmed twice: FTD young amethyst is CR 9, and PaBTSO stats **Lowarnizel** at CR 9 |
| Hydra (MM) | 8 | MM | (Grandlejaw named, skip) |
| Kraken (MM) | 23 | MM | (Ghaluzesh named, skip) |

## Slaadi

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Gray Slaad (MM) | 9 ⚠ *was 3* | MM |  |
| Red Slaad (MM) | 5 | MM |  |
| Blue Slaad (MM) | 7 | MM |  |

## Nagas

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Spirit Naga (MM) | 8 | MM | (Valsyx/Charnyz named, skip) |
| Guardian Naga (MM) | 10 | MM |  |
| Bone Naga (MM) | 4 | MM | Bone Naga (Spirit/Guardian) — both CR 4 |

## Other

| Monster | CR | Stat block | Notes |
|---|---|---|---|
| Doppelganger (MM) | 3 | MM | (Vyerith/Vhalak named, skip) |
| Flumph (MM) | 1/8 ⚠ *was 1/4* | MM | (Wise Borblish named, skip) |
| Medusa (MM) | 6 | MM | (Honna named, skip) |
| Humanoid Mutate (PaBTSO) | 4 ⚠ *was 2* | PaBTSO | Appendix A |
| Alhoon (MM/SQ) | 10 | **MPMM** | (Oshundo named, skip) |
| Refraction of Ilvaash (PaBTSO) | 15 ⚠ *was 16* | PaBTSO | final boss, named — skip as minion |

---

## Corrections applied (28 of 95 rows)

Every row below was wrong in the hand-built version. **These errors propagated into**
`monsters_phase3_hierarchy.md`, which computes Δ (boss CR − rank-and-file CR) from this table — three of its
verdicts flipped once they were corrected. The errors cluster almost entirely in PaBTSO Appendix A's custom
stat blocks (the obelisk-plot tier) and they overwhelmingly **understate** threat.

| Monster | was | is | error |
|---|---|---|---|
| Gray Slaad (MM) | 3 | **9** | +6 |
| Intellect Snare (PaBTSO) | 3 | **8** | +5 |
| Encephalon Cluster (PaBTSO) | 5 | **10** | +5 |
| Aberrant Zealot (PaBTSO) | 3 | **8** | +5 |
| Flesh Meld (PaBTSO) | 2 | **7** | +5 |
| Mind Flayer Clairvoyant (PaBTSO) | 7 | **11** | +4 |
| Oculorb (PaBTSO) | 13 | **9** | -4 |
| Young Amethyst Dragon (PaBTSO) | 13 | **9** | -4 |
| Goblin Psi Commander (PaBTSO) | 1/2 | **4** | +3.5 |
| Infected Elder Brain (PaBTSO) | 14 | **11** | -3 |
| Aberrant Zealot, Tentacled (PaBTSO) | 5 | **8** | +3 |
| Fiendish Auger (PaBTSO) | 2 | **5** | +3 |
| Mind Flayer Nothic (PaBTSO) | 4 | **2** | -2 |
| Brain Breaker (PaBTSO) | 10 | **12** | +2 |
| Cloaker Mutate (PaBTSO) | 8 | **10** | +2 |
| Humanoid Mutate (PaBTSO) | 2 | **4** | +2 |
| Goblin Psi Brawler (PaBTSO) | 1/4 | **2** | +1.75 |
| Infected Townsperson (PaBTSO) | 1/4 | **2** | +1.75 |
| Quaggoth (MM) | 1 | **2** | +1 |
| Drow Elite Warrior (MM) | 4 | **5** | +1 |
| Mind Flayer Prophet (PaBTSO) | 7 | **8** | +1 |
| Grell Psychic (PaBTSO) | 3 | **4** | +1 |
| Encephalon Gemmule (PaBTSO) | 2 | **3** | +1 |
| Otyugh Mutate (PaBTSO) | 5 | **6** | +1 |
| Refraction of Ilvaash (PaBTSO) | 16 | **15** | -1 |
| Psychic Gray Ooze (PaBTSO) | 1/4 | **1** | +0.75 |
| Redbrand Ruffian (PaBTSO) | 1/4 | **1/2** | +0.25 |
| Flumph (MM) | 1/4 | **1/8** | -0.125 |

**Unverified.** `Gnawble (PaBTSO)` was listed at CR 2 citing Appendix A. There is no gnawble stat block —
gnawbles are Far Realm *rift features*, carried between rifts as keys to reopen the gateway (PaBTSO ch. 9),
not a statted creature. The row is kept and marked rather than carrying an invented number.

**Must be resolved through `_copy`:** `Goblin Boss Archer`, `Mind Flayer Nothic`, `Ash Zombie`,
`Infected Townsperson`, `Psionic Shambling Mound`, `Aberrant Zealot (Tentacled)`. These carry no CR of
their own in the JSON; four of the corrections above are rows where that inheritance was not followed.

