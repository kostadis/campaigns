# Voice Critique (run 2) — Soma, scene 08: Secrets of the Buried Temple

**Run:** 2026-09-02, **second critique** · **Input shape:** per-scene · **Source read:** `session_doc_scene_08_secrets_of_the_buried_temple.scrubbed.md`

**Supersedes** the earlier critique of this scene, which read a stale `.scrubbed.md` fork of an older render.

## Inputs resolved

| Input | Resolved to | State |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `0a3d011c5f27`, 105 lines | **resolved — and now matches the run record.** The 10:39–10:44 re-render moved this scene onto the current rulebook |
| HARD BANS | `narrate/base.md` | resolved |
| Voice spec | `voice/soma_new_pipeline.md` | resolved (declared in `config/party.yaml`) |
| Examples | `examples/soma.md` | resolved |
| Global examples | none (`shared_examples:` absent) | ok |
| `voice_lint` | 0 errors / 0 warnings, per-scene **and** on an assembled proxy | clean; bookkeeping checks confirmed to have run on the proxy |
| Scan A — em-dashes | **0** in narration prose | ok |
| Scan A2 — trailing-dash provenance | **0** reaching narration | ok |

## Measure, this render vs the previous one

| | now | previous render | |
|---|---|---|---|
| Prose words / total | 556 / 846 — **65.7% prose** | 529 / 947 — 55.9% | **better** |
| Orphan quote runs | **3**, longest 3 | 7, longest 5 | |
| Epigrammatic closers | **0–1** | 2 | |
| Behavioral taxonomy | 0 | 0 | |

## This render fixed the scene

Every finding the previous critique raised against scene 08 is resolved or substantially improved.

| Previous finding | Status now |
|---|---|
| Un-narrated table procedural (22 quote lines) | **resolved** — prose share up from 55.9% to 65.7%; the door-by-door exchange is compressed into narration |
| Passive-perception / ability-score block (7 spans, hand-scrubbed in run 1) | **resolved by the re-render itself** — the model dropped it; nothing to scrub |
| 7 orphan quote runs, longest 5 | **3 runs, longest 3** |
| GM speech as dialogue (*"Pile of ochre jellies falls on your heads. No."*) | **gone** — now narration: *"No ochre jellies fall from the ceiling. This is fortunate, though less interesting."* |
| 2 epigrammatic closers | **0–1** |
| Missing reclassification hatch | still absent, but no longer load-bearing — the two remaining table lines were excised by scrub decision (23, 33), not by a fabricated hatch |

## Flags

### [1] Orphan quote runs ×3, all minor

33–38, 53–58, 95–100 — three lines each, all two-speaker exchanges with narration on both sides. **All three clear on reading**; none is a finding. Reported for completeness because the scan returned them.

### [2] Nothing else

Zero epigrammatic closers of the banned kind, zero taxonomy moves, zero portable tics, zero connective em-dashes, first-person present throughout, no POV bleed.

## Worth protecting in any future pass

- **11** *"Of course she does. The rest of us have been staring at stone, while she has been staring at the correct stone."*
- **93** *"She is probably right. I do not leave."*
- **47** *"Temples can be badly built, but stoneworkers do not usually waste this much labor without a reason."*
- **123** *"We can dig later, when the temple has fewer ways to fall on my bale."*

The cover-blocks deduction (105–119) survived and reads more clearly than it did before. This is now the second-strongest scene in the chapter after scene 03.

## Locked-dialogue anachronism — GM scope call, still open

**87–91, *The Princess Bride*.** The re-render improved the handling on its own: *Mostly dead.* is now Soma's **narration** at line 87 rather than a quoted line, with only *"…is still alive."* and *"That's right. Slightly alive."* in quotes. Your ch02 ruling keeps this. No action unless you want the marginal-note treatment.

## Verdict

Clean. No re-render needed and no spot-edits recommended — this render is the one to keep.

---
*Review only. Nothing applied. Cross-scene ledger in `voice_critique_summary.md`.*

