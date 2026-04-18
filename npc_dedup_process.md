# NPC Deduplication — Process Dump

## Goal
Collapse a directory of ~138 NPC dossiers (`/home/kroussos/campaigns/toee/docs/npcs/`) where many NPCs appeared 2–6 times under filename variants (transcription typos, alias-as-filename, role-as-filename) into a single canonical file per NPC. Final count: 100.

## Discovery Method
1. `ls` the npcs directory — group filenames by suspected same-NPC clusters using:
   - **Spelling drift:** `harch` / `hartsch`, `albrith` / `albreth`, `lareth` / `larith`, `palsmarie` / `pasmarie`, `glannon` / `glennon`, `osler` / `ostler`, `goodingoat` / `goodingoot` / `gundigoot`
   - **Alias-as-filename:** `the_duke.md` vs `thorne.md`, `tharok_stevan_tharok_stonevein.md` vs `tharok.md`
   - **Role-as-filename:** `headgnome_glennddarc.md` (role + name) vs proper name file
   - **Compound filenames:** `brother_eldin_brother_eldrin.md` (the LLM literally concatenated two candidate spellings)
   - **Garbage filenames:** `i_don_t_see_any_session_summary_notes_in_your_message...md` (LLM error response saved as a filename)
2. **Always Read both files before deciding.** Filename similarity ≠ same NPC. Confirmed NOT-duplicates: `dren` ≠ `dren_halveth` (Crimson Guard vs Broken Blades), `dala` ≠ `dalia`, `krell` ≠ `lieutenant_krell`, `mari_clee` ≠ `pasmarie_clee`, `rannos` / `ranos_davl` / `ranus_duval`.

## Decision Framework (per pair/cluster)
For each cluster, classify:
- **Strict subset → simple delete.** One file's content is fully contained in another. No merge needed.
- **Overlapping with unique content on each side → merge.** Pick canonical filename, fold in unique facts from the other(s), then delete sources.
- **Different NPCs that happen to share a name fragment → keep both.**

When in doubt: **prompt the user one-by-one** via `AskUserQuestion` (loaded via ToolSearch). User authority required for:
- Whether two NPCs are the same person
- Which filename is canonical
- Resolving contradictory facts between the two files

## Canonical Filename Rules (user-confirmed preferences)
- **Use book-canon spelling** when it exists (`ostler_gundigoot.md`, not the phonetic `goodingoat`).
- **Prefer short slug for well-known characters** (`thorne.md` over `thorne_duke.md` / `the_duke.md`).
- **Prefer proper name over role-prefixed** (`alremm.md` over `the_prophet.md`).
- **Prefer the spelling the user states is correct** when they correct one ("larith was a typo").

## Merge Content Rules
The standard NPC dossier has these sections — merge per section:
1. **Identity** — keep the most specific role; concatenate alias forms in parens (e.g., `Brother Eldin (also Eldrin / Eldren)`).
2. **Personality & Motivations** — union of bullets; deduplicate semantically.
3. **History with the Party** — chronological merge by date; if two files describe the *same* event with different detail, write a single richer bullet.
4. **Current Status** — take the most recent state; if files contradict, the later-dated one wins (or ask the user).
5. **Relationships** — union; if both files describe the same relationship, prefer the more specific phrasing.
6. **Arc Score Events** — union; preserve every recorded event.

Preserve unique facts even when small ("Honey Tavern Inn" was a typo for "Honey Haven Inn" → keep one canonical name but note the alias if it appears in transcripts).

## Interactive Pattern (when prompting user one-by-one)
- Use `AskUserQuestion` (deferred tool — load via `ToolSearch` first with `query: "select:AskUserQuestion"`).
- **Validation gotcha:** every question must have ≥2 options. Always include a "different NPCs — keep both" escape hatch even when you're sure they're the same.
- Batch related questions in a single `AskUserQuestion` call when possible (it accepts multiple questions).
- For each pair: state the suspected match, summarize the unique content on each side, propose a canonical filename, ask user to confirm or override.

