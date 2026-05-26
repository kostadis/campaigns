# Staged Consistency Checks — Pipeline Quality Pattern

## What this document is

A methodology pattern, discovered during the Phandalin Chapter 41 narration (2026-05-17), for stopping LLM-pipeline error amplification in the session-doc pipeline. **The discovery is that the consistency check belongs at every LLM extraction boundary, not just once at the end.**

The companion skill is `staged-consistency` (`~/.claude/skills/staged-consistency/`), which walks the workflow.

---

## The problem

The CampaignGenerator pipeline is a chain of LLM extractions:

```
VTT transcript
    │
    ▼  (gmassist render — first LLM pass)
gm-assist.md
    │
    ▼  (enhance_summary.py — second LLM pass)
session-summary.md  +  enhanced_sections.md
    │
    ▼  (scene_extract.py — per-scene LLM pass; pulls verbatim quotes)
scene_extractions_new/0N_*.md
    │
    ▼  (session_doc.py — narrator LLM pass)
final narration
```

Each stage is an LLM transformation that can introduce, propagate, or amplify errors. Per the global CLAUDE.md LLM Pipeline Design Rule: **LLMs are renderers, not architects**. They are unreliable at scope, ordering, attribution, and verbatim fidelity to source material the prep specifies.

What we observed in Phandalin Ch 41:

1. The VTT transcript itself contained Otter/Zoom mishearings: prep "*the boar comes*" → captured as "*the bear comes*"; prep "*my great-uncle said dawn comes for everyone*" → captured as "*my uncle Seidan comes for everyone*"; prep "*lightning bolt sigil*" → captured as "*boar tusk sigil*"; etc.
2. `gm-assist.md` (first pass) faithfully carried those mishearings forward, plus invented a fabricated NPC affiliation (Prutha "committed to the Order of the Gauntlet") and a fabricated item ("Elemental Cleaver") from player-improv chatter.
3. `session-summary.md` (second pass) inherited every error from gm-assist and added a couple of its own (killing-blow misattribution: Prutha vs. Valphine, when the actual killer was Soma).
4. `scene_extractions_new/02_*.md` etc. (third pass) preserved verbatim quotes — including the misheard ones — and added them to the per-scene record.
5. `session_doc.py` (narration pass) pulled from the scene extractions and re-rendered every accumulated error into beautiful prose.

The fix attempted late (just running `check_consistency.py` once on the final narration) caught some structural inconsistencies but **missed every transcription error** — because the LLM doing the check has no access to the prep's authoritative line.

When we corrected the late-stage outputs (session-summary, enhanced_sections) without going back to the scene extractions, **the next narration run re-injected the errors** by pulling from the still-broken per-scene files.

---

## The fix: consistency checks at every boundary

Run `check_consistency.py` (with prep as `--context`) **at every LLM extraction boundary**, with a human review/fix cycle gating each transition:

```
VTT
 │
 ▼ gmassist render
gm-assist.md ───► [consistency check 0] ──► (human reviews, fixes gm-assist.md)
 │
 ▼ enhance_summary.py
session-summary.md ───► [consistency check 1] ──► (human reviews, fixes session-summary.md)
 │
 ▼ scene_extract.py
scene_extractions_new/0N_*.md ───► [consistency check 2 — verbatim quotes pass] ──► (human reviews, fixes per-scene quotes)
 │
 ▼ session_doc.py
final narration ───► [consistency check 3] ──► (human reviews, fixes narration)
```

**The non-obvious one is check 2 (scene extractions).** This is the stage where verbatim quotes — which the narrator reads literally — live. If you only check the summary/enhanced layers and skip the scene extractions, fixes at the summary layer get silently overwritten the next time you narrate.

---

## What the check catches at each stage

| Stage | What this check catches that the others miss |
|---|---|
| **0 — gm-assist** | NPC fabrications (e.g. fake affiliations like "Order of the Gauntlet"), invented items (e.g. "Elemental Cleaver"), scope confusion (events from outside the session inserted), wrong character attribution for actions |
| **1 — session-summary / enhanced** | Cross-section contradictions inside the document (one section credits Prutha, another credits Valphine), pronoun drift, mechanical errors (e.g. nat-20 rule misapplication) |
| **2 — scene extractions (verbatim quotes)** | Verbatim transcription errors that match the audio but conflict with prep canon (sigil description, named-character lines, signed cryptic notes). **This is the layer that re-injects errors into narration if skipped.** |
| **3 — narration** | Voice drift, banned phrases, prose-level fabrications introduced by the narrator pass |

---

## Why prep is the load-bearing context

Every other context source (party.md, world_state.md, the LLM's own structural reasoning) can catch **structural** problems but cannot catch **transcription** problems. Prep is the only source that knows what was actually intended at the table — the exact wording of cult correspondence, the canonical name of an NPC, the shape of a sigil.

**Without prep as `--context`, the consistency check is doing roughly half its job.** It will catch contradictions inside the recap but miss every misheard word from the VTT. In Phandalin Ch 41 this meant the late-stage check returned a confident "no major issues" while the document carried 11 prep-canonical contradictions in plain sight.

If a session has no prep file, the check is still worth running — it just won't catch transcription errors. The skill should note this explicitly in its final report so the user isn't misled.

---

## Fix propagation: a hazard, not a free lunch

When a fix is identified at, say, stage 1, applying it ONLY to the stage-1 artifact leaves downstream artifacts stale. Two practical options:

1. **Re-derive downstream**: fix the stage-1 artifact, then re-run the downstream stages from that point. Cleaner pipeline state, costs tokens.
2. **Apply the fix at every layer manually**: cheaper, but you have to touch every file. Easy to miss the scene extractions.

When applying manually, **always include the per-scene files in your propagation pass**. They are the layer that feeds the narrator.

When a fix touches verbatim quotes (per-scene files), preserve audit trail by adding an italic editorial note in the speaker attribution explaining the discrepancy between raw Otter/Zoom capture and prep canon. Future readers can see what was changed and why.

---

## Limits

- This pattern slows the pipeline down. The point is correctness, not speed.
- The check at each stage costs tokens. Running it on every commit is overkill; running it on a session-doc that's going to be shared with players is worth it.
- Some "errors" the check flags are intentional table flavor (player improvisations, jokes, OOC table terms like "the blacklist"). The human review step is where those are protected.
- Auto-applying the check's suggested fixes is a footgun. Always read each fix before applying — especially for verbatim quotes, where the "fix" might be removing flavor the players value.

---

## See also

- `~/.claude/skills/staged-consistency/SKILL.md` — orchestration skill
- `~/.claude/skills/gmassist-precheck/SKILL.md` — covers the stage 0 → stage 1 transition (the original experiment that inspired this generalization)
- `~/.claude/skills/consistency-check/SKILL.md` — single-file check (the primitive that all stages call)
- `~/CampaignGenerator/check_consistency.py` — the script all stages invoke
- Global CLAUDE.md "LLM Pipeline Design Rule" — the principle this pattern is an instance of
