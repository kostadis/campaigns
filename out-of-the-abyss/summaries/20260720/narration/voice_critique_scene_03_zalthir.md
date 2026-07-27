# Voice Critique — Zalthir, scene 03: The Aftermath of the Sanctum Attack

**Narration:** summaries/20260720/narration/session_doc_scene_03_the_aftermath_of_the_sanctum_attack.md
**Voice spec:** voice/zalthir_voice.md
**Per-char examples:** examples/zalthir.md

## Flags

### [1] Mechanical scan A — em-dash overuse

Seven narration-level em-dash lines (none inside `"..."` dialogue, though two precede an italic aside rather than sit inside it):

| Line | Text | Suggested |
|---|---|---|
| 9 | "...put them down — empty steel, no bodies inside..." | Convert to colon: "...put them down: empty steel, no bodies inside..." |
| 11 | "...already open — smashed off its frame by the thing..." | Convert to comma: "...already open, smashed off its frame by the thing..." |
| 25 | "...when he handed it over — *I have given it now...*" | This is the genre spec's sanctioned "em-dash for interrupted speech or thought" use (introducing a remembered line). Defensible as-is; if converting, a colon reads just as well. |
| 41 | "...had a scroll — a Candlekeep sage keeps one..." | Split into two sentences: "...had a scroll. A Candlekeep sage keeps one..." |
| 49 | "...set beside the real things — Brother Harren taught it..." | Split or semicolon: "...set beside the real things. Brother Harren taught it, or the tall one who smelled of incense; I was never certain which." |
| 53 | "...tolling wrong — an alarm pattern, cold and institutional..." | Convert to colon: "...tolling wrong: an alarm pattern, cold and institutional..." |
| 59 | "...had a saying — or possibly Brother Quellin did — that the most dangerous..." | This exact phrasing (with both dashes) is lifted directly from the voice spec's own "Things he'd say" line. Flagged per the mechanical scan, but likely intentional and worth keeping as-is. |

**Why:** The scan flags every narration-level em-dash unconditionally. Several here (25, 59) match the genre file's own explicit allowance for em-dash as "interrupted speech or thought," so they're weaker candidates for change than 9, 11, 41, 53, which are plain connective asides that read just as well with a period or colon.

### [2] Voice spec conflict — "filed" used twice in one section

> "'What do we do next, gentlemen?' I filed him under *useful for now* and said nothing."

> "The decoy in one hand, the bell overhead, the First Reader with her throat open somewhere in the dark. I filed it and watched the door."

**Why:** The genre spec caps bookkeeping/recording verbs at one per section for every narrator, and for Zalthir specifically calls "filed" a verb that's "rarely written." Using it twice in the same section — once early, once as the closing line — spends the rarity twice and dilutes the closing beat, which is clearly meant to land as the section's one quiet "filed it."
**Suggested rewrite:** Cut the first instance. "'What do we do next, gentlemen?' I said nothing and watched him work it out." Leave the closing "I filed it and watched the door" as the section's single, earned use.

### [3] Register-wrong vocabulary — "shape"

> "The key stayed dark. Inert. A cold shape of metal in a room full of things singing."

**Why:** "The shape of X" is the genre file's explicitly named, zero-tolerance Claude tic ("Never use. If you find yourself reaching for it, name the actual thing instead"). This is a clean, direct hit on that banned construction, not a borderline case.
**Suggested rewrite:** "The key stayed dark. Inert, dead metal in a room full of things singing."

## Verdict

Zalthir's voice is otherwise very well-held here — the terse declaratives, the "Brother [name]" thought-source device, and the aphorism reuse from his own spec are all on-target. The two real issues are mechanical (em-dash density) and a spent-twice bookkeeping verb; both are quick spot-edits, not a re-narration case.
