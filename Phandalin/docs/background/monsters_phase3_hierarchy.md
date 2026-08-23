# Phase 3 — Boss-Tier ΔCR Hierarchy (Phandalin Essentials Kit campaign)

**Method (from `name-module-monsters` skill):**
- ΔCR = CR(boss) − CR(highest rank-and-file in that tribe).
- Δ < 4 → **NOMINAL** (leader in name only — a stat-block upgrade, not a threat jump).
- Δ > 4 → **HARD** (genuinely more dangerous than the rank and file).
- Δ == exactly 4 → **NOMINAL+** (borderline-hard — flagged for review; none in this campaign).
- Boss *weaker* than an elite subordinate (negative Δ) = **peer finding** — reported, not an error.
- Apex creatures that command no tribe (ancient dragons, dracoliches) = **apex/HARD *threat***, not a "tribe boss."
- All CRs from `monsters_cr_reference.md` (base + extended tables). Named individuals are
  EXCLUDED from renaming but their CR is used here to evaluate the boss tier.

**Scope note:** This is a *multi-book* campaign (4 modules). Per the skill, the authoritative
leadership view is a chain-of-command supplement, provided below. Boss CRs for named faction
leaders are taken from the extended CR table; their stat blocks are NOT renamed (Phase 2 excluded them).

---

## A. Campaign Chain of Command (leadership-org supplement)

```
APEX THREATS (command no tribe; apex/HARD threat)
├── Cryovain — adult white dragon (DoIP)            CR 13   [killed by campaign's end]
├── Claugiyliamatar ("Old Gnawbone") — ancient green dragon (SDW/DC)
│      possessed by Ebondeath                        CR 22   [apex HARD]
└── Ebondeath / Chardansearavitriol — black-dragon dracolich spirit (SLW/DC)
       the campaign's true mastermind                CR 14   [apex HARD]

FACTION BOSSES (named, EXCLUDED from renaming)
├── Fheralai Stormsworn — Talos war priest            CR 8   → Tribe 1 (Cult of Talos) + Tribe 21 wing
├── Ularan Mortus — Myrkul war priest                CR 8   → Tribe 2 (Cult of Myrkul) + undead galleon
├── Galas Windrage — Talos war priest (pirate wing)  CR 8   → Tribe 26 (Ship Rethnor)
├── Emberlost — bound death knight (galleon soul)    CR 17  → Tribe 21 (Undead Galleon)
├── Rega Swarn — master thief (Chimera Crew)         CR 5   → Tribe 22
├── Gahza — sahuagin high priestess                  CR 2   → Tribe 24
├── Lhammaruntosz ("Claws of the Coast") — bronze dragon CR 15 → Tribe 19 (Bronze Shrine)
├── Thalivar's ghost / Gallio Elibro — wizards       CR 4 / 6 → Tribe 17 (Thalivar's Beacon)
├── Jarlaxle Baenre — drow lord (Bregan D'aerthe)    (no block) → Tribe 27
└── Hissain / Grannoc / Yargath / Zeleen — local leaders (excluded) → Tribes 3,4,15,16
```

---

## B. Per-Tribe ΔCR Analysis

Convention: "boss" = the named faction leader (excluded) where one commands the tribe; otherwise the
highest-CR generic creature is noted as "leaderless / external leadership." Δ is computed against the
**highest rank-and-file CR** in that tribe.

| Tribe | Boss (CR) | Highest rank-and-file (CR) | ΔCR | Verdict |
|-------|-----------|----------------------------|-----|---------|
| 1 Cult of Talos | Fheralai Stormsworn (8) | Half-blue dragon gladiator (9) | **−1** | NOMINAL (peer) — her elite gladiators outrank her |
| 2 Cult of Myrkul / Ebondeath | Ularan Mortus (8) | Drowned Death-Knight Vestige (17, generic) | **−9** | NOMINAL (peer) — a stronger unnamed vestige serves the cult; Ebondeath = apex HARD |
| 3 Orcs | external (Grannoc/Yargath, excluded) | Orc (1/2) | n/a | Leaderless / external Talos leadership |
| 4 Blights | Grannoc (2, excluded) | Vine Blight (1/2) | 1.5 | NOMINAL |
| 5 Axeholm | Axeholm castellan (named, excluded) | Ghoul (1) | n/a | Named leadership only |
| 6 Dragon Barrow | — | Invisible Stalker (6) | n/a | Leaderless |
| 7 Dwarven Excavation | — | Ochre Jelly (2) | n/a | Leaderless |
| 8 Shrine/Ogres | — | Ogre (2) | n/a | Leaderless |
| 9 Mountain's Toe | — | Carrion Crawler (2) | n/a | Leaderless |
| 10 Loggers' Camp | — | Ankheg (1) | n/a | Leaderless |
| 11 Gnomengarde | Korboz/Gnerkli (excluded) | Mimic (2) | n/a | Named leadership only |
| 12 Tower of Storms | Miraal/Moesko (excluded) | Hunter Shark (2) | n/a | Named leadership only |
| 13 Displaced Lone | — | Manticore (3) | n/a | Single creature |
| 14 Boars | Gorthok (excluded) | Boar (1/4) | n/a | Named leadership only |
| 15 Whiskered Gang | Zeleen (excluded) | Wererat (2) | n/a | Named leadership only |
| 16 Mere of Dead Men | — (regional beasts) | Hydra (8) / Yuan-ti Abom (7) | n/a | Leaderless regional |
| 17 Thalivar's Beacon | Thalivar ghost (4)/Gallio (6, excluded) | Stone Golem (14) | **−10** | NOMINAL (peer) — the stone golems are the real threat |
| 18 Trail Beasts | Pinchwit (excluded) | Wyvern (6) | n/a | Named leadership only |
| 19 Bronze Shrine | Lhammaruntosz (15, excluded) | Alkilith (12) | **3** | NOMINAL — dragon only 3 above its demon infiltrator |
| 20 Claugiyliamatar's Creatures | Claugiyliamatar (22, excluded) | Wood Woad (5) | **17** | **HARD** (apex) |
| 21 Undead Galleon | Emberlost (17, excluded) | Stone Giant Skeleton / Blackguard (8) | **9** | **HARD** (named boss) |
| 22 Chimera Crew | Rega Swarn (5, excluded) | Veteran (3) | **2** | NOMINAL |
| 23 Iniarv's Tower Undead | Ularan / Chimera (excluded) | Greater Zombie (5) | n/a | External leadership |
| 24 Sahuagin | Gahza (2, excluded) | Giant Shark Skeleton (5) | **−3** | NOMINAL (peer) — Gahza outranked by her skeleton |
| 25 Leilon Defenders | Hazz Yorrum / Neverember (excluded) | Veteran / Knight (3) | n/a | Named leadership only |
| 26 Ship Rethnor | Galas (excluded) / unnamed bandit captains | Bandit Captain (2) | 0 | NOMINAL (peer) — *Throatcutter* officers = peers |
| 27 Bregan D'aerthe | Jarlaxle / named captains (excluded) | Drow Elite Warrior (8) | n/a | External leadership |
| 28 Gulch Wereboars | — | Wereboar (4) | n/a | Feral pack, leaderless |

---

## C. Boss-Tier Hierarchy Tree (visual)

