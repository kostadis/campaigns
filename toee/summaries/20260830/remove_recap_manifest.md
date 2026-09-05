# remove-recap manifest — session 20260830, Chapter 34 "The Sleeper in the Iron Coffin"

**Run date:** 2026-09-05
**Ran at:** after `/staged-consistency` Stage 0 (2026-09-05) and Stage 1 (this run),
**before** `/scene-extract`. This is the recommended insertion point on the skill's
cost table: nothing downstream had been produced, so nothing renumbered and nothing
needed re-narrating.

**Duplicated chapter:** `summaries/20260823/` — **Chapter 33, "The Necromancer's
Thank You Note", 2026-08-23.**

---

## How it was found

Not by the detector. `/staged-consistency` Stage 1 turned it up while auditing
`session-summary.md`: the recap's opening paragraph was a near-verbatim
enhancement of VTT cue 71, and the same events were already carried by Chapter
33's own documents (Minotaur ×30, ghoul ×15, Shield +1 ×9, reception hall ×8).

The consistency check could not have found this and did not: no grounding doc or
prep file records that the tape opens with a recap, and every fact in the recap is
true — it is simply true of the previous chapter.

---

## Phase 1 — detect (deterministic)

Input: a scene-shaped file built from VTT lines 7–231 with the Stage-0 speaker map
(`Kostadis Roussos`→GM, `Thomas Kolivakis`→Zephyr, `Nicholas Roussos`→Sequoia,
`george`→Zinnia). There was no `scene_extractions_smoothed/` — this ran
pre-extraction.

```
=== 01_opening_recap.md   [RECAP — strong]  score 4/6
    56 quotes, GM share 0.86, longest GM-only run 41
    past-tense markers 163 vs live-play markers 1
    opening_markers: ['\blast time\b']
    boundary candidates -> closing sting at line None, first live play at line 24
```

**The script's boundary proposal was wrong and was not used.** Its single
"live-play marker" is `"Hello, gentlemen, can you hear me?"` matching the pattern
`you hear` — pre-session scheduling chatter, not play. The boundary was taken from
the tape instead, where the GM states it aloud.

### The boundary, from the tape

| VTT line | |
|---|---|
| 51 | *"I put the summary over there in the Google chat. For those of you who are curious, read it."* |
| 59 | *"So… Shall we begin?"* |
| **71** | recap opens — *"The party stood at the threshold of a ruined reception hall…"* |
| **223** | recap closes — *"…As the saying goes, beggars can't be pickers."* |
| **231** | **"Remember all of that?"** — explicit close marker |
| 259 | *"I need to load… I need to open up a file."* — session proper begins |

---

## Phase 2 — rescue: NOTHING WAS RESCUED, and here is why that is safe

`recap_unique.py` reported *"every bullet is well covered upstream"*, but that
result was **not** relied on: run pre-extraction there are no `*(…)*` editorial
annotations for it to mine, which is precisely the channel the skill warns new
canon hides in. All 56 cues were read by hand.

**1. GM asides / new canon — none.** The span is an uninterrupted monologue: 41 of
56 consecutive GM cues, GM share 0.86, 163 past-tense markers against 1 (spurious)
live-play marker. No correction, no clarification, no reveal to the party.

**2. Chapter 34 bookkeeping — none.** The pre-recap chatter is scheduling only:
*"is George on the call?"*, *"can you hear me?"*, *"I put the summary over there in
the Google chat."* No level-ups, no subclasses, no spells gained, no rests.

**3. Beats Chapter 33 missed — none.** Proper-noun coverage of the spoken recap
against `summaries/20260823/gm-assist.md` + `session-summary.md`: **36 of 37**
names covered. Closing beats checked individually — Barkinar ×11, Romag ×8,
Minotaur-eats-undead ×3, "beggars" ×1, black cloaks ×10, Chief of
Staff/Operations ×3, educational system/curriculum ×7.

### The one uncovered name

**`Xemia`** — VTT 215: *"Xemia helped calm her haul haul him back to the surface."*

