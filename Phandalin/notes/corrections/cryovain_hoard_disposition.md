# Cryovain's hoard — took vs. claimed

**Decision (2026-08-07, GM ruling during the ch46 consistency review):**
Vukradin **took** the hoard. He refused to **claim** it.

## The rule

The distinction is the whole point of the thread, and the grounding docs have been
collapsing it into "refused it," which is wrong:

- **Took** — the gold physically left Icespire Hold with the party. They carry it.
- **Refused to claim** — Vukradin will not treat it as party loot. His standing position
  is that it must either be **returned to its rightful owners** or **added to the UBT
  fund**. Never spent on the party.

So the party *has* ~3,000 gp of Cryovain's hoard, and simultaneously has no spendable
money. That is intentional: it is the mechanical engine of Vukradin's "every last copper
is blood" arc and of his poverty despite three campaign victories.

## What this fixes

`docs/campaign_state.md` and `docs/party.md` read:

> "~3,000 gp Cryovain hoard at Icespire Hold — unclaimed (Vukradin refused it)"

Wrong on location, misleading on disposition. Correct reading:

> Cryovain hoard — **carried by the party** as a fused, untransformed slag. Not claimed
> as loot. Donated to the UBT fund (ch46). Cannot be disbursed: the gold is fused inside
> a magical containment with a planar anomaly on it (identified by Soma via Meril's
> Staff). Requires an expert in Neverwinter to extract. Ser Kaelen tasked with it.

**Corrected by hand 2026-08-07** in both docs, at GM request:

- `docs/party.md` — obligations line, collective-resources line, Vukradin's motivations
- `docs/campaign_state.md` — Neverwinter pending objectives, active obligations, and
  key resources (the hoard was **missing entirely** from the asset list — the party's
  single largest holding was untracked)

Both docs are **generated** (CampaignGenerator outputs). These edits will be clobbered
on the next regeneration; each carries a `> **Hand-correction (2026-08-07)**` block under
its header pointing back here so the loss is visible. The durable fix is upstream — see
below.

## Root cause: the bible contradicts itself

The generated docs did not invent this. `docs/chapters/` states both readings, and the
generator picked the wrong one:

| Source | Says | |
|---|---|---|
| ch35:291 | a bandit tries to pull the hoard piece free of Vukradin's hands — "Vukradin held" | carried |
| ch44:410 | "the lump of fused dragon's gold sitting **untransformed in our packs**" | carried |
| ch45:10 | "the lump of dragon hoard nobody would touch **still sitting up at Icespire** like a stone in a boot" | **wrong** |
| ch45:128 | "I **left** three thousand pieces of Cryovain's frozen hoard **sitting in a hold**" | **wrong** |
| ch45:168–170 | Vukradin gestures at it on the town green — "we have **this** melted hoard of dragon gold"; "Everyone looked at the slag" | carried |

Lines 10 and 128 of `chapter_45_universal_basic_treasure.md` are the origin of the error,
and they contradict lines 168–170 of the same chapter — the slag cannot be at Icespire
and on the town green in the same session. Until those two lines are rewritten, every
regeneration will reproduce "unclaimed at Icespire Hold." They are authored in-character
POV prose, so the rewrite is a GM call, not a mechanical fix.

## The slag IS the hoard

There is no separate "lump of gold" item. The ch46 scene extractions refer to the same
object three ways — all one thing:

- "the untransformed lump of gold from Cryovain's hoard that the party refused to use" (scene 01)
- "this melted horde of dragon gold that we can't do anything else with" (scene 03)
- "a fused slag of dragon gold" donated to the UBT fund (scene 03 summary)

## Apply to

- ch46 recap and narration — never say the hoard was left at Icespire Hold or that
  Vukradin "refused it"; say he refused to *claim* it
- future recaps — the party is gold-rich and cash-poor at the same time; preserve that
- the containment/planar-anomaly extraction is an **open Neverwinter thread**, not a
  resolved beat
- entity registry — the anomaly links the slag to the planar thread only as Soma's
  in-character read; not yet confirmed canon (see scene 03, "those weird gnome things")

## Source
GM ruling 2026-08-07 during the ch46 (2026-06-23) scene-extraction consistency review.

Tracked as [campaigns#137](https://github.com/kostadis/campaigns/issues/137) — includes
the ch45 line-level fix, and a third unresolved disposition found in prep (the ice-block
was promised to the Eastern Heart orc band on the Icespire Hold reclamation).
