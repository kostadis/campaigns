# Stage 2 scene extractions — provenance

Generated 2026-09-03. Promoted from `/tmp/scene_extractions_v2` after an A/B run.

## Command

```bash
/home/kroussos/.venvs/main/bin/scene_extract \
  <session>/session_20250812.partialmap.vtt \
  --summary <session>/session-summary.md \
  --output-dir <session>/scene_extractions \
  --backend codex-cli --model gpt-5.6-sol --codex-reasoning-effort medium \
  --max-tokens 32000 --batch-scenes --batch-max-tokens 32000
```

One batched call, 6 scenes, transcript sent 1x instead of 6x.

## Why `--party` / `--party-config` / `--players-config` are ABSENT

Stéphane was absent this session and **Gary voiced both Valphine and Brewbarry**
(established acoustically — see `speaker_attribution.md`). The deterministic
speaker rewriter cannot express that: `speaker_map()` builds a `dict[str, str]`
and maps each display name to **the first** of that player's `plays` that the
roster has. So `plays: [Valphine Sotorra, Brewbarry]` resolves to Valphine and
stops.

Verified directly — the stock config and a session-local override with Gary
bound to both produce a **byte-identical** map:

```
Gary Young -> Valphine Sotorra          (both configs)
Stéphane Bourdeaud -> Brewbarry         (Stéphane speaks 0 lines in this VTT)
```

Running with `--party` would therefore rewrite all 236 of Gary's lines to
"Valphine Sotorra", silently destroying every Brewbarry attribution — including
his rage, his halberd, and his harpy kill — *before the model sees anything*.
`players.session.yaml` in this directory does NOT fix this; it is kept only as
the record of the identity finding.

## What was done instead

`session_20250812.partialmap.vtt` — the display-name VTT with only the three
UNAMBIGUOUS speakers rewritten by hand, `Gary Young:` left intact:

```
GM: 662   Vukradin: 594   Soma: 510   Gary Young: 236   UNKNOWN: 115
```

Deterministic where it is correct; honestly ambiguous where it is not.

## Result

| | v1 (no map at all) | v2 (this, partial map) |
|---|---|---|
| GM | `Kostadis Roussos` x171 | `GM` x150 |
| Vukradin | `David Mendenhall` x156 | `Vukradin` x131 |
| Soma | `Wade Brown` x123 | `Soma` x117 |
| Gary's PCs | `Gary Young` x64 | `Gary Young` x58 |
| UNKNOWN | 32 | 34 |
| quotes verified | 1164/1164 | **947/947, 0 refused** |

398 of 456 labels (87%) are correct characters.

## OPEN — the review queue

The 58 `**Gary Young**` blocks need a per-block ruling: Brewbarry or Valphine.
The extractor's italic context notes already resolve many (`*asking how Brewbarry
can reach the harpies*`). Of the 58: **8 name Brewbarry, 7 name Valphine, 43 name
neither** — but most of the 43 are decidable by class feature (thrown hand axes
and rage are Brewbarry; crossbow and mace are Valphine), the same discriminator
used throughout the Stage 0/1 adjudications.

Do NOT bulk-assign. Do NOT run a global replace toward either PC — that is the
`gary_brewbarry_label_collapse` failure this whole arrangement exists to avoid.

## KNOWN, UNEXAMINED

v2 extracted 69,001 bytes vs v1's 82,613 — **16% less content** from the same
transcript and identical batch settings. Both runs verify 100%, so nothing was
invented; the difference is how much the model chose to quote. A scene-by-scene
diff of what v2 omitted was offered and **not run** before promotion. If a later
pass finds a beat missing, `/tmp/scene_extractions` (v1) is the comparison set —
until /tmp is cleared.
