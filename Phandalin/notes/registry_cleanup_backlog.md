# Entity registry — cleanup record

Adjudication record for the `/registry-cleanup` passes of 2026-08-03.
**All backlog items are resolved.** Kept as the record of what was ruled, so a
future pass doesn't re-ask settled questions or "fix" things deliberately left.

State after the second pass: **562 entities, 110 aliases, 0 slug canonicals,
0 glossary lint errors.**

GM's standing rule across both passes: **trust the canonical.**

---

## Resolved — pass 2 (2026-08-03)

### Wintermoon double-entity
`Syleen Wintermoon` (proper) and `sylvine_wintermoon` (slug) were the same NPC —
the Stone-Cold Reavers leader. DoIP names no Wintermoon at all (the Reavers are
generic veterans; Dobin Noreth is the only named member), so the NPC is
campaign-invented and the module could not arbitrate. Docs favoured *Sylvine*
4:1, but the GM ruled **Syleen** canonical.

- Merged the slug into `Syleen Wintermoon`; stripped the re-added alias.
- Stripped the `Sylvine` alias the merge carried over — a garbling in the alias
  list suppresses its own glossary correction.
- Added `Sylvine → Syleen` to the glossary (no lowercase form in any transcript,
  so it is safe as a standing rule).

### Slug canonicals — all 29 eliminated
25 renamed, 4 merged. None carried a `note:`, so nothing was lost.

Judged rather than mechanically title-cased:
- `daran_edermath_silverleaf` → **Daran Edermath** + alias **Silverleaf**
  (bible: *"Later, I would learn his name, Daran Edermath, but he's known as
  Silverleaf"*). Note added recording the source.
- `rot_tusk_ogre` → **Rot-Tusk Ogre** (hyphen, matching 19 `docs/` hits)
- `out_of_phase_dwarves_axelholm_inhabitants` → **Out-of-Phase Dwarves (Axeholm)**
  — the slug embedded *axelholm*, the garbling stripped in PR #115
- `borg_the_hammer` → **Borg the Hammer**; `teega_the_smith` → **Teega the Smith**
- Placeholders renamed as written: The Cult Fanatic, The Orc Scout,
  The Dwarven King, The Anchorite Half-Orc, The Stag

**Guard references were updated with the renames.** Two slugs (`borg_the_hammer`,
`rot_tusk_ogre`) appeared inside `rejected_aliases` groups; renaming the canonical
without updating those would have silently orphaned the guards.

### Duplicate merges
`aletra` → Aletra Sotorra · `elara` → Elara Seasong Meliamne ·
`runa` → Runa Vokdottir. All four target notes preserved; every re-added slug
alias stripped afterwards.

### Anti-merge guards — one removed, one repaired
`elara → Elara Seasong Meliamne` was blocked twice.

1. A pair guard `['Elara', 'Elara Seasong Meliamne']` — GM ruled it **stale**
   (gm-assist and grounding docs treat Elara as her given name); removed.
2. A four-way guard `['lyra', 'Ilvara', 'elara', 'Elara Seasong Meliamne']` —
   this one is **legitimate**: Lyra, Ilvara and Elara are near-homophones that
   must never be merged into each other. Only `elara` was removed from the group;
   the Lyra/Ilvara/Elara guard is intact.

### Remaining bucket-B / unmapped
- `mentor's staff` on `Meril's Staff` — **KEPT** (table shorthand, like `Brin`).
- `River's District` — ruled a garbling. Alias stripped; `River's District →
  River District` added to the glossary.
- `Castle Nevermember` → **Castle Never** added to the glossary. It had been left
  unmapped by PR #115 after the broken slash-alternation row was repaired.

---

## Confirmed KEEPS — do not "fix" these

These will keep appearing in the audit. That is expected, not a missed item.

- **Bucket A:** `Jenna Roscoe`, `Ser Kaelen Thorne`, `Xanthopoulos` — real full
  names (30–39 `docs/` hits each). They surface only because the glossary carries
  full-name→short-name normalization rows, which are table shorthand rather than
  transcription corrections.
- **Bucket C:** canonical `Adabra Gwynn` — likewise a real full name.
- **Bucket B:** `Anchorite of Talos` (singular), `facktore` (diacritic-free),
  `Falcon Hunting Lodge` (possessive-free), `Mountain's Toe Mine` (short form),
  `mentor's staff` (descriptive short form).
- Glossary short forms `Brin`, `Giles`, `Horia`, `Chief Accountant` are legitimate
  aliases; the four non-idempotent doubling rows that shadowed them were dropped
  in PR #115.

## Still worth doing sometime

- `lint_glossary.py` has no check for canonicals containing `" / "` — the bug that
  corrupted output in PR #115. Worth adding upstream.
- `registry.py` has no `rename` or `unalias` verb; both operations here were direct
  YAML edits plus `strip_aliases.py`.
