# MemPalace Usage Guide — Phandalin Campaign
*Lessons learned from the arc cleanup sessions, April 2026*

---

## The Core Pattern: Mine Now, Chronicle Later

Session prep produces two kinds of content. They go to different places at different times.

### Mine Immediately (canon lore)
Content that is true about the world regardless of what happens at the table:

- **New NPCs** — full drawer in phandalin/npcs + KG entries for relationships and traits
- **Backstory corrections** — KG entries that update or replace previous facts (e.g. Falcon's companions killed by Iymrith, not in her lair)
- **World-building canon** — drawers + KG for foundational mythology, faction structure, campaign principles
- **NPC mechanics** — KG entries for crack conditions, DCs, reachability (these are designed, not emergent — they're true before the session)
- **Strategic positions** — KG entries for who's watching whom on the board (e.g. Tiamat watching Iymrith and Zariel)

### Do NOT Mine (planning documents)
Content that describes what *might* happen stays in notes/ as files:

- Session shape and beat structure
- Outcome branches (Branch A / Branch B)
- Momentum system mechanics
- Read-aloud notecards
- DM logistics and checklists

These are planning tools. They don't belong in the mempalace because they describe possibilities, not facts. They stay as campaign notes and are accessed via the campaign MCP tool, not via mempalace search.

### Mine After the Session (chronicle beats)
After the session runs, add a chronicle entry that captures:

- What actually happened (which branch was taken)
- How NPCs actually behaved (did Falcon crack? did Ossian ask?)
- Momentum outcome and consequences
- What the party chose and what it costs them
- Any new facts that emerged from play

This goes in the chronicle wing as an adventure beat, sourced from the session transcript.

---

## KG Predicate Vocabulary for Campaigns

Standard predicates (member_of, killed_by, allied_with) work for basic facts. Campaign design needs a richer vocabulary for character design and session prep retrieval.

### Character Design Predicates
| Predicate | Use | Example |
|-----------|-----|---------|
| `cracked_by` | What reaches a character emotionally | Falcon → cracked_by → someone_asking_Senne_name |
| `blind_spot` | What the character cannot see about themselves | Aldric → blind_spot → hasn't_asked_Adabra_peaks_plan |
| `reachable_by` | Who can get through, with mechanical conditions | Brynn → reachable_by → Vukradin_with_disadvantage_if_Corbin_unowned |
| `key_question` | The line an NPC will deliver | Ossian → key_question → what_does_naturalism_do_with_orcs_in_practice |
| `characterized_by` | A specific personal detail that makes them real | Senne → characterized_by → pressed_flowers_in_books |

### Strategic Predicates
| Predicate | Use | Example |
|-----------|-----|---------|
| `watching` | Who is tracking whom on the board | Tiamat → watching → Iymrith_artifact_scheme |
| `strategic_position` | Board-level awareness | Tiamat → strategic_position → fourth_player |
| `motive_for_recruiting` | Why one entity uses another | Tiamat → motive_for_recruiting_Adabra → self_aiming_weapon |
| `would_discard` | Disposability in an alliance | Tiamat → would_discard → Adabra_at_first_convenient_opportunity |
| `crack_moment` | Designed turning point for a character arc | Adabra → crack_moment → Tiamat_burns_something_she_loves |

### World-Building Predicates
| Predicate | Use | Example |
|-----------|-----|---------|
| `believe_themselves_to_be` | Shared species belief | dragons → believe_themselves_to_be → root_admins_of_the_planes |
| `function_as` | Role in the world | dragons → function_as → bankers_in_mortal_economies |
| `is_actually` | Trope inversion | dragon_stole_princess → is_actually → debt_cancellation_by_murder |
| `maps_onto` | Real-world analogue | trope → maps_onto → 12th_century_antisemitism |
| `rejects` | Campaign principle | campaign_principle → rejects → biological_determinism |

---

## Drawer Best Practices

### NPC Drawers
Write full character profiles, not summaries. A future session searching for "Falcon grief" or "Aldric enclave" needs to retrieve the complete picture — motivation, crack conditions, what works and what doesn't, relationship to the current arc.

Include:
- Identity and faction (name, rank, role in the scene)
- Motivation (why they're doing what they're doing)
- The crack (what reaches them, mechanical conditions)
- What doesn't work (what the party will try that won't land)
- After the scene (what happens to them next)

### World-Building Drawers
For mythology and campaign principles, include the reasoning — not just the fact but why it matters for play. "Dragons are bankers" is a fact. "This is why 'dragon stole the princess' is actually debt-cancellation murder, which maps onto 12th century antisemitism" is the context that makes the fact useful.

---

## Wing/Room Architecture

The three-wing architecture works for this campaign:

| Wing | Room | What goes here |
|------|------|---------------|
| chronicle | (by chapter/session) | What actually happened — adventure beats, session summaries |
| narrative | (by character/scene) | In-character narrative, voice moments, POV snippets |
| phandalin | npcs | All character profiles regardless of faction or arc |
| phandalin | (other rooms as needed) | World-building, mythology, faction structure |

**What does NOT go in the mempalace:**
- Planning documents (session prep, DM checklists, beat structures) → notes/
- Arc design documents (custom arcs, level-band designs) → notes/arc_cleanup/ or notes/epic_tier/
- Tracking files (published module content) → docs/tracking*.txt

The mempalace is for retrieval of what IS true. Notes are for what MIGHT happen. Tracking files are published ground truth.

---

## The Workflow

1. **Design session** — write notes in arc_cleanup/ or epic_tier/
2. **Extract canon** — mine new NPCs, backstory corrections, world-building to mempalace (KG + drawers)
3. **Run the session** — use the notes files at the table
4. **After session** — add chronicle beat from transcript; update any KG entries that changed based on actual play
5. **Discard or archive** — planning documents that were consumed by the session can be archived or left as historical reference
