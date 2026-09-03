## Consistency Report

### 1. Incorrect crevasse treasure total

- **Location:** Scenes — “A Heroic Recap”
- **Issue:** The chest is said to contain 160 gp, 160 sp, and an additional treasure worth 20 gp.
- **Evidence:** `campaign_state`, `world_state`, and `party.md` consistently record **120 gp and 160 sp**, plus five malachite gems, three potions, and Talon. The transcript’s treasure narration is garbled, but the normalized campaign documents agree on 120 gp.
- **Suggested fix:** Replace “160 gold pieces, 160 silver pieces, an additional piece of treasure worth 20 gold” with “120 gold pieces and 160 silver pieces.”

### 2. Bugbears incorrectly described as contained beneath the manor

- **Location:** Summary; Locations — “Tresendar Manor”
- **Issue:** The recap says the surviving bugbears “still lived somewhere below” and remained an unresolved danger “somewhere beneath the manor,” implying they were still trapped inside.
- **Evidence:** `campaign_state` and `world_state` establish that one bugbear died and **three wounded bugbears escaped the hideout**. Nosk possessed a key that opened every hideout door, so the locked manor door did not contain them. The party does not know this and believes they remain inside.
- **Suggested fix:** Qualify this as party belief: “The party believed the three surviving bugbears remained beneath the manor, but they were actually loose.”

### 3. The escape is overstated as successfully sealing the bugbears in

- **Location:** Summary opening; Scenes — “A Heroic Recap”
- **Issue:** The oil is said to have bought enough time “to seal the manor door behind them,” suggesting the door secured the threat.
- **Evidence:** `world_state` states that the door was never an effective barrier because Nosk carried the master key. The transcript confirms only that the party shut and locked the door and heard hammering; it does not establish containment.
- **Suggested fix:** Use the characters’ perspective: “They shut and locked the manor door, believing they had sealed the surviving bugbears inside.”

### 4. The number and state of the surviving bugbears are left misleadingly vague

- **Location:** Summary; Locations — “Tresendar Manor”
- **Issue:** The recap repeatedly refers only to “the bugbears” surviving, without recording that one died and three survived wounded.
- **Evidence:** `campaign_state`, `world_state`, and `party.md` explicitly establish **one bugbear killed by the oil fire and three surviving, wounded, and loose**.
- **Suggested fix:** State: “One bugbear died in the fire; three survived wounded.”

### 5. “Burning corridor” is questionable during Veyra’s attempted return

- **Location:** Summary opening
- **Issue:** Veyra is described as nearly turning back “into the burning corridor.”
- **Evidence:** `campaign_state` says the oil burned for only two rounds. Veyra turned back while passing the crevasse after the party had fled down the tunnels; the transcript does not establish that she was about to re-enter active flames.
- **Suggested fix:** Replace with “nearly turned back toward the crevasse and the pursuing bugbears.”

### 6. Hamun’s emotional description contradicts his stated fear

- **Location:** Summary — arrival of Hamun Kost
- **Issue:** Hamun is described as wearing “the calm expression of someone who had never once been afraid of anything in his life.”
- **Evidence:** During the same encounter, Hamun candidly says he does not approach Agatha because he does not want to be killed by a banshee. The transcript supports confidence, but not complete fearlessness.
- **Suggested fix:** Replace with “the calm expression of someone confident in his power.”

### 7. The promised meal is stated too firmly

- **Location:** Summary; NPCs — “Hamun Kost”
- **Issue:** Hamun is said to have promised a fine meal upon the party’s return.
- **Evidence:** In the transcript, Hamun says **“maybe”** he will have a fine meal for them. The meal is a possibility, while the Cragmaw Castle information is the actual promise.
- **Suggested fix:** Change to “promised the information and suggested that he might also provide a fine meal.”

### 8. Creative zombie names are presented as established session facts

