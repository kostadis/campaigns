# Voice Critique — Vukradin, scene 02: The Gray Begins at the Wall

**Run:** 2026-09-02 · **Input shape:** per-scene · **Supersedes** the 2026-09-01 critique of this scene (the narration has been re-rendered since).

## Inputs resolved

| Input | Resolved to | State |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `5f211a965c9f` | ⚠ **UNRECONSTRUCTABLE** — an uncommitted intermediate between `HEAD` and the current working copy. Whether the closer ration reached this render cannot be determined. |
| HARD BANS | `narrate/base.md` | resolved |
| Voice spec | `voice/vukradin_new_pipeline.md` | resolved (declared in `config/party.yaml`) |
| Examples | `examples/vukradin.md` | resolved |
| Global examples | none (`shared_examples:` absent) | ok |
| Party doc | `docs/party.md` | 4/4 PCs |
| `voice_lint` | 0 errors, 0 warnings | **but its bookkeeping/convergence checks silently do not run on per-scene input** (no `## Name — Scene` headings). Re-run on an assembled proxy: still 0 errors. |

**Doc-level budgets are not evaluable from a single scene.** See `voice_critique_summary.md` for the ledger.

## Prose measure

683 prose words / 1381 total — **49.5% prose**.

## Flags

### [1] Epigrammatic closers ×4 — contributes to the doc-wide Vukradin breach

- l. 35 *"...neither can be eaten unless a merchant accepts moral conviction in place of payment."*
- l. 95 *"Everyone benefits except the dead people whose possessions are sitting in a monster's chest."* — **keep this one**; it is the chapter's moral spine and it is his voice
- l. 131 *"It is an extraordinary legal theory. Property remains property inside Neverwinter, ceases to belong to anyone beyond the masonry, and becomes property again once carried back through the gate by an approved contractor."*
- l. 143 *"It is also a retirement fund wearing the hat of an orphaned-property office."*

Budget is 1 per narrator per session, and he has 2 more in scene 05. Target 2 total. Trim 35 and 143; 131 can stay if 95 goes, but not both.

### [2] Cross-narrator convergence with Valphine (scene 04) — see summary flag [4]

> l. 143: “It is also a retirement fund wearing the hat of an orphaned-property office.”

pairs with Valphine 04:31 *"Delight in a proprietor is merely appetite wearing clean clothes."* Same *institution wearing garment of respectability* frame, two narrators, a scene and a half apart. **Keep this one, cut hers.**

### [3] Unattributed dialogue — 6 runs, 2 real

- **65–74** (5 lines, ≥4 speakers) — real. *"And after we clear a monster, then what do we do?" / "Do you bring their scalps? Seems vile." / "Do we take them to Lord Neverember?" / "No, no, no." / "Like a cat delivering a dead mouse."* Nothing identifies any speaker.
- **145–150** — l. 149 *"The city guards. You've signed up to be trafficking in stolen goods."* is genuinely ambiguous between Vukradin and Soma; l. 151 is tagged Soma, which argues 149 is not.
- **13–20** — cleared, deliberate chorus on the name *Phandalin*.
- 97–104, 119–126, 137–142 — cleared, framed two-handers (Vukradin/guard) with alternation intact.

**Leave the explicit non-attributions alone:** *"Someone behind me admits,"* (25) and *"someone says,"* (165) correctly mark lines the smoothed layer cannot assign.

## Verdict

The guard argument is the best-constructed sequence in the chapter and the *"the gray begins at the wall"* payoff lands. Two orphan runs and a four-closer surplus; both spot-editable.

---
*Review only. Nothing here has been applied. Full ledger, cross-scene convergence and the GM scope calls are in `voice_critique_summary.md`.*

