# Lessons from the Ch. 47 scene-extraction audit

**Date:** 2026-08-03
**Evidence base:** `summaries/20260729/scene_extractions/`, generated twice — once with
DeepSeek, once with Opus 4.8 — and audited line-by-line against the speaker-labelled VTT.
**Verifier:** `verify_quotes.py` — 5-gram coverage of every quote against all three
transcripts. ~30 lines, deterministic, no model in the loop.

> **Correction notice.** The first two versions of this document blamed the generating
> model for "fabricating quotes" and "injecting canon." That was wrong, twice. The cause
> was deterministic code. The diagnostic history is kept below because the misdiagnosis is
> itself the most transferable lesson here.

---

## 1. What actually happened

`session_doc/scene_extract.py` passed the VTT through `build_alias_normalizer` **before the
model ever saw it** (`--dossier-dir` → `input_normalizer`). That function does a whole-word,
case-insensitive, longest-first regex substitution of every registry alias → its canonical
name. So the models were faithfully transcribing an already-corrupted transcript.

| Tape | Alias rule | Model received, and dutifully quoted |
|---|---|---|
| "Spire of the **Morninglord**" | `Morninglord` → Lathander | "Spire of the **Lathander**" |
| "**Lord** Neverember" | `Lord Neverember` → Dagult Neverember | "**Dagult** Neverember" |
| "The **Lord Protector** has followed" | `Lord Protector` → Dagult Neverember | "The **Dagult Neverember** has followed" |
| "who's the **open Lord of Waterdeep**" | (mis-assigned alias) | "who's the **Dagult Neverember**" |
| "Lord **Cassian**" | `Cassian` → Lord Cassian Meliamne | "**Lord Lord** Cassian Meliamne" |
| "**Aldus** Aldus" | `Aldus` → Aldus Hern | "**Aldus Hern Aldus Hern**" |
| "a **dragon**? Yes, a **dragon**" | `dragon` → Cryovain | "a **Cryovain**? Yes, a **Cryovain**" |
| GM says "**mine.**" | `mine` → Mountain's Toe Gold Mine | "**Mountain's Toe Gold Mine.**" |

## 2. The category error

**An alias is an identity assertion, not a rewrite rule.**

The registry exists so an agent seeing *Morninglord* and *Lathander* knows they denote one
entity. That is a **read-time lookup**, many→one, non-destructive: you learn the referent
while the text still says what it said. The pipeline used it as a **write-time transform**,
which destroys the one thing a verbatim record exists to preserve — *which surface form was
actually spoken*.

The consequence that makes this worth writing down: **the correct aliases do most of the
damage.** `Morninglord → Lathander` is right. `Cassian → Lord Cassian Meliamne` is right.
Cleaning the alias data cannot fix a consumer that is asking the index the wrong question.

Proof, run after stripping the five genuinely-bad aliases: 4 of 11 corrupted tape lines were
fixed, **7 still corrupted** — all via legitimate aliases. Including one created *by the
cleanup itself*: moving `Open Lord of Waterdeep` onto Laeral Silverhand (where it factually
belongs) turned "Lady Laeral Silverhand, who's the open Lord of Waterdeep" into
"who's the **Laeral Silverhand**." Correcting the data made it corrupt correctly.

**Design rule:** pass the equivalence set to the model as *knowledge*, never as a *transform*.
The system-prompt roster already did this. Removing the rewrite lost nothing.

## 3. The misdiagnosis, and the tell that was there all along

I attributed to the model what deterministic code had done — through two full audits.

**What broke it:** regenerating with a different model. DeepSeek and Opus 4.8 produced
*identical* substitutions. Hallucinations don't replicate across model families; find-and-
replace does.

**The tell I walked past twice:** the doubling. `Lord Lord Cassian Meliamne`,
`Aldus Hern Aldus Hern`, `Dagult Dagult Neverember`, and one five-deep
`Lord, Lord, Lord, Lord, Lord Cassian Meliamne`. **No language model writes that.** It is the
signature of a substitution whose replacement text re-contains its own match. I catalogued
the doubling as a finding and never asked what mechanism could produce it.

