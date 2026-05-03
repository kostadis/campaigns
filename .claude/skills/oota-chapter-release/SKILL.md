---
name: oota-chapter-release
description: Release a played OOTA chapter — re-split the bible, rebuild the abyss palace, bump MEMPALACE_HORIZON.md, tag the campaign state as `oota-chapter-N`, push branch + tag, and open a PR against main. Invoke when the user says "we are done with chapter N" / "release chapter N" / "tag chapter N" for the Out-of-the-Abyss campaign. The flow is intentionally treated as a release, not a casual commit, because the tag becomes the long-lived "checkpoint" for that chapter.
---

# OOTA Chapter Release

This skill is the codified version of the chapter-bump workflow for
the Out-of-the-Abyss campaign. It treats each played chapter as a
*release*: a tagged, reviewable point in history that can be
checked out years later.

## When to invoke

Trigger phrases:
- "we are done with chapter N"
- "we finished chapter N"
- "release chapter N"
- "tag chapter N"
- "/oota-chapter-release N"

The argument is the **campaign chapter number** (e.g. `50`). This is
the session number, not the bible-file number — they differ because
of the chapter-18 decimal cluster (see `MEMPALACE_HORIZON.md` for the
encounter-order math).

Operate from `/home/kroussos/campaigns/out-of-the-abyss/`. Refuse if
the working directory is anywhere else, or if the current branch
already has uncommitted changes outside `docs/chapters/`,
`docs/distill_extractions/`, `docs/npcs/`, the root grounding docs,
and `MEMPALACE_HORIZON.md` (those are the expected dirty files; bail
if anything else is dirty so we don't sweep unrelated work into the
release commit).

## Inputs to confirm with the user before acting

Use `AskUserQuestion` (one at a time) for anything ambiguous:

1. **Chapter number** if not given.
2. **Chapter title** — derive from the bible heading
   (`grep -E "^# Chapter N " docs/TheUnderdark.md`); if not present,
   ask the user for a working title and warn that the bible has not
   been updated.
3. **Whether to run `split_chapters.py`** — only needed if the bible
   contains chapter N (`grep -E "^# Chapter N\b" docs/TheUnderdark.md`
   returns a hit) AND the corresponding chapter file is missing or
   stale. Skip the split if the bible doesn't have chapter N yet, but
   record this in the horizon doc as "bible not yet updated".

## Steps

Use `TaskCreate` to track these as a checklist. Execute in order.

### 1. Pre-flight checks

```bash
pwd  # must be /home/kroussos/campaigns/out-of-the-abyss
git rev-parse --abbrev-ref HEAD  # remember current branch
grep -cE "^# Chapter" docs/TheUnderdark.md  # current bible heading count
ls docs/chapters/*.md | wc -l  # current chapter file count
/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace abyss status
```

Capture the *before* drawer counts — they go into the commit message
and PR body as `was → now` deltas.

### 2. Branch off main

```bash
git checkout main
git pull --ff-only origin main  # only if user asks; otherwise skip
git checkout -b oota-chapter-N-release  # N substituted
```

If the branch already exists, ask whether to reuse or pick a new
name.

### 3. Re-split the bible (conditional)

Only run if step 1 found chapter N in the bible AND the existing
`docs/chapters/` numbering is stale.

```bash
python ~/src/CampaignGenerator/split_chapters.py docs/TheUnderdark.md --output-dir docs/chapters
```

After split:

- Check `docs/chapters/mempalace.yaml` is still present. If the
  splitter wiped it, restore from git:
  `git show HEAD:out-of-the-abyss/docs/chapters/mempalace.yaml > docs/chapters/mempalace.yaml`
- Compare old tracked file list (`git ls-files docs/chapters/`) to
  the new on-disk list. If filenames have shifted (encounter-order
  renumbering), `git rm` the old set and `git add` the new set —
  git's rename detection handles this if you stage both halves
  before diffing. **Do not** try to manually rename; let the splitter
  produce the canonical set.
- The splitter often drops the `chapter_01_arrival.md` prologue
  (content before the first `# Chapter` heading). That is expected
  and intentional — preserve the deletion.

### 4. Decide: incremental re-mine vs full rebuild

**Full rebuild** (mandatory) if step 3 ran and any chapter file path
changed — orphan drawers from the old narrative-wing source paths
will pollute search otherwise.

**Incremental re-mine** is fine when only `docs/distill_extractions/`
and `docs/npcs/` changed (no rename in `docs/chapters/`).

For full rebuild:

```bash
mv ~/.mempalace/palaces/abyss ~/.mempalace/palaces/abyss.bak.$(date +%Y%m%d-%H%M%S)
```

Record the backup path; it goes into `MEMPALACE_HORIZON.md` under
"Backups currently on disk".

### 5. Re-mine in order

Always: chronicle → narrative → abyss (subdirs before root).

```bash
mp="/home/kroussos/worldanvil_pipeline/venv/bin/mempalace --palace abyss"
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
$mp search "Zuggtmoy wedding" --wing abyss
```

Top result must be an NPC dossier (`yestabrod.md` historically), not
`TheUnderdark.md`. If `TheUnderdark.md` shows up, **stop**: the
ignore file has regressed. Do not commit until it's fixed.

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
clean release.

Commit with a message that captures `was → now` deltas for drawer
counts and any path renames. Include a `Co-Authored-By: Claude` line.

### 9. Tag the release **before pushing the branch**

```bash
git tag -a oota-chapter-N -m "OOTA release: end of chapter N — *Chapter Title*

Bible chapter file: chapter_FF_<slug>.md
Last session date: YYYY-MM-DD
Palace drawer total: NNNN (chronicle/narrative/abyss = X/Y/Z)"
```

Use **annotated tags** (`-a`), not lightweight — they carry the
release metadata and survive `git filter-branch`/squash-merge cleanup
better.

### 10. Push branch and tag

```bash
git push -u origin oota-chapter-N-release
git push origin oota-chapter-N
```

Push the tag explicitly — `git push` alone does not push tags. The
tag points to the branch tip, so it survives even if the PR is
squash-merged and the branch is deleted: `git checkout oota-chapter-N`
will always reproduce the campaign state at that point.

### 11. Open PR against main

```bash
gh pr create --base main --head oota-chapter-N-release \
  --title "OOTA: release chapter N — Chapter Title" \
  --body "..."
```

PR body should include:
- Summary (re-split? full rebuild? what changed)
- Drawer count delta table (`was → now`)
- File-change summary (chapter renames, sidecar additions, etc.)
- Test plan: `mp status` totals, `mp search "Zuggtmoy wedding"`
  sanity check.
- Tag link: "Tagged as `oota-chapter-N`."

### 12. Stop. Ask before merge.

Report the PR URL and the tag name. Then **wait** for the user's
explicit approval before merging. The skill ends here; do not
auto-merge.

## Failure modes & rollbacks

- **Splitter wipes `chapters/mempalace.yaml`** — restore from git
  before re-mining, or the wing's room config is lost.
- **Sanity check returns `TheUnderdark.md`** — `.mempalaceignore`
  regressed. Inspect, fix, redo step 5–6 before continuing. Do not
  tag a polluted palace.
- **Wrong chapter number on the tag** — tags can be moved with
  `git tag -d oota-chapter-N && git push origin :refs/tags/oota-chapter-N`
  followed by re-tagging, but only do this **before** anyone else
  has fetched the tag. Confirm with the user first.
- **Branch already exists** — ask the user whether to reuse, pick a
  new name (e.g. `oota-chapter-N-release-v2`), or abort.

## Why this is a "release" and not a commit

Three reasons the user called this out:

1. **The palace state is a derived artifact** that's expensive to
   rebuild. Each release captures a known-good palace snapshot
   (via the `abyss.bak.YYYYMMDD-HHMMSS` directory), not just text
   diffs.
2. **The chapter renumbering is destructive** — the splitter renames
   every file in `docs/chapters/`. Without a tag, "go back to how
   the campaign looked at chapter N" is genuinely hard.
3. **The horizon doc is the coordination contract** between the
   human and Claude across sessions. Bumping it is a deliberate
   handshake, not a casual edit.

So: tag, push the tag, open the PR, and wait. Treat each chapter
like a software release.