- **Location:** Locations — “Old Owl Well”; NPCs — “Hamun Kost”
- **Issue:** The twelve zombies are called the “Kost Wardens,” with individuals named Warden Dreth and Warden Holl.
- **Evidence:** These names come from `monsters_phase2_descriptions.md`, explicitly labeled a **creative deliverable** for previously unnamed monsters. Neither the transcript nor the campaign-state documents establish that these names were learned or used during play.
- **Suggested fix:** Remove the names from the session recap, or label them as GM-only descriptive names added after the session.

### 9. The zombies’ former identities are presented with unwarranted certainty

- **Location:** Summary; Scenes — “Arrival at the Old Owl Well”; Locations — “Old Owl Well”
- **Issue:** Two zombies are identified as a “former sentinel” and a “Red Wizard acolyte.”
- **Evidence:** Those identities derive from the creative monster-description document. During the session, the party saw zombies, and the recap’s detailed identities were not established through dialogue or checks.
- **Suggested fix:** Describe only observable features: “one sun-peeled zombie and another wearing a singed Red Wizard-style robe.”

### 10. “Scarlet Fist” is presented as an established faction name

- **Location:** NPCs — “Nosk”
- **Issue:** Nosk is called “the leader of the Scarlet Fist.”
- **Evidence:** “Scarlet Fist” originates in `monsters_phase2_descriptions.md`, a creative naming document. The transcript and core campaign-state documents identify the group only as four bugbear reinforcements sent by the Black Spider.
- **Suggested fix:** Replace with “leader of the Black Spider’s four-bugbear reinforcement group,” or explicitly mark “Scarlet Fist” as a later GM-only label.

### 11. Daran’s objective is reframed as artifact recovery

- **Location:** Summary; Scenes — “Consulting Daran Edermath”
- **Issue:** The recap says Daran ultimately wanted the party to investigate because something might be “worth recovering,” and implies artifact retrieval was his principal goal.
- **Evidence:** The transcript states that Daran’s quest was to determine whether **a threat to Phandalin was brewing at Old Owl Well**. He did express interest in the party obtaining whatever might be there, but that was secondary.
- **Suggested fix:** Clarify: “Daran’s primary concern was whether Old Owl Well posed a threat to Phandalin, though he also hoped any valuable discovery would fall into responsible hands.”

### 12. The recap omits that the party already had a separate paid Wyvern Tor contract

- **Location:** Summary; Scenes — “Arrival at the Old Owl Well”
- **Issue:** Hamun’s Wyvern Tor favor is treated as a newly acquired standalone task without noting that the party had already accepted Harbin Wester’s 120-gp contract to clear the same marauders.
- **Evidence:** `campaign_state`, `world_state`, `party.md`, and `player_quest_log.md` all record the existing **120 gp Wyvern Tor contract**, negotiated by Pip and accepted in Chapter 5.
- **Suggested fix:** Add that accepting Hamun’s favor aligned with the party’s existing contract from Harbin, allowing the same mission to satisfy both obligations.

### 13. Wyvern Tor’s full roster is GM-only knowledge presented beside observed facts

- **Location:** Locations — “Wyvern Tor”; NPCs — “Axe-Biter Bugbear Sentry”
- **Issue:** The recap states that the camp contains Brughor Axe-Biter, four bugbears, and Gog, although the party had only observed one sentry and the cave entrance.
- **Evidence:** The roster comes from module and GM reference material, not from anything discovered during this session. The transcript ends before the party scouts the cave’s occupants.
- **Suggested fix:** If this is player-facing, remove the full roster. If it is GM-facing, label it explicitly as “GM-only module roster; not yet known to the party.”

### 14. “Resonated with an unseen magical force” is more certain than the recorded observation

- **Location:** Summary; Items — “Black Stone”; Memorable Moments
- **Issue:** The recap repeatedly states that Zenvon’s stone and Veyra’s crystal mutually resonated through an unseen magical force.
- **Evidence:** The campaign documents establish that **Veyra’s crystal flared brighter near Zenvon’s stone**. They do not clearly establish a separately observed two-way resonance or force.
- **Suggested fix:** Use the directly supported description: “Veyra’s crystal flared brightly when brought near Zenvon’s black stone, suggesting a magical connection.”