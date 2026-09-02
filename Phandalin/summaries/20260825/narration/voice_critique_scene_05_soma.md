# Voice Critique — Soma, scene 05: Lim's Secret Supplier

**Narration:** `session_doc_scene_05_lim_s_secret_supplier.scrubbed.md`
**Input shape:** per-scene
**Doc-level budgets:** evaluated across the whole document in `voice_critique_summary.md` — a single-scene critique cannot evaluate them.

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `voice/_genre.md` @ `6e67c59f94b4` | run record + config; 61 lines |
| Rulebook vs run record | match — not edited since this render | sha comparison |
| HARD BANS | `base.md` | 4.1K |
| Voice spec | `voice/soma_new_pipeline.md` | declared `voice:` in `config/party.yaml` |
| Per-char examples | `examples/soma.md` | declared `examples:` |
| Global examples | none | no `shared_examples:` declared |
| voice_lint | ran | 0 errors, 0 warnings, 1 skipped check (no ```yaml voice_lint``` block) |

## Flags

**None.**

Zero flags is a legitimate result, and this section earns it. Nothing here is generic, nothing breaches a rule the rulebook states, and nothing converges with another narrator's register.

## What I checked and cleared

- **`the way` frame** — L9 (`the way he does it is to walk into her kitchen`) matched the grep but is not the banned move: it is a plain relative clause introducing an action, not a simile taxonomising behaviour.
- **Behavioral taxonomy** — none.
- **Tell-not-show** — none. The scene's emotional load is carried by objects and repetition, which is what her spec and the rulebook both ask for: `She stirs a pot that does not need stirring.` (L35) → `She stirs the pot. It still doesn't need stirring.` (L137). The callback does the work that naming the feeling would have ruined.
- **Third person** — L129 (`That Soma sat by the water and mended nets`) is Soma naming her own past self, deliberate and load-bearing against Lim's "I remember a different Soma." Not a POV slip.
- **Em-dashes** — every one is inside verbatim dialogue marking interruption. Zero connective dashes in prose.
- **Anachronisms in narration prose** — none. `fair trade` (L49, L59, L121) is the campaign's premise, GM-ruled during the scrub.

## Worth keeping

> *Fair trade.* Somewhere under this city there is a gang quoting Vukradin. (L59)
> Nobody has to draw it for me. The trade routes are held by cartels now; goods moving under the city are goods that pay nobody at the gate. Smugglers. (L81)
> "Yep." Shell answer, flat as a tide table. "The only constant in life is change." (L125)
> So do I. That Soma sat by the water and mended nets and let the world rot at its own pace. I don't say that. (L129)
> She stirs the pot. It still doesn't need stirring. Neither of us says the next thing. (L137)

L59 is the best single line in the document: it lands the campaign's economics conceit as a character joke, in her register, in eleven words.

## Reclassified table speech

**One hatch, one span** — a GM restatement of Brewbarry's approach to Lim, rendered in the narration at L15 as reported speech. Correct call.

## Verdict

Clean. No re-narration signal and nothing worth spot-editing.
