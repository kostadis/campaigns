---
name: phandalin-chapter-release
description: Release a played Phandalin chapter — re-split the bible, rebuild the phandalin palace, bump MEMPALACE_HORIZON.md, tag the campaign state as `phandalin-chapter-N`, push branch + tag, and open a PR against main. Invoke when the user says "we are done with chapter N" / "release chapter N" / "tag chapter N" for the Phandalin campaign. The flow is intentionally treated as a release, not a casual commit, because the tag becomes the long-lived "checkpoint" for that chapter.
---

# Phandalin Chapter Release

This skill is the codified version of the chapter-bump workflow for
the Phandalin campaign. It treats each played chapter as a *release*:
a tagged, reviewable point in history that can be checked out years
later.

## When to invoke

Trigger phrases:
- "we are done with chapter N"
- "we finished chapter N"
- "release chapter N"
- "tag chapter N"
- "/phandalin-chapter-release N"

The argument is the **campaign chapter number** (e.g. `40`). For
Phandalin this is the play-session chapter number, which may not
match the bible-file numbering — the chapters dir currently has two
overlapping splits (75 files for 39 played chapters as of horizon
2026-05-04). Confirm with the user which numbering scheme is
canonical at release time; until the splitter is re-run cleanly,
prefer the play-session numbering (`chapter_NN_<session-title>.md`)
over the bible-split numbering
(`chapter_NN_neverwinter_expansionism_…`).

Operate from `/home/kroussos/campaigns/Phandalin/`. Refuse if the
working directory is anywhere else, or if the current branch already
has uncommitted changes outside `docs/chapters/`,
`docs/distill_extractions/`, `docs/npcs/`, the root grounding docs,
and `MEMPALACE_HORIZON.md` (those are the expected dirty files; bail
if anything else is dirty so we don't sweep unrelated work into the
release commit).

## Inputs to confirm with the user before acting

Use `AskUserQuestion` (one at a time) for anything ambiguous:

1. **Chapter number** if not given.
2. **Chapter title** — derive from the bible heading
   (`grep -E "^# Chapter N " docs/NeverwinterExpansionismandtheNorth.md`);
   if not present, ask the user for a working title and warn that the
   bible has not been updated.
3. **Whether to run `split_chapters.py`** — only needed if the bible
   contains chapter N (`grep -E "^# Chapter N\b" docs/NeverwinterExpansionismandtheNorth.md`
   returns a hit) AND the corresponding chapter file is missing or
   stale. Skip the split if the bible doesn't have chapter N yet, but
   record this in the horizon doc as "bible not yet updated".
4. **Whether to also clean up the dual-numbering pollution.** If the
   user wants this release to also collapse the two overlapping
   splits in `docs/chapters/` into one canonical convention, that's a
   bigger operation than a normal release — do it as a separate
   discussion, not silently inside the release flow.

## Steps

Use `TaskCreate` to track these as a checklist. Execute in order.

### 1. Pre-flight checks

```bash
pwd  # must be /home/kroussos/campaigns/Phandalin
git rev-parse --abbrev-ref HEAD  # remember current branch
grep -cE "^# Chapter" docs/NeverwinterExpansionismandtheNorth.md  # current bible heading count
ls docs/chapters/*.md | wc -l  # current chapter file count
/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace phandalin status
```

Capture the *before* drawer counts — they go into the commit message
and PR body as `was → now` deltas.

### 2. Branch off main

```bash
git checkout main
git pull --ff-only origin main  # only if user asks; otherwise skip
git checkout -b phandalin-chapter-N-release  # N substituted
```

If the branch already exists, ask whether to reuse or pick a new
name.

### 3. Re-split the bible (conditional)

Only run if step 1 found chapter N in the bible AND the existing
`docs/chapters/` numbering is stale.

```bash
python ~/src/CampaignGenerator/split_chapters.py docs/NeverwinterExpansionismandtheNorth.md --output-dir docs/chapters
```

After split:

- Check `docs/chapters/mempalace.yaml` is still present. If the
  splitter wiped it, restore from git:
  `git show HEAD:Phandalin/docs/chapters/mempalace.yaml > docs/chapters/mempalace.yaml`
- Compare old tracked file list (`git ls-files docs/chapters/`) to
  the new on-disk list. If filenames have shifted, `git rm` the old
  set and `git add` the new set — git's rename detection handles this
  if you stage both halves before diffing. **Do not** try to manually
  rename; let the splitter produce the canonical set.

### 4. Decide: incremental re-mine vs full rebuild

**Full rebuild** (mandatory) if step 3 ran and any chapter file path
changed — orphan drawers from the old narrative-wing source paths
will pollute search otherwise.

**Incremental re-mine** is fine when only `docs/distill_extractions/`
and `docs/npcs/` changed (no rename in `docs/chapters/`).

For full rebuild:

```bash
mv ~/.mempalace/palaces/phandalin ~/.mempalace/palaces/phandalin.bak.$(date +%Y%m%d-%H%M%S)
```

Record the backup path; it goes into `MEMPALACE_HORIZON.md` under
"Backups currently on disk".

### 5. Re-mine in order

Always: distill_extractions → narrative → phandalin (subdirs before root).

