# `attempts/hand-edited/` — GM rewrites, not model output

**These files were written by hand. Nothing here is a model's output, and none of it
should be read as evidence of what any model produces.**

`summaries/attempts/` is a model-comparison corpus. Its other two arms are raw generation
output, keyed by the numeric session ordinals that `summaries/` itself stopped using when
`a2e989c7` re-keyed sessions by date:

| Directory | Sessions | What it is |
|---|---:|---|
| `dgx-deep-seek/` | 39 | Raw DeepSeek output, untouched |
| `haiku/` | 29 | Raw Haiku output, untouched |
| `hand-edited/` | 20 | **GM rewrites of the same sessions** |

## Why this directory exists separately

The rewrites started life as in-place edits to `summaries/<N>/session-summary.md` — the
paths that became `attempts/dgx-deep-seek/<N>/` in the re-key. Landing them back at those
paths would have overwritten the raw DeepSeek output with hand-written prose, and left
nothing in the tree to say so. A later `dgx-vs-haiku` comparison would then have been
reading a human's writing as a model's, and scoring it accordingly.

That is the whole reason for the split. **Do not merge this directory back into
`dgx-deep-seek/`**, and do not treat a file here as a generation sample.

## What the edits actually are

Structural and prose passes over the generated drafts, not corrections of fact: bolded
`**Date:**` headers, `---` rules, and richer sentences — added beats the draft omitted
(a missed Ice Knife, a failed Command), sharper phrasing, restored specifics.

They are useful as a **target**: the gap between `dgx-deep-seek/<N>` and
`hand-edited/<N>` for the same session is roughly what a generation pass still leaves for
a human to do.

## Coverage

20 of the 39 sessions: 1–6, 8–10, 12, 13, 15, 23–30 (no 7, 11, 14, 16–22, 31+). The gaps
are simply sessions that never got a pass, not a judgement about them.
