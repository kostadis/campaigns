# Consistency Report — Chapter 54 ("The case of the missing tickles")

Document: `summaries/20260601/session-summary.md`
Checked against: `docs/party.md`, `docs/campaign_state.md`, `docs/world_state.md`,
and Candlekeep prep — `candlekeep_pickup_crime_scene_to_interviews.md`,
`candlekeep_day_one.md`, `candlekeep_murders_module_inventory.md`,
`candlekeep_murders_arc.md`.

## Method note

The automated `check_consistency.py` pass returned **"no errors."** That verdict was
incomplete. A follow-up hand-check against the module inventory and session prep
(the precision pass — names, attribution, ordering) surfaced five issues the
single-pass LLM missed. This report supersedes the script's clean bill.

## What was correct (confirmed against the module inventory)

- All suspect/NPC name spellings: Janussi, A'lai Aivenmore, Sylvira Savikas,
  Daral Yashenti, Fheminor Scrivenbark, Teles Ahvoste, Kalan Strongbranch,
  Hollypocket, Queenie, Tadric.
- Core mystery logic: Daral's poisoned *Golden Ass* Deadwinter gift; the
  heart-removed-to-block-resurrection deduction; the Deadwinter prophecy
  ("the keeper falls, the heart is sold"); Fheminor as Janussi's intended
  successor; the disguise-self conspiracy framing Sylvira.
- Stonespeaker Crystal mechanics (2 charges / long rest).

## Findings and resolutions

### 1. Fembris Lancer — internal gender contradiction — FIXED
Summary called Fembris "he" (scene beat) and "she" (NPC entry).
**Ruling:** standardize to **she/her**. Applied.

### 2. Fembris Lancer — species diverged from prep — FIXED
Prep: "young **half-elf** adjutant" (with "Bookwyrm" a separate NPC).
Module inventory: "Fembris Lancer — acolyte adjutant" (no species).
Summary: "**green dragonborn** bookwyrm."
**Ruling:** prep is canon — Fembris is a **half-elf** adjutant; "green dragonborn"
was a transcription error. Corrected in both the scene beat and the NPC entry.

### 3. Fheminor "returned drunk at 10:30 p.m." — misattribution — FIXED
Canon makes **Daral** the alcoholic (module inventory: "Great Reader; alcoholic";
prep: "Daral visibly drunk"; the cat's "stinky breath one"). The drunk late-night
door-pounding return belongs to Daral, not Fheminor.
**Ruling:** re-attributed to Daral. Fheminor's entry now keeps only her sober
evening arrival; Daral's entry carries the ~10:30 p.m. drunk return and final
argument.

### 4. Magic Missile — "three wounds" vs "two holes" — NOT AN ERROR (self-corrected)
Initially flagged as a 3-vs-2 contradiction and edited to "three" throughout.
The scene extraction carries the GM's verbatim words:
*"There are three roughly circular impact wounds... Two of the impacts have
created a hole in the chair back."* So the canon is **three wounds, two of which
punched through** — the summary's "two holes" was correct. The edit was reverted;
the opening-paragraph prose was tightened to "three impact wounds — two of them
punched clean through" so it no longer reads as if all three penetrated.

### 5. Disguise tell delivered via a different sense — NO FIX (informational)
Prep's planted "disguise self" tell is *"Queenie hissed at her — ten years, never
once hissed."* The summary delivers the same revelation as *"looked like Sylvira
but did not smell like her."* Same clue, different sensory channel — the table
routed it through the direct cat interview (Stonespeaker). Not an error; recorded
so prep and summary don't later read as contradicting each other.

## Propagation check — `scene_extractions_new/` (6 scene files)

Checked whether the summary-level errors propagated downstream into the per-scene
VTT extractions. **They did not — the scene files are clean.** The errors were
introduced at the summary-synthesis layer, not inherited from the extractions:

- **Fembris species/gender (#1, #2):** scene files never give Fembris a species,
  "bookwyrm/dragonborn" label, or pronoun. The "green dragonborn bookwyrm / he-vs-she"
  detail exists only in the summary. No propagation.
- **Fheminor "drunk at 10:30" (#3):** scene 06 has the cat seeing Fheminor merely
  *arrive* ("the short-legged one... and then, later, Daral, the stinky breath one");
  scene 05 correctly attributes the 10:30 p.m. drunk door-pounding return to **Daral**
  (verbatim: *"Then he came back at 10.30pm, drunk as a skunk..."*). The scene layer
  was right; the summary fabricated the Fheminor-drunk detail. My summary re-attribution
  matches the scene truth.
- **Magic Missile (#4):** scene 02 holds the correct canon (three wounds, two holes) —
  see finding #4. This is what exposed my own bad edit, now reverted.

Net: no fixes needed in `scene_extractions_new/`. The check confirmed the summary is
the only layer that drifted.

## Forward note

Finding #2 means the **prep and any Fembris dossier still describe a half-elf
adjutant + a separate Bookwyrm NPC**, while play has settled Fembris as the
party's "bookwyrm" assistant. Reconcile the prep/dossiers forward if that merge
is intended to stick.