An ASR garble of **Zinnia**, which is already how the enhancement pass rendered it
(*"Zinnia helped Calmer haul him back to the surface"*). Not new canon.

> **OPEN — glossary candidate.** `Xemia` is **not** in
> `notes/vtt_transcription_corrections.md`. It is a new wrong-form for **Zinnia**
> and wants a glossary row. Not written: adding a row is a canon edit and was not
> part of this run's ruling. `calm her` → `Calmer` in the same cue is already
> known ASR behaviour.

---

## Phase 3 — GM rulings (2026-09-05)

1. **Cut it all at that boundary.** Chapter 34 begins at the prisoners' torn chains.
2. **Trim `gm-assist.md` too** — it is what `enhance_summary` reads, so leaving it
   would let the next run reintroduce the whole recap.
3. **Keep the three load-bearing entries, reframed as prior state** — the Minotaur,
   the Shield +1, and the Necromancer's Note.

---

## Phase 4 — what was cut

Every cut range was guarded by an assertion on its exact first and last line before
anything was written (fail-closed), and both files were snapshotted first.
Post-edit both were diffed against the snapshot to confirm that the only **added**
lines were the reframes and seam repairs listed below.

### `session-summary.md` — 568 → 428 lines

| Section | Cut | Kept |
|---|---|---|
| `## Summary` | 14 paragraphs (lines 7–34) | opens at the prisoners |
| `## Memorable Moments` | 6 of 18 blocks | 12 |
| `## Scenes` | 4 of 10 — Minotaur's Throne, Temple Storerooms, Ambush of the Demented Ghoul, The Sunken Treasure | 6, opening at The Missing Prisoners |
| `## Locations` | 3 of 9 — Ruined Reception Hall, Temple Storerooms, Water Supply Chamber | 6 |

### `gm-assist.md` — 281 → 200 lines

| Section | Cut | Kept |
|---|---|---|
| `## Summary` | 8 paragraphs (lines 6–21) | opens at the prisoners |
| `## Memorable Moments` | 4 of 7 blocks | 3 |
| `## Scenes` | the same 4 scenes | 6 |
| `## Locations` | the same 3 locations | 6 |

> **A partial first pass, corrected.** `gm-assist.md`'s Summary was trimmed first
> and the other three sections were missed — they restate the same Chapter 33
> material as bullets and entries. Caught by a dangling-reference sweep and
> completed in the same run. This is the skill's own documented failure mode
> ("cutting scene 01 and stopping is the most likely way to half-fix this").

### Carryover entries — kept, reframed as prior state

| Entry | Chapter 34 relevance that justifies keeping it |
|---|---|
| NPCs › The Minotaur | Fed from the party's body supply; Dren reports it "has food for three days" and is left with authority to keep it fed |
| Items › Shield +1 | Gives Calmer AC 21 in the Greater Temple storeroom ambush, where one predator misses all five strikes |
| Items › Necromancer's Note | Drives the whole chapter — the hunt for its author, and the decision to burn the refuse chamber rather than leave him the remains |

### Seams repaired

- **Both documents opened mid-thought** on "the four prisoners", who were
  introduced only in the cut recap. Rewritten to establish them in their own first
  sentence, re-ordering existing clauses and asserting nothing new.
- **Items › Frostbrand** (`session-summary.md`) opened with *"It reminded Sequoia
  that their plan had always been to remain discreet"* — an event in the cut recap
  (VTT 123). Orphaned sentence dropped; the Chapter 34 content kept.

---

## Follow-up rulings (2026-09-05, same session) — all four CLOSED

### 1. `Xemia` → `Zinnia` — CLOSED

Not a new ruling in substance: the Zinnia glossary row already carried **`Xenia`**,
and `Xemia` is that same wrong-form with one letter changed. Added to the
**left-hand** column of the existing row — accumulating evidence, not an inversion;
the bolded canonical form was untouched.

