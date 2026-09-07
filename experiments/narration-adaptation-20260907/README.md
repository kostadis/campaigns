# Narration adaptation findings — September 7, 2026

**Evidence archive only. These drafts are not campaign canon or selected chapter
revisions. No narration implementation or campaign configuration changes are
included.**

Tracking issue: [CampaignGenerator #408](https://github.com/kostadis/CampaignGenerator/issues/408).
Implementation is deferred for the user to consider. The archive PR records
evidence and should not automatically close that issue.

## Start here

- [Findings and the user's decision](FINDINGS.md).
- [Pipeline-history and design audit](docs/design/NarrationPipelineAudit.md).
- [Whole-chapter adaptation](experiments/20260907-phandalin-adaptation/response.md)
  and its [comparison with the historical chapter](experiments/20260907-phandalin-adaptation/comparison.html).
- [Single-scene A/B reader](experiments/20260907-phandalin-scene-composition/comparison.html),
  [preferred B draft](experiments/20260907-phandalin-scene-composition/version-B.md),
  and [evaluation with user feedback](experiments/20260907-phandalin-scene-composition/review.md).

HTML readers are self-contained files to open locally; GitHub displays their
source rather than serving them as pages. The Markdown drafts are directly
readable on GitHub.

## Result in brief

The user preferred **B**, the general adaptation brief from the first September 7
experiment, over added scene-specific composition direction. The user described
their prose as straightforward and simple and the characters as creatures of
action. Habitual “I thought X, then corrected myself” narration was specifically
unwelcome. B is a starting point, not a finished implementation or proof that
the existing production path is satisfactory.

The factual record can live in provenance-linked VTT, summary, correction, and
extraction layers. The narrative should preserve consequential facts and
recognizable dialogue while allowing invented inner life and readable adaptation.
It need not reproduce every transcript fragment or every clarification.

## Contents and provenance

The original experiments ran in `/home/kostadis/CG-find-bug`. Their directories
are copied under `experiments/` with all frozen prompts, inputs, runners, manifests,
run records, and raw outputs intact. The audit is copied under `docs/design/`;
its three repository-local code/design links were changed to pinned GitHub links
so they remain useful from this campaign archive.

- Source campaign commit: `bbf4e3c064b4e13b47ed523606a62936638a0cc6`.
- CampaignGenerator experiment checkout: `d9c5de87a0ec4831c1cdc999b26491851b1f7c01`.
- Campaign PR base at archive creation: `148282c0` (`origin/main`). The audit and
  generation results describe their pinned snapshots, not a fresh audit of this base.
- Actual model/effort: `gpt-6-astra` / `medium`, recorded separately for all three
  calls. No rerolls or post-generation prose edits were made.
- File-level source and response hashes are recorded in each experiment. They
  preserve provenance; they do not certify factual or literary quality.

The first experiment changed several prompt/reference choices and used the
historical chapter only for comparison. The second held the user input and
settings constant and changed one instruction block, with one sample per arm.
That block combined planning with a specific literary interpretation. Neither
experiment establishes statistical reliability or a generally optimal pipeline.

## Verify without model calls

From this directory:

```sh
python3 -B verify_archive.py
```

The verifier checks frozen inputs and run/output hashes, actual model selection,
the shared A/B message and single-block difference, neutral copies and assignment,
the original blind notes, and local HTML links. It imports no generation code,
uses no network, and does not rewrite artifacts. A saved
[publication verification report](verification.json) records the initial check.

**Do not execute the archived `run.py` files to replay from this location.** They
are preserved evidence, including original local paths and original directory
assumptions. The preceding experiment's failed reader and separate presentation
helper are retained too. For another trial, use a new experiment directory and
explicit generator/source paths; do not edit these frozen records or invoke any
generation as part of reviewing this archive.

No files outside this Phandalin archive are part of the campaign PR. Existing
VTTs, reviewed summaries/extractions, voice/genre files, final chapters, grounding
documents, indexes, and the CampaignGenerator implementation remain untouched.