```bash
mp="/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace phandalin"
$mp mine docs/distill_extractions
$mp mine docs/chapters
$mp mine .
```

Capture the post-mine counts:

```bash
$mp status
```

### 6. Sanity check

Mandatory before tagging — verifies `.mempalaceignore` still excludes
the bible:

```bash
$mp search "Carver march on Icespire" --wing phandalin
```

Top result must be an NPC dossier or `planning.md`, **not**
`docs/NeverwinterExpansionismandtheNorth.md`. If the bible shows up,
**stop**: the ignore file has regressed. Do not commit until it's
fixed.

Run a second sanity check on the narrative wing to make sure the
chapters are reachable:

```bash
$mp search "Adabra intervention" --wing narrative
```

Top result should be one of the `chapter_NN_*.md` files.

### 7. Update `MEMPALACE_HORIZON.md`

Edit the **Current horizon** block:
- `Last campaign chapter played: N — *Chapter Title*`
- `Last bible chapter file:` — point at the new chapter file
  (or note "unchanged — chapter N not yet appended to the bible").
- `Last session date:` — read from the most recent
  `summaries/YYYYMMDD/session-summary.md` Date field.
- `Palace last fully (re)built:` — today's date if a full rebuild
  ran, otherwise leave the prior date.

Update the **Drawer counts at this horizon** table with the
post-mine numbers from step 5.

If a full rebuild ran, append the new backup path under "Backups
currently on disk".

### 8. Stage, commit

Stage *only* the files touched by the release:

```bash
git add docs/chapters/ MEMPALACE_HORIZON.md
```

Do **not** `git add -A`. The workspace usually has dozens of
unrelated dirty files; sweeping them in defeats the point of a
clean release. **Per the campaign-isolation rule in
`~/campaigns/CLAUDE.md`, never include changes from other campaigns
in this commit.** Run `git status` and verify only `Phandalin/`
prefixes appear before staging.

Commit with a message that captures `was → now` deltas for drawer
counts and any path renames. Include a `Co-Authored-By: Claude` line.

### 9. Tag the release **before pushing the branch**

```bash
git tag -a phandalin-chapter-N -m "Phandalin release: end of chapter N — *Chapter Title*

Bible chapter file: chapter_FF_<slug>.md
Last session date: YYYY-MM-DD
Palace drawer total: NNNN (distill_extractions/narrative/phandalin = X/Y/Z)"
```

Use **annotated tags** (`-a`), not lightweight — they carry the
release metadata and survive `git filter-branch`/squash-merge cleanup
better.

### 10. Push branch and tag

```bash
git push -u origin phandalin-chapter-N-release
git push origin phandalin-chapter-N
```

Push the tag explicitly — `git push` alone does not push tags. The
tag points to the branch tip, so it survives even if the PR is
squash-merged and the branch is deleted: `git checkout phandalin-chapter-N`
will always reproduce the campaign state at that point.

### 11. Open PR against main

```bash
gh pr create --base main --head phandalin-chapter-N-release \
  --title "Phandalin: release chapter N — Chapter Title" \
  --body "..."
```

PR body should include:
- Summary (re-split? full rebuild? what changed)
- Drawer count delta table (`was → now`)
- File-change summary (chapter renames, sidecar additions, etc.)
- Test plan: `mp status` totals, `mp search "Carver march on Icespire"`
  sanity check, `mp search "Adabra intervention" --wing narrative`.
- Tag link: "Tagged as `phandalin-chapter-N`."

### 12. Stop. Ask before merge.

Report the PR URL and the tag name. Then **wait** for the user's
explicit approval before merging. The skill ends here; do not
auto-merge.

## Failure modes & rollbacks

- **Splitter wipes `chapters/mempalace.yaml`** — restore from git
  before re-mining, or the wing's room config is lost.
- **Sanity check returns `NeverwinterExpansionismandtheNorth.md`** —
  `.mempalaceignore` regressed. Inspect, fix, redo step 5–6 before
  continuing. Do not tag a polluted palace.
- **Wrong chapter number on the tag** — tags can be moved with
  `git tag -d phandalin-chapter-N && git push origin :refs/tags/phandalin-chapter-N`
  followed by re-tagging, but only do this **before** anyone else
  has fetched the tag. Confirm with the user first.
- **Branch already exists** — ask the user whether to reuse, pick a
  new name (e.g. `phandalin-chapter-N-release-v2`), or abort.
- **Dual-numbering pollution gets worse** — if the splitter produced
  yet another numbering convention, **stop** and surface this to the
  user; do not tag a release with three overlapping splits.

## Why this is a "release" and not a commit

Three reasons:

1. **The palace state is a derived artifact** that's expensive to
   rebuild. Each release captures a known-good palace snapshot
   (via the `phandalin.bak.YYYYMMDD-HHMMSS` directory), not just text
   diffs.
2. **The chapter renumbering is destructive** — the splitter renames
   every file in `docs/chapters/`. Without a tag, "go back to how
   the campaign looked at chapter N" is genuinely hard.
3. **The horizon doc is the coordination contract** between the
   human and Claude across sessions. Bumping it is a deliberate
   handshake, not a casual edit.

So: tag, push the tag, open the PR, and wait. Treat each chapter
like a software release.
