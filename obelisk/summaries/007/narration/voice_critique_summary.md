# Voice Critique Summary — Session 007, narrator: Zenvon Forepot

**Scope:** 8 scenes, 6,813 words, re-run 2026-08-01 19:10–19:15.
**Inputs:** `scene_extractions_smoothed/` · `voice/zenvon_voice.md` · `examples/zenvon.md` + `examples/house_style.md` · `docs/party.md` · `--reflections` (campaign_state + world_state).
**Backend:** `claude-code` / `claude-fable-5` (subscription). Critique by Opus 5.

> This replaces an earlier critique of the 18:36–18:51 run. Those reports and that narration are retained in `narration/.pre_rerun/`.

---

## 1. What the re-run fixed

The first run had two defects, both in the pipeline rather than the prose.

**Wrong input layer.** All 17 original `sd_narrate` invocations passed `--scene-extractions .../scene_extractions` — the raw layer. The `/voice-smooth` output never reached narration. Blast radius was smaller than it sounds: of 74 quoted lines, 65 were identical in both layers and 6 tracked raw. All 6 now track smoothed, including scene 06's signature deception line, which the first run had rebuilt with three hesitations the smoothing pass had deliberately removed.

**Entity-registry canonicalisation applied to dialogue.** `sd_narrate` auto-discovers `docs/entity_registry.yaml` and normalises aliases *before* Pass 5. The registry lists `Nezznar the Spider` (aliases `Spider`, `The Spider`) and `Iarno "Glasstaff" Albrek` (alias `Glasstaff`), so spoken aliases were rewritten to canonical names **inside quotation marks**:

- `"Tell me more about Glasstaff and Spider"` → `"…about Iarno and Nezznar the Spider"`
- `"Black Spider."` → `"The Black Spider. Nezznar."`
- Wick — a thug who "just carries crates" — was made to say `"Iarno?"`

`campaign_state.md:65` records the Black Spider as *"confirmed real… **No name, no face, no location**."* The party does not have "Nezznar." Fixed by moving the registry aside for the run (`load_alias_map` → `{}` → identity normaliser, `campaignlib/npc.py:78`); **the registry has been restored.** Nezznar now appears zero times in the narration, and cannot return via `--reflections` — the string is absent from both `campaign_state.md` and `world_state.md`.

The re-run also dropped a third, quieter defect: the first run's scene 07 had Zenvon say *"I would prefer to eliminate him…"*, which is the wording from `examples/zenvon.md`, not the session. It now carries the actual line (*"I would prefer to attack him…"*).

**Structural note.** Both fixed defects are the same failure: a transform that is correct for *identity* or *prose* was applied to *speech*. The registry schema is `aliases, fragments, note, provenance, source, type` — there is no knowledge-state field, so it cannot express "not yet known to the party." That gap has not gone away; it just has no vector into this run. It resurfaces in scene 08 through `--reflections` (see §3).

---

## 2. The one new defect — `--prose-mode` reaching inside quotations

Scene 01, two instances, both verified against the smoothed extraction *and* all three VTT transcripts:

| Source & VTT | Narration |
|---|---|
| `"Wait, 8 points of damage does nothing?"` | `"Wait, that does nothing?"` |
| `"I'm gonna move back. I'm just at 4 points of damage, so…"` | `"I'm gonna move back. I'm just about out, so…"` |

`--prose-mode` is documented as "Strip mechanical / GM framing from **narration**." It stripped mechanics from dialogue. The second instance is the more serious: *"I'm just at 4 points of damage"* is a specific HP state, and *"I'm just about out"* asserts something the player did not say. The number is stable across all three transcripts, so there is no transcription ambiguity involved.

This is the same class as the two defects in §1, and it is the last one standing. It did not generalise beyond scene 01 — scenes 02–08 show no equivalent stripping.

---

## 3. Scene 08 naming — ✅ RESOLVED

**GM ruling, 2026-08-01: *"he doesn't know the name."*** Applied in `.scrubbed.md`: `Mirna Dendrar and her two children` → `The Dendrars`. Zenvon keeps the family name (Wick gave it up in scene 07; the GM confirmed the link on the spot) and loses the first name he was never told. No first name of any freed captive now appears anywhere in the narration.

Original finding retained below.

