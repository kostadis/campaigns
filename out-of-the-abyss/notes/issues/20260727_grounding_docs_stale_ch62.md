# ISSUE — Grounding docs claim Chapter 62 but reflect Chapter 61

**Filed:** 2026-07-27
**Severity:** High — all four grounding docs assert a party position, a live
antagonist, and a party level that are all wrong. Any prep built on them
without cross-checking `docs/chapters/` inherits the errors.
**Scope:** `docs/campaign_state.md`, `docs/world_state.md`, `docs/planning.md`,
`docs/party.md`
**Authoritative source used to verify:** `docs/chapters/chapter_62_the_key_is_secured.md`

---

## Summary

All four grounding docs are stamped as current through Chapter 62. **None of
them contain a single event from Chapter 62.** They describe the Chapter 61
cliffhanger and label it Chapter 62.

The single sentence that captures it: the docs say the party is **confined in
Deneir's Sanctum** with an unresolved standoff pending. In fact the party has
**left the Sanctum, crossed the keep, found Kalan alive, been deputised as
Watchers of Candlekeep, run to the North Galleries, killed Moziqodo in the
domed rotunda, and saved Tadric** — and they are standing in the rotunda now.

---

## Verification performed

| Check | Result |
|---|---|
| `docs/distill_extractions/extract_063.md` exists and covers Ch.62 | ✅ **28 hits** for Ch.62-unique markers (`Sea Warden` / `deputiz` / `Tadric`) |
| `docs/distill_extractions/extract_062.md` (Ch.61) contains those markers | **0 hits** — confirms 063 is the Ch.62 extract |
| Ch.62-unique facts present in any of the four grounding docs | **0** across all four *(one apparent `bookwyrm.*dead` hit in `world_state.md:82` is a false positive — that sentence is about **Alkrist** being dead)* |
| Grounding-doc mtimes | All four: **27 Jul 2026 00:13** — regenerated together |
| Per-NPC dossier sidecars | ✅ **Current.** `docs/npcs/a_lai_aivenmore.new_notes.063.md` correctly records Ch.62 in full |

**The extraction layer has Chapter 62. The synthesis layer did not consume it.**

---

## Per-document differences

### `docs/campaign_state.md` — *"Authoritative as of Chapter 62"*

| Says | Actual (Ch.62) |
|---|---|
| "Party Current Situation … **confined in Deneir's Sanctum** … under guard" | They left hours ago. **They are in the domed rotunda**, standing over Moziqodo's corpse. |
| "A'lai holds the first High Tower key … **awaiting Moziqodo, who brings the second**" | **Moziqodo is dead** — killed by the party in the rotunda. He was the pit fiend, not a courier on the way. |
| "**Kalan Strongbranch's fate:** Last seen running, breathless. Alive or not — unknown." | **Alive.** Found at the Sea Warden's Tower. He **deputised all four as Watchers of Candlekeep.** |
| NPC table: "Bookwyrm \| **Alive** (status post-key-seizure unconfirmed)" | **Dead.** Throat torn, heart intact and in place. |
| NPC table: "Tadric \| Alive \| Crime-scene guard; rattled" | He was **carrying the real key #2**, was nearly killed for it, and was healed by Grygum. |
| "Daz: **inert High Tower key** (helmed-horror beacon)" | It was **Kalan's decoy from the first hour**, and **Grygum** is holding it now, not Daz. |
| No Moziqodo row in the NPC table at all | He is the session's antagonist and is now dead. |
| Not recorded anywhere | Party deputised as Watchers; real key #2 recovered; milestone to **level 9**. |

### `docs/world_state.md` — *"Current state as of Chapter 62"*

| Says | Actual (Ch.62) |
|---|---|
| "**Most recent development (ch62):** A'lai Aivenmore has **seized the first Hightower key from Bookwyrm**" | **Wrong mechanism and wrong chapter.** Moziqodo tore Bookwyrm's throat out and took the key. A'lai is the buyer, not the hand. This is the Ch.61 cliffhanger mislabelled. |
| "awaiting an unknown party, **Moziqodo**, who is bringing the second key" | Moziqodo is a **pit fiend** and is **dead.** |
| "**Kalan Strongbranch** was last seen running hard … his survival is unknown" | Resolved. Alive, at the Sea Warden's Tower. |
| Candlekeep NPC table: "**Bookwyrm** \| Alive" | **Dead.** |
| Candlekeep NPC table: "Kalan \| Alive (**survival now uncertain, ch62**)" | Certain. |
| §9 Canon Timeline item 10: "**Ch62** — A'lai seizes the first key from Bookwyrm and retreats to the High Tower awaiting Moziqodo. Kalan's fate unknown." | This is **Chapter 61**. Chapter 62 is missing from the timeline entirely. |

### `docs/planning.md`

