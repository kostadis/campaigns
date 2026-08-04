# Voice Critique Summary — Chapter 47 (2026-07-29)

**Narration set:** `summaries/20260729/narration/session_doc_scene_01..07_*.md` (raw — no `.scrubbed.md` variants exist yet)
**Inputs available for every scene:** `voice/_genre.md`, `voice/<name>_new_pipeline.md`, `examples/<name>.md`
**Input note:** this campaign's voice specs are named `<name>_new_pipeline.md`, not the `<name>_voice.md` the skill looks for. Nothing was missing; the fallback was not needed.

## Status — applied 2026-08-03

Fixes were applied to the **`.scrubbed.md`** layer (never the raw `.md`), per the skill's rule that `assemble.py` reads the scrubbed variant. All seven scenes now have a `.scrubbed.md`.

**GM rulings taken before applying:**

| Question | Ruling |
|---|---|
| Mechanics — restore dice results or leave stripped? | **Leave stripped.** Flag closed by ruling, not by edit. The `_genre.md` / `/scrub` conflict is resolved in `/scrub`'s favour for social scenes. |
| Tense — hand-convert 03 and 05, or wait for a re-run? | **Hand-convert both now**, because a re-run regenerates through the un-fixed `sd_narrate.py` and would re-corrupt the restored quotes. |
| Flags needing NEW prose | **Edits only — no new sentences.** |
| Scene 01's three misattributions | **Fix all three.** |

**Applied:** 34 guarded sentence-level edits across scenes 01, 02, 04, 06, 07; full present→past conversion of scenes 03 and 05; 3 attribution corrections in scene 01. Narration-level em-dashes went **26 → 0** across all seven files.

**Verified after applying:** quoted spans changed vs. raw = 10, which is exactly the 7 approved alias restorations plus the 3 spans of the approved ledger rewrite — no other quote was touched. Residue re-scan 0/7 files. Register-vocab scan clean. No player real names.

**Second pass — the deferred prose, written on request (same day, ruling reversed):**

All five items are now closed. 14 insertions, no quoted text altered.

| Flag | What was written |
|---|---|
| Scene 04 [5] | Closing beat after the lottery line, landing on a verdict pair ("Restricted. Done.") per the spec's verdict-word list. |
| Scene 05 [4] | Four Valphine reads broken into the two Cassian quote-blackouts — the manifold priced as a military asset, "Nobody official" turned into an inference, and two on the gnome. |
| Scene 05 [5] | A faith beat at the studio-fund line, using the spec's own vocabulary (radiant / indifferent / inexhaustible) and her standing read that surface-dwellers mistake restraint for kindness. |
| Scene 06 [3] | The "And yet" construction added at the caught-thief beat, with the paragraph break carrying the pause. |
| Scene 07 [1] | All four quote-chains broken into paragraphs with Vukradin interior between them — the counting-off before the scheduling refusal, Brewbarry improving the gala, the ensemble finishing the wine name, and the ledger landing on "Done." |

**One deliberate deviation, flagged for your call.** `brewbarry_new_pipeline.md` quotes the signature as **"My rage consumes me. And yet—"**, with an em-dash. Writing it that way would have reintroduced the one narration em-dash in the file. It is written as **"And yet."** with the paragraph break carrying the pause; `examples/brewbarry.md` supports the non-dash form ("And yet, there is something about this man's fear"). Revert to the dash if you want the spec form exactly.

**Verification after the second pass:** spoken text compared segmentation-insensitively across all seven scenes — scenes 02, 05 and 06 byte-identical to raw; 01, 03, 04 and 07 differ only by the approved alias restorations and the ledger rewrite. One dialogue span in scene 07 was *split* in two (`"Performance, it's gonna be a late night, yeah."` / `"Are you arresting me?"`) with no character added or removed — the sentence break was already there. Narration em-dashes still 0/7. Residue 0/7. Register-vocab clean. Banned "with the [Adj] [Noun] of someone who" construction: absent. No player names.

**Still open (upstream, not fixable in this layer):**

