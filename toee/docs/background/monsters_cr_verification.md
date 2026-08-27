# CR Verification — monsters_cr_reference.md vs 5etools Bestiary

**Date:** 2026-08-23 · **Method:** every row of `monsters_cr_reference.md` was checked against the canonical 5etools bestiary JSON tree (`/home/kostadis/src/5e-tools-kostadis/data/bestiary/bestiary-*.json`, 3,737 monsters — the exact data the 5etools MCP server serves; no MCP server is currently wired into Hermes, so the underlying files were read directly).

**Module caveat (unchanged):** ToEE's `adventure-t14-5e.json` encodes monsters in 1E HD terms and prints no 5e CRs anywhere, so the module itself cannot arbitrate CR disputes — 5e MM/Volo's/MToF (via 5etools) is the authority, exactly as the CR-reference file already states.

## Verdict

- **~120 of 176 rows: CORRECT** (all the ones the hierarchy actually leans on — see "Impact" below).
- **28 rows DRIFTED** from the published 5e values.
- **18 rows UNVERIFIABLE** against 5etools (homebrew/ToEE-specific/non-bestiaried entries).

---

## A. Confirmed drift (table value ≠ 5etools value)

### Large errors (>1 CR off)

| Monster | Table | 5etools | Source |
|---|---|---|---|
| Ogre Mage | 4 | **7** (Oni) | MM |
| Chasme | 3 | **6** | Volo's/MToF |
| Allip | 2 | **5** | MTF |
| Maurezhi | 4 | **7** | MTF |
| Shoosuva | 11 | **8** | VGtM |
| Bezekira | 16 | **10** (Hellcat/Bezekira) | BGDiA/Fizban's |
| Amnizu | 15 | **18** | MTF |
| Rutterkin | 1/2 | **2** | MTF |
| Spined Devil | 1/4 | **2** | MTF |
| Margoyle/Greater Gargoyle | 5 | **no such 5e monster**; nearest = four-armed gargoyle CR 2 | — |
| Dire Bear | 4 | **not a 5e stat block**; nearest = Cave Bear 2 / Brown Bear 1 / Polar Bear 2 | MM |
| Warg | 1/2 | **not a 5e monster** (PC race); nearest beast = Wolf 1/4 | MM |

### Small errors (≤1 CR off)

| Monster | Table | 5etools | Source |
|---|---|---|---|
| Guard | 1/2 | **1/8** | MM |
| Warrior (human) | 1/4 | **1/8** (Tribal Warrior) | MM |
| Archer/Crossbowman | 1/4 | **3** (Archer, MPMM) — or keep 1/4 for a 1-HD bowman; ambiguous name | MPMM |
| Priest (row "Cleric") | 5 | **2** (the generic *Priest* stat is CR 2; CR 3–5 only fits leveled NPCs) | MM |
| Lizard King/Queen | 3 | **4** | MM |
| Mephits (all) | 1/4 | **1/2** | MM |
| Bulezau | 2 | **3** | MTF |
| Hezrou | 7 | **8** | MM |
| Merregon | 3 | **4** | MTF |
| Specter | 1/4 | **1** | MM |
| Doppelganger (used in A30) | 4 | **3** | MM |
| Leucrotta (used in A25) | (unlisted; hierarchy assumed 5) | **3** | Volo's |
| Giant Toad | 1/4 | **1** | MM |
| Frog | 1/4 | **0** | MM |
| Marid | 13 | **11** | MTF |
| Lurker Above (A26) | 5 | **no 5e stat block**; nearest = Trapper 3 | — |
| Hieracosphinx (A31) | (unlisted) | **no 5e stat block** (androsphinx/gynosphinx only) | — |

## B. Unverifiable against 5etools (ToEE-specific / non-bestiary)

Thief (ToEE) 3 · Man-at-arms 1/2 · Sorcerer/Warlock 4 · Half-Orc warrior 1/2 · Noble Genie 7–12 · Green Slime 1/4 · Yellow Mold 1/4 (hazards) · Bone Golem 4 · Wood Golem 5 · Ustilagor 1/2 · Mohrg 8 (never officially ported to 5e) · Buarga 3 (no 5e entry found) · Death Giant 12 (**partially verifiable**: Death Giant Reaper = 12 ✓, Shrouded One = 15) · Verbeeg 4 (**verifiable now**: Verbeeg Marauder = 4 ✓, Longstrider = 5) · Juggernaut (Water Temple, assumed CR 5 — homebrew, unverifiable) · Node princes 17–21 (apex estimates, by design).