```
HARD  ▓▓▓ (boss genuinely more dangerous than the rank and file)
 ├─ Claugiyliamatar's Creatures  (ancient green dragon 22 vs wood woad 5, Δ17) — APEX
 ├─ Undead Galleon Crews         (death knight Emberlost 17 vs blackguard/skeleton 8, Δ9) — NAMED BOSS
 └─ Cult of Myrkul — Ebondeath   (dracolich 14 apex; Ularan only 8 vs vestige 17) — APEX

NOMINAL  ▓▓ (leader ≈ rank-and-file upgrade, or outranked by elites / peer finding)
 ├─ Cult of Talos        Fheralai 8 < half-dragon gladiator 9   (Δ −1, peer)
 ├─ Cult of Myrkul       Ularan 8 < drowned death-knight 17     (Δ −9, peer)
 ├─ Thalivar's Beacon    Gallio 6 < stone golem 14             (Δ −10, peer)
 ├─ Sahuagin             Gahza 2 < giant shark skeleton 5       (Δ −3, peer)
 ├─ Bronze Shrine        Lhammaruntosz 15 > alkilith 12         (Δ 3)
 ├─ Chimera Crew         Rega 5 > veteran 3                     (Δ 2)
 ├─ Blights              Grannoc 2 > vine blight 1/2            (Δ 1.5)
 └─ Ship Rethnor         bandit captain 2 = bandit captain 2    (Δ 0, peer)

LEADERLESS / EXTERNAL LEADERSHIP  ░ (no generic boss; ΔCR n/a)
 ├─ Orcs (Talos-led), Axeholm, Dragon Barrow, Dwarven Excav, Shrine/Ogres,
 │  Mountain's Toe, Loggers' Camp, Gnomengarde, Tower of Storms, Displaced Lone,
 │  Boars, Whiskered Gang, Mere of Dead Men, Trail Beasts, Iniarv's Undead,
 │  Leilon Defenders, Bregan D'aerthe, Gulch Wereboars
```

---

## D. Bottom Line

**Boss-tier verdicts:**
- **HARD (3):** Claugiyliamatar's Creatures (apex), Undead Galleon Crews (named boss Emberlost), Cult of Myrkul *via* Ebondeath apex.
- **NOMINAL (8):** Cult of Talos, Cult of Myrkul (Ularan), Thalivar's Beacon, Sahuagin, Bronze Shrine, Chimera Crew, Blights, Ship Rethnor.
- **LEADERLESS / external leadership (17 tribes):** no generic boss entity; leadership is a named/excluded NPC or absent.
- **NOMINAL+ (Δ==4) edge cases: NONE** — no tribe sat exactly on the borderline.

**Notable peer findings (boss weaker than an elite subordinate):**
1. **Fheralai Stormsworn (war priest 8)** is *outranked* by her own half-blue-dragon gladiators (9). The Cult of Talos's real teeth are its elite monsters, not its priestess.
2. **Ularan Mortus (8)** is outranked by the unnamed Drowned Death-Knight Vestige (17) serving in his Mausoleum — the cult's horror is the undead, not the priest.
3. **Gallio Elibro (6) / Thalivar's ghost (4)** are far below the Stone Golems (14) they bound at the Beacon — the golems are the encounter's true threat.
4. **Gahza (2)** commands a Giant Shark Skeleton (5) she cannot match — her priestesses' ritual outranks her personally.

**Apex threats (HARD, command no tribe):** Cryovain (13, killed), Claugiyliamatar (22, possessed), Ebondeath (14 dracolich). These are the campaign's scaling wall, not tribal bosses.

**CR table completeness:** `monsters_cr_reference.md` was extended with 31 module-appendix / MM creature CRs (war priest, anchorite of Talos, sword wraith, air elemental myrmidon, dark tide knight, blackguard, half-dragon gladiator, drow elite warrior, stone giant skeleton, boneclaw, skeletal swarm, greater zombie, etc.) before this analysis, per the skill's "extend the table before Phase 3" rule. Eleven entries carry "(est)" flags for DM review (half-dragon templates, skeleton variants, swarms).

**Coverage:** all 28 tribes (161 consolidated groups) from `monsters_phase1_scan.md` carry a ΔCR verdict here. Every named leader used in the boss tier is on the Phase 2 EXCLUDED list and was never renamed.
