# Consistency Report — "The Sleeper in the Iron Coffin" (2026-08-30, Ch. 34)

## Errors in the recap

### 1. Barkinar "promoted to the upper levels" — wrong direction
- **Location:** Summary (necromancer-hypothesis paragraph: "Barkinar had led the Earth Temple before being promoted to the upper levels")
- **Issue:** Barkinar was promoted *downward/inward*, not to the upper levels. The Earth Temple he left already sits in the Upper Temple (levels 1–2); his promotion took him to the Greater/Deep Temple command.
- **Evidence:** **AUTHORITATIVE CANON**, Barkinar entry: "Previously LED THE EARTH TEMPLE… was then promoted to Commander of the Greater Temple's Troops… Succession chain Landers -> Barkinar -> Romag. GM ruling 2026-09-05 (session 20260830)." Canon location entries place the Greater Temple's seat at area 419 on Dungeon Level Four; `vtt_known_additions.md` defines "Upper Temple" as levels 1–2 (the elemental sub-temples). Every GM prep doc says he was "promoted to the deep temple" / "promoted downstairs."
- **Suggested fix:** "…before being promoted to Commander of the Greater Temple's Troops (the Deep Temple below), after which Romag had taken his place."

### 2. Skole's note — garbled pronoun
- **Location:** Summary, Scenes › Return to Nulb, Items › Skole's Note ("Skole says the captain is still telling people you're dead. **You** thought you might enjoy the update.")
- **Issue:** "You thought you might enjoy the update" is incoherent — the note is *from* Skole *to* the party. The recap's own NPC entry contradicts the quote: "dryly suggests that Sequoia might enjoy the update."
- **Evidence:** GM script (`nulb-knows-now.md`, Scene 3): "Skole says the captain is still telling people you're dead. **He** thought you might enjoy the update." The parallel gm-assist export paraphrases the same way.
- **Suggested fix:** "…He thought you might enjoy the update." (Correct in all three occurrences.)

### 3. Falrinth's opening line — transcript garble
- **Location:** Summary ("I cannot be seen sending a runner, and you cannot be before to be seen. To be seen receiving one.")
- **Issue:** Grammatically broken mid-quote — this reads as raw VTT noise carried into the recap, not table delivery.
- **Evidence:** GM script (`nobody-told-nulb.md`, Scene 3): "I cannot be seen sending a runner and you cannot **afford to be seen** receiving one." Related minor garble in the same speech: recap's "the gates are **watching**" vs. script's "the gates are **watched**."
- **Suggested fix:** "…and you cannot afford to be seen receiving one." Consider also "the gates are watched."

## Conflicts with the parallel gm-assist export — verify against the transcript

### 4. Who chided Frostbrand ("one job")?
- **Location:** Summary + Scenes › Garbage Room ("Sequoia rolled twelve damage dice on a critical… and curse Frostbrand for having 'one job'"); Items › Frostbrand
- **Issue:** The recap says **Sequoia** cursed Frostbrand over his own damage roll; the gm-assist export of the same session says **Calmer** "jokingly chided it for not doing its job." Attribution is a precision decision and the two generated docs disagree. Secondary question: the twelve-dice crit math (2d6 weapon + 10d6 sneak) fits Sequoia's *magical short sword*, while canon's Frost Brand is a longsword found in the Fire Temple — so whether Sequoia even wields Frostbrand is unclear.
- **Evidence:** gm-assist.md, Items › Frostbrand; **AUTHORITATIVE CANON** item entry "Frost Brand (unnamed intelligent longsword)… found in the Temple of Fire's trapped iron box"; world_state assigns Sequoia the "Magical short sword (from werewolf lair)."
- **Suggested fix:** Check the tape for the speaker; correct the attribution and clarify whose hand held which blade.

### 5. Undercommon — spoken or not?
- **Location:** Summary + Scenes › Supply Room Ambush ("No one spoke Deep Speech or Undercommon well enough to negotiate")
- **Issue:** The gm-assist export says "Zephyr's **attempt to communicate with them in Undercommon** was met only with sneering silence" — i.e., Zephyr did speak it. The recap says nobody could. This matters for future language checks on Zephyr's sheet.
- **Evidence:** gm-assist.md, Scenes › Supply Room Ambush and Summary.
- **Suggested fix:** Verify against transcript; harmonize (e.g., "Zephyr attempted a warning in broken Undercommon, but no one spoke it well enough to negotiate" if both are partially right).

### 6. Spirit Guardians — cast once or twice?
- **Location:** Spells › Spirit Guardians; Scenes › Supply Room Ambush
- **Issue:** Recap: cast once, concentration broken by a claw hit, not recast. gm-assist: "Cast **twice** by Calmer during the storeroom ambush."
- **Evidence:** Both documents cover the same fight; they disagree on spell-slot expenditure.
- **Suggested fix:** Verify on tape; matters for resource tracking.

### 7. Zephyr's title — Chief of Staff vs. Chief of Operations
- **Location:** Summary ("Zephyr, acting as Chief of Operations"), Scenes › Missing Prisoners ("Chief of Staff **or** Chief of Operations"), Calmer's quotes ("As the Chief of Staff…", "This is why I have made you Chief of Staff")
- **Issue:** The recap uses both titles for Zephyr and explicitly hedges. Downstream docs will need one canonical title.
- **Evidence:** Internal inconsistency within the recap; gm-assist uses "Chief of Staff" throughout.
- **Suggested fix:** Ask the GM for a ruling; "Chief of Staff" has the stronger attestation (both direct quotes).

