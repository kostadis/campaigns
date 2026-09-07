# Remove-recap manifest — 2026-09-01 session

Applied: 2026-09-06  
Session directory: `summaries/20260902`  
Previous session checked: `summaries/20260825`

## Ruling

The GM approved removing the complete opening scene, **Pre-Session Banter and
Recap**, from both pipeline documents:

- `session-summary.md`, the enhanced session summary;
- `gm-assist.md`, configured as `paths.session_recap` for downstream narration.

The approved boundary is immediately before **Rumors and Preparations at the
Common Chord**. In the corrected VTT, the GM says “when we last left our Noble
Adventures” at line 787; current-session bookkeeping about the pending Lord
Neverember dinner begins at line 863. Live in-fiction play begins at line 1331
with the party at the Common Chord.

The `## Summary` prose in both pipeline documents already began with the
current session's Common Chord events, so neither prose section required a
trim. `zoom_summary.md` is an upstream vendor artifact and was not edited.

## Detection evidence

The campaign's native extraction format is incompatible with `find_recap.py`,
as recorded in `notes/scrub_register_policy.md`. Scene extraction had not yet
run, so the verified first-scene bullets were placed in a temporary surrogate
solely for deterministic detection and rescue analysis.

- Surrogate detector score: **2/6 — recap possible**.
- Markers fired: `recap` in the heading and an 86% GM share.
- Additional signal: eight past-tense markers and zero live-play markers.
- Transcript evidence outside the detector's regex: “Here's the summary of
  events according to Brewbarry” and “when we last left our Noble
  Adventures.”

The first scene contained pre-session discussion of *The 26 Words That Created
the Internet*, the previous chapter's events, and preparation to undertake the
already-established crate stakeout. The following scene contains the
current-session bookkeeping and was preserved.

## Rescue analysis

`recap_unique.py` compared the proposed recap against 74,957 words from
`summaries/20260825`.

- GM asides or editorial annotations: **none**.
- Level, subclass, spell, rest, or similar current-session bookkeeping:
  **none detected**.
- Poorly covered bullets: only the out-of-character Section 230/book discussion
  and comparison of American and European approaches to internet regulation.

Those poorly covered bullets are unrelated pre-session conversation, not
campaign canon or gaps in the previous chapter. They were dropped rather than
rescued.

The campaign-bearing recap material was already present upstream, including:

- the nine-crate mystery and planned stakeout;
- Brewbarry's kitchen confrontation with Lim;
- Petra's disclosed cover act and likeness arrangement;
- Brewbarry's cowbell role.

The recap's simplified 500-gold wording was not rescued. The previously ruled
state remains authoritative: the 500 gp likeness payment is pending the
performance two days later.

Current-chapter information beginning in the following scene was preserved in
place: the unscheduled Lord Neverember dinner, rumor of his Drow advisor,
Valphine's view of House Margaster as competition, Brewbarry's secured business
capital and import problem, and preparations for the stakeout.

## Rebuild and renumbering

The `scene_extractions` directory was empty, and no
`scene_extractions_smoothed`, `plan.md`, or narration artifacts existed for
this session. Therefore:

- no derived scene file was deleted;
- no scenes were renumbered;
- no plan rebuild was required;
- no narration was regenerated;
- the corrected and raw VTT files were not edited.

## Standing policy

The campaign-wide recap policy now records the GM's standing default: when the
previous chapter resolved, remove its opening retelling and drop preceding
scheduling or unrelated modern-topic chatter with it. Preserve current-chapter
bookkeeping and the existing combat-resume exception.
