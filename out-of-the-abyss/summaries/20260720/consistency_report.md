## Consistency Report — Chapter 59: "The Key is Secured"

---

### ISSUE 1 — NPC Name Error (Persistent, Entire Recap)
- **Location:** Summary, Memorable Moments, Scenes (multiple), NPCs, Items
- **Issue:** Kalan is called **"Kalan Stormbranch"** throughout the entire recap.
- **Evidence:** `campaign_state.md`, `entity_registry.yaml`, and `threefold_proof.md` all use **"Kalan Strongbranch"**; aliases include "Strongbench" but never "Stormbranch."
- **Suggested fix:** Replace every instance of "Stormbranch" with "Strongbranch."

---

### ISSUE 2 — Wrong Number of Helmed Horrors
- **Location:** Summary ("three towering helmed horrors"), Scenes/Chaos in Deneir's Sanctum ("Three helmed horrors smashed through the windows and doors"), Locations/Deneir's Sanctum
- **Issue:** Recap says **three** helmed horrors; campaign documents say **two**.
- **Evidence:** `campaign_state.md`, Completed Encounters §19: *"Two helmed horrors came through the windows."* Party Current Situation: *"Two ruined helmed horrors and one inert key on the floor."*
- **Suggested fix:** Change all occurrences of "three" to "two" helmed horrors.

---

### ISSUE 3 — Moziqodo Attributed to Ilvara, Not Sylvira (Two Locations)
- **Location:** Memorable Moments ("linking her murder to **Ilvara's** abyssal spawn son"); Scenes/The Death of Bookwyrm ("Daz recalls information about **Ilvara's** abyssal spawn son")
- **Issue:** Moziqodo is Sylvira Savikas's son, not Ilvara Mizzrym's. Ilvara is dead and had no abyssal spawn son. The same recap correctly identifies him as Sylvira's son in the Summary, NPCs section, and the Battle scene.
- **Evidence:** `entity_registry.yaml`: *"Moziqodo — 'The Beast of Candlekeep'; Sylvira's demonspawn son."* `campaign_state.md` §3 and §World State: Sylvira is bedridden and Moziqodo is her son. `20260712` prep doc: *"Moziqodo — a clock, not a boss. Carries the new banked backstory (A'lai's long game against Sylvira)."*
- **Suggested fix:** In both locations, replace "Ilvara's abyssal spawn son" with "Sylvira's abyssal spawn son."

---

### ISSUE 4 — Moziqodo Misclassified as "Pit Fiend" (Persistent, Entire Recap)
- **Location:** Summary ("the pit fiend"), Memorable Moments ("slaying the pit fiend Moziqodo"), Scenes/Battle in the Domed Rotunda ("a pit fiend named Moziqodo"), NPCs/Moziqodo ("A massive and powerful pit fiend"), Items/Dawnbringer, Items/Real High Tower Key
- **Issue:** Moziqodo is called a "pit fiend" throughout. He is not. A pit fiend is CR 20 with AC 19 and ~300 HP. The GM prep doc scales Moziqodo at **CR 5, AC 15, HP 85** — consistent with a unique demonspawn, not a devil of that tier. The entity registry never uses the term "pit fiend."
- **Evidence:** `entity_registry.yaml`: *"Moziqodo — 'The Beast of Candlekeep'; Sylvira's demonspawn son."* `20260712_candlekeep_nothing_under_detect_magic.md`: *"Moziqodo — CR5, AC 15, HP 85, climb 40/Shadow Leap. ~2-round kill clock on a lone Watcher."* `candlekeep_hightower_session.md`: "Moziqodo — scaled CR 5 (HP −30% … Abyssal Plague bite rider intact)."
- **Suggested fix:** Replace all instances of "pit fiend" when referring to Moziqodo with "abyssal spawn" or "demonspawn." Example: "A massive and powerful **demonspawn** revealed to be the abyssal spawn son of Sylvira."

---

### ISSUE 5 — Kalan's Title Understated
- **Location:** NPCs/Kalan Stormbranch: "An academic investigator and high-ranking member of the Avowed"
- **Issue:** By the time of this session, Kalan has already been reinstated to his formal position. Calling him merely a "high-ranking member" erases his actual standing.
- **Evidence:** `campaign_state.md`, Completed Encounters §18: *"Kalan Strongbranch reinstated as Head of the Avowed."* `entity_registry.yaml`: *"Kalan Strongbranch — Gatewarden; archmage."* `world_state.md` NPC table: *"Candlekeep, reinstated as Head of the Avowed."*
- **Suggested fix:** "The reinstated **Head of the Avowed** and **Gatewarden** of Candlekeep, whose 'Threefold Proof' methodology was recently vindicated…"

---