## Questionable claims

### 8. Vurakhal present at the Minotaur scene?
- **Location:** Summary ("The Minotaur's own language was Abyssal, which none of the party understood — not even Vurakhal, the fire salamander"); Scenes › Minotaur's Throne
- **Issue:** Vurakhal's involvement in this scene is unattested in the parallel export (which mentions only sign language and broken Common), and canon stations him elsewhere.
- **Evidence:** **AUTHORITATIVE CANON**, Vurakhal entry: "bound salamander retainer… **guarding the Fire Temple altar (area 212)**." gm-assist.md omits him from the scene entirely. (Content-wise plausible — salamanders speak Ignan, not Abyssal — but presence needs verification.)
- **Suggested fix:** Verify against the transcript whether Vurakhal was present/consulted; otherwise trim to "which none of the party understood."

### 9. "A war that had ended beneath their feet ten days earlier"
- **Location:** Summary and Locations › Nulb ("ten days earlier"/"ten days ago")
- **Issue:** The specific "ten days" figure appears nowhere else and would become a hard timeline anchor if left. Possible conflation with the arc's recurring "ten years" (Y'dey/Thrommel).
- **Evidence:** GM prep says the war ended "days ago" (`nulb-knows-now.md` road read-aloud) and that Nulb's map is "a week out of date" (`nobody-told-nulb.md`); gm-assist gives no number. world_state dates are Planting 20–29 with the war engineered mid-tenday.
- **Suggested fix:** Verify on tape; if unsupported, soften to "days earlier."

### 10. Toll the Dead called "this new spell of mine"
- **Location:** Summary + Spells › Toll the Dead ("This new spell of mine is very effective")
- **Issue:** Toll the Dead is long-established for Calmer — it killed the Chimera (Ch. 23/27) and delivered the killing blow on Romag (Ch. 28). "New" contradicts the record. If it's a verbatim in-character joke, keep the quote but don't let "new spell" propagate as fact.
- **Evidence:** campaign_state: "Chimera killed by Calmer's Toll the Dead"; "Calmer's Toll the Dead delivered killing blow" (Romag assassination). gm-assist records the casting without the "new" framing.
- **Suggested fix:** Verify the quote; if paraphrase, drop "new."

### 11. "The holy gentleman" (singular) in the coffin revelation
- **Location:** Summary + Scenes › A Message from the Shadows
- **Issue:** Falrinth's script and his own earlier quote in this recap use the plural "holy gentlemen." The singular subtly changes who keeps the sleeper.
- **Evidence:** `nobody-told-nulb.md` Scene 3 script: "The holy gentlemen keep something in it"; recap's own Orb quote: "any of the holy gentlemen who would like me dead."
- **Suggested fix:** Verify on tape; likely "holy gentlemen."

### 12. Minor internal drift: "black-coated" / "black-cloaked" / "black cloak" bandits
- **Location:** Summary, Scenes › Sunken Treasure, Items › Black Cloaks
- **Issue:** Three variants for the same descriptor. Trivial, but a future search on the wrong variant will miss references.
- **Suggested fix:** Standardize (recommend "black-cloaked bandits").

## Verified-correct items — do NOT "fix" these

- **Alrrem "now deceased"** (NPCs › Alrrem): campaign_state and world_state list Alrrem as *alive*, but they are stale (coverage ends ~Ch. 25/28). **AUTHORITATIVE CANON** confirms his death — Vurakhal entry: "surrendered… **after Alrrem's death** stranded it on the Material Plane." The recap is right; flag the grounding docs for regeneration, not the recap.
- **Shield +1** (Items): module canon says shield +2, but **AUTHORITATIVE CANON** (Cistern Chamber entry) records the explicit table ruling: "delivered as a SHIELD +1 and claimed by Calmer (session 20260830)… Table ruling stands over module canon." The AC 21 figure is likewise tape-confirmed in that entry.
- **Zinnia he/him throughout:** correct per **AUTHORITATIVE CANON** ("male, he/him… Extraction passes repeatedly degender him"). Note the conflict is in **party.md**, which uses she/her for Zinnia — that document is the one in error.
- **Hold Monster (Calmer), Chill Touch (Zephyr), "focus point" (Zinnia):** all legal under the table's 2024/5.5e ruleset per party.md's explicit note; previously confirmed false positives against 2014 lists.
- **Lucius Graeme spelling:** matches canon and the glossary ruling ("Lucius Graham → Lucius Graeme"); do not regress to "Graham."
- **"Rhennee":** confirmed canonical in `vtt_known_additions.md` (GM ruling 2026-09-05); absence from the entity registry is a pending promotion, not an error.
- **Necromancer backstory** (served under Barkinar, passed over when Romag was elevated): consistent with the canon succession ruling Landers → Barkinar → Romag; supersedes the older prep draft that made him "Romag's predecessor."
- **"Broken Blades"** used correctly; note campaign_state/world_state still contain the known garble "Crimson Guard" for this company (glossary: Crimson Guard → Broken Blades) — a stale-doc issue, not a recap issue.

## Summary
Three genuine errors to correct (items 1–3), four attribution/mechanics conflicts with the parallel export requiring transcript verification (4–7), five soft-verify items (8–12), and several stale-context conflicts where the recap is right and campaign_state/world_state/party.md need regeneration (Alrrem's death, Zinnia's pronouns, "Crimson Guard").