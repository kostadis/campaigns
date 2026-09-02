# Voice Critique — Soma, scene 03: First Sight of Phandalin

**Run:** 2026-09-02 · **Input shape:** per-scene · **Supersedes** the 2026-09-01 critique of this scene (the narration has been re-rendered since).

## Inputs resolved

| Input | Resolved to | State |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `0a3d011c5f27` | resolved — matches the current working copy |
| HARD BANS | `narrate/base.md` | resolved |
| Voice spec | `voice/soma_new_pipeline.md` | resolved (declared in `config/party.yaml`) |
| Examples | `examples/soma.md` | resolved |
| Global examples | none (`shared_examples:` absent) | ok |
| Party doc | `docs/party.md` | 4/4 PCs |
| `voice_lint` | 0 errors, 0 warnings | **but its bookkeeping/convergence checks silently do not run on per-scene input** (no `## Name — Scene` headings). Re-run on an assembled proxy: still 0 errors. |

**Doc-level budgets are not evaluable from a single scene.** See `voice_critique_summary.md` for the ledger.

## Prose measure

693 prose words / 883 total — **78.5% prose**, the highest ratio in the chapter.

## Flags

### [1] Epigrammatic closers ×2

- l. 21 *"It is quaint. This is rarely good."*
- l. 61 *"Some places mistake that for a plan."* — **keep this one**; it closes her tactical survey and earns its position.

She has 2 more in scene 08; budget is 1 across the session. Target 1–2 total.

### [2] Quote typography is mixed *within this scene*

6 curly `“ ”` and 10 straight `"` characters. Every other scene is internally consistent. Normalize at assembly.

## Notes, not flags

- l. 49 *"How long have we been walking?"* reads as player-to-GM table speech. Scenes 01–03 have **no `.scrubbed.md`** — `/scrub` never ran on them. Worth a scrub pass before assembly.

## Verdict

The strongest scene in the chapter. The defensive read of Phandalin — no wall, no river, no garrison, armed residents — is doing real work and is entirely in Soma's physical-world-first lens. One closer to trim.

---
*Review only. Nothing here has been applied. Full ledger, cross-scene convergence and the GM scope calls are in `voice_critique_summary.md`.*

