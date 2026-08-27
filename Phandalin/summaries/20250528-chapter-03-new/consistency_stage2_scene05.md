# Consistency Report — "Exploring the Stone Bedrooms" (Ch. 3 scene)

## Issue 1 — Religion check (17) attributed to Valphine is uncertain on the tape

- **Location**: Scene summary, bullet 5 ("Valphine identifies the armor via a religion check (17)")
- **Issue**: The attribution is stated flatly, but the tape does not cleanly support it. The "17" lands on **Vukradin's (Dave's) caption**, the GM audibly cannot decide whose roll counts ("Soma discover, re- recalls or Vukradin. No, not Vucri... What about Valphine?"), Soma also rolled ("my jank roll"), and the GM's ruling is plural: "those who rolled above 15 discovered."
- **Evidence**:
  - *Against Valphine*: "17" is on Dave's caption; the scene doc itself flags this ("the roll the summary credits to Valphine lands on Dave's caption").
  - *For Valphine*: "Go, cleric, go" (Valphine is the party's cleric per `party_ch02.md`); and Vukradin's follow-up "So I do not know that they're worthless?" implies **his** roll was under 15 — so the 17 likely wasn't his.
- **Suggested fix**: Keep Valphine as the identifier but mark the attribution as GM-inferred, not tape-confirmed: "identified via a religion check (17; roll attribution unclear on the tape — GM resolved it to Valphine)." Confirm with the GM before this feeds any downstream doc. (Per the standing rule: verify roll/caster attribution before accepting "X did Y" from a recap.)

## Issue 2 — The 22-perception treasure sweep attributed to Valphine is inference, not tape

- **Location**: Scene summary, bullet 6, and "[The Sweep Comes Up Empty]"
- **Issue**: "Valphine sweeps the room ... with a 22 perception" — but both "I look for more treasure" and "22 perception" are folded into **GM captions**. No caption in the entire scene identifies the searcher. Vukradin's "So *you guys* can scrape up the treasure" is plural.
- **Evidence**: The scene doc's own captions: "GM — Vukradin runs off; Valphine's treasure sweep is folded into the GM's caption" and "GM — Valphine's 22 perception, question and answer merged into one caption." The inference *is* reasonable (Soma has her own captions throughout this scene, so a merged-into-GM speaker is most plausibly Gary), but it is an inference.
- **Suggested fix**: Annotate as "(attribution inferred — Valphine's audio merges into the GM caption in this segment)"; confirm against the sibling transcription.

## Issue 3 — Diarization failure: no Valphine or Brewbarry caption exists anywhere in this scene

- **Location**: Whole document (Verbatim moments)
- **Issue**: Every single caption is GM / Soma / Vukradin. Gary's (Valphine) lines are demonstrably merged into GM captions, and Brewbarry/Stéphane is absent entirely. This makes **every** Valphine claim in this scene rest on inference, and leaves it ambiguous whether Stéphane was present (Gary covers Brewbarry when he's absent, per campaign conventions).
- **Evidence**: Issues 1–2 above; campaign CLAUDE.md ("Gary covers Brewbarry when Stéphane absent"); the ch48 transcript-preference caveat shows a second transcription usually exists for cross-checking.
- **Suggested fix**: Note the diarization gap in the scene doc header, and cross-check the sibling/re-transcription for this time window before treating any Valphine attribution here as settled.

## Issue 4 — Timeline gap: the unresolved Ogre #2 / Gnomengarde detour is silently dropped

- **Location**: Scene summary, bullet 1 (and the whole Chapter 3 recap this scene belongs to)
- **Issue**: Per the Chapter 2 archive, the campaign left off **mid-combat with an ogre in a mountain valley en route to Gnomengarde**. Chapter 3 (including this scene) resumes at the dwarven temple with no narration of the ogre's fate or the party's return trip. The archive explicitly says the resolution "belongs to whatever chapter narrates it next" — and Chapter 3's recap doesn't narrate it.
- **Evidence**: `campaign_state.md` — "Ogre Encounter #2 ... IN PROGRESS, unresolved at chapter's end"; "Party Current Situation: ... mid-combat with a hungry ogre." Nothing in `gm-assist.md` (Ch. 3) mentions the ogre or Gnomengarde.
- **Suggested fix**: Ask the GM where the ogre resolution was played (opening of this session? offscreen?) and add a one-line bridge to the Chapter 3 recap so the incremental archive ladder doesn't inherit a hole.