## Pitfalls Encountered
- **Don't trust filename similarity.** The user corrected me on `dren` / `dren_halveth` — looked like spelling drift, was actually two different NPCs in different factions.
- **Long parallel `Write` batches can be interrupted.** Doing 14 Writes in one message risks the user interrupting partway. Either do them serially or in smaller batches.
- **Garbage filenames are real.** An LLM error response had been saved as a filename — verify by Read before treating as a "duplicate"; in this case it was an empty/error file and got deleted outright.
- **Compound filenames signal prior unresolved ambiguity** (`brother_eldin_brother_eldrin.md`) — someone earlier punted the merge decision; resolve it now.

## Execution Order
1. Read both/all files in a cluster (parallel Reads OK — no dependency).
2. Decide: delete, merge, or keep both.
3. For merges: `Write` the canonical file with merged content.
4. After all merges in a batch are written, **bulk-delete sources in a single `rm -v` command** — easier to audit than per-file deletes.
5. Run `ls | wc -l` to confirm the final count.

## Specific Merges Performed (this run)
| Canonical | Sources merged | Notes |
|---|---|---|
| `hartsch.md` | harch.md, harch_hartsch.md | Spelling drift |
| `ostler_gundigoot.md` | 6 ostler/osler variants | Book-canon spelling chosen; created NEW canonical file |
| `alremm.md` | alrrem.md | User confirmed = head of Fire Temple / "the prophet" |
| `thorne.md` | thorne_duke.md, thorne_the_duke.md, the_duke.md | Title-as-filename collapse |
| `lareth_the_beautiful.md` | lareth.md, larith_the_beautiful.md | User: "larith was a typo"; preserved frame-up insignia detail |
| `albreth.md` | albrith.md, albrith_albreth.md | Same NPC, same fight |
| `belsornig.md` | canon_belsoring.md, canon_belsornig.md | Chimera + brigands + Snej supplier all same NPC |
| `tharok.md` | tharok_stevan_tharok_stonevein.md | Full-name variant collapsed |
| `brother_eldin.md` | brother_eldin_brother_eldrin.md, brother_eldren.md | Eldin/Eldrin/Eldren noted as aliases |
| `captain_tolub.md` | captain_tolubb.md | Folded in Jorin Pike Kale ship-schedule detail |
| `hestort_flintshine.md` | hestort_flintshine_tort.md | Folded in Terjon-claim detail |
| `thalsor_of_the_stone.md` | thalsor.md | Folded in Romag correspondence detail |
| `glennon_clee.md` | glannon.md | "Honey Tavern" was typo for "Honey Haven" |
| `pasmarie_clee.md` | palsmarie_clee.md | Folded in Honey Tavern scene + Gnonsbim contradiction |

## Simple Deletions (strict subsets, no merge needed)
`aunt_emma_green_hag.md`, `joradin.md`, `mistress_lenora_glimmerfield.md`, `master_aldous_glimmerfield.md`, `quinna_pool.md`, `spugnoir.md`, `prefect_terjon.md`, `vesrek.md`, `serena.md`, `madame_selentis.md`, `headgnome_glennddarc.md`, plus the garbage-filename file.

## Skill Authoring Notes
A future `/dedupe-npcs` skill should:
1. Take the npcs directory as input.
2. Cluster by filename similarity (Levenshtein + role-prefix stripping + alias substring).
3. For each cluster, Read all files in parallel.
4. **Surface the cluster to the user with a summary, not auto-merge** — this is a precision decision (per global rule on LLM pipeline design): same-person identification is structural, not rendering. LLM proposes, human disposes.
5. Once user confirms a cluster + canonical name, LLM can do the *merge rendering* (combining sections) — that part is rendering, safe to automate.
6. Bulk-delete sources only after all merges in the batch are written.
7. Report final count + diff.
