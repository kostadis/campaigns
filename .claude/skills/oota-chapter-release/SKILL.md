---
name: oota-chapter-release
description: Release a played OOTA chapter — re-split the bible, rebuild the abyss palace, bump MEMPALACE_HORIZON.md, tag the campaign state as `oota-chapter-N`, push branch + tag, and open a PR against main. Invoke when the user says "we are done with chapter N" / "release chapter N" / "tag chapter N" for the Out-of-the-Abyss campaign. The flow is intentionally treated as a release, not a casual commit, because the tag becomes the long-lived "checkpoint" for that chapter.
---

# OOTA Chapter Release

This skill is the codified version of the chapter-bump workflow for
the Out-of-the-Abyss campaign. It treats each played chapter as a
*release*: a tagged, reviewable point in history that can be
checked out years later.

> **Revised 2026-07-27 after the chapter 59 release.** That run hit
> five separate problems this document had wrong or silent about: a
> hardcoded path pointing at a stale clone, a dead binary path, a
> chapter-number rule that produces off-by-one tags, a mining step
> that silently drops two wings, and a sanity check too narrow to
> catch the actual pollution. Each is now a numbered step or caveat.
> See "Lessons from chapter 59" at the end for the full account.

## When to invoke

Trigger phrases:
- "we are done with chapter N"
- "we finished chapter N"
- "release chapter N"
- "tag chapter N"
- "/oota-chapter-release N"

The argument is the **campaign chapter number** (e.g. `50`), not the
bible-file number. Deriving one from the other is error-prone — see
step 1b, and do not skip it.

## Inputs to confirm with the user before acting

Use `AskUserQuestion` for anything ambiguous:

1. **Chapter number** — always confirm, even when you think you have
   it. A wrong tag is expensive to fix once fetched. Present the
   corroborating evidence from step 1b so the confirmation is cheap.
2. **Chapter title** — from the bible heading (step 1b). If absent,
   ask for a working title and warn the bible has not been updated.
3. **Whether to run `split_chapters.py`** — see step 3; usually not
   needed.
4. **What to do with dirty pipeline output** — see step 2b.

## Steps

Use `TaskCreate` to track these as a checklist. Execute in order.

### 1a. Locate the campaign tree — do not assume

**There are two clones of `kostadis/campaigns.git` on this machine.**
As of 2026-07-27:

| Path | State |
|---|---|
| `/home/kroussos/out-of-the-abyss/out-of-the-abyss` | current; used for the chapter 59 release |
| `/home/kroussos/campaigns/out-of-the-abyss` | 27 commits behind `origin/main`, 209 dirty files, missing the newest chapter file |

They are separate clones, **not** symlinks — `stat` reports different
inodes. Earlier versions of this skill hardcoded the second path,
which would cut a release from a tree lacking the chapter being
released. The palace at `~/.mempalace/palaces/abyss/` is a single
shared store, so mining from the stale clone silently overwrites good
drawers with old content.

Verify before anything else:

```bash
git rev-parse --show-toplevel
git rev-list --left-right --count HEAD...origin/main   # want 0 behind
ls docs/chapters/ | tail -3                            # newest chapter present?
```

If the session's working directory disagrees with the user's
expectation, **ask** — do not pick one.

### 1b. Derive the chapter number — the offset is not constant

The campaign number and the bible-file number differ, and **the gap
between them changes**. Do not subtract a fixed offset.

- `+4` through campaign chapter 54 (the `# Chapter 18.05`–`18.4`
  sub-chapter cluster)
- `+3` from campaign chapter 56 onward — the source skips
  `# Chapter 55` entirely

**Rule: read the campaign number off the `# Chapter N` heading inside
the chapter file, never off the filename.** Corroborate across three
sources, which should agree:

```bash
head -1 docs/chapters/<newest>.md                       # internal heading
grep -nE '^# Chapter [0-9]+ ' docs/TheUnderdark.md | tail -3
head -1 summaries/<newest-date>/session-summary.md
```

For chapter 59 all three read `# Chapter 59 The Key is Secured` while
the file was `chapter_62_the_key_is_secured.md`. Tagging from the
filename would have produced `oota-chapter-62`; the documented `+4`
offset would have produced `58`. Both wrong.

### 1c. Capture before-state

```bash
mp="/home/kroussos/.venvs/main/bin/mempalace --palace abyss"
$mp status
```

Note the binary path. **`/home/kroussos/worldanvil_pipeline/venv/bin/mempalace`
no longer exists** — the venv is gone though the directory remains,
so the failure is a bare "No such file or directory".

Record per-wing drawer counts; they become `was → now` deltas in the
commit message and PR body.

> **Counting caveat.** `wc -l`, `grep -c` and `ls | wc -l` returned
> mutually contradictory numbers during the chapter 59 run (a 1 MB
> file reported 0 lines; a heading count came back 62 then 63 with
> the file provably unchanged). Shell output decoration is not
> reliable here. **Use Python for any count a decision depends on**,
> and never conclude "the split is stale" from a shell count alone —
> compare heading slugs to filename slugs directly.

### 2. Branch off main

```bash
git checkout main
git pull --ff-only origin main
git checkout -b oota-chapter-N-release
```

If local `main` is stale and the tree is dirty, `git checkout main`
fails rather than clobbering. Fast-forward the ref without checking
it out: `git fetch origin main:main`.

If the branch exists, ask whether to reuse or rename.

### 2b. Decide what to do with dirty pipeline output

The workspace normally has dozens of dirty files from grounding runs.
Two questions, both for the user:

1. **Is the pipeline still running?** Check twice ~20s apart plus
   `find docs -newermt '-10 minutes'`. Never mine a moving target.
2. **Should the tag reproduce the palace?** If yes, the pipeline
   output that will be mined must be committed *first*, in its own
   commit before the release commit. Otherwise the palace holds files
   absent from git and `git checkout oota-chapter-N` will not
   reproduce it.

This trades against the "stage only the release files" rule in step 8.
Both are defensible; make the user choose rather than deciding
silently.

### 3. Re-split the bible (conditional — usually skip)

Only if the bible contains chapter N **and** `docs/chapters/` is
genuinely stale. Verify staleness properly (Python, per step 1c):

```python
# heading count == file count, and slugs align in order => split is CURRENT
```

Beware false positives: a naive slugifier will mismatch on apostrophes
(`Ent'moch`), accents (`Faerûn`) and genuinely untitled sub-chapters.
Three "mismatches" in the chapter 59 run were all slugifier artifacts;
the split was current and no re-split was needed.

```bash
python ~/src/CampaignGenerator/split_chapters.py docs/TheUnderdark.md --output-dir docs/chapters
```

After split:

- Restore `docs/chapters/mempalace.yaml` if the splitter wiped it:
  `git show HEAD:out-of-the-abyss/docs/chapters/mempalace.yaml > docs/chapters/mempalace.yaml`
- If filenames shifted, `git rm` the old set and `git add` the new;
  let rename detection handle it. Do not rename by hand.
- The dropped `chapter_01_arrival.md` prologue is expected.

### 4. Audit what the root mine will actually ingest — MANDATORY

**This step did not exist before chapter 59 and is the one that would
have prevented the whole mess.** `.mempalaceignore` does *not* inherit
from `.gitignore`, so anything newly added to the repo — or merely
present on disk — is mined until explicitly excluded.

Simulate the ignore rules and list what would be mined, grouped by
extension, before spending a rebuild:

```python
# walk the campaign root, apply .mempalaceignore (dir rules + fnmatch globs),
# print Counter(suffix) and the non-.md files by size
```

Expect **only `.md`**. Anything else is a finding. The chapter 59 audit
surfaced 137 non-prose files / 7.3 MB that had been mined for months:
four D&D Beyond PDFs, a 305 KB entity-triage state blob, `aliases.json`,
`connections.json`, `entity_registry.yaml`, and the whole
`scratch/exp-*/` experiment tree (git-ignored, but mempalace was never
told).

Also check for **multiple overlapping sources of the same entity**.
Three NPC sets were being mined into one wing — `docs/npcs/`,
`docs/v2/npcs/` and `docs/ensemble/merged_dossiers/` — so one entity
could have three competing dossiers and the stalest could win a query.
If you find more than one source for a category, stop and ask which is
the source of record.

### 5. Decide: incremental re-mine vs full rebuild

**Mining only ever ADDS drawers.** Any change that must *remove*
content requires a full rebuild:

- a source of record changed (e.g. `docs/npcs/` → `merged_dossiers/`)
- `.mempalaceignore` gained a rule
- chapter files were renamed by a re-split

Incremental is fine only when content was purely *added* under
already-mined paths.

For a full rebuild, move the palace aside — this doubles as the backup:

```bash
mv ~/.mempalace/palaces/abyss ~/.mempalace/palaces/abyss.bak.$(date +%Y%m%d-%H%M%S)
```

Record the path for `MEMPALACE_HORIZON.md`.

### 6. Re-mine — all FIVE wings

```bash
mp="/home/kroussos/.venvs/main/bin/mempalace --palace abyss"
$mp mine docs/distill_extractions   # chronicle
$mp mine docs/chapters              # narrative
$mp mine .                          # abyss (root)
$mp mine notes                      # notes
$mp mine summaries                  # summaries
```

**`notes/` and `summaries/` are in the root `.mempalaceignore`, and
that does not mean they are unwanted.** It stops the *root* mine from
double-mining them. They are configured wings with their own
`mempalace.yaml` and `.mempalaceignore`, and they populate only when
mined by explicit path. A three-wing rebuild drops them silently —
no error, no warning, ~5,700 drawers gone from search. This nearly
happened in the chapter 59 run and was caught only by diffing the
status output against the previous one.

Subdir wings go before root wherever the root ignore does not already
exclude them; `notes/`+`summaries/` are excluded there, so their
position after root is safe.

**Run mining in the background.** The root mine has exceeded 10
minutes and will blow a foreground tool timeout. Write output straight
to a log file — **do not pipe through `tail`**, which buffers
everything until exit and makes progress invisible.

### 7. Sanity checks — broader than "is the bible in there?"

Mandatory before tagging. The old check only looked for
`TheUnderdark.md`, which passed cleanly while the palace was badly
polluted by other means. Check the *shape* of the result, not one
filename:

```bash
$mp search "Zuggtmoy wedding" --wing abyss
$mp search "who murdered Janussi" --wing abyss   # or current-chapter canon
```

**Pass:** top result is a prose entity dossier (`.md`) from the
current source of record.
**Fail:** top result is `TheUnderdark.md` (ignore regressed), *or* any
`.json`/`.yaml`/data file (non-prose content is being mined), *or* a
dossier from a superseded source.

In the chapter 59 run the first rebuild returned `aliases.json` at
rank 1 — a bare alias map outranking every NPC dossier. Do not tag a
palace that fails this. Fix `.mempalaceignore`, rebuild, re-check.

When a check fails, **enumerate the whole corpus (step 4) rather than
excluding the single file the search happened to return.** Fixing
file-by-file cost a full rebuild cycle before the general problem
— "non-prose data is in the palace" — was identified.

### 8. Update `MEMPALACE_HORIZON.md`

**Current horizon** block:
- `Last campaign chapter played: N — *Chapter Title*` plus a short
  beat list (pull from the session summary, don't invent)
- `Last bible chapter file:` — the new chapter file
- `Last session date:` — from `summaries/YYYYMMDD/session-summary.md`
- `Palace last fully (re)built:` — today if a full rebuild ran,
  otherwise the prior date, and say which and why

Refresh the **drawer counts** table with post-mine numbers for all
five wings. If a full rebuild ran, append the backup path under
"Backups currently on disk" with a note on what makes it worth
keeping.

Record any **accepted coverage gaps** — entities that stopped being
searchable because a source was retired. Chapter 59 lost
`brother_vareth`, `asha_vandry` and `blind_monk` when `docs/v2/npcs/`
was dropped. Future sessions need to know that was a decision, not a
bug.

### 9. Stage, commit

```bash
git add docs/chapters/ MEMPALACE_HORIZON.md .mempalaceignore
```

Do **not** `git add -A`. Include `.mempalaceignore` whenever mining
rules changed — the palace is reproducible only if the rules that
built it are committed alongside.

If step 2b decided pipeline output should be committed, that is a
**separate, earlier** commit — keep the release commit clean.

### 10. Tag the release **before pushing the branch**

```bash
git tag -a oota-chapter-N -m "OOTA release: end of chapter N — Chapter Title

Bible chapter file: chapter_FF_<slug>.md
Last session date: YYYY-MM-DD
Palace drawer total: NNNN (chronicle/narrative/abyss/notes/summaries = V/W/X/Y/Z)"
```

Annotated (`-a`), never lightweight.

### 11. Push branch and tag

```bash
git push -u origin oota-chapter-N-release
git push origin oota-chapter-N
```

Push the tag explicitly — `git push` alone does not push tags.

### 12. Open PR against main

Body should include: summary (re-split? rebuild? why), drawer delta
table (`was → now`, all five wings), file-change summary, any
`.mempalaceignore` rule changes with rationale, accepted coverage
gaps, test plan (`status` totals + both sanity queries), and
"Tagged as `oota-chapter-N`."

### 13. Stop. Ask before merge.

Report the PR URL and tag name, then **wait** for explicit approval.
Do not auto-merge.

## Failure modes & rollbacks

- **Sanity check returns a `.json`/`.yaml` file** — non-prose content
  is mined. Audit the full corpus (step 4), add format exclusions,
  full rebuild. Do not tag.
- **Sanity check returns `TheUnderdark.md`** — `.mempalaceignore`
  regressed on the bible rule.
- **Drawer count jumps by tens of thousands** — something large and
  unexcluded got mined. Compare per-room deltas; the room that
  exploded names the culprit. Chapter 59: `abyss/general` went
  136 → 13,577 from `docs/ensemble/` (2,085 files, 29 MB).
- **Drawer count drops unexpectedly** — a wing was not mined. Check
  all five paths were passed explicitly.
- **Wrong chapter number on the tag** —
  `git tag -d oota-chapter-N && git push origin :refs/tags/oota-chapter-N`,
  then re-tag. Only before anyone else has fetched. Confirm first.
- **Splitter wipes `chapters/mempalace.yaml`** — restore from git
  before re-mining.
- **Branch already exists** — ask: reuse, rename, or abort.
- **`git checkout main` refuses** — local `main` is stale and the tree
  is dirty. `git fetch origin main:main` updates the ref without a
  checkout.

## Lessons from chapter 59 (2026-07-27)

Recorded because each cost real time and would otherwise recur.

1. **A hardcoded path outlived its truth.** The skill named a clone
   that had drifted 27 commits behind and no longer contained the
   chapter. Paths in skills need verifying, not trusting.
2. **A fixed offset was documented for a variable gap.** The bible
   skipped `# Chapter 55`, moving the offset from +4 to +3. Any rule
   of the form "subtract K" will eventually produce a wrong tag.
3. **The ignore file is not the gitignore.** `scratch/` was
   git-ignored for months and mined the whole time.
4. **An exclusion list is a whitelist in disguise.** Every directory
   added to the repo is mined by default. `docs/ensemble/` arrived via
   a PR merged hours earlier and tripled the palace. Audit the corpus,
   don't audit the diff.
5. **A narrow sanity check passes while the thing it protects is
   broken.** "Is `TheUnderdark.md` in the results?" was green
   throughout. Check the shape of a good answer instead.
6. **Fixing the reported symptom is slower than enumerating.** Two
   rebuild cycles were spent excluding files one at a time before the
   general rule ("prose only") was written.
7. **Exclusion means eviction, and eviction means rebuild.** Mining
   only adds. This is why a rules change is never a re-mine.
8. **Silence is the dangerous failure.** Dropping two wings produced
   no error at all. Diff `status` against the previous release every
   time.

## Why this is a "release" and not a commit

1. **The palace is a derived artifact** that is expensive to rebuild —
   the chapter 59 rebuild ran well over 20 minutes. Each release
   captures a known-good snapshot via `abyss.bak.YYYYMMDD-HHMMSS`.
2. **Chapter renumbering is destructive** — the splitter renames every
   file in `docs/chapters/`. Without a tag, "go back to how the
   campaign looked at chapter N" is genuinely hard.
3. **The horizon doc is the coordination contract** between the human
   and Claude across sessions. Bumping it is a deliberate handshake.
4. **The mining rules are part of the artifact.** A tag that captures
   content but not the `.mempalaceignore` that shaped the palace does
   not reproduce the palace.

So: tag, push the tag, open the PR, and wait. Treat each chapter like
a software release.
