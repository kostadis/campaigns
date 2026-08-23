# Monster Challenge Rating (CR) Reference — Temple of Elemental Evil (T1-4, 5e)

**Purpose:** Source-of-truth CR table for the boss-hierarchy logic in `monsters_phase3_hierarchy.md`.

**Boss-tier rule (per user):**
- CR difference between a tribe's monster and its boss is **< 4** → **NOMINAL boss** (a leader in name, not a large leap in threat).
- CR difference is **> 4** → **HARD boss** (a genuinely more dangerous threat than the rank-and-file).
- Gap **exactly 4** → **NOMINAL+ (borderline-hard)** — flagged for review, never silently called "hard."

**Verification:** every row was audited against the canonical 5etools bestiary
(2026-08-23) — see `monsters_cr_verification.md` for the full drift report.

**CR source note:** ToEE's `adventure-t14-5e.json` is *1E notes converted to 5e*. Its Appendix B: Monsters encodes monsters in 1E terms (Hit Dice, not 5e CR) — e.g. Zuggtmoy 49 HD, node princes unspecified. The authoritative 5e CRs below come from the **5e Monster Manual / Volo's / Mordenkainen's** and the **ToEE 5e conversion** (e.g. the published *Temple of Elemental Evil* 5e by Goodman Games / the 3.5e→5e community conversion, which this homebrew tracks). Where a named NPC's CR is better expressed as a *character level* (the leadership inventory gives levels), I list the equivalent monster-stat CR in brackets. 1E HD is shown in parentheses for ordering only.

**Rank-and-file convention:** When a tribe has multiple unnamed tiers, use the **highest rank-and-file CR** for the conservative (smallest-gap) comparison and note the range.

## Humanoids & humanoid troops
| Monster | CR | Notes (1E HD) |
|---|---|---|
| Bandit | 1/8 | (1 HD) |
| Bandit Captain | 2 | (4+ HD) |
| Brigand / Thug | 1/2 | ToEE uses "brigand" for Temple raiders (1–2 HD) |
| Guard | 1/8 | (1 HD) — 5etools/MM (was 1/2) |
| Cultist | 1/8 | (1 HD) |
| Cult Fanatic | 2 | (3 HD) |
| Acolyte | 1/4 | (1 HD) |
| Spy | 1 | |
| Thief (ToEE) | 3 | leadership inv: Dala/Pearl L3 thief → CR 3 |
| Assassin | 8 | leadership inv: Gremag L7 assassin → CR ~8 |
| Warrior (human) | 1/8 | (1 HD) = Tribal Warrior, 5etools/MM |
| Veteran | 3 | (4–5 HD) |
| Berserker | 2 | |
| Gladiator | 5 | |
| Knight | 3 | |
| Champion | 9 | |
| Archer / Crossbowman | 1/4 | (1 HD); NOTE: MPMM's *Archer* stat is CR 3 — an elite archer, not a 1-HD bowman |
| Man-at-arms | 1/2 | |
| Mage (human) | 6 | (3+ HD); Otis L10 ranger-knight → CR ~10 |
| Archmage | 12 | |
| Cleric (human) | 5 | generic MM *Priest* stat = CR 2; Calmert/Terjon ≈ L3–5 leveled NPCs → CR 3–5 |
| Priest | 2 | (3 HD) |
| Druid | 2 | Jaroo L7 druid → CR ~7 |
| Sorcerer / Warlock | 4 | |
| Monk | 3 | |

## Goblinoids, giants & ogres
| Monster | CR | Notes (1E HD) |
|---|---|---|
| Goblin | 1/4 | |
| Hobgoblin | 1/2 | |
| Bugbear | 1 | |
| Orc | 1/2 | |
| Half-Orc (warrior) | 1/2 | Thogran Ashmaw half-orc cleric/fighter → CR ~5 |
| Ogre | 2 | (4+1 HD) |
| Ogre Mage (ToEE "ogre mage") | 7 | (5+1 HD) = Oni, 5etools/MM (was wrongly listed as 4) |
| Ogre Chieftain (named) | 4–6 | Garghuk/Gloarok → CR ~5–6 (named, excluded) |
| Troll | 5 | (6+3 HD) |
| Ettin | 4 | (10 HD) |
| Cyclops | 6 | |
| Verbeeg | 4 | 5etools: Verbeeg Marauder 4, Longstrider 5 |
| Fomorian | 8 | (10+ HD) |
| Hill Giant | 5 | (8+ HD) |
| Stone Giant | 7 | |
| Fire Giant | 9 | Varek Redflame leads Fire Guards; giants allies of Alrrem |
| Frost Giant | 8 | |
| Cloud Giant | 9 | |
| Storm Giant | 13 | |
| Death Giant (ToEE L3) | 12 | 5etools: Death Giant Reaper 12, Shrouded One 15 |