### ISSUE 6 — Methodology Name Misspelled
- **Location:** NPCs/Kalan: "thrice-fold proof methodology"
- **Issue:** The methodology is consistently titled "Threefold Proof," not "thrice-fold proof."
- **Evidence:** `threefold_proof.md` document title and text throughout; `campaign_state.md` §18: *"his rejected 'Threefold Proof' is now the institutional investigative framework."*
- **Suggested fix:** Replace "thrice-fold proof" with "Threefold Proof."

---

### ISSUE 7 — Internal Contradiction: A'lai's Role (Confirmed Architect vs. Mere Suspect)
- **Location:** Summary ("The conspiracy's architect was now clear") vs. Scenes/Aftermath and Strategy ("they still did not know who was truly pulling the strings behind this conspiracy, and their suspicions turned heavily toward A'lai")
- **Issue:** The Summary states A'lai's role as architect was definitively established by Fembris's confession. The Aftermath section then treats him as someone the party merely "suspects heavily," as if the earlier confirmation never happened. This inconsistency will confuse future sessions about what the party actually knows.
- **Evidence:** The Summary itself: *"This crucial revelation explained exactly why Tadric and the party had been targeted while Kalan himself remained untouched. The conspiracy's architect was now clear."* The Aftermath contradicts this: *"their suspicions turned heavily toward A'lai."*
- **Suggested fix:** Clarify that the party confirmed A'lai as the **immediate** architect but does not know if a higher power is directing him. For example: *"They knew A'lai was behind the attacks, but did not yet know who — if anyone — was pulling his strings."*

---

### ISSUE 8 — Potion of Flying Attribution Conflicts with Campaign State
- **Location:** Scenes/A Recap of Intrigue ("Zalthir used Glabbagool to discreetly steal a potion of flying from Alkrist's safe"); Items/Potion of Flying ("that Zalthir surreptitiously stole from Alkrist's safe using Glabbagool")
- **Issue:** The recap frames this as Zalthir directing Glabbagool to steal the potion. The campaign state frames it as Glabbagool's autonomous act.
- **Evidence:** `campaign_state.md`, Key Resources: *"Glabbagool — has **autonomously** stolen and kept a Potion of Flying."* (Emphasis mine; no mention of Zalthir's direction.)
- **Suggested fix:** Verify with session transcript which attribution is accurate. If Glabbagool acted autonomously, the items and scenes entries should reflect that. This distinction matters because Glabbagool's autonomous agency is a recurring characterization thread.

---

### ISSUE 9 — Ward Description Incomplete (Omits Flight Suppression)
- **Location:** Summary ("The great shield that prevented teleportation and suppressed fire throughout Candlekeep"); Locations/Candlekeep; NPCs/Daral
- **Issue:** The recap describes the ward as suppressing only teleportation and fire. The GM design document adds that it also suppresses **flight**.
- **Evidence:** `candlekeep_hightower_session.md`: *"Candlekeep's wards specifically block **teleportation, flight, and fire damage** — that's the entire security model."*
- **Suggested fix:** Add "flight" to the ward description: "…prevented teleportation, suppressed flight, and suppressed fire throughout Candlekeep…" This matters for future sessions since losing the wards also restores flight to attackers and defenders.

---

### ISSUE 10 — Chapter Number Mismatch
- **Location:** Recap title ("Chapter 59")
- **Issue:** The campaign state labels the helmed horror ambush in Deneir's Sanctum as **(ch61)**, and states it is "Current as of Chapter 61." The recap calls this same event "Chapter 59." One of these numbers is wrong, or there is a chapter-counter discrepancy that needs to be reconciled before it propagates.
- **Evidence:** `campaign_state.md`, Completed Encounters §19: *"Helmed horror ambush in Deneir's Sanctum **(ch61)**."* `campaign_state.md` header: *"Current as of Chapter 61."*
- **Suggested fix:** Verify which chapter counter is authoritative (per `CLAUDE.md`: "chapter file number is authoritative — but bible-file # ≠ real session-chapter #"). Confirm the session chapter number and update whichever document is wrong; do not let both numbers coexist uncorrected.

---

### FLAGGED FOR UPDATE — Campaign State NPC Table Out of Sync
- **Location:** `campaign_state.md`, NPC Current States table
- **Issue:** Bookwyrm is still listed as **Alive** ("Hostile-concealed; performs cooperation, steered investigators wrong") in the NPC table, despite the recap (and the campaign state's own "Current Situation" section) describing events that occur after her death.
- **Evidence:** Recap describes Bookwyrm's murder as occurring during this session. The campaign state header says "Current as of Chapter 61," which should post-date her death. The NPC table has not been updated.
- **Suggested fix:** Update the NPC table to mark Bookwyrm as **Dead** and move her to the deceased list. Add a brief note of cause (throat torn out; High Tower key taken). Failing to do so will cause future session prep to incorrectly treat her as a live NPC.