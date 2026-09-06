# Voice Critique — session 20260830, Chapter 34 (6 scenes)

**Input shape:** per-scene, directory. Effective set follows `collect_scene_files` precedence —
`.scrubbed.md` for scenes 02 and 03, raw `.md` for 01, 04, 05, 06.

**3,840 prose words** (verbatim dialogue, italic thought and HTML comments excluded).
**3 flags — 2 confirmed, 1 plausible — all in scene 02.** Four scenes are clean.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `9d58d0d40afa`, 80 lines | run record, post-#276 |
| Rulebook vs run record | **match** | all six `.knobs.json` carry the same digest, and it equals the live file |
| HARD BANS | `base.md` | read from the CampaignGenerator checkout |
| Voice specs | **4/4 resolved** — calmer, sequoia, zephyr, zinnia | `config/party.yaml` `voice:` declarations |
| Per-char examples | **0 declared** | no `examples:` key on any character |
| Global examples | **none** | no `shared_examples:` |
| `examples/` orphans | **6 files, reaching no prompt** | see below |
| Party doc | `docs/party.md` | 4/4 PCs parsed |
| voice_lint | ran, exit 0 | 0 errors, 0 warnings, **6 skipped checks (1/scene)** |

### The digest looked wrong and was not

`sha256` of the file's raw bytes is `0acc4f5db373` / 81 lines against a recorded
`9d58d0d40afa` / 80 — which reads as "the rulebook was edited after this render." It was not.
The file is unmodified in git and its mtime is ~19h *before* the render. The pipeline digests
`text.strip()`, which gives `9d58d0d40afa` and 80 lines exactly. **Recorded so the next run does
not re-raise it as a false alarm.**

### 6 example files reach no prompt

`combat_and_consequences.md`, `ensemble_comedy_and_npcs.md`, `introspection_and_observation.md`,
`multi_pov_and_pacing.md`, `political_maneuvering.md`, `stakeout_and_interrogation.md`.

Under the post-#301 declared-not-routed rule, a file nothing declares is **unused, not shared** —
there is no fall-through global block any more. `config/party.yaml` gives every character a
`voice:` and none an `examples:`, and declares no `shared_examples:`. So the narrator wrote all
six scenes from a voice spec with **zero example prose**.

This is not a defect in the render — it is the #301 fix working as designed — but it means every
suggested rewrite in these reports is `[grounded in spec only]`, and it is why category 6
(cliché / on-the-nose simile) could not be checked against this campaign's own sentences.
Declaring `examples:` on the four characters, or a `shared_examples:` list, would change what
the next render receives.

### voice_lint's skip is a real "not checked", but a benign one

Every scene reports `[skipped] bookkeeping/filing checks — voice/_genre.md has no
```yaml voice_lint block`. That is cause 3 of the five: **this campaign declares no filing
register**, so there is nothing to check. It is not a delivery failure. The doc-level banned
constructions *did* run and returned zero.

## Budget ledger

Scope: whole document, 6 scenes, 3,840 prose words.
Budgets from `voice/_genre.md` @ `9d58d0d40afa` and `base.md`.

| Budget | Observed | Budget | Verdict |
|---|---|---|---|
| "the shape of" | 0 | 0 (HARD BAN) | ok |
| portable portrait ("with the X of a man who") | 0 | 0 (HARD BAN) | ok |
| behavioral taxonomy, any shell | 0 | 0 (HARD BAN) | ok |
| recap framing | 0 | 0 (HARD BAN) | ok |
| rulebook banned tics | 0 | 0 | ok |
| adverb-heavy combat | 0 | 0 | ok |
| POV bleed | 0 confirmed | 0 | ok |
| tense (first-person past spine) | 1 present-tense run, licensed | — | ok |
| connective em-dashes | 3 in 3,840 prose words | — | *not checked — rulebook states the permission, not a prohibition* |
| bookkeeping / filing caps | — | — | *not checked — no `yaml voice_lint` block* |
| doc-level numeric budgets | — | — | *not checked — rulebook declares none* |

Nothing this campaign's rulebook states is breached. The em-dash row is a **note**: the rulebook
licenses the dash for interrupted speech or thought and is silent on connective use, so per the
skill's 3c the honest report is that the rule does not distinguish. At 3 in 3,840 words there is
no overuse to discuss either way.

## Findings

**[1] False interruption assertion — `“I hit—”`, scene 02. CONFIRMED.**
The tape has `I hit…` (cue 533), and the next speaker to matter is Sequoia himself. Nobody spoke
over him. Provenance: the `/voice-smooth` pass converted the raw layer's trail-off ellipses to
em-dashes — **raw `scene_extractions/`: 30 `…"` and 0 `—"`; smoothed: 5 `…"` and 20 `—"`**. Seven
of the 20 reached narration and six are legitimate (`"Figure out why, and then—"` is cut off by
Dren; `"Just burn the—"` is completed by the GM; the rest are self-arrests). This one is not.
Fix: restore `“I hit…”`.

**[2] Unattributed dialogue — `“Really? Yeah.”`, scene 02. CONFIRMED.**
Assigned to **Sequoia** upstream — the scene's own first-person narrator — but printed untagged
between two Varek lines and two Zephyr lines. Three speakers, so alternation identifies nobody.
Scan C raised 11 runs; the other 10 are tagged two-handers and were cleared.

**[3] Cross-narrator register bleed — scene 02. PLAUSIBLE.**
"Apparently our control of the Temple did not yet include dropping the sky on a garbage heap."
is a Zephyr-shaped aside in Sequoia's POV. Plausible, not confirmed — his spec licenses dry
demolition, and the line is good.

## Per-scene

| Scene | Narrator | Prose words | Share | Flags |
|---|---|---:|---:|---|
| 01 The Missing Prisoners | Zephyr | 647 | 16.8% | — |
| 02 Garbage Room and Fire Temple | Sequoia | 569 | 14.8% | **3** |
| 03 The Supply Room Ambush | Zinnia | 808 | 21.0% | — |
| 04 Administrative Headaches and Orders | Zephyr | 595 | 15.5% | — |
| 05 A Message from Shadows | Calmer | 703 | 18.3% | — |
| 06 Return to Nulb | Sequoia | 518 | 13.5% | — |

Shares are even; no scene under-narrates.

## Locked-dialogue anachronisms — GM scope call

**None outstanding.** `/scrub` settled this session's register question already: the modern
administrative vocabulary (`supply chain`, `logistics`, `inventory control`) is ruled **in canon**
as the campaign's premise, and `friendly neighborhood necromancer` is ruled **keep**. Both are
recorded in `notes/scrub_register_policy.md` §3b, so they are not re-raised here.

## Reclassified table speech

One hatch per scene, six total. Each is `sd_narrate` making a scope call about what is
out-of-fiction; `assemble.py` strips them, so this is the last review point. Nothing in them
looked wrongly reclassified — they are the roll-by-roll and map-handling residue `/no-mech`
did not reach, which is the correct destination for it.

## Verdict

Scene 02 carries all three flags and two are one-line fixes; the other four scenes breach nothing
the rulebook states. The strongest finding is not a voice problem at all — it is a punctuation
assertion inherited from the smoothing layer, where converting 30 trail-off ellipses into 20
em-dashes silently claimed an interruption that the tape does not record.