**Mirna Dendrar is never named in any session-7 source.** The extraction and `session-summary.md` say only *"two women and a young boy"* / *"the Dendrar family."* The name reaches narration through `--reflections` injecting `world_state.md`. It is grounded in your grounding docs, not invented — but Zenvon has no on-screen moment of learning it. `world_state.md:48` flags the same discrepancy itself, and records the children as Nars (13) and **Nilsa (18)**, so an 18-year-old is one of the "two women," not one of the "two children" the narration describes. Left as a decision, not an edit — see the scene 08 report.

---

## 4. Findings across the eight scenes

| Scene | Em-dash | Register | Verbatim | Other |
|---|---|---|---|---|
| 01 Battle in the Crypts | 16 | `filed` | **2 altered quotes** (§2) | over-built simile |
| 02 Exploring the Crypts | **3** | `filed` | clean | house-style address |
| 03 Ambush in the Slave Pens | 16 | `angle` | clean | examples-file sentence quoted verbatim |
| 04 Rescue and Pursuit | 8 | *(false pos.)* | clean | — |
| 05 Pit Trap and Cellar | **4** | clean | clean | lyrical verb; narrated silence |
| 06 Deception in the Barracks | 10 | clean | clean | — |
| 07 The Bandit's Gambit | 6 | `shape` (borderline) | clean | narrated silence |
| 08 Return to the Cells | 7 | *(false pos.)* | clean | Mirna naming (§3) |
| **Total** | **70** | 4 real, 2 false | **2 altered** | — |

**Quote verification:** 75 quotes checked against the smoothed source; **72 verbatim**, 2 altered by `--prose-mode`, 1 legitimately merged from the gm-assist bullet (marked verbatim in the extraction). **Speaker attribution: zero defects.**

### Strongest recurring theme: em-dashes

70 across the session, with **scenes 01 and 03 carrying 32 between them**. Every scene report has a conversion table with per-line replacements. One caveat recorded in the scene 04 report: line 53 is reported speech carrying the source's own punctuation and must **not** be converted — the mask heuristic cannot see that, and a blind sweep would damage it.

### Two smaller patterns worth a single decision each

- **Narrated silence** (scenes 05, 07): *"I have never told her so, and I will not start now"* / *"I am not going to describe it."* The spec is emphatic that his silences *are* the characterisation; announcing a refusal converts a silence into a statement about one. Both scenes have a better sentence sitting right next to the flagged one.
- **House-style direct address** (scenes 02, 08): *"I will tell you what I did not say"* / *"I am telling you plainly."* Both come from `examples/house_style.md` — the global file, whose header warns *"Only the manner transfers."* The surrounding content is on-voice; only the frame is borrowed.

---

## 5. What held

- **The ESL ruling held throughout.** Sentence-final `", yes"` (*"Makes sense, yes"*, *"minimum back, yes"*), doubled acknowledgement (*"Storylines. Storylines."*, *"yes, yes"*, *"Got it, got it"*), the `"So,"` opener, mid-sentence `"like,"`, and the preserved formal reach of `"eliminate him"` all shipped unnormalised. Nothing was traded down to idiomatic English.
- **`"Turn on bed"`** — Zenvon's mishearing of "Turn Undead" — is rendered with the narrator's own gloss rather than silently corrected. The single best test of the ruling in the session, and it passed.
- **The inline `[Zenvon]` mixed-attribution tags work.** Scene 05's whip line sits inside a **GM** block in the smoothed source, tagged `[Zenvon]` during the voice-smooth pass; the narration resolved it and assigned the speech correctly. Useful input for whether the seven tagged blocks need upstream re-attribution — on this evidence, not urgently.
- **Saturation improved sharply.** Ledger vocabulary fell from 73 tokens to 39; the borrowed *"for a moment I was not counting anything / Then I was again"* construction fell from 4 scenes to 1 (scene 03, flagged).

---

## 6. Recommendation

Everything outstanding is a spot-edit or a decision. **No scene needs re-narrating.**

1. Fix the two scene-01 quotes by hand (§2). If you re-run instead, `--prose-mode` will strip them again — this needs a pipeline fix or a manual patch, not another pass.
2. Sweep the em-dashes scene by scene from the tables, skipping scene 04 line 53.
3. Decide the Mirna question (§3).
4. Decide once on narrated silence and on the house-style address, then apply to both instances of each.

**Standing pipeline items, for whenever you next run this:**
- `--scene-extractions` must point at `scene_extractions_smoothed`.
- The entity registry must be moved aside for narration runs, or `sd_narrate` needs a flag to restrict alias normalisation to prose. There is currently no such flag.
- `--prose-mode` should not modify text inside quotation marks.

These reports are review-only. Nothing in the narration files has been modified.
