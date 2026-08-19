# Voice Critique — Valphine Sotorra, scene 04: The Skull Cavity

**Narration:** `session_doc_scene_04_the_skull_cavity.md`
**Input shape:** per-scene (directory run; scrubbed variant preferred where it exists)

## Inputs resolved

| Input | Resolved to | How |
|---|---|---|
| Genre rulebook | `Phandalin/voice/_genre.md` @ `6e67c59f94b4` | run record (`.knobs.json`, post-#276); 61 lines, ~7.5K chars |
| Rulebook vs run record | **match** — current file digest equals render-time digest (verified with the pipeline's own `sha256(text.strip())[:12]`) | sha comparison |
| HARD BANS | `~/src/CampaignGenerator/config/agents/session_doc/narrate/base.md` | 4.1K |
| Voice spec | `voice/valphine_new_pipeline.md` | rule (c): unique key `valphine_new_pipeline` for first name `valphine` |
| Per-char examples | `examples/valphine.md` | stem equals first name; single file, no concatenation |
| Global examples | none | all four example files route per-character |
| Party doc | `docs/party.md` | roster **3/4** PCs carry `Player:` lines — Brewbarry's block lacks one (campaigns#144 silent-partial hazard) |
| voice_lint | ran on `session_doc_scene_04_the_skull_cavity.md` | 0 errors, 0 warnings, 1 note: bookkeeping checks **skipped** — rulebook has no ` ```yaml voice_lint ` block (campaign declares no filing register) |

## Budget ledger

Scope: single scene — doc-level budgets NOT evaluable here; see `voice_critique_summary.md` for the directory-wide ledger.

## Flags

No flags.

## Notes

- **Dialogue anachronism, GM scope call:** "door that's gonna, like, open up Scooby-Doo style" (line 25) sits inside a verbatim quote. The scrub pass declared scene 4 clean and never surfaced it — noting it now for a ruling. Removal would be an authorial rewrite of player speech; the campaign licenses absurdist table comedy, and the 1.4/10.1 precedents lean keep.
- Scan A2: ten quote-final dashes, all inherited from the smoothed layer. Spot-checks against the raw tape show cue-splits and genuine cut-ins (line 67's is a real interruption — the dwarves' "Oh, no, no, no" arrives over Vukradin). Line 23's reattributes the front half of a Vukradin cue to Valphine as mockery — the raw layer shows one continuous Vukradin block; the fiction's mock-quote device covers it, but it is a tape divergence worth knowing about.
- The reclassified hatch below is the largest in the directory (16 spans). Two of them ("I rolled very poorly on my insight check…", "…this is just the normal way of these surface dwellers. Strange, but fine. Overbrighters.") were folded into narration at line 109 — a correct use of the hatch.

## Reclassified table speech

- `"one. I can't wait for the little one. I just gotta know what this opens up to. So — do you go now or later?"`
- `"Might ask the bard to go sing himself off a cliff at some point. Is that gonna happen?"`
- `"The bard is always the most annoying character, right, Nick?"`
- `"Yeah. The annoying bard, exactly."`
- `"It's almost like a stereotype. Does Norbert come back to see his treasure? What's his name? I keep forgetting — Norbus. Norbus, sorry. I don't know why I have Norbert."`
- `"I like that the drow is there, making it a very awkward situation."`
- `"I rolled very poorly on my insight check for them — you can roll on yours. I think this is just the normal way of these surface dwellers. Strange, but fine. Overbrighters."`
- `"Daylords. All right, let me see — what should I roll? Insight? I guess I'd be inclined to think they actually were going to — so, Valphine, are you gonna—"`
- `"try to intimidate them to not split it 50/50? No, my insight was a seven as well. So they take—"`
- `"We get eight, they get seven? No — they get eight, you get seven. It would be nice. We need to get two gems and then—"`
- `"At some point in this campaign, I'm going to be so poor and have so few nice items that I'm gonna be three levels below where I'm supposed to be. It'll be awesome."`
- `"A reason I'm broke. Have you figured that out yet?"`
- `" He's a starving artist. There's a reason. He's incredibly naive. It's not that my music is bad."`
- `"And I am so taking you on as my late-stage son."`
- `"You thought the bard was bad. Okay — check out the underpowered bard. Even better."`

Each span is the model ruling a quote to be out-of-fiction table talk. `assemble.py` strips the comment — this report is the last review point.

## Verdict

No flags. Valphine's read of the gem-splitting negotiation — the undercount as liturgy, the whetstone as etiquette, the closing audit of Vukradin's maneuver — is the best sustained sequence in the document. Review the 16-span hatch before assembly; it is the model making sixteen scope calls in one scene.