## Issue 5 — "The archaeologists" front-runs the same session's reveal

- **Location**: Scene summary, bullet 6; "[The Sweep Comes Up Empty]"
- **Issue**: Dazlyn and Norbus are **prospectors** per all Chapter 2 grounding docs; they only admit to being "amateur archaeologists" at the *end* of this session (gm-assist's "Amateur Archaeologists" scene). Calling them "the archaeologists" at this earlier point in the session imports the later reveal backward.
- **Evidence**: `campaign_state.md`, `world_state.md`, `planning_ch02.md`, `entity_registry.yaml`: "Shield dwarf prospector" for both. gm-assist: "sheepishly admitted they were amateur archaeologists" — later in the same session.
- **Suggested fix**: "the dwarves" or "the prospectors" in this scene; reserve "archaeologists" for scenes after the admission (or accept it as retrospective narrator knowledge — but then say so once, deliberately).

## Issue 6 — Composite quote with uncertain speaker

- **Location**: Scene summary, bullet 3 ("'They're stone. They'll last forever. That's great.'")
- **Issue**: The quote is a stitch: the GM's caption ends "...They're, they're fine beds. They're" (truncated) and Soma's caption is "stone. They'll last forever. That's great." As printed, it's presented as one unattributed utterance; the first word-and-a-half may be the GM's.
- **Evidence**: The Verbatim moments section of this same document.
- **Suggested fix**: Attribute the sarcasm to Soma and trim to what's on her caption ("They'll last forever. That's great."), or mark the fuller line as a caption-spanning composite.

## Issue 7 (minor) — Hallway geography overstated/ambiguous

- **Location**: Scene summary, bullets 1–2 ("a hallway filled with rubble — rubble to the west, a door to the east")
- **Issue**: The GM's actual description is a self-correcting garble: "To the left is some rubble. To the right, to the west is some rubble. Um, to the east is a door." "Rubble west / door east" is a plausible reading, but "filled with rubble" is stronger than the tape, and "left" vs "west" was never disambiguated.
- **Evidence**: GM verbatim caption in this document.
- **Suggested fix**: "rubble blocking one end (west, per the GM's correction), a door to the east."

## Issue 8 (minor) — "Repeatedly runs back and forth" is chapter-scope, not scene-scope

- **Location**: Scene summary, bullet 6
- **Issue**: Within this scene, Vukradin makes exactly one run (the vestments report). The "repeatedly" pattern belongs to the whole session (vestments, skeleton, skull cavity).
- **Evidence**: The verbatim moments show a single declared run; gm-assist's Memorable Moments carry the "every time" pattern at chapter level.
- **Suggested fix**: "Vukradin runs back to report the vestments — the first of what becomes a running gag this session."

---

## Corroborated (no action needed)

- Three stone bed frames, secret door, stone font on the southwest wall, wardrobe with rotted red leather vestments of Abbathor's priests — all match module geography in `entity_registry.yaml` (E8 "Priests' Bedchamber," E9 "Vestry") and the GM's verbatim descriptions.
- Abbathor as "evil dwarf god of greed" — matches `campaign_state.md` and the registry.
- The long rest before exploring north — matches gm-assist Ch. 3 (rest offered by the dwarves after the jelly fight).
- Passive perception 15 finding the secret door — matches the tape ("Highest passive perception's 15" / "Passive is 15 ... You have found another secret door").
- The scene occurring at all is consistent with the Chapter 2 open thread ("Dwarven Temple — deeper interior unexplored") — this is forward play, not a contradiction. Note only that the provided `campaign_state`/`world_state` are deliberate **Chapter-2 archives**, so they cannot positively validate most Chapter-3 content; nothing in the scene contradicts them except the dropped ogre thread (Issue 4).