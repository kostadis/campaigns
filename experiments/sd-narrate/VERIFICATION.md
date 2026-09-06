# Consolidation verification — 2026-09-06

This records migration checks, **not new narration or dialogue quality evaluations**. No live model calls were made during consolidation.

## Preserved evidence

- 317 file copies, 5,675,734 bytes, match their source bytes under SHA-256. This includes all six original proposed/tested prompt files plus v2/rationale, every raw narration/dialogue response, original submitted messages, reviews, logs, metadata, and the existing experiment scripts/tests. The ledger distinguishes archival copies, maintained prompt copies, frozen inputs, and supplementary inputs.
- All 337 recorded input-hash comparisons are represented: 327 match; ten reference unavailable older versions of the same Phandalin `run_experiment.py`. Those ten entries are explicitly labeled in the ledger, not counted as verified historical inputs.
- The ten exceptions involve three prior hashes of that runner only. No recorded campaign-source, voice, draft, or prompt-file hash is missing or mismatched. All nine A/B/C input ledgers match completely.
- Historical failed/prepared attempts remain failed/prepared in their original metadata. None has been relabeled as a successful render.
- Original model outputs, metadata, and reader HTML were not rewritten. New portable readers are separate derived files.

## Executed checks

```bash
python -B tooling/archive_paths.py
python -B tooling/verify_readers.py
python -B -m pytest -q -p no:cacheprovider tooling/tests
```

- **17 helper tests pass**, covering the original runner checks plus relocation/fixture resolution, immutable archive checks, original prompt reconstruction, and replay safety/failure reporting.
- All **nine A/B/C preparations** reproduce their original saved system prompt, user prompt, and normalized baseline **byte-for-byte**. Tests mock the model boundary and assert neither client creation nor API calls occur during preparation.
- Portable CLI smoke checks prepared the nine dialogue trials and the Obelisk scene 3 narration replay in new external `/tmp` directories. No `--render` was used.
- The A/B/C reader rebuilt successfully from the relocated metadata and frozen inputs, without reading original campaign paths.
- **16 portable HTML readers**, **119 local file links**, and **four inline JavaScript blocks** checked successfully. Node's syntax checker was used; this was not a browser visual/interactivity test. The historical readers retain historical links; use `readers/` for portable copies.
- Common credential/private-key patterns were scanned before staging; no matches were found. This is a precautionary pattern scan, not an exhaustive security audit.

## What remains external

The runnable helpers need Python and the installed CampaignGenerator public `campaignlib` package. Tests additionally need pytest; JavaScript syntax checking needs Node. Live reruns require an explicitly configured backend and `--render` authorization. The fixture archive does not contain credentials or a vendored application checkout.

Replaying stored messages reproduces the input text, not the old full loader implementation or deterministic model output. The archived campaign-dependent runners and READMEs remain historical evidence; use the maintained `tooling/` entry points and root README.