Heuristics worth keeping:

- **Doubling ⇒ substitution, not generation.** Repeated tokens around a canonical name mean a
  find-and-replace, every time.
- **Canon-*correct* "fabrications" ⇒ suspect a lookup table.** A model that invents facts gets
  them wrong sometimes. Every one of these was right, because they came from curated data.
- **Reproducible across models ⇒ not the model.** The cheapest discriminator available, and
  it should be the *first* test when output looks systematically wrong, not the last.
- **A "fabricated" quote can be a real one inflated.** `Mountain's Toe Gold Mine` looked like
  an invented GM line. The GM said one word: "mine."

## 4. What the verifier was and wasn't good for

n-gram coverage against the source found every affected quote — 24 of them — and cost
nothing. It is the right gate and should run on every extraction.

But it **only reports divergence from source; it does not diagnose cause.** It flagged the
alias corruptions and the model's legitimate ASR repairs (`shitty L` → *shitty ale*,
`Role` → *Roll*, `Lionschild Koster` → *Lionshield Coster*) with the same signal. Of 49
low-coverage quotes in the first run, ~12 were corruption and the rest were correct repairs
or benign cue-merges. The verifier produces a **triage queue, not a verdict** — routing is
its job; adjudication is not.

## 5. Fixes applied (2026-08-03)

1. **`session_doc/scene_extract.py`** — `input_normalizer` removed outright from both the
   live and batch paths. Scene extraction never rewrites the VTT. The canonical roster still
   reaches the model via `system_suffix`. (An opt-in `--normalize-vtt-aliases` flag was added
   first, then deleted: a flag nobody should ever set is a trap.)
2. **`campaignlib/npc.py`** — idempotency guard in `build_alias_normalizer`. When an alias
   occurs inside its own canonical, the canonical's prefix-through-the-alias is registered as
   a key so longest-first matching consumes the prefix already present instead of re-emitting
   it. Fixes `Lord Cassian` → `Lord Cassian Meliamne` rather than `Lord Lord Cassian Meliamne`.
   This matters for the *remaining* legitimate consumers (`campaign_state.py`, `distill.py`),
   which synthesize derived docs and were exposed to the same doubling.
3. **Registry** — stripped `dragon` + `white dragon` (Cryovain), `mine` + `The Mine`
   (Mountain's Toe Gold Mine), `Open Lord of Waterdeep` (mis-assigned to Dagult Neverember;
   Laeral Silverhand added as an entity to carry it). Data hygiene, worth doing on its own
   merits — but **not** what fixed the corruption. See §2.

## 6. For the agentic flow

Unchanged from the earlier draft, and now better supported:

```
model drafts  →  deterministic verifier  →  triage queue  →  adjudicate only the queue
                 (n-gram vs source)          (only failures)
```

Plus one addition earned by this incident: **when output looks systematically wrong, test
whether it reproduces across models before theorising about the model.** It is one cheap run,
and it discriminates the entire class of deterministic-preprocessing bugs — the class most
likely to be misread as model failure, because its output is fluent and factually correct.

**The strongest structural fix remains: have the extractor emit cue IDs, not quote text**, and
let the pipeline resolve IDs to verbatim strings. That makes *both* failure modes — model
fabrication and upstream text mutation — impossible rather than merely detectable, because
no layer between the tape and the output is holding a mutable copy of the quote.

## 7. Cross-check: two verifications, neither substitutable

The `/consistency-check` on `session-summary.md` earlier the same day found **zero** of these.
Not a defect: it asks "does this agree with canon?", and every one of these corruptions *is*
canon — that is literally where they came from.

| Check | Question | Catches |
|---|---|---|
| `/consistency-check` | Does this agree with canon? | Contradictions, drift, gaps |
| n-gram coverage | Was this actually said? | Fabrication, grafting, upstream mutation |

A canon-consistency check gives a canon-injecting pipeline a clean bill of health.
