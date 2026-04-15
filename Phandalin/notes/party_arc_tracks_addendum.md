# Party Arc Tracks — Addendum to `party.md`

**Status:** Addendum covering a known bug in CampaignGenerator's `party.py`
(see `/home/kroussos/src/CampaignGenerator/TODO.md`). The generated
`docs/party.md` currently claims *"Only Brewbarry has a formally defined arc
score mechanic"* — that assertion is **wrong**. This file is the ground
truth until the generator is fixed.

---

## PC Arc Score Tracks

Three of four Phandalin PCs have complete, formally-defined arc score tracks
in `docs/tracking/`. The fourth (Vukradin) has none **by design**.

| PC | Track Name | Scale | Source File |
|----|------------|-------|-------------|
| **Brewbarry** | The Thistle's Echo Score — Telemetry of the Stolen Watch | 0–10 | `docs/tracking/The Thistle's Echo Score_ Telemetry of the Stolen Watch.md` |
| **Valphine** | The Searing Dawn Score | 0–10 | `docs/tracking/The Searing Dawn Score.md` |
| **Soma** | Soma's Meril's Legacy Score | 0–10 | `docs/tracking/soma-legacy.md` |
| **Vukradin** | *(none — by design)* | — | — |

---

## Brewbarry — The Thistle's Echo Score

**What it measures:** Brewbarry's gradual realization that his exile from
the Uthgardt tribe wasn't his fault. He was surgically neutralized by
Thistle Wendrod (a minor Seelie fey in Queen Titania's court) via a
magically potent goodberry concoction. Brewbarry believes it was his own
drunken negligence.

**Current value:** ~0–2 (implied — still pre-threshold)
**Next threshold:** 3

**Thresholds:**
- **3** — Psychological shift. Questions the timeline; hears phantom fairy
  wings and a bowstring snap; wonders if mundane mead could really have
  felled a Goliath.
- **6** — Subconscious rage activates. Irrational hatred of flying creatures,
  fey, and tricksters. **Starts distrusting Soma's magical food and potions.**

**Triggers (+1 each):**
- Magical food consumption (especially Soma's goodberries)
- Aerial archery by ally or enemy
- Seelie-style deception used by Vukradin or Valphine against a guard or
  sentry

**Standing GM recommendation:** "Stolen Rations" trigger — next rest, normal
food spoils, forcing magical food reliance. Describe unnatural fullness, tell
the player this is the last thing Brewbarry remembers before losing his
honor. +1.

---

## Valphine — The Searing Dawn Score

**What it measures:** Valphine's ascension as the Morninglord's most
unorthodox pain-worshiping living saint. Tracks her progress shedding
Lolth's sadistic tyranny and embracing Lathander's *redemptive, cauterizing*
pain. Hidden truth: Lathander isn't curing her Underdark trauma — he's
weaponizing it.

**Current value:** unspecified in source doc (assumed 0–2 until logged
otherwise)

**Tiers:**
| Score | State | Manifestation |
|-------|-------|---------------|
| 0–2 | **Sun-Kissed Novice** | Stabs own leg to heal it. Healing leaves temporary painless burn scars that fade. |
| 3–5 | **Priestess of the Crucible** | Healing feels like agonizing cauterizing heat; allies flinch even as healed. |
| 6–8 | **Halo of Embers** | Eyes permanently molten gold. Liars feel phantom sunburn on their neck. |
| 9–10 | **Searing Saint** | Cosmically recognized prophet of Lathander's wrath. Unlocks Absurd Boon. |

**Triggers (+1 each):**
- **Rejection of the Orthodox** — publicly dismissing Father Jerome,
  Merrygold Brightshine, or other "soft" Lathanderians
- **Pain-Aversion Therapy** — inflicting controlled pain on an NPC/ally then
  immediately healing it
- **Burden of the Shield** — using *Emboldening Bond* or *Balm of Peace* to
  willingly absorb an ally's pain/fear/exhaustion onto herself
- **Cult Expansion** — successfully converting a new NPC to her "Radiant
  Revelation" sect

**The Absurd Boon — "Supernova of Menzoberranzan"** (at score 10, once per
campaign): When Valphine drops to 0 HP or offers herself as sacrifice, she
becomes a miniature sun. Enemies within 60 ft: CON save or 10d10 radiant +
permanent Blinded. Allies within 60 ft: full heal + all conditions cured,
described as excruciating forge-heat flesh-knitting agony. Thematic payoff:
salvation and absolute suffering proven to be mathematically identical.

**Standing GM recommendation:** "The Heretic's Trial" — send an orthodox
Lathander paladin to audit her temple, force a theological debate, interrupt
with an immediate threat, let Valphine save the paladin's life via
Pain-Aversion Therapy.

---

## Soma — Soma's Meril's Legacy Score

**What it measures:** Soma's development in embodying Meril's discerning,
interventionist nature. Tracks her progress understanding and combating
both mundane and cosmic disturbances (especially Adabra's radicalism and
the Kraken Society). Unique structural feature: **Meril's Staff physically
awakens new abilities as the score rises** — the arc is mechanically
coupled to the item.

**Current value:** 0 at attunement — incremental status unclear

**Variable-magnitude triggers (unlike the other two PC arcs):**
| Value | Trigger | Example |
|------:|---------|---------|
| **+1** | Subtle Discernment | Aiding Interventionists in Withering Grove over Adabra; IDing psionic influence |
| **+2** | Active Intervention | Disrupting Kraken Society psionic outposts; securing psionic artifacts |
| **+3** | Unveiling Deception | Uncovering Adabra's draconic cultist dealings; recognizing illithid-tech weaponry |
| **+4** | Planar Harmony | Stabilizing planar breaches; confronting Adabra's Tiamat pact or Aletra directly |

**Staff evolution:**

- **Score 0 — Meril's Memento:** Quarterstaff + Nature's Whisper (advantage
  on Survival) + Discern Corruption (30 ft, 1/long rest)
- **Score 3 — Interventionist's Eye:** +1 weapon, Healing Bloom, Clear Mind
  reaction vs. charm/fear/psionic, advantage on Insight to detect false
  natural disasters
- **Score 6 — Planar Shield:** +2 weapon, Planar Sense (120 ft, distinguishes
  planar anomaly / extraplanar creature / KP device), Sanctuary of Harmony
  (20 ft zone immune to psionic fear + disadvantage on extraplanar attacks),
  Resonance of Truth (detect mental control / lies about conspiracies)
- **Score 9 — Cosmic Intervention:** +3 weapon, Warden of the Planes (3
  charges: Dispel Magic 5th, Plane Shift self, Scrying), Mielikki's Embrace
  (60 ft aura; unnatural creatures disadvantage to attack, natural allies
  temp HP + advantage on saves), Harmonize Planar Flow (1/week, DC 18 spell
  check to stabilize/close a planar anomaly or disable a KP device)

**Design note — why this arc is special:** It's the only PC arc with
variable trigger magnitudes, and it's tightly coupled to the villain
taxonomy. The +1/+2 tier maps to local Kraken + Adabra plots; +3 maps to
the Kraken deep reveal and Adabra's fanaticism; +4 maps to endgame KP /
Tiamat / Iymrith / Aletra. The score therefore doubles as a **DM-facing
diagnostic** for whether Soma's mechanical kit is ready for each villain
tier.

---

## Vukradin — No Arc Track (By Design)

Vukradin does not have an arc score track, and **one should not be created.**

**Rationale:** Vukradin is written with zero internal tension — a naive
Silver Tongue worldview that sees no conflict in his own goals. An arc
score mechanic implies a trajectory from one state toward another. That
framing is incompatible with the character. His "development" is measured
by what the world refuses to validate about him, not by an internal counter.

Player (Dave) has been explicit about this characterization and corrects
surface-level reads that try to impose internal tension onto Vukradin.

If future pipeline output suggests creating a Vukradin arc score, ignore it.
The character works *because* there's no dial to turn.

---

## Cross-references

- `docs/tracking/` — authoritative arc score definitions
- `docs/planning.md` — threat tracker (separate from PC arc scores; tracks
  Brundar's Echo, Planar Distortion, Fury of the Wild, Echoes Score —
  villain/faction-side, not PC-side)
- `/home/kroussos/src/CampaignGenerator/TODO.md` — the upstream bug that
  makes this addendum necessary