## Gnolls, lizardfolk, troglodytes, yuan-ti
| Monster | CR | Notes |
|---|---|---|
| Gnoll | 1/2 | |
| Gnoll Pack Lord | 2 | |
| Gnoll Witherling | 1/4 | |
| Lizardfolk | 1/2 | |
| Lizard King/Queen | 4 | 5etools/MM (was 3) |
| Troglodyte | 1/4 | |
| Yuan-ti (pureblood) | 1 | |
| Yuan-ti (malison) | 3 | |
| Yuan-ti (abolisher/abomination) | 7–8 | |

## Elementals & genies
| Monster | CR | Notes |
|---|---|---|
| Air Elemental | 5 | |
| Earth Elemental | 5 | |
| Fire Elemental | 5 | |
| Water Elemental | 5 | |
| Invisible Stalker | 6 | |
| Water Weird | 3 | |
| Magmin | 1/2 | |
| Salamander | 5 | |
| Azer | 2 | |
| Mephit (all types) | 1/2 | 5etools/MM (was 1/4) |
| Dust/Ice/Steam/Magma/Smoke/Water/Air/Earth/Fire Mephit | 1/2 | 5etools/MM (was 1/4) |
| Xorn | 5 | |
| Galeb Duhr | 6 | |
| Dao | 11 | |
| Djinni | 11 | |
| Efreeti | 11 | |
| Marid | 11 | 5etools/MTF (was 13) |
| Noble Genie | 7–12 | |
| Elemental (Greater / node prince) | 17+ | node princes (Crushing Wave etc.) approximate CR 17–21; NAMED, excluded as monsters |

## Fiends — demons (tanar'ri)
| Monster | CR | Notes (1E HD) |
|---|---|---|
| Manes | 1/8 | |
| Dretch | 1/4 | |
| Quasit | 1 | |
| Rutterkin | 2 | 5etools/MTF (was 1/2) |
| Bulezau | 3 | 5etools/MTF (was 2) |
| Vrock | 6 | (8 HD) |
| Hezrou | 8 | (9 HD) — 5etools/MM (was 7) |
| Glabrezu | 9 | (11+ HD) |
| Nalfeshnee | 13 | (12 HD) |
| Marilith | 16 | (9+ HD) |
| Balor | 19 | (15+ HD) |
| Chasme | 6 | 5etools/Volo's-MTF (was 3) |
| Shadow Demon | 4 | |
| Barlgura | 5 | |
| Goristro | 17 | |
| Shoosuva | 8 | 5etools/VGtM (was 11) |
| Maurezhi | 7 | 5etools/MTF (was 4) |

## Fiends — devils (baatezu / baatezu)
| Monster | CR | Notes (1E HD) |
|---|---|---|
| Lemure | 0 | |
| Nupperibo | 1/2 | |
| Spined Devil (Spinagon) | 2 | 5etools/MTF (was 1/4) |
| Bearded Devil (Barbazu) | 3 | (4+1 HD) |
| Erinyes | 12 | |
| Bone Devil (Osyluth) | 9 | (8+3 HD) |
| Barbed Devil (Hamatula) | 5 | (6+3 HD) |
| Chain Devil (Kyton) | 8 | |
| Horned Devil (Cornugon) | 11 | (10+2 HD) |
| Ice Devil (Gelugon) | 14 | (11+2 HD) |
| Pit Fiend | 20 | (15+ HD) |
| Imp | 1 | |
| Amnizu | 18 | 5etools/MTF (was 15) |
| Narzugon | 13 | |
| Bezekira | 10 | 5etools = Hellcat (Bezekira), BGDiA/Fizban's (was 16) |
| Cambion | 5 | |
| Hell Hound | 3 | |
| Yeth Hound | 4 | |
| Merregon | 4 | 5etools/MTF (was 3) |
| Buarga | 3 | |

