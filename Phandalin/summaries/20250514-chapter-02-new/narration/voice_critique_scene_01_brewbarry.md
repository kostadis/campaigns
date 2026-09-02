# Voice Critique — Brewbarry, scene 01: The Band Comes Together

**Run:** 2026-09-02 · **Input shape:** per-scene · **Supersedes** the 2026-09-01 critique of this scene (the narration has been re-rendered since).

## Inputs resolved

| Input | Resolved to | State |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | ⚠ **STALE** — this is `HEAD`, the 61-line rulebook. It has no epigrammatic-closer ration, no `I file` ban, no extra-tic patterns and no `yaml voice_lint` block. Scene 01 was never checked against the rules now in force. |
| HARD BANS | `narrate/base.md` | resolved |
| Voice spec | `voice/brewbarry_new_pipeline.md` | resolved (declared in `config/party.yaml`) |
| Examples | `examples/brewbarry.md` | resolved |
| Global examples | none (`shared_examples:` absent) | ok |
| Party doc | `docs/party.md` | 4/4 PCs |
| `voice_lint` | 0 errors, 0 warnings | **but its bookkeeping/convergence checks silently do not run on per-scene input** (no `## Name — Scene` headings). Re-run on an assembled proxy: still 0 errors. |

**Doc-level budgets are not evaluable from a single scene.** See `voice_critique_summary.md` for the ledger.

## Prose measure

624 prose words / 835 total — **74.7% prose**, the highest in the chapter.

## Flags

**None.** Zero epigrammatic closers, zero taxonomy moves, zero portable tics, zero connective em-dashes. Short declaratives throughout, matching `examples/brewbarry.md`. The tribe/drums/piano contrast (ll. 33–43) and the survey card at l. 73 are exactly the concrete, bodily register the spec asks for.

## Cleared candidates

- **Orphan quote run 93–98** (3 lines) — cleared. Framed by *"Soma wants percussion under the music."* (91) and closed by *"She notices things."* (99); the reader can follow it.

## Verdict

Clean. Re-render only because the rulebook it was rendered against is two versions behind the rest of the chapter — not because of anything in the prose.

---
*Review only. Nothing here has been applied. Full ledger, cross-scene convergence and the GM scope calls are in `voice_critique_summary.md`.*