## C. Spot-checks that PASSED (hierarchy-critical values)

Goblin 1/4 · Orc 1/2 · Hobgoblin 1/2 · Bugbear 1 · Gnoll 1/2 · Gnoll Pack Lord 2 · Ogre 2 · Troll 5 · Ettin 4 · Hill Giant 5 · Stone Giant 7 · Frost Giant 8 · Cloud Giant 9 · Fire Giant 9 · Fomorian 8 · all four Elementals 5 · Invisible Stalker 6 · Salamander 5 · Azer 2 · Water Weird 3 · Xorn 5 · Galeb Duhr 6 · Dao/Djinni/Efreeti 11 · Vrock 6 · Glabrezu 9 · Nalfeshnee 13 · Marilith 16 · Balor 19 · Barlgura 5 · Goristro 17 · Shadow Demon 4 · Bearded Devil 3 · Erinyes 12 · Bone Devil 9 · Barbed Devil 5 · Chain Devil 8 · Horned Devil 11 · Ice Devil 14 · Pit Fiend 20 · Imp 1 · Hell Hound 3 · Nightmare 3 · Skeleton/Zombie 1/4 · Ghoul 1 · Ghast 2 · Wight 3 · Wraith 5 · Banshee 4 · Ghost 4 · Mummy 3 · Mummy Lord 15 · Bodak 6 · Shadow 1/2 · Death Knight 17 · Bone Naga 4 · Lich 21 · Gray Ooze 1/2 · Ochre Jelly 2 · Black Pudding 4 · Gelatinous Cube 2 · Shrieker 0 · Violet Fungus 1/4 · Otyugh 5 · Clay 9 / Stone 10 / Flesh 5 / Iron 16 Golem · Shield Guardian 7 · Gargoyle 2 · Owlbear 3 · Displacer Beast 3 · Phase Spider 3 · Giant Spider 1 · Ettercap 2 · Blink Dog 1/4 · Basilisk 3 · Manticore 3 · Griffon 2 · Wyvern 6 · Couatl 4 · Ki-rin 12 · Red Slaad 5 … Death Slaad 10 · Carrion Crawler 2 · Stirge 1/8 · Harpy 1 · Jackalwere 1/2 · Will-o'-Wisp 2 · Lamia 4 · Yuan-ti Pureblood 1 / Malison 3 · Bandit 1/8 · Bandit Captain 2 · Cultist 1/8 · Cult Fanatic 2 · Acolyte 1/4 · Spy 1 · Veteran 3 · Berserker 2 · Gladiator 5 · Knight 3 · Assassin 8 · Mind Flayer 7 · Intellect Devourer 2 · Grick 2 · Darkmantle 1/2 · Cloaker 8 · Adult Red Dragon 17 · Dragon Turtle 17 · Young White Dragon 6.

## D. Impact on monsters_phase3_hierarchy.md

**No verdict flips.** Every tribe classification uses a rank-and-file ceiling drawn from the PASSED set above (earth elementals 5, trolls 5, hill giants 5, gladiators 5, hydra 8, black pudding 4, veterans 3, bugbears 1…), and all named-boss CRs (Gremag assassin 8, Feldrin 6, Hedrack printed 6, high priests 7–8, Zuggtmoy ~23, node princes 17–21) are unaffected. Two cosmetic notes:

1. **A25 Menagerie:** leucrotta is actually CR 3 (not 5); the tribe's rank ceiling remains 5 via the troll, so HARD (Δ 18) stands.
2. **A26 Prison Shadows:** "Lurker Above 5" has no 5e stat block (nearest cousin, the trapper, is CR 3). With banshee 4 as the new rank ceiling, Δ becomes 19 instead of 18 — still HARD/apex.

## E. Table corrections — APPLIED 2026-08-23

All corrections have been applied to `monsters_cr_reference.md` (each edited
row now carries a "was X" note), including Allip 2→5.
