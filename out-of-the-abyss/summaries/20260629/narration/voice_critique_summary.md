# Voice Critique — Summary: `gm-assist-doc.md` (OOTA, session 20260629)

**Target:** `summaries/20260629/gm-assist-doc.md` — the assembled concatenation of the six per-scene `.scrubbed.md` files in `narration/`.
**Inputs loaded:** `voice/{thorin,grygum,zalthir}_voice.md` + `examples/{thorin,grygum,zalthir}.md` (all read in full).
**Review-only:** no narration file was modified. Any fixes go in the per-scene `.scrubbed.md` files so `assemble.py` picks them up — never the raw `.md`.

## Scene → narrator map

| Scene | Narrator | Section | Per-scene report |
|---|---|---|---|
| 01 | Thorin | The Murder Mystery Sidebar | `voice_critique_scene_01_thorin.md` |
| 02 | Grygum | The Academic's Dilemma | `voice_critique_scene_02_grygum.md` |
| 03 | Zalthir | Confrontation in Bookwyrm's Office | `voice_critique_scene_03_zalthir.md` |
| 04 | Zalthir | The Opening of Alkrist's Safe | `voice_critique_scene_04_zalthir.md` |
| 05 | Grygum | Waiting in Deneir's Sanctum | `voice_critique_scene_05_grygum.md` |
| 06 | Thorin | Ambush of the Helmed Horrors | `voice_critique_scene_06_thorin.md` |

## Headline

**The document is strongly in-voice.** The hardest signature beats land correctly and verbatim-grounded: Thorin's giants/position line (06), Grygum's Stroud-chess comfort story and "I have done it for a mushroom" (02), Zalthir's Glabbagool-discipline marking (03). Per-sentence generic prose is sparse. No flags were manufactured to pad the pass.

**The one recurring, actionable problem is signature-line repetition across scenes** — the same load-bearing lines fired twice, which spends singular voice moves and, in one case, breaks a voice-spec rule. This is a *de-duplication* pass, not a per-sentence rewrite pass.

### Strongest recurring theme — cross-scene signature repetition (ranked)

1. **[STRONGEST — voice-spec violation] Zalthir's monk aphorism, reused near-verbatim in scenes 03 and 04.** Both open "The Garden Shadow had a saying — or possibly Brother Quellin did … the most dangerous person in a room isn't the one with the blade drawn. It's the one who has already decided they've won." (`gm-assist-doc.md:218` and `:308`). The spec is explicit: *"IMPORTANT: Use a different monk name every time this surfaces… The uncertainty about which monk taught what is the point"* (`zalthir_voice.md:64`), and the line is the spec's own canonical example (`:62`). Firing it twice unchanged converts the device into a catchphrase. **Fix:** scene 03 keeps it (it introduces the Bookwyrm read); scene 04 cuts or re-keys it.
2. **Grygum's Bahamut closer, reused as scene-ender in scenes 02 and 05.** "Bahamut may or may not have been reading over my shoulder. I wrote it down either way." (`:184`) vs. "Bahamut may or may not have been watching. I took notes either way." (`:398`). His single most load-bearing line, spent to close both his scenes. **Fix:** keep it on one scene (05's phrasing is cleaner); end the other on a different Grygum beat.
3. **[structural] Zalthir scenes 03 & 04 render the same event (safe-opening) from the same POV twice** — the potion-of-flying grift and Glabbagool's "I like the flying skill / that was a good skill" reaction both appear twice (`:276` ≈ `:324`). In-voice both times; the issue is duplication, not register. **Fix:** a structural call about whether both Zalthir POVs of one beat should ship.

## Mechanical scans

- **Scan A — em-dashes: 151 across 114 lines.** Per your decision, this is treated as **one systemic note**, not enumerated per instance: the paratactic, dash-heavy rhythm reads as intentional house style shared across all four narrators, not a per-scene defect. It is *not* flagged in the per-scene reports. If you ever want the dash density brought down, that is a deliberate campaign-wide global pass (every scene, every narrator) — not something to do piecemeal here.
- **Scan B — register-wrong vocabulary: 2 hits, both cleared as in-voice false positives.**
  - `filed` (Grygum) — `gm-assist-doc.md:76` ("filed that quietly under the column marked *irony*") and `:152` ("Humiliation, filed correctly"). Grygum's established note-taker/ledger idiom. Cleared.
  - `geometry` (Thorin) — `gm-assist-doc.md:440` ("spend them when the geometry wants it"). Thorin's own tactical vocabulary; the spec uses the exact word for him (`thorin_voice.md:36, 78`). Cleared.
  - Reported as "scan fired, judgment cleared" so the scans are visibly run.

## Per-scene disposition

| Scene | Narrator | State | The one thing to touch |
|---|---|---|---|
| 01 | Thorin | Near-clean | Optional spot-edit: "truth-magic still humming in the air" (`:8`) → stone-weight frame |
| 02 | Grygum | Excellent | Cross-scene Bahamut closer (`:184`) — see theme #2 |
| 03 | Zalthir | Strong | **Keep** the monk aphorism (`:218`); mild tell "regal, in control" (`:192`) optional |
| 04 | Zalthir | Repetition-heavy | **Cut/re-key** the monk aphorism (`:308`); resolve flying-skill duplication (`:324`) |
| 05 | Grygum | Strong | Warm-down the healing lyric (`:382`); Bahamut closer (`:398`) — see theme #2 |
| 06 | Thorin | Strongest / clean | Nothing — Scan-B `geometry` cleared; signature line landed correctly |

## Bottom line

Ship-quality voice throughout. If you only make one change, make it the **Zalthir aphorism** (scene 04) — it is the single spec-rule violation in the document. The **Grygum Bahamut closer** de-duplication is the second. Everything else is optional polish. All suggestions are grounded in the loaded spec/examples; nothing here has been applied to the narration.