- `sd_narrate.py:190-198` still normalizes `sx["moments"]`. The 8 restorations below are a per-session stopgap.
- Scenes 04 and 05 still narrate the same events twice, inherited from the scene split in `scene_extractions/`.

## Flag counts

| Scene | Narrator | Flags | Narration em-dashes | Register-vocab hits |
|---|---|---|---|---|
| 01 Factions and Fame in Neverwinter | Soma | 6 | 0 | 0 |
| 02 Past the Common Chord | Brewbarry | 6 | 2 | 0 |
| 03 Arrival at the Moonstone Mask | Valphine | 6 | 6 | 0 |
| 04 Lord Cassian and the Performance | Vukradin | 5 | 7 | 0 |
| 05 The Statue Returned, a Quest Begun | Valphine | 5 | 0 | 0 |
| 06 The Margaster Shakedown | Brewbarry | 3 | 0 | 0 |
| 07 A Summons from the Lord Protector | Vukradin | 5 | 11 | 0 |
| **Total** | | **36** | **26** | **0** |

Mechanical scan B came back completely clean across all seven files — no `shape`/`filed`/`geometry`/`structure`/`vector`/`calculated` in any narration prose. The two `angle` hits in scene 01 are the idiomatic "what's your angle" sense inside reported dialogue and are correct. That register problem, which recurs most sessions, did not appear at all this time.

---

## Blocking finding — verbatim quotes are being rewritten by the alias map

**This is not a voice issue and no per-scene edit can fix it.** A systematic alias diff of `scene_extractions_smoothed/` against `narration/` found **8 corrupted spans across 4 scenes** — quotes in the narration that do not match what was said:

| Scene | Narration | Source (`scene_extractions_smoothed/`) |
|---|---|---|
| 01 | `"Right, so there's, like, Dagult Neverember?"` | `"Right, so there's, like, Lord Neverember?"` |
| 01 | `"who's the Laeral Silverhand."` | `"who's the Open Lord of Waterdeep."` |
| 01 | `"Lord Dagult Neverember, Dagult Neverember of Neverwinter"` | `"Lord Dagult Neverember, Lord Protector of Neverwinter"` |
| 03 | `"But Dagult Neverember has declared..."` | `"But Lord Neverember has declared..."` |
| 04 | `"Oh, you're a Vukradin. Sing a song!"` | `"Oh, you're a bard. Sing a song!"` |
| 07 | `"...Dagult Neverember of Neverwinter, I extend a formal welcome..."` | `"...Lord Protector of Neverwinter, I extend a formal welcome..."` |
| 07 | `"The Dagult Neverember has followed your recent activities"` | `"The Lord Protector has followed your recent activities"` |
| 07 | `"The Dagult Neverember has an interest in Neverwinter's cultural future"` | `"The Lord Protector has an interest in Neverwinter's cultural future"` |
| 07 | `"...at dawn at the… at the Lathander stuff."` | `"...at dawn at the… at the Morninglord stuff."` |

**All 8 were restored by hand in the `/scrub` pass on 2026-08-03** — see the `.scrubbed.md` files. That is a stopgap for this session only; the defect below still ships on every future narration run.

Note `"who's the Laeral Silverhand"`: `Open Lord of Waterdeep` is a legitimate alias correctly pointing at Laeral Silverhand, and substituting it produced a sentence in which she is her own title. This is the corollary from `notes/llm_quote_pipeline_lessons.md` in its purest form — **the correct aliases do most of the damage.**

**Cause, confirmed in code.** `docs/aliases.json` contains:

```json
"Dagult Neverember": ["Lord Neverember", "Lord Protector", "Neverember", "Lord Pretender"]
"Vukradin": ["Bard"]
```

and `session_doc/sd_narrate.py:190-198` applies that map as a **write-time substitution** to the scene extractions before the model ever sees them:

```python
alias_map = load_alias_map(args.dossier_dir, registry_path=find_alias_registry(Path.cwd()))
normalize, _ = build_alias_normalizer(alias_map)
if alias_map:
    recap = normalize(recap)
    for sx in scene_extractions:
        sx["moments"] = normalize(sx["moments"])   # <-- the ## Verbatim moments block
        sx["summary"] = normalize(sx["summary"])
        sx["body"]    = normalize(sx["body"])
```

