# Quote Verification Report

**Generated**: 2026-09-06T04:04:23
**Transcript**: `summaries/011-20260904/GMT20260904-220136_Recording.transcript (1).cleaned.vtt`
**Threshold**: 0.85 (near/unverified boundary)
**Minimum tokens to score**: 4

| verdict | count | share |
|---|---|---|
| verified | 943 | 93% |
| near | 59 | 6% |
| **unverified** | 8 | 1% |
| unscored | 5 | 0% |
| exempt | 0 | 0% |

**Refused by the extraction contract (#250)**: 0.

## Not checked

- Inline `"…"` spans in prose — not reliably dialogue (a plaque honouring the "liberators of the Ordning" is a label, not speech). Only `> "…"` blockquotes are verified.
- Speaker attribution. This report answers *were these words said*, not *did this person say them*.
- `## Scene summary` sections — human-authored gm-assist content, not model output.

## Refused — the contract will not choose for you

Extraction contract #250 (`docs/design/ExtractionContract_proposal.md`), rules R1 and R3. A refusal is **not** a claim that the text is wrong. It is a claim that this pipeline is not the thing that should decide, so the span stays as it is until you rule on it. Nothing here was auto-corrected and nothing here will be — and nothing here is blocked either: `sd_narrate` still renders these. Refusal means flagged.

None. No span was refused by R1 or R3.

## Unverified — review these

### `05_the_battle_against_gog.md:129`

- **Quote**: "Raises his great club."
- **Score**: 0.78
- **Nearest transcript line** (Kostadis Roussos): "Or, Ray's is this great club."

### `02_ambush_at_the_ravine.md:343`

- **Quote**: "Alright, so we'll put the bugbear's body."
- **Score**: 0.79
- **Nearest transcript line** (Kostadis Roussos): "Alright, so we'll put a… Bugs of your body."

### `04_the_ambush_inside_the_cave.md:459`

- **Quote**: "Alright, Sister Maela… seeing the orc dead."
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Score**: 0.79
- **Nearest transcript line** (Kostadis Roussos): "Alright, Sister Maela… Seeing, the ogre, the, the bugbear dead."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:302`

- **Quote**: "Lying in Cragmaw Castle."
- **Score**: 0.79
- **Nearest transcript line** (Nikhil): "Lying in the Cragmaw closure."

### `04_the_ambush_inside_the_cave.md:267`

- **Quote**: "Yeah, and then I have… I have Nick."
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Score**: 0.83
- **Nearest transcript line** (Nikhil): "Yeah, and then I have the… Have a night."

### `02_ambush_at_the_ravine.md:101`

- **Quote**: "the bugbear sees her, and growls."
- **Score**: 0.84
- **Nearest transcript line** (Kostadis Roussos): "the bugbearer… Caesar, and growls."

### `05_the_battle_against_gog.md:450`

- **Quote**: "Swings his… swings his… his greatclub."
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Score**: 0.85
- **Nearest transcript line** (Kostadis Roussos): "Swings his… swings his… his mace."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:105`

- **Quote**: "It's all… it's drawn in charcoal."
- **Likely stitched**: contains `...` — two separate utterances joined into one quote. Usually fixed by splitting it, not by rewording.
- **Score**: 0.85
- **Nearest transcript line** (Kostadis Roussos): "It's all… it's John and Charcoal."

## Near — an edit happened here (traceable, not verbatim)

Most of these are disfluency edits: the extraction tidied a filler word out of a real line. Listed after the unverified section on purpose — they are the majority and should not bury the findings that matter.

**But `near` means *an edit*, not *a safe edit*.** Similarity cannot tell the two apart: a measured DeepSeek run scored `"My kind has been spreading violence"` (transcript: `"Mankind …"`) at **0.92** and the harmless `"No, I have"` for `"No, I, I have,"` at **0.94** — the meaning-changing edit ranked *below* the harmless one, and no threshold separates them, because both are edits of the same tiny size. Skim this list for changed *words*, not low scores.

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:45`

- **Quote**: "Pip goes to this corner."
- **Score**: 0.85
- **Nearest transcript line** (Nikhil): "So I go to this corner."

### `01_arrival_at_wyvern_tor.md:43`

- **Quote**: "Do I have the range to shoot an arrow?"
- **Score**: 0.85
- **Nearest transcript line** (Nikhil): "Do I have the range to shoot a… Idle?"

### `05_the_battle_against_gog.md:54`

- **Quote**: "Me Gog. You kill Brughor. Me eat you alive."
- **Score**: 0.86
- **Nearest transcript line** (Kostadis Roussos): "A mini dog, you kill, Brughor, me eat you alive."

### `03_scouting_the_cave.md:165`

- **Quote**: "How about if he alerts the bugbears and the ogre?"
- **Score**: 0.87
- **Nearest transcript line** (Nikhil): "How about it has alert the bugbears and the oak."

### `02_ambush_at_the_ravine.md:200`

- **Quote**: "You rolled a 7."
- **Score**: 0.87
- **Nearest transcript line** (Kostadis Roussos): "So you rolled a 16?"

### `04_the_ambush_inside_the_cave.md:324`

- **Quote**: "I'll use the shortsword again."
- **Score**: 0.87
- **Nearest transcript line** (Nikhil): "I'll use the short for it again."

### `04_the_ambush_inside_the_cave.md:408`

- **Quote**: "Yeah, I'm gonna use my Insight."
- **Score**: 0.87
- **Nearest transcript line** (Nikhil): "Yeah, I'm gonna use my website."

### `04_the_ambush_inside_the_cave.md:381`

- **Quote**: "Alright, hold on. So, okay, this bugbear, seeing him die, goes, 'I'm outta here' at 13."
- **Score**: 0.90
- **Nearest transcript line** (Kostadis Roussos): "Alright, hold on. So, okay, so this bug we were seeing him die at goes, I'm outta here at 13."

### `05_the_battle_against_gog.md:543`

- **Quote**: "Now, what is the story behind, you know, the relationship between these guys and Hamun Kost, like…"
- **Score**: 0.90
- **Nearest transcript line** (Nikhil): "Now, what is the story behind, you know, the relationship between the skies and the hormone costs, like…"

### `04_the_ambush_inside_the_cave.md:435`

- **Quote**: "You're gonna let the bugbears run away?"
- **Score**: 0.90
- **Nearest transcript line** (Kostadis Roussos): "You're gonna let the lit bugbrews run away?"

### `04_the_ambush_inside_the_cave.md:357`

- **Quote**: "No, you use your sword… you have a shortsword and a scimitar. Remember, you have one in each hand?"
- **Score**: 0.91
- **Nearest transcript line** (Kostadis Roussos): "No, you use your sort… you have to sort, sort, sort, and a scimitar. Remember, you have one in each hand?"

### `03_scouting_the_cave.md:96`

- **Quote**: "Okie dokie. Zenvon, you don't notice anything, so Sister Maela pokes her head as well."
- **Score**: 0.91
- **Nearest transcript line** (Kostadis Roussos): "Okie dokie. Sister Maela, you don't notice anything, so Sister Maela pokes her head as well."

### `05_the_battle_against_gog.md:303`

- **Quote**: "What weapon are you using? Go to Actions."
- **Score**: 0.92
- **Nearest transcript line** (Kostadis Roussos): "What webinar are you using? Go to Actions."

### `07_dinner_with_the_red_wizard.md:429`

- **Quote**: "No, no, no, we don't tell him that we have the crystal."
- **Score**: 0.92
- **Nearest transcript line** (Nikhil): "No, no, no, we don't tell him that we have the customer."

### `07_dinner_with_the_red_wizard.md:603`

- **Quote**: "The rest of the time, it adds nothing."
- **Score**: 0.92
- **Nearest transcript line** (Kostadis Roussos): "The rest of the time, it adds notes."

### `05_the_battle_against_gog.md:492`

- **Quote**: "Gog, yes, yes. Hey, Gog, listen,"
- **Score**: 0.92
- **Nearest transcript line** (Nikhil): "Gog, yes, yes. Hey, Gog, Visem,"

### `04_the_ambush_inside_the_cave.md:63`

- **Quote**: "You know, the guarding bugbear, and what?"
- **Score**: 0.93
- **Nearest transcript line** (Nikhil): "You know, the guarding bugbear, and word?"

### `07_dinner_with_the_red_wizard.md:294`

- **Quote**: "Roll an Insight check."
- **Score**: 0.93
- **Nearest transcript line** (Kostadis Roussos): "Roland Insight Check."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:359`

- **Quote**: "Before we leave, Pip, since you killed the ogre."
- **Score**: 0.93
- **Nearest transcript line** (Nikhil): "Before we leave, Pip, since you killed the, or auger."

### `05_the_battle_against_gog.md:591`

- **Quote**: "He makes his saving throw. Gog is outraged."
- **Score**: 0.93
- **Nearest transcript line** (Kostadis Roussos): "She makes her, saving throw. Gog is outraged."

### `05_the_battle_against_gog.md:513`

- **Quote**: "Anything about Hamun Kost? Tell us what has happened in the past."
- **Score**: 0.93
- **Nearest transcript line** (Nikhil): "Anything about hormone costs? Tell us what has happened in the past."

### `02_ambush_at_the_ravine.md:274`

- **Quote**: "Veyra… Looks at him again, and decides to cast another… Magic Missile."
- **Score**: 0.94
- **Nearest transcript line** (Kostadis Roussos): "Veyra… Looks at him again, and decides to cast another… Magic result."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:170`

- **Quote**: "So when Veyra had written that name last time, the crystal had flared."
- **Score**: 0.94
- **Nearest transcript line** (Kostadis Roussos): "So when Veyra had written that name last time, the crystal had blown."

### `04_the_ambush_inside_the_cave.md:438`

- **Quote**: "Yeah, just fight with the ogre."
- **Score**: 0.94
- **Nearest transcript line** (Nikhil): "Yeah, just fight with the over."

### `05_the_battle_against_gog.md:42`

- **Quote**: "And he blows it, so he takes 2d8—takes 10 points of damage."
- **Score**: 0.94
- **Nearest transcript line** (Kostadis Roussos): "And he blows it, so he takes 2d8 Rick, takes 10 points of damage."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:218`

- **Quote**: "They attack all the travelers on the… highway, I suppose."
- **Score**: 0.94
- **Nearest transcript line** (Nikhil): "They attack all the travelers on the… I wait, I suppose."

### `05_the_battle_against_gog.md:60`

- **Quote**: "Another bugbear runs out."
- **Score**: 0.94
- **Nearest transcript line** (Kostadis Roussos): "Another bug beer runs out."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:397`

- **Quote**: "Yes, awesome, okay. I give my share to Pip."
- **Score**: 0.94
- **Nearest transcript line** (Nikhil): "Yes, awesome, okay. I did my share to Pip."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:167`

- **Quote**: "The goblin gives her a bad feeling."
- **Score**: 0.94
- **Nearest transcript line** (Nikhil): "The goggling gives her a bad feeling."

### `02_ambush_at_the_ravine.md:301`

- **Quote**: "Alright, the bugbear is dead."
- **Score**: 0.95
- **Nearest transcript line** (Kostadis Roussos): "Alright, the bug beer is dead."

### `07_dinner_with_the_red_wizard.md:225`

- **Quote**: "give you the exact details. Veyra, would you like to tell what you saw on the wall?"
- **Score**: 0.95
- **Nearest transcript line** (Nikhil): "give you the exact details. Where would you like to tell what, you saw on the wall?"

### `07_dinner_with_the_red_wizard.md:501`

- **Quote**: "In lots of feats. Oh, like… 100."
- **Score**: 0.95
- **Nearest transcript line** (Nikhil): "In lots of feet. Oh, like… 100."

### `02_ambush_at_the_ravine.md:179`

- **Quote**: "But… Hold on, watch. The bugbear goes 1, 2, 3, 4, 5… 6."
- **Score**: 0.95
- **Nearest transcript line** (Kostadis Roussos): "But… Hold on, watch. The bug here goes 1, 2, 3, 4, 5… 6."

### `02_ambush_at_the_ravine.md:295`

- **Quote**: "And he kills the bugbear."
- **Score**: 0.96
- **Nearest transcript line** (Kostadis Roussos): "And he kills the bugbearer."

### `01_arrival_at_wyvern_tor.md:501`

- **Quote**: "He's got his pike in front of him, and he's looking, and you can see him looking over his shoulder. Roll an Insight check."
- **Score**: 0.96
- **Nearest transcript line** (Kostadis Roussos): "He's got his poik in front of him, and he's looking, and you can see him looking over his shoulder, a Roland Insight check."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:162`

- **Quote**: "Strange goblin with an elongated head was with the cragmaw band, but we gave it… Let's look at that."
- **Score**: 0.97
- **Nearest transcript line** (Nikhil): "Strange problem with an elongated head was with the cragmaw band, but we gave it… Let's look at that."

### `07_dinner_with_the_red_wizard.md:438`

- **Quote**: "Oh, you don't… you don't tell him about Veyra's Blue Crystal."
- **Score**: 0.97
- **Nearest transcript line** (Kostadis Roussos): "Oh, you don't… you don't tell her about Veyra's Blue Crystal."

### `05_the_battle_against_gog.md:147`

- **Quote**: "Veyra steps over here… Let's see what her spell situation is like."
- **Score**: 0.97
- **Nearest transcript line** (Kostadis Roussos): "ZRA steps over here… Let's see what her spell situation is like."

### `04_the_ambush_inside_the_cave.md:252`

- **Quote**: "Shortsword, yes, okay, I'm gonna use my short sword,"
- **Score**: 0.97
- **Nearest transcript line** (Nikhil): "Shotswold, yes, okay, I'm gonna use my short sword,"

### `02_ambush_at_the_ravine.md:322`

- **Quote**: "About the bugbear, that, that is, that is to your credit."
- **Score**: 0.97
- **Nearest transcript line** (Kostadis Roussos): "About the bugbearers, that, that is, that is to your credit."

### `01_arrival_at_wyvern_tor.md:240`

- **Quote**: "You know, throw off his pike, or, you know."
- **Score**: 0.98
- **Nearest transcript line** (Nikhil): "You know, throw off his bike, or, you know."

### `01_arrival_at_wyvern_tor.md:28`

- **Quote**: "Sorry, sorry. The faint smell of smoke hangs in the air as you ascend a rugged ridge down the lower slopes of the hill. 50 yards away, a cave mouth opens up at the bottom of a ravine, hunkered down by a boulder 20 yards outside the cave. Evidently keeping watch is a single bugbear."
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "Sorry, sorry. The faint smell of smoke hangs in the air as you ascend a rugged ridge down the lower slopes of the hill. 50 yards away, a cave mouth opens up at the bottom of a ravine, hunkered down by a boulder 20 yards outside the cave. Evidently keeping watch is a single budbearer."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:254`

- **Quote**: "She looks at it, she looks at her, and she stands there. Where? And Maela's laughing, because…"
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "She looks at it, she looks at him, and she stands there. Where? And Maela's laughing, because…"

### `04_the_ambush_inside_the_cave.md:213`

- **Quote**: "Can you roll, can you roll your initiative, can you roll your initiative? We can keep your old initiatives, or you can re-roll, it's up to you."
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "Can you roll, can you roll your initiative, can you roll your initiative? John, we can keep your old initiatives, or you can re-roll, it's up to you."

### `01_arrival_at_wyvern_tor.md:180`

- **Quote**: "Do you know what that is? If you don't, it's a wep… it's a weapon. It's a… it's a long, pointy weapon. It's like a polearm."
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "Do you know what that is? If you don't, it's a wep… it's a weapon. It's a… it's a long, punky weapon. It's like a polearm."

### `02_ambush_at_the_ravine.md:77`

- **Quote**: "Veyra, picks up, picks up her notebook, she looks at the bugbear, realizes the bugbear, she has enough time to dodge him, so she steps up and stands in front, stands in front."
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "Veyra, picks up, picks up her notebook, she looks at the bug beer, realizes the bug beer, she has enough time to dodge him, so she steps up and stands in front, stands in front."

### `07_dinner_with_the_red_wizard.md:642`

- **Quote**: "Charging into a room and killing 5 bugbears is the fastest way to get a third of your party killed."
- **Score**: 0.98
- **Nearest transcript line** (Kostadis Roussos): "Charging into a room and killing 5 bug beers is the fastest way to get a third of your party killed."

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:374`

- **Quote**: "Sure, but the ogre was very big, and he got the last kill, so I thought, you know, maybe… and I've not done anything football too long. It's not that you guys will not get anything, but…"
- **Score**: 0.99
- **Nearest transcript line** (Nikhil): "Sure, but the auger was very big, and he got the last kill, so I thought, you know, maybe… and I've not done anything football too long. It's not that you guys will not get anything, but…"

### `06_secrets_in_the_charcoal_and_looting_the_cave.md:233`

- **Quote**: "It's all connected. The bugbears, the strange goblins, the crystals… my mentor…"
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "It's all connected. The bugbeers, the strange goblins, the crystals… my mentor…"

### `07_dinner_with_the_red_wizard.md:522`

- **Quote**: "And just pick a feat, alright? So, okay, just to be clear, you can either pick a feat."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "And just pick a feast, alright? So, okay, just to be clear, you can either pick a feast."

### `03_scouting_the_cave.md:78`

- **Quote**: "You see a bunch of, you notice a bunch of things, right? There's 4 bugbears, there's an ogre."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "You see a bunch of, you notice a bunch of things, right? There's 4 bugbeers, there's an ogre."

### `05_the_battle_against_gog.md:135`

- **Quote**: "This bugbear also decides he's, you know, there's a time and a place for bravery, and this is not it."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "This bugbearer also decides he's, you know, there's a time and a place for bravery, and this is not it."

### `07_dinner_with_the_red_wizard.md:408`

- **Quote**: "You know, to keep up to his name when I use this sword."
- **Score**: 0.99
- **Nearest transcript line** (Nikhil): "You know, to keep up to his name when I use this word."

### `05_the_battle_against_gog.md:423`

- **Quote**: "Yeah, so he's down to 20. You can use… you can see his, health bar, right?"
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "Yeah, so she's down to 20. You can use… you can see his, health bar, right?"

### `04_the_ambush_inside_the_cave.md:423`

- **Quote**: "Okay. What you notice… what you perceive is that the bugbears kind of are, like, I'm at, like, see him dead, and, like, just want to get out of here."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "Okay. What you notice… what you perceive is that the bugbearers kind of are, like, I'm at, like, see him dead, and, like, just want to get out of here."

### `04_the_ambush_inside_the_cave.md:303`

- **Quote**: "Yeah, that would… that would have been a mess. Alright, he's actually got 2 hit points, I miscalculated it. Okay, so he's got 2 hit points. Sister Maela."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "Yeah, that would… that would have been a mess. Alright, she's actually got 2 hit points, I miscalculated it. Okay, so she's got 2 hit points. Sister Maela."

### `03_scouting_the_cave.md:150`

- **Quote**: "Or, you know, we could run in there and try to kill them all. Last time we faced 4 bugbears, we had to run for our lives, so I'm not entirely certain that's something we want to do."
- **Score**: 0.99
- **Nearest transcript line** (Kostadis Roussos): "Or, you know, we could run in there and try to kill them all. Last time we faced 4 bugbeers, we had to run for our lives, so I'm not entirely certain that's something we want to do."

### `07_dinner_with_the_red_wizard.md:333`

- **Quote**: "Well, let me say something for you, my dear boy. He looks at Pip. I happen to be an expert archaeologist."
- **Score**: 1.00
- **Nearest transcript line** (Kostadis Roussos): "Well, let me say something for you, my dear boy. She looks at Pip. I happen to be an expert archaeologist."

### `07_dinner_with_the_red_wizard.md:91`

- **Quote**: "peasants, that happened to have been in the wrong place at the wrong time with a powerful wizard, red wizard. Hamun is delighted, Hamun sees you, and he says."
- **Score**: 1.00
- **Nearest transcript line** (Kostadis Roussos): "peasants, that happened to have been in the wrong place at the wrong time with a powerful wizard, red wizard. Amun is delighted, Hamun sees you, and he says."

## Unscored — too short to judge

Under 4 tokens. A quote this short matches something in any transcript, so neither a high nor a low score means anything. Not an accusation.

- `01_arrival_at_wyvern_tor.md:294` — "Stealth?"
- `02_ambush_at_the_ravine.md:194` — "Rolling for shortbow."
- `05_the_battle_against_gog.md:96` — "So… Pip."
- `05_the_battle_against_gog.md:234` — "True Strike?"
- `07_dinner_with_the_red_wizard.md:411` — "In combat."
