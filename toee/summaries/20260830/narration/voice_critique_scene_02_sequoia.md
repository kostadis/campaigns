# Voice Critique — Sequoia, scene 02: Garbage Room and Fire Temple

**Narration:** `session_doc_scene_02_garbage_room_and_fire_temple.scrubbed.md`  
**Input shape:** per-scene

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `9d58d0d40afa`, 80 lines | run record (`.knobs.json`), post-#276 |
| Rulebook vs run record | **match** — all six scenes carry the same digest, and it equals the live file | `sha256(text.strip())[:12]` |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | read |
| Voice spec | resolved via roster declaration | `config/party.yaml` → `voice:` |
| Per-char examples | **NONE — 0 of 6 files declared** | no `examples:` keys, no `shared_examples:` |
| Global examples | none | no `shared_examples:` |
| Party doc | `docs/party.md` | 4/4 PCs |
| voice_lint | ran, exit 0 | 0 errors, 0 warnings, **1 skipped check** |


> **Suggested rewrites are `[grounded in spec only]`.** All six files in `examples/` are
> orphans — no roster entry declares them and there is no `shared_examples:` block, so
> under the post-#301 declared-not-routed rule they reach no prompt. The narrator wrote
> this scene with a voice spec and no examples.

## Budget ledger

Scope: single scene — **doc-level budgets NOT evaluable**; see `voice_critique_summary.md`
Budgets from: `voice/_genre.md` @ `9d58d0d40afa`

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| "the shape of" | 0 | 0 (base.md HARD BAN) | ok |
| portable portrait ("with the X of a man who") | 0 | 0 (base.md HARD BAN) | ok |
| behavioral taxonomy (any shell) | 0 | 0 (base.md HARD BAN) | ok |
| banned tics ("what could only be described as", "the cusp of", "the particular kind of") | 0 | 0 (rulebook) | ok |
| adverb-heavy combat (quickly/swiftly/brutally) | 0 | 0 (rulebook) | ok |
| recap framing | 0 | 0 (rulebook) | ok |
| connective em-dashes | 0 in prose | — | *not checked — rulebook states the permission (interrupted speech/thought) but no prohibition* |
| bookkeeping / filing caps | — | — | *not checked — rulebook declares no `yaml voice_lint` block* |
| doc-level numeric budgets | — | — | *not checked — rulebook declares none* |


## Flags

### [1] Rulebook conflict — false interruption assertion (CONFIRMED)

> “I hit—”

**Why:** A quote ending `—"` asserts the speaker was interrupted. The tape (cue 533) reads
`I hit…`, and the next two cues are the GM saying "Alright." and then **Sequoia himself**
continuing with "I'mma just roll this manually." Nobody spoke over him; he trailed off and
picked up his own turn. The assertion is false, and the narrator did not author it — the
`/voice-smooth` pass converted the raw extraction's `…"` endings to `—"` (raw: 30 `…"` / 0
`—"`; smoothed: 5 `…"` / 20 `—"`). Seven of those 20 reached narration; this is the one
that is wrong.

**Suggested rewrite:** `“I hit…”` — restore the trail-off. No attribution verb is attached,
so nothing is stranded. *[grounded in spec only]*

### [2] Unattributed dialogue — the narrator's own line reads as the NPC's (CONFIRMED)

> “Really? Yeah.”

**Why:** `scene_extractions_smoothed/02_*.md` assigns this to **Sequoia** — who is this
scene's first-person narrator. In the narration it sits untagged between two Varek lines
and two Zephyr lines, so alternation attributes it to Varek. Three speakers in one run;
alternation stops identifying anyone past two. This is Scan C's real hit — the other ten
runs in this directory are tagged two-handers and were cleared.

**Suggested rewrite:** tag it — `“Really?” I said. “Yeah.”` — or fold it into an action
beat. **Do not touch a word inside the quote.** *[grounded in spec only]*

### [3] Cross-narrator register bleed (PLAUSIBLE)

> Apparently our control of the Temple did not yet include dropping the sky on a garbage heap.

**Why:** `_genre.md` gives Sequoia "the minimum viable words needed to describe an
unpleasant fact" and gives the wry administrative aside to Zephyr ("Zephyr calculates
whether the cover is still profitable"). This sentence is a Zephyr-shaped joke in
Sequoia's POV. Marked plausible rather than confirmed: Sequoia's spec does license dry
demolition, and the sentence is funny. Compare his scene 06 close — "Useful lie." — which
is the register the spec describes.

**Suggested rewrite:** `We did not have the sky. We had a garbage heap.` *[grounded in spec only]*


## Reclassified table speech

none


## Verdict

The false interruption on “I hit—” is inherited from the extraction layer, not authored
here, and is a one-character fix; the untagged “Really? Yeah.” is the only thing in this
scene a reader would stumble on. Spot-edit both; no re-narration warranted.