`sx["moments"]` is the verbatim quote block. Every quote in every scene is passed through the alias table on the way in.

This is the same defect PR #231 removed from `scene_extract.py`. It is still live in `sd_narrate.py`, one stage downstream. The tells documented in `notes/llm_quote_pipeline_lessons.md` are all present: the doubling (`"Lord Dagult Neverember, Dagult Neverember of Neverwinter"`), and the fact that the *correct* aliases do the damage — `Lord Protector` really is Dagult Neverember, and Vukradin really is the bard, which is exactly why the substitution is invisible to a fact-check and fatal to a record of what was said.

**Recommendation:** file this against CampaignGenerator as a sibling to #231 and re-run narration once `sd_narrate.py` stops normalizing `moments`. Until then, the five quotes above should be restored by hand in any `.scrubbed.md` before assembly.

---

## Recurring themes, in order of what to spend re-narration budget on

**1. Both Valphine scenes are in present tense.** Scenes 03 and 05 narrate entirely in present ("We leave", "Cassian sits at it"); 01, 02, 04, 06, 07 are past. `_genre.md` states the rule without qualification — "**First-person past tense, always**" — so the assembled document flips tense twice. This is the one finding that is cheaper to fix by re-running the two scenes than by editing them.

**2. Em-dash density is concentrated, not spread.** 24 of the 26 narration-level dashes sit in scenes 03, 04 and 07; scenes 01, 05 and 06 have zero. In scene 07 (11 dashes) they are a symptom rather than a tic — the narrator drops out for four long stretches and the paragraphs become quote chains stitched with dashes. Fixing the structure there removes most of the dashes for free.

**3. Mechanics were stripped from every scene.** Every dice result in the source is gone from the narration: Vukradin's "20 persuasion," his natural 20 and Valphine's 16 on the forged writ, Valphine's passive 17 at the door. `_genre.md` says "Drop hit points, distances, spell names directly into prose. Mechanics are not separate from feeling," and Vukradin's spec names the procedural register as one of three things that must be present. **This one needs your ruling** — the `/scrub` skill exists to remove exactly these numbers, so `_genre.md` and `/scrub` are in direct conflict and I am not going to resolve that by assumption.

**4. Three speaker misattributions in scene 01,** all assigning GM or Vukradin lines to Valphine. Details in `voice_critique_scene_01_soma.md`; these belong to `/session-summary-consistency`, not here.

**5. Scenes 04 and 05 narrate the same events twice.** The statue handover, "For free drinks," the finger-click, the "wrapped around their finger" exchange and the performance all appear in both, because `scene_extractions/04` and `05` both contain the handover. That is a scene-splitting problem upstream of narration and cannot be fixed in either narration file.

---

## Where the voices are working

Worth saying, because it tells you where *not* to spend budget: scene 06 (Brewbarry) is the cleanest file in the set — zero dashes, zero register hits, three small flags — and its closing beat is the best writing in the session. Valphine's Menzoberranzan readings in scene 03 ("A body destroyed beyond raising is not misfortune; it is craftsmanship. Someone paid extra"), Soma's algae-bloom and beaver-dam observations in scene 01, and Vukradin's Alducia passage in scene 07 are all fully in spec. The narrators are distinct from each other; the problems are mechanical and structural, not a collapse into house style.

---

## Reminders

- **This report is review-only.** Nothing in the narration files was modified. You decide which flags to act on.
- **Apply fixes to `.scrubbed.md`, not the raw `.md`** — that is what `assemble.py` picks up. No `.scrubbed.md` files exist yet, so the first fix pass creates them.
- **Per-sentence edits are cheapest** for flags 2–5 above. The present-tense problem in scenes 03 and 05 is the exception: re-running `session_doc.py --scene 3 5` after tightening the tense instruction is less work than converting two files by hand — and it is worth doing *after* the `sd_narrate.py` alias fix, so the quote corruption is cleared in the same pass.
