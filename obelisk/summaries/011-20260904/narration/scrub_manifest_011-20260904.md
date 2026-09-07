# Scrub manifest — 011-20260904 (Chapter 11)

Run date: 2026-09-06. Target: all seven `session_doc_scene_*.md` files in
`summaries/011-20260904/narration/`.

The deterministic scanner returned **1 candidate across 7 scenes**. The Phase
1b reading pass found no additional unresolved residue after applying the
campaign's standing register policy and checking modern phrasing against the
smoothed extractions.

## GM-authored divergences

This span deliberately differs from the tape and generated narration. A future
fidelity check must not restore the measured tactical distance.

| Scene | Line | Tape / narration as generated | Scrubbed | Class |
|---|---:|---|---|---|
| 01 | 41 | `advances south about ten feet` | `advances south a few paces` | tactical distance (`foot_count`) |

## New canon (`provenance: on_the_fly`)

- None. No proper nouns, items, proverbs, institutions, aliases, or scholarly
  glosses were invented during this run.

## GM rulings on what is NOT residue

- No new campaign-level register rulings were made. The standing ren-faire
  policy remains in force: modern idiom from the table stays, while
  narrator-invented anachronism remains reviewable.
- The narration's `a hundred billion questions` was checked against the source.
  It renders the GM's taped description of Veyra rather than inventing a new
  narrator register, so the standing policy covers it and it remains unchanged.
- Exact treasure and reward amounts remain in-world facts, not combat or table
  mechanics. Scene 06's chest inventory and scene 07's promised reward remain
  unchanged.

## Notes

- Scene 01 produced the run's only `.scrubbed.md`; its one approved replacement
  was re-scanned successfully and reviewed with its neighbouring sentences.
- Scenes 02–07 were fully reviewed and correctly produced no `.scrubbed.md`.
  Assembly falls back to each raw scene file.
- `--party-md` loaded **0 player names**. The scanner expects literal
  `Player: X` lines, while `docs/party.md` uses Markdown field formatting. The
  reading pass covered the player-name class and found no real player names in
  narration prose.
- No scanner false positives were persisted to `ignore`; pre-existing ignores
  and durable rules are unchanged.
