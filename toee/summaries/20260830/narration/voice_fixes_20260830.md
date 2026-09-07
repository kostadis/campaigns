# Voice fixes — session 20260830, Chapter 34

Applied 2026-09-05 from the `/voice-critic` triage (all three findings ruled **ACT**).

## ⚠ These fixes are NOT durable

They live only in `session_doc_scene_02_garbage_room_and_fire_temple.scrubbed.md`.
**`/scrub` regenerates `.scrubbed.md` from the raw `.md`, so the next scrub run on scene 02
silently wipes all three.** They are not in `notes/.scrub_state.json` and nothing else
remembers them. **This file is the replay record** — re-apply from the table below after any
future scrub of scene 02.

The raw `session_doc_scene_02_garbage_room_and_fire_temple.md` is deliberately unchanged, so
the two files now disagree. `assemble.py` prefers `.scrubbed.md`, so assembly is correct today.

## The three spans

| ID | Line | Before | After |
|---|---:|---|---|
| F1 | 187 | `“I hit—”` | `“I hit…”` |
| F2 | 159 | `“Really? Yeah.”` | `“Really?” I said. “Yeah.”` |
| F3 | 47 | `Apparently our control of the Temple did not yet include dropping the sky on a garbage heap.` | `We did not have the sky. We had a garbage heap.` |

**F1** removes a false interruption assertion. The tape (cue 533) reads `I hit…`; nobody spoke
over Sequoia. The em-dash was introduced by `/voice-smooth`, which converted trail-off ellipses
into em-dashes wholesale (raw layer: 30 `…"` / 0 `—"`; smoothed: 5 / 20).

**F2** attributes a line the extraction assigns to Sequoia — the scene's own first-person
narrator — which was printed untagged inside a Varek/Zephyr alternation and read as Varek's.
No word inside either quote was changed.

**F3** replaces a Zephyr-shaped wry aside with Sequoia's flat register, per `_genre.md`
("the minimum viable words needed to describe an unpleasant fact").

## Second-pass verification

| Check | Before | After | Note |
|---|---|---|---|
| `voice_lint` | 0 err / 0 warn / 6 skipped | 0 err / 0 warn / 6 skipped, exit 0 | unchanged, as expected |
| Trailing `—”` reaching narration | 7 | **6** | F1 landed; the remaining 6 are legitimate interruptions |
| Banned constructions (4 shells) | 0 | 0 | no regression |
| Collisions introduced | — | none | `“ I said` now appears twice, but in scenes 02 and 04 under different narrators; `garbage heap` and `the sky` are reused only within the line they replaced |

**Scan C's run count did not move (11 → 11), and that is a limitation of the scan, not a failed
fix.** Its heuristic counts any line starting `“` and ending `”` as an unattributed quote line —
and `“Really?” I said. “Yeah.”` satisfies both while being fully attributed. The scan
**over-counts attributed split quotes**. Read the run rather than the number.