## Undead
| Monster | CR | Notes (1E HD) |
|---|---|---|
| Skeleton | 1/4 | |
| Zombie | 1/4 | |
| Ghoul | 1 | |
| Ghast | 2 | |
| Wight | 3 | |
| Wraith | 5 | |
| Specter | 1 | 5e MM (was listed as 1/4; 1E 5+3 HD → often bumped to CR 3 in conversions) |
| Banshee | 4 | |
| Mummy | 3 | |
| Mummy Lord | 15 | |
| Mohrg | 8 | (12 HD) |
| Bodak | 6 | (10 HD) |
| Shadow | 1/2 | |
| Allip | 5 | 5etools/MTF (was 2) |
| Banshee | 4 | |
| Ghost | 4 | |
| Vampire | 13 | |
| Death Knight | 17 | |
| Bone Naga | 4 | |
| Nightmare | 3 | |
| Lich | 21 | |

## Oozes & slimes
| Monster | CR | Notes (1E HD) |
|---|---|---|
| Gray Ooze | 1/2 | |
| Ochre Jelly | 2 | (5 HD) |
| Black Pudding | 4 | (10 HD) |
| Gelatinous Cube | 2 | |
| Green Slime | 1/4 | (1E hazard; 5e trap/ooze) |
| Yellow Mold | 1/4 | (hazard) |
| Assassin Vine | 3 | |
| Shrieker | 0 | |
| Violet Fungus | 1/4 | |
| Otyugh | 5 | |

## Constructs & golems
| Monster | CR | Notes |
|---|---|---|
| Clay Golem | 9 | |
| Stone Golem | 10 | |
| Flesh Golem | 5 | |
| Iron Golem | 16 | |
| Bone Golem | 4 | (ToEE specific) |
| Wood Golem | 5 | (ToEE specific) |
| Shield Guardian | 7 | |
| Gargoyle | 2 | (4 HD) |
| Margoyle / Greater Gargoyle | 2 | no such 5e stat block; nearest = four-armed gargoyle CR 2 (ToEE variant, was 5) |

## Beasts & others
| Monster | CR | Notes |
|---|---|---|
| Dire Wolf | 1 | |
| Warg | 1/4 | no 5e warg monster (warg is a PC race); nearest beast = Wolf 1/4 |
| Dire Bear | 2 | no 5e dire bear stat block; nearest = Cave Bear 2 / Polar Bear 2 (was 4) |
| Black Bear | 1/2 | |
| Owlbear | 3 | |
| Displacer Beast | 3 | |
| Blink Dog | 1/4 | |
| Phase Spider | 3 | |
| Giant Spider | 1 | |
| Ettercap | 2 | |
| Giant Toad | 1 | 5etools/MM (node natives; was 1/4) |
| Frog | 0 | 5etools/MM (node natives) |
| Leucrotta | 3 | 5etools/Volo's — Menagerie rank ceiling stays 5 via troll |
| Giant Lizard | 1/4 | |
| Ustilagor | 1/2 | (ToEE demon-fungus bat) |
| Rust Monster | 1/2 | |
| Xorn (see genies) | 5 | |
| Intelligence Devourer | 2 | |
| Mind Flayer | 7 | |
| Grick | 2 | |
| Darkmantle | 1/2 | |
| Cloaker | 8 | |
| Basilisk | 3 | |
| Manticore | 3 | |
| Griffon | 2 | |
| Wyvern | 6 | |
| Couatl | 4 | |
| Ki-rin | 12 | |
| Slaad (all) | 5–10 | |

**Note on the "boss" match-up:** Use the tribe's *rank-and-file* CR vs the boss's CR. ToEE's named bosses are mostly *character-stat* NPCs (levels given in the leadership inventory) — convert to monster CR by the standard level→CR mapping (Lvl 5 ≈ CR 5, Lvl 7 ≈ CR 7–8, Lvl 10 ≈ CR 10, Lvl 12 ≈ CR 12). The four High Priests (Romag/Alrrem/Belsornig/Kelno) are ~L7 clerics → CR ~7–8; Hedrack ~L11 → CR ~11; Zuggtmoy (49 HD, unique) → CR ~23 (apex). Deggum/Barkinar/Feldrin are mid-level commanders (L5–7) → CR 5–8.