The cue was also recorded: **`cue-0052`** in `transcript_corrections.yaml`, fixing
both garbles in the line — `Xemia` → `Zinnia` and `calm her haul haul` → `Calmer
haul`. Safe to change because the cue sits inside the cut recap span, so no
surviving artifact quote depends on it.

### 2. Items › Magical Trident — CUT from both documents

Checked against the whole tape, not just the documents: **"trident" and "Terjon"
each appear exactly once on the entire recording — VTT 127, inside the cut recap.**
Nothing after line 231. The "reference by Calmer" that justified the entry *was*
the cut speech, so the entry had no Chapter 34 content at all. Cut, consistent with
the boundary ruling; Chapter 33's document keeps the record.

### 3. `Rosco` → `Sequoia` — ruled an ASR garble

GM ruling: not a name. Added as a wrong-form on the **Sequoia** glossary row, and
recorded as **`cue-0574`**.

Evidence: Nicholas Roussos plays Sequoia and was narrating in the third person;
`Rosco` appears in no canonical source, no other transcript, and Sequoia has no
companion, familiar or alias in `party.md`. The second independent transcription
renders the same moment as only *"Like, you had one job."* — so there was **no
cross-tool agreement that the word was spoken**, which is the test that would have
argued for it being real. The enhancement pass had already silently resolved it to
Sequoia; this makes that resolution an explicit ruling that will now be caught on
every future transcript.

### 4. Frostbrand attribution + Vurakhal — both applied

- **`gm-assist.md` Items › Frostbrand** said *"Calmer later jokingly chided it"*.
  The tape (cue 574) is Nicholas → **Sequoia**. Corrected, and its orphaned
  Chapter 33 opening sentence dropped in the same edit, matching the repair already
  made in `session-summary.md`. This closes Stage 1 finding #8.
- **Vurakhal** — my Phase 2 framing of this as "an upstream gap the enhancement
  pass missed" was **wrong, and is corrected here.** Reading the three cues in
  context, he never appears in Chapter 34: he is *offered and declined twice*.
  VTT 1055 — *"Do you go to Vurakhal directly, or do you go through the captain of
  the guard…?"* → *"Go to the captain of the guard."* VTT 1351 — *"Do you want to
  take those [fire arrows], or do you want to get Vurakhal?"* → *"I'll take the
  fire."* There was no scene to miss. Both declines are now recorded in the Fire
  Temple material of both documents, from the tape, with nothing invented.

### 5. Frostbrand ownership — CLOSED, GM ruling 2026-09-05

**"Sequoia also possesses Frostbrand."**

This turned out not to be new canon. It is already recorded in six places, and the
disagreement was between those and the **live** grounding docs, which had never
caught up:

| Already correct | |
|---|---|
| `docs/chapters/chapter_31_…talking_swords.md:130` | *"What's your name?" **Frostbrand**.* — the sword names itself, from the tape |
| `docs/world_state_draft.md:41, 153` | *"sentient ice longsword… now **bonded to Sequoia**"*; chose him after rejecting Zinnia and Calmer |
| `docs/campaign_state_draft.md:21, 87` | *"Sequoia claimed **Frostbrand**"* (Ch31) |
| `docs/party_draft.candidate.md:16, 38` | Frostbrand plus two shortswords |
| `notes/handouts/player_quest_log.md:120` | *"Sequoia — … **Carries Frostbrand**"* |
| `notes/handouts/player_quest_log_calmer.md:127` | *"**Sequoia** — Bears Frostbrand…"* |

**Applied** — note the GM said *also*, so Frostbrand was **added** alongside the
short sword, never substituted for it:

- `docs/party.md:19` — party-wide magic items now read *"Frostbrand and magical
  short sword (Sequoia)"*.
- `docs/party.md` Sequoia › Items of Significance — Frostbrand added above the
  short sword, with the Ch31 bonding and the fact that it chose him.
- `docs/world_state.md:33` — Frostbrand added above the short sword, with its
  origin in the Fire Temple's trapped offering box (area 212).