| Says | Actual (Ch.62) |
|---|---|
| Moziqodo dossier: "**Alive**; last location unknown (ch62)… Expected by A'lai to arrive with the second key" | **Dead**, in the rotunda, identified by Tadric. |
| Bookwyrm dossier: "**Alive**; Candlekeep, top floor chambers. Acting Head of Candlekeep" | **Dead.** Her office is a ruin and her dying note (*"He is using the beast to—"*) is on the desk. |
| Kalan dossier: "Alive; overseeing the Alkrist safe and Deneir's Sanctum" + "survival and current whereabouts are **uncertain**" | At the **Sea Warden's Tower**; deputised the party; handed over the Watcher's Stair shortcut. |
| Active Plots #1: "The second key was transferred from Kalan → Grygum → Daz" | Correct as far as it goes, but **omits that this key was a decoy** and the real one was on Tadric — the central reveal of the chapter. |
| Active Plots #2: titled "**Kalan's Fate & the Domed Rotunda**" | Both halves of that title were resolved in Ch.62 and the entry records neither. |
| Fembris dossier | Omits his Ch.62 confession that **A'lai was in the room** when the key was reported to Bookwyrm — the second pillar of the Threefold Proof. |

### `docs/party.md`

| Says | Actual (Ch.62) |
|---|---|
| "**Current location:** Candlekeep — confined in **Deneir's Sanctum**" | The domed rotunda, North Galleries. |
| "The **inert key Daz carries** is a helmed-horror beacon" | The decoy, and **Grygum** holds it. Daz holds the **sapphire** (taken from A'lai in the session that follows). |
| "A'lai … awaits **Moziqodo**, who is bringing the second" | Dead. |
| "**Kalan Strongbranch's fate:** … survival unknown" | Resolved. |
| ⭐ "Zalthir — **Monk 8**" · "Thorin — **Fighter 8**" · "Grygum — **Cleric 8**" · "Daz — **Wizard 8**" | ⭐ **The party milestoned to 9** at the end of Ch.62 (Thorin's POV: *"the quiet knock inside the chest…"*; he ribs Zalthir for levelling). **All four class lines are one level low** — this is the entry most likely to cause a live mechanical error at the table. |
| Collective assets | Omits the **real key #2**, recovered from Tadric. |

---

## Root cause

**Verified:** the Ch.62 extraction (`extract_063.md`) exists and is complete.
The four grounding docs were regenerated together at 27 Jul 00:13 and consumed
extracts up to **062** only.

**Not yet confirmed — needs a look at the actual invocation:**

- `CLAUDE.md` documents the regeneration commands as taking **`summaries.md`**
  as input (`campaign_state.py summaries.md`, `distill.py summaries.md`,
  `party.py --summaries summaries.md`). **There is no `summaries.md` at the
  campaign root.** So the input path actually used is undocumented, and may
  differ per script.
- Whether this is (a) a stale run that predated `extract_063`, (b) an off-by-one
  in the extract range, or (c) an input path that points somewhere that stops at
  062 — is unresolved.

**Contributing factor — the known BOM off-by-one.** Per the campaign's own notes,
a UTF-8 BOM on `docs/TheUnderdark.md` hides the first heading from
`split_chapters.py`, so **every chapter file is numbered one low** — the file
`chapter_62_the_key_is_secured.md` carries the internal header *"# Chapter 59."*
The extraction counter (`extract_063`) is offset differently again. **Three
counters disagree**, which makes "are we current through 62?" unanswerable by
inspection and easy to get wrong.

---

## Impact

- **Prep built on these docs inherits live-antagonist errors.** The
  `/gm-session-prep` run for the next session initially drafted against a plan
  in which Moziqodo was still inbound with a key. Caught only by reading
  `chapter_62_the_key_is_secured.md` directly.
- **The prepped back-half scripts carry the same class of drift** —
  `candlekeep_hightower_session.md` asserts *"Manshoon is incoming — his shape
  came clear at Monday's cliffhanger"*, but Manshoon has **zero mentions across
  chapters 57–62** and had never been named at the table. Two ⛔ "still owed"
  marks in `candlekeep_arc_flowchart_v2.md` (Sylvira first contact, Glabbagool's
  Whispering Dome) are likewise stale — both ran, in Ch.60 and Ch.58.
- **The level-8 entry in `party.md` is a table-facing mechanical error.**

---

## Suggested actions

1. **Re-run the four generators including `extract_063`**, and diff the output
   against this file's tables before trusting it.
2. **Fix `CLAUDE.md`'s documented commands** — they reference a `summaries.md`
   that does not exist. Whatever the real input is, document it.
3. **Reconcile the three counters** (chapter-file number, internal header
   number, extract number) or record the offsets somewhere a reader hits first.
   The BOM fix is a GM call per `MEMPALACE_HORIZON.md`, but the *offsets* can be
   documented today.
4. **Add a cheap staleness check** — assert that the highest-numbered extract is
   represented in the regenerated docs, and fail loudly if not. A single
   Ch.N-unique string grep would have caught this.
5. **Until fixed, treat the four grounding docs as Chapter-61 documents**, and
   verify anything load-bearing against `docs/chapters/` per the trust hierarchy
   in `CLAUDE.md`.

---

*Staging note: this is an issue report, not canon. The corrected Ch.62 state is
recorded in `notes/session_prep/20260727_candlekeep_the_man_with_the_metal_hand.md`
under "Corrections to the prepped files."*
