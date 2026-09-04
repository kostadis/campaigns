# narration_dgx — Chapter 10 narrated on the DGX Spark

**This is a recorded experiment, not shippable narration. Do not assemble from
this directory.** The shipping narration is `../narration/` (codex-cli,
`gpt-5.6-sol`, medium effort).

Run 2026-09-04, immediately after the `/remove-recap` + `/no-mech` pass, against
the *same* inputs as the committed run so the only variable is the backend.

```
sd_narrate session_2026_08_21_chapter_10_….md \
  --plan plan.md \
  --scene-extractions scene_extractions_smoothed \
  --per-scene-output narration_dgx \
  --party docs/party.md --party-config config/party.yaml \
  --players-config config/players.yaml \
  --voice-dir voice --examples examples \
  --prose-mode --reflections --narrate-tokens 3200 \
  --backend dgx --endpoint http://192.168.1.147:8001 \
  --model deepseek-ai/DeepSeek-V4-Flash-0731
```

Exit 0, seven scenes.

## The defects are deliberately left in

Fixing them would destroy the comparison. They are the finding.

### 1. The reclassification step does not happen (the important one)

Zero `<!-- table-speech reclassified: … -->` hatches in all seven scenes, against
four on the codex-cli run. That is **not** a clean result — it is the step not
running. On scene 03 alone, codex-cli reclassified 16 GM table-lines; DeepSeek
instead emitted them as quoted dialogue:

| File | Line | What it actually is |
|---|---|---|
| scene 02 | `"Okay, no."` | Zenvon-the-player realising his mistake |
| scene 02 | `"Yes, that's right."` | player confirming a spelling |
| scene 03 | `"Okay, so we'll rest. Alright. Toblen…"` | player announcing a long rest |
| scene 03 | `"Alright. So… next morning, you wake up."` | GM transitioning the session |

This is exactly the failure `/no-mech` exists to prevent, reappearing at the
**narration** layer via a different backend. It is not an input problem: those
lines are legitimately present in the smoothed extractions because they sit
inside roleplay scenes, and codex-cli handled them correctly.

### 2. Proper-noun drift

`Conybury` ×4 in scene 05, where every other scene in this run — and every scene
of the codex-cli run — has the canonical `Conyberry`.

### 3. Seam defect

Scene 04 opens with a verbatim duplicate of scene 03's closing sentence
(*"Morning arrived the way mornings do…"*). The codex-cli run had two seam
defects of the same class; both were fixed there, neither is fixed here.

## Comparison

| | codex-cli (gpt-5.6-sol) | DGX Spark (DeepSeek-V4-Flash-0731) |
|---|---|---|
| Scenes / exit | 7 / 0 | 7 / 0 |
| Reclassification hatches | 4 scenes | 0 — step not happening |
| Table speech as dialogue | 0 | 4 lines |
| Pattern-matched residue | 1 (`quest log`) | 0 |
| Seam defects | 2 (fixed) | 1 (left in) |
| Proper-noun errors | 0 | `Conybury` ×4 |
| Output volume | 49.2 KB | 42.9 KB |

The volume gap concentrates in **scene 01**, the bullets-only scene: 4.6 KB vs
1.9 KB. With no quotes to work from, the local model had markedly less to say —
the case where the hosted model's headroom showed most.

Scene 07 is the local run's best work and stands comparison with the committed
version on prose quality alone.

## What the run bought on the wiring

The `--backend dgx` seam works end to end. Voice files, party and player configs,
plan section indices, per-scene output naming, and `--narrate-tokens` were all
honoured, and the emitted files are structurally identical to the codex-cli ones.
No seam damage, no shape differences.

All the friction was configuration, and both items are real bugs:

- **`config/session_doc.yaml:44` has the wrong model id** — it names
  `deepseek-ai/DeepSeek-V4-Flash-DSpark`, but the vLLM server at
  `192.168.1.147:8001` advertises `deepseek-ai/DeepSeek-V4-Flash-0731`. The
  `dgx` profile fails outright as written; this run passed the served id
  explicitly on the command line.
- **Every backend block in that file says `backend: anthropic`**, the `dgx` one
  included. Either the field is vestigial or the profile loader is not setting
  it.