- `docs/entity_registry.yaml` — the **note** on the Frost Brand entry now records
  Sequoia as bearer. Verified surgical: of 918 entities, exactly one note field
  changed and no name, type or alias anywhere was touched.

These are spot edits on generated grounding docs, the same treatment CF5 got for
the party levels. Regeneration remains the durable fix, and is tracked by CF12.

### 6. Registry name — CLOSED, GM ruling 2026-09-05

**"It's Frost Brand the item type, and the name of the sword's personality is
Frostbrand."** Two names, two things.

The entry's parenthetical was therefore obsolete — the intelligence had named
itself in Ch31, long after that placeholder was written. Renamed, with the item
type kept as an alias:

```diff
- - name: Frost Brand (unnamed intelligent longsword)
-   type: item
+ - name: Frostbrand
+   type: item
+   aliases:
+     - Frost Brand
```

**Filed under the personality name per the `Snoop` precedent already in this
registry** — `[item] Snoop — intelligent longsword +1, LG alignment, Int 13…` —
which is the same shape: a sentient sword entered under its own name with the item
type in the note. The alias keeps a transcript that says "Frost Brand" resolving
here instead of scanning as an unknown proper noun.

Verified surgical: of 918 entities **exactly one differs**, `Frostbrand` is unique
as a name, `Frost Brand` unique as an alias, and no other entry claims either. The
old name survives in exactly one place — inside the note, as renaming provenance.

**Projections regenerated** (`registry project .`). `docs/entity_inventory.md` and
`docs/aliases.json` are both marked *generated — do not hand-edit*, and both were
stale on rulings from the merged PR, so the regeneration also picked up four
approved changes that had never been projected: Cistern Chamber's shield +1 (CF4),
Barkinar's and Landers' succession chains (CF3), and the removal of the `Tolubb`
aliases from Captain Tolub (CF13). No unrelated drift.

**Deliberately not changed.** `docs/background/toee-t14-adventure-inventory.md:805`
and `notes/proper_nouns_adventure.txt:445` both still read *"Frost Brand (unnamed
intelligent longsword)"*, and correctly so: the first is the published module's own
record, where the sword genuinely is unnamed, and the second is a flat dictionary
rebuilt *from* those module inventories. The naming happened at this table, not in
the module. Frostbrand is already covered for scanning purposes by the registry and
by the spell-pass glossary.

## Post-ruling verification

- `sd_corrections check` — **81 corrections in the record, 81 still apply; all
  1,319 cues explained; the tape is reproducible.**
- `sd_verify_quotes` against the regenerated tape — 5 verified / 4 near / 3
  unverified, **identical to before the tape was regenerated**, confirming the two
  new cue edits disturbed no quoted span. The 3 unverified were adjudicated by hand
  in Stage 1 and are faithful (each spans two adjacent cues).
- Full glossary sweep (264 wrong-forms) — **zero hits** in `session-summary.md`,
  `gm-assist.md`, and the regenerated cleaned tape.

## Renumbering

**None.** No `scene_extractions*/`, no `plan.md`, and no `narration/` existed when
this ran. Scene numbering will be clean from the first extraction.

## Untouched, by the hard invariant

`GMT20260830-150238_Recording.transcript.vtt` (raw archive),
`GMT20260830-150238_Recording.transcript.cleaned.vtt` (generated tape),
`transcript_corrections.yaml` (the record), and
`session_2026_08_30_..._transcript.vtt` (second independent transcription).
The recap **was** said; the tape is the record of what was said.
`summaries/20260823/` was not touched either — the recap is the copy, and Chapter
33 is the original.

## Standing question for this campaign

There is no `notes/scrub_register_policy.md` in `toee/`. Two rulings from this run
are worth promoting into one if the campaign keeps recurring:

1. Does this campaign cut opening recaps by default? (Ruled yes, this session.)
2. Is the pre-recap scheduling chatter dropped with them? (Dropped, this session —
   it was inside the same cut and carried nothing.)
