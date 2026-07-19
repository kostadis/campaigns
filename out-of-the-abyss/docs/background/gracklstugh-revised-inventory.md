# Gracklstugh Revised — Turmoil in the City of Blades — module proper-noun inventory

**Source:** `Gracklstugh Revised - Turmoil in the City of Blades` (890770-Gracklstugh_Revised_-_Turmoil_in_the_City_of_Blades.json, source ID `890770GR`; registered in `refs.yaml` as "City of Gracklstugh"), 213 section titles / 893 phrase candidates scanned.

**Provenance:** deterministic regex pass + 10-way parallel LLM chunk extraction, merged and deduplicated (module-inventory skill, 2026-07-18). Contested attributions were checked against the real per-chunk structured attributes (not just prose) and ruled by Kostadis on 2026-07-18 (see Rulings below). Two additional near-duplicates and one bad-alias conflation, missed by the automated checks, were caught and ruled during rendering.

This is the **source-material list**, not the campaign's homebrew — for the campaign's adapted Gracklstugh state see `docs/world_state.md`, `docs/campaign_state.md`, and `docs/npcs/` as applicable.

---

## Rulings & contested attributions

| Issue | Detail | Ruling |
|---|---|---|
| Amber Thrazgad | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as species=duergar, gender=female, status=alive |
| Cairngorm Clan | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as species=stone giant |
| Cult of Orcus | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as no conflicting attribute |
| Deepking Horgar Steelshadow V | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as species=duergar, gender=male, status=alive |
| Orcus | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as no conflicting attribute |
| Whorlstone Area 1b (Buppido's Lair) | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as no conflicting attribute |
| Whorlstone Area 7 (Assassins' Headquarters) | Merge-tool description-text fallback misattributed another entity's species/status word | Dismissed as false positive; settled as no conflicting attribute |
| Demogorgonic Abomination | Chunk agents genuinely disagreed on category | Ruled: category = other |
| Rihuud | Chunk agents genuinely disagreed on category | Ruled: category = npc |
| the Wyrmsmith | Chunk agents genuinely disagreed on category | Ruled: category = npc |
| Clan Thrazgad / Thrazgad Clan | Near-duplicate missed by automated similarity check | Merged as Clan Thrazgad |
| Whorlstone Area 14b (Zubriska's Barracks) / Zubriska's Hideout | Near-duplicate missed by automated similarity check | Merged as Whorlstone Area 14b (Zubriska's Barracks / Hideout) |
| Clan Xardelvar | Auto-merged via a bad alias from one chunk; fuller chunks describe distinct entities | Split into Clan Xardelvar, Xarrorn |
| Clan Xundom | Auto-merged via a bad alias from one chunk; fuller chunks describe distinct entities | Split into Clan Xundom, Kavalrachni |
| 31 near-duplicate name pairs (numbered/directional) | String-similarity false positives (Whorlstone Area N vs N+1, etc.) | All confirmed distinct, none merged |

---

## NPCs

### Duergar Clan Leaders

- **Adrik Blackskull** — 553-year-old male duergar leader of Clan Blackskull (Stonemasons); a blustering blowhard who believes in claiming power through station.
- **Amber Thrazgad** — Laird of Clan Thrazgad in Southfurrow District; reports stolen ore, suspects the Gray Ghosts, and offers a 20% armorsmithing discount for its recovery.
- **Audhild Xornbane** — 308-year-old female duergar leader of Clan Xornbane (Scouts and Prospectors); highly intelligent, flowery, believes in suffering to prove worth.
- **Baern Xundom** — 392-year-old male duergar leader of Clan Xundom (Steeder Breeders); stern, believes in responsibility and obedience; Gartokkar's brother.
- **Bruenor Burakrinwurn** — 639-year-old male duergar leader of Clan Burakrinwurn (Dock Operators); blind and nearly deaf, suspicious of everyone, values rooting out lies.
- **Dagnal Thordensonn** — 585-year-old male duergar leader of Clan Thordensonn (Jewelers); curious and honorable.
- **Delg Coalhewer** — 262-year-old male duergar leader of Clan Coalhewer (Coal Miners); ponderous and believes in charity where possible.
- **Einkil Anvilthew** — 329-year-old male duergar leader of Clan Anvilthew (Toolmakers); curious about everyone he meets and believes strongly in redemption.
- **Flint Thuldark** — 257-year-old male duergar leader of Clan Thuldark (Metalworks and Jewels); nervous and sullen, believes in respecting others' work.
- **Gunnloda Firehand** — 489-year-old female duergar leader of Clan Firehand (Smelters); irritable and agitated, believes in speaking plainly and fairly.
- **Gurdis Bukbukken** — 484-year-old female duergar leader of Clan Bukbukken; argumentative about fungi-farming practices and prone to whimsy after drinking.
- **Helja Henstak** — 354-year-old female duergar leader of Clan Henstak (Food); very anxious about food stores, believes in moderation and rationing.
- **Kathra Muzgardt** — 574-year-old female duergar leader of Clan Muzgardt (Brewers); arrogant and extremely greedy, believes money is key to power.
- **Mardred Parlynsurk** — 360-year-old female duergar leader of Clan Parlynsurk (Clothing Manufacturers); friendly, believes in neutrality and focusing on her work.
- **Orsik Saltbaron** — 363-year-old male duergar leader of Clan Saltbaron (Salt Miners); honest, believes in independence and letting others find their paths.
- **Riswynn Hammercane** — 451-year-old female duergar leader of Clan Hammercane (Construction Engineers); friendly, believes logic is key to life's satisfaction.
- **Thangus Ironhead** / **Thangus** — Laird of Clan Ironhead in Northfurrow District; tells the party of the Deepking's edict barring the Ironheads from accepting new work orders.
- **Vondal Xardelvar** — 317-year-old male duergar leader of Clan Xardelvar (Gas Miners); hot-tempered and believes in honor.

### The Deepking's Court

- **Captain Blackskull** — Suspected by Deepking Horgar of treason and of coveting his throne since she was young; named with scorn on his hit list.
- **Deepking Horgar Steelshadow V** / **Deepking** / **Deepking Horgar** / **Horgar** / **Horgar Steelshadow V** / **Steelshadow V** / **the Deepking** — Deepking (ruler) of Gracklstugh; duergar dwarf wielding Brimtongue and a dwarven thrower; grants smithing orders in exchange for recovering the stolen dragon egg.
- **Gorglak** — Gate guard wrongly suspected of ordering the assassination attempt on Werz Saltbaron, which the Deepking himself actually commanded.
- **Lingrick Xardelvar** — Named sarcastically as Deepking Horgar's 'most gaseous ally' at the end of his hit list of targets.
- **Olga** — Horgar's daughter and heir to the Steelshadow throne; Themberchaud urges the party to assassinate her as poetic justice for his stolen egg.
- **Shal** — Horgar's consort, currently the only person besides him permitted past the Royal Vault's guardian spells; revealing her true form could cure his madness.

### Cult of Demogorgon & the Whorlstone Conspiracy

- **Buppido** — Derro whose misguided necromantic experiments gave Orcus an early foothold in the Whorlstone Tunnels before his cult spread beneath Gracklstugh.
- **Narrak** — Derro warlock of the fiend leading the Cult of Demogorgon from the Cultist Hideout (Area 12); encountered Demogorgon and seeks to lure it to Gracklstugh.
- **Pliinki** — Derro savant mutating the stolen red dragon egg and failed Thrazgad ore in the Obelisk (Area 14); insane but dedicated Council of Savants member.
- **Rihuud** — Stone giant mutated by the Cult of Demogorgon, nephew of Stonespeaker Hgraam; his rampage draws Gartokkar's attention to the party.
- **Ulnara** — Derro savant occupying the Dumping Pit (Area 13) with an ogre zombie, zombies, and a crawling claw; goes invisible to cast lightning bolt.
- **Uskvil** — Derro savant, master thief and one of three Gray Ghost leaders; helped steal the dragon egg and ore, now aids Pliinki's ritual.

### Empty-Scabbard Killers, Gray Ghosts & Assassins

- **Aliinka** — Twin sister of Zubriska, one of three Gray Ghost leaders and the Council's investigator into thief rumors; resides in the Halls of Sacred Spells.
- **Droki** — Derro courier serving the Council of Savants, Gray Ghosts, Empty-Scabbard Killers, and other factions; enigmatic and absurd, though not a Council member.
- **Eldgrim** / **Eldgrim, Master Assassin** — Duergar soulblade, master assassin and second-in-command of the Empty-Scabbard Killers under Qualux; distributes charity while scouting recruits for the illithid.
- **Ivar** — One of three soulblade guards (36 hit points) protecting Eldgrim at Area 7, wielding a mind blade alongside Ulara and Shari.
- **Lorthio** — Former leader of the Empty-Scabbard Killers; his remains were used by Qualux to birth a maturing elder brain for the illithid colony.
- **Qualux** — Mind flayer occupying Area 8, secretly directing Eldgrim and the Empty-Scabbard Killers while cultivating a fledgling elder brain colony born from Lorthio.
- **Shari** — One of three soulblade guards (36 hit points) protecting Eldgrim at Area 7, wielding a mind blade alongside Ulara and Ivar.
- **Ulara** — One of three soulblade guards (36 hit points) protecting Eldgrim at Area 7, wielding a mind blade alongside Ivar and Shari.
- **Werz Saltbaron** / **Werz** — Duergar smuggler and low-level Gray Ghost, illicitly trading with Kazook Pickshine; the Deepking secretly ordered his attempted assassination at the Darklake Docks.
- **Zubriska** — Twin sister of Aliinka, one of three Gray Ghost leaders; manages operatives from her Whorlstone barracks while secretly plotting against the cult.

### Stone Guard, Keepers of the Flame & Clan Politics

- **Errde Blackskull** / **Captain Errde Blackskull** / **Errde** — Duergar captain of the Stone Guard whose clan has been killed by the Empty-Scabbard Killers; grows convinced the Deepking is the city's source of corruption.
- **Gartokkar Xundom** / **Gartokkar** / **Gartokkar Xundorn** — Leader of the Keepers of the Flame; given the egg or the hit list, he backs Horgar and orders the party to kill any illithids found.
- **Grinta Ironhead** / **Grinta** — Hot-tempered granddaughter of Clan Ironhead's laird Thangus who strives for change; might be pushed toward insurrection if shown the hit list.
- **Stonespeaker Hgraam** / **Hgraam** — Stonespeaker of the Cairngorm Clan; won't help remove the Deepking but may withhold intel from Horgar to spare his clan a derro conflict.
- **the Wyrmsmith** / **His Arrogance** / **His Rotundity** / **Themberchaud** / **Themberchaud the Wyrmsmith** / **the Pampered** / **the Portly** / **the Scheming Red** — Adult red dragon and Wyrmsmith of Gracklstugh, restless under the Keepers of the Flame's stewardship; seeks independence and his own dominion in the city.

### Blingdenstone & Other NPCs

- **Dorbo Diggermattock** — Co-determined, with Sark Axebarrel, the weapons and armor Blingdenstone's deep gnomes need for the Battle of Blingdenstone.
- **Dorhun** — Figure whose favor the party can win by knocking out Rihuud instead of killing him.
- **Glabbagool** — Telepathically-inclined ally who could detect Qualux's strong psionic presence near the Empty-Scabbard Killers' territory, from 300-500 feet away.
- **Ilvara** — Figure slain by the author's party, along with others, only a few days after they escaped Velkynvelve and before reaching Gracklstugh.
- **Kazook Pickshine** / **Kazook** — Contact who provides the lead to Werz Saltbaron and later opens his bag of holding to extract gems for trading with Gracklstugh's smiths.
- **Pelek** — Ghost that still appears after the fight in Buppido's Lair (Area 1b), per the original adventure.
- **Pudding King** — Leader of an army of oozes that Blingdenstone's deep gnome soldiers need acid-resistant gear to fight.
- **Sark Axebarrel** — Named the items necessary for the Battle of Blingdenstone alongside Dorbo Diggermattock in the Desired Goods listing.
- **Senni Diggermattock** — Suggested using the party as trade emissaries to make Blingdenstone appear bigger and better-connected to Gracklstugh's factions.
- **Stool** — Telepathically-inclined ally who could detect Qualux's strong psionic presence near the Empty-Scabbard Killers' territory, from 300-500 feet away.
- **Xalith** — Figure tied to the Drow Pursuit; this supplement explicitly ignores Xalith since the author's party finished that pursuit before reaching Gracklstugh.
- **Ylsa** — Merchant whose task reward is changed to Clan Henstak's favor, usable for advantage in one clan negotiation.

## Deities

- **Asmodeus** — Ruler of the Nine Hells; tortured a lesser devil into eternal servitude, binding its spirit to Brimtongue, which urges wielders to contact him.
- **Demogorgon** / **Prince of Demons** / **the Prince** — Prince of Demons; target of the Cult of Demogorgon's worship, whom Gracklstugh's corrupted Council tried to lure and sacrifice the city to.
- **Diirinka** — Deity Buppido was attempting to sacrifice to when he accidentally contacted Orcus instead, in his lair (Area 1b).
- **Laduguer** — Duergar deity for whom Laduguer's Furrow district is named; Eldgrim sometimes disguises himself as one of Laduguer's clerics while roaming the streets.
- **Orcus** — Demon Prince of Undeath whose appearance at Cyrog's chamber scattered fleeing illithids, one becoming Qualux; may inspire a future cult using Whorlstone corpses.

## Locations

### Whorlstone Tunnels

- **Assassins' Tunnel** / **Area 5b** — Tunnel used by Empty-Scabbard Killers soulblades to reach the Raucous Mesa.
- **Cranium Rat Den** / **Area 6c** — Chamber housing a swarm of cranium rats plus additional cranium rats within the Assassins' Den.
- **Cultist Chasm** / **Area 5a** — Chasm used by Cult of Demogorgon derro to reach the Raucous Mesa.
- **Mindwitness Chamber** / **Area 6e** — Chamber housing two soulblades and a mindwitness created from a captured spectator, Qualux's greatest triumph.
- **Northeast Barracks** / **Area 6b** — Chamber housing four soulblades and two intellect devourers within the Assassins' Den.
- **Northwest Barracks** / **Area 6a** — Chamber housing five soulblades and 2d4 cranium rats within the Assassins' Den.
- **Qualux's Quarters** / **Area 8** / **Tunnel with Spikes** / **Whorlstone Area 8** — Table of contents lists Area 8 as Qualux's Quarters; the Whorlstone quickref instead describes it as a hazardous spiked tunnel reactivated by cultists.
- **Small Den** / **Area 6d** — Chamber housing two soulblades and an intellect devourer within the Assassins' Den.
- **Whorlstone Area 1 (Entrance)** / **Area 1** / **Entrance** — Entrance to the Whorlstone Tunnels named in this supplement's table of contents; no further description appears in this chunk.
- **Whorlstone Area 10** / **Area 10** / **Cultist Outpost** / **Cultist Pens** — Table of contents lists Area 10 as Cultist Pens; the Whorlstone quickref describes it as Narrak's forward Cultist Outpost with Demogorgon sigils and black ichor.
- **Whorlstone Area 11** / **Area 11** / **Cultist Barracks** / **Quasit Playground** — Table of contents lists Area 11 as Quasit Playground; the Whorlstone quickref describes it as a Cultist Barracks hiding a letter from Zubriska to Uskvil.
- **Whorlstone Area 12** / **Area 12** / **Cultist Hideout** / **Narrak's Headquarters** — Table of contents lists Area 12 as Cultist Hideout; the Whorlstone quickref describes it as Narrak's Headquarters, with a Demogorgon altar and severed heads.
- **Whorlstone Area 13 (Dumping Pit)** / **Area 13** / **Dumping Pit** — Whorlstone chamber of reanimated multi-headed zombies made from Empty-Scabbard Killer corpses, where Uskvil performs necromantic rituals.
- **Whorlstone Area 14 (The Obelisk)** / **Area 14** / **Obelisk** / **The Obelisk** — Gray Ghosts' Whorlstone headquarters holding the pulsating obelisk and the chained red dragon egg Pliinki and Uskvil are trying to channel into it.
- **Whorlstone Area 14a (Doors)** / **Area 14a** / **Doors** — Whorlstone corridor of magically sealed doors keyed to ritual components (egg, ore, blood, shadow, mind); only the egg sigil is active.
- **Whorlstone Area 14b (Zubriska's Barracks / Hideout)** / **Area 14b** / **Thieves' Hideout** / **Whorlstone Area 14b (Zubriska's Barracks)** / **Zubriska's Barracks** / **Zubriska's Hideout** — Zubriska's Whorlstone hideout, holding thieves' tools, a scroll of teleport, and her journal plotting to betray the cult and claim the obelisk.
- **Whorlstone Area 14c (Thief Barracks)** / **Area 14c** / **Thief Barracks** — Gray Ghosts dormitory in Whorlstone holding sabotage target lists and a note referencing the mysterious 'One Who Watches.'
- **Whorlstone Area 1a (Pool Bypass)** / **Area 1a** / **Pool Bypass** — Whorlstone sub-area named in this supplement's table of contents; no further description appears in this chunk.
- **Whorlstone Area 1b (Buppido's Lair)** / **Area 1b** / **Buppido's Lair** — Chamber cursed by Orcus after Buppido's failed sacrifice, raising the dead here as undead; Pelek's ghost appears here.
- **Whorlstone Area 2 (Diseased Pool)** / **Area 2** / **Diseased Pool** — Whorlstone area named in this supplement's table of contents; no further description appears in this chunk.
- **Whorlstone Area 3** / **Area 3** / **Tunnel Junction** / **Zombie Hall** — This document's table of contents lists Area 3 as Zombie Hall; its Whorlstone quickref instead describes Area 3 as Tunnel Junction, a transit point.
- **Whorlstone Area 4** / **Area 4** / **Collapsed Passage** / **Fungi Thicket** — Table of contents lists Area 4 as Fungi Thicket; the Whorlstone quickref describes it as a Collapsed Passage the Gray Ghosts are trying to clear.
- **Whorlstone Area 5** / **Area 5** / **Raucous Mesa** / **Storage Cache** / **The Raucous Mesa** — Table of contents lists Area 5 as Raucous Mesa; the Whorlstone quickref describes it as a Storage Cache hiding a letter from Uskvil to Pliinki.
- **Whorlstone Area 6** / **Area 6** / **Assassins' Den** / **Assassins' Dens** / **Barracks** — Table of contents lists Area 6 as Assassins' Den; the Whorlstone quickref describes it as a Barracks occupied by derro savants running sleep experiments.
- **Whorlstone Area 7 (Assassins' Headquarters)** / **Area 7** / **Assassins' Headquarters** — Eldgrim's Whorlstone lair holding Deepking Horgar's sealed hit list naming local nobles, a drow priestess, and the derro savant Pliinki as targets.
- **Whorlstone Area 9** / **Area 9** / **Fountain of Evil** / **Hydra's Nest** — Table of contents lists Area 9 as Fountain of Evil; the Whorlstone quickref describes it as the hydra's territory, littered with corpses from Area 13.
- **Whorlstone Tunnels** / **Whorlstone** — Undercity tunnel system beneath Gracklstugh, split between Cult of Demogorgon and Gray Ghost territory with hazardous unclaimed zones between the two hubs.

### City Districts

- **Darklake District** — A district of Gracklstugh beyond which the party's patron-issued badges grant free roam; also the boundary beyond which Droki is not yet found.
- **Derro Territory** — A region referenced for background and encounter rules on derro hostility toward non-derro visitors entering the Halls of Sacred Spells.
- **Flowstone District** — A district of Gracklstugh containing the Keepers of the Flame Headquarters and Themberchaud's Lair, where the missing dragon egg's secret is known.
- **Laduguer's Furrow** — District the party is sent or summoned into after their initial arrival, where badges grant free reign to meet the major smithing clans.
- **Northfurrow District** — A district of Gracklstugh containing Clan Ironhead's Compound, where the party can meet laird Thangus Ironhead and his granddaughter Grinta.
- **Southfurrow District** — District named among Gracklstugh's places of interest in this supplement's table of contents; no further description appears in this chunk.
- **West Cleft and East Cleft Districts** / **East Cleft** / **East Cleft District** / **East Cleft district** / **East Clefts** / **West Cleft** / **West Cleft District** / **West Cleft district** / **West Clefts** — Districts where Uskvil formerly resided and where Droki can be sought as a lead into the Whorlstone Tunnels; also a target of Horgar's derro purge.

### Gracklstugh Landmarks

- **Blade Bazaar** — Darklake District marketplace selling weapons, armor, shields, and Darklake Stout; hub for smithing-order clan politics and Droki sightings.
- **Cairngorm Cavern** — Duergar clan compound named in this supplement's table of contents as part of the Spoils of War appendix; no further description appears in this chunk.
- **City Gates** — Gracklstugh's main land entrance, where the Stone Guard question and inspect the goods of arriving traders.
- **Darklake Brewery** — Location within the Darklake District named in this supplement's table of contents; no further description appears in this chunk.
- **Darklake Docks** — Docks where Werz Saltbaron is attacked by the Empty-Scabbard Killers and rescued by the party; garbage collectors and laborers gather here.
- **Furrow Gates** — Location within the Darklake District named in this supplement's table of contents; no further description appears in this chunk.
- **Gracklstugh** / **the city** — City whose rumors include the Deepking's crackdowns, murders, rats, Stone Guard corruption, and the Whorlstone Tunnels; home to the Gray Ghosts guild.
- **Halls of Sacred Spells** / **Halls of Sacred Stones** — A derro worship site accessed via magic or a hidden entrance tunnel in the West Cleft District; hostile derro and neutral derro savants dwell within.
- **Keepers of the Flame Headquarters** / **Keepers of the Flame Barracks** / **Themberchaud's Lair** — Base of the Keepers of the Flame faction in Flowstone District, where Gartokkar Xundom and Themberchaud the Wyrmsmith can be met.
- **Overlake Hold** — Large prison-and-guard-station, mistakenly described in the book as the Deepking's temple home; Captain Errde Blackskull meets the party here.
- **The Darklake** / **Darklake** — The underground lake by which the party can enter Gracklstugh, an alternative to entering the city by land.
- **The Ghohlbrorn's Lair** — Location within the Darklake District named in this supplement's table of contents; no further description appears in this chunk.
- **The Hold of the Deepking** / **Hold of the Deepking** — Location further within the city where the book alternately places the Deepking's temple home, contradicting Overlake Hold's description.
- **The Royal Vault** / **Royal Vault** — Deepking's five-chambered vault beneath his throne, guarded by locks, symbol spells, and mass suggestion compelling intruders to surrender.
- **The Shattered Spire** — Location where Werz Saltbaron later meets the party, thanks them, and opens Kazook Pickshine's bag of holding to extract trade gems.

### Beyond Gracklstugh

- **Blingdenstone** — Deep gnome city sending the party as trade emissaries to Gracklstugh, preparing for the Battle of Blingdenstone against the Pudding King.
- **Cyrog's Chamber** — Chamber where Orcus appeared, scattering the few surviving illithids who fled, one of whom later became Qualux.
- **Mantol Derith** — Trading post where Kazook Pickshine has been illicitly trading with the duergar smuggler Werz Saltbaron.
- **Nine Hells** — Plane where Brimtongue can hurl a struck foe for a minute; fiends may stay indefinitely, others appear before Asmodeus if it completes.
- **Pickshine Mines** — Mines belonging to Kazook Pickshine, source of the spell gems entrusted to the party's bag of holding.
- **Velkynvelve** — Drow outpost the author's party escaped from, slaying Ilvara and others only a few days before reaching Gracklstugh.
- **Whiteshell Mine** — Source of the Whiteshell Salt the party is transporting to trade in Gracklstugh, prized as the Underdark's fancy sea salt.
- **Wormwrithings** — Region the party has no need of a route to, since Ylsa's task reward is changed to Clan Henstak's favor.

## Creatures

- **Gorgthrax** — Name the stolen red dragon egg assumes on hatching; a demonically-influenced, two-headed wyrmling drawn to serve Demogorgon as a mount.
- **Grula-Munga** — The ettin among Narrak's guards and underlings defending the Cultist Hideout (Area 12).
- **Hydra** / **Area 9 Hydra** — Multi-headed guardian of Whorlstone Area 9's travel routes, listed among the tunnels' primary actors; hunts and attacks any group passing through, regardless of faction.
- **Zombies with Multiple Heads** — Multi-headed zombies reanimated from slain Empty-Scabbard Killers in Whorlstone Area 13, product of cult experiments to create hybrid warriors; mindless but aggressive.

## Items

- **Brimtongue** — Sentient legendary warhammer loyal to Asmodeus; can hurl a struck creature through the Nine Hells, wielded here by Deepking Horgar.
- **Council of Savants Letters** — Correspondence recovered in the Whorlstone Tunnels linking instructions from Narrak and Pliinki to the theft of the dragon egg and other disruptions.
- **Darklake Stout** — Beer brewed at the Darklake Brewery; can be purchased at the Blade Bazaar.
- **Dwarven Thrower** — A thrown warhammer Horgar wields, dealing bonus damage and extra damage against giants, that flies back to his hand after a ranged attack.
- **Eldgrim's Shield of Far Sight** / **shield of far sight** — Magical shield gifted to Eldgrim by Qualux, bearing an embedded derro eyeball through which Qualux can see and cast Mind Blast.
- **Empty-Scabbard Killers Hit List** / **Hit List** — Sealed parchment signed by Deepking Horgar found in Eldgrim's Whorlstone lair, naming assassination targets and proving the Deepking's direct ties to the killers.
- **Horgar's Cape of the Mountebank** / **Cape of the Mountebank** — Enhanced cape of the mountebank that gains bonus charges to cast dimension door when worn by a creature attuned to Brimtongue.
- **Horgar's Hit List** / **The Deepking's Hit List** — List of assassination targets written and signed by Deepking Horgar, found on Eldgrim's desk in Area 7.
- **Missing Red Dragon Egg** / **Missing Dragon Egg** / **Red Dragon Egg** / **Stolen Egg** / **red dragon egg** / **the egg** / **the missing dragon egg** / **the missing red dragon egg** — Red dragon egg stolen from the Keepers of the Flame by the Gray Ghosts, held in Whorlstone Area 14 as insurance against Themberchaud's future replacement.
- **Potion of Dragon's Breath** — Potion from Themberchaud's treasure hoard, given to the party to help deliver the killing blow against Horgar's daughter Olga.
- **The Binding of the Obelisk** — Open book in Narrak's Whorlstone lair detailing rituals to awaken the stolen dragon egg using Clan Thrazgad's acid-resistant ore.
- **Thrazgad Clan's Missing Ore** / **the ore** — Acid-resistant ore stolen from Clan Thrazgad by the Gray Ghosts, found useless for repairing the Whorlstone obelisk despite the cult's efforts.
- **Thrazgad Ore** / **Missing Ore** / **Missing Thrazgad Ore** — Stolen acid-resistant ore of the Thrazgad Clan, found in crates near the Obelisk where Pliinki failed to incorporate it.
- **Trident of the Lake** — +2 trident found in Vault 2 of the Royal Vault, granting water breathing and the ability to speak Aquan while attuned.

## Factions

### Duergar Clans

- **Clan Anvilthew** / **Clan Anvilthew (Toolmakers)** — Duergar toolmaker clan of 400 members in the central Southfurrow District, led by Einkil Anvilthew.
- **Clan Blackskull** / **Clan Blackskull (Stonemasons)** — Stonemason clan of 750 in the Darklake District, led by Adrik Blackskull; Errde Blackskull is his grandniece.
- **Clan Bukbukken** / **Clan Bukbukken (Farming)** — Duergar farming clan of 400 members in the west Northfurrow District, led by Gurdis Bukbukken.
- **Clan Burakrinwurn** / **Clan Burakrinwurn (Dock Operators)** — Duergar dock-operator clan of 270 members in the central Darklake District, led by Bruenor Burakrinwurn.
- **Clan Coalhewer** / **Clan Coalhewer (Coal Miners)** — Duergar coal-mining clan of 1,000 members in the east Northfurrow District, led by Delg Coalhewer.
- **Clan Firehand** / **Clan Firehand (Smelters)** — Duergar smelting clan of 900 members in the central Flowstone District, led by Gunnloda Firehand.
- **Clan Hammercane** / **Clan Hammercane (Construction Engineers)** — Duergar construction-engineer clan of 260 members in the central Southfurrow District, led by Riswynn Hammercane.
- **Clan Henstak** / **Clan Henstak (Food)** — Duergar clan whose favor Ylsa offers as a reward, granting advantage on social checks in one clan negotiation.
- **Clan Ironhead** / **Clan Ironhead (Weaponsmiths)** / **Clan Ironhead's Compound** / **Ironhead** / **Ironheads** — Weaponsmithing duergar clan forbidden from taking independent contracts by Horgar's edict, led by Thangus Ironhead and resented by his heirs like Grinta.
- **Clan Muzgardt** / **Clan Muzgardt (Brewers)** — Duergar brewing clan of 220 members in the east Darklake District, led by Kathra Muzgardt.
- **Clan Parlynsurk** / **Clan Parlynsurk (Clothing Manufacturers)** — Duergar clothing-manufacturer clan of 500 members in the mid-west Darklake District, led by Mardred Parlynsurk.
- **Clan Saltbaron** / **Clan Saltbaron (Salt Miners)** — Salt Miner clan of 330 in the Northfurrow District, led by Orsik Saltbaron; nephew Werz trades at Darklake Docks.
- **Clan Steelshadow** / **Clan Steelshadow (Weaponsmiths)** / **Steelshadow** / **Steelshadow Clan** / **Steelshadows** / **the Steelshadows** — Deepking Horgar's own duergar clan, the Weaponsmiths who hold Gracklstugh's smithing monopoly and receive Clan Ironhead's forced surplus work under his edict.
- **Clan Thordensonn** / **Clan Thordensonn (Jewelers)** — Duergar jeweler clan of 300 members in the west Flowstone District, led by Dagnal Thordensonn.
- **Clan Thrazgad** / **Clan Thrazgad (Armorsmiths)** / **Clan Thrazgad's Compound** / **Thrazgad** / **Thrazgad Clan** — Armorsmithing duergar clan led by Amber Thrazgad, whose acid-resistant ore was stolen by the Gray Ghosts and taken to the Whorlstone Tunnels.
- **Clan Thuldark** / **Clan Thuldark (Metalworks and Jewels)** — Duergar metalworking and jewel-crafting clan of 330 members in the west Flowstone District, led by Flint Thuldark.
- **Clan Xardelvar** / **Clan Xardelvar (Gas Miners)** — Gas Miner duergar clan of 380 members in the west Flowstone District, led by Vondal Xardelvar; gains +5 in mass combat from Xarrorn reinforcements.
- **Clan Xornbane** / **Clan Xornbane (Scouts and Prospectors)** — Duergar scout and prospector clan of 300 members in the northwest Darklake District, led by Audhild Xornbane.
- **Clan Xundom** / **Clan Xundom (Steeder Breeders)** — Steeder Breeder duergar clan of 360 members in the west Flowstone District, led by Baern Xundom, brother of Gartokkar Xundom who leads the Keepers of the Flame.

### Military Corps

- **Darkhafts** — One of Gracklstugh's four duergar military corps, sharing roughly 500 troops with Kavalrachni and Xarrorn beyond the 500-strong Stone Guard.
- **Kavalrachni** / **Kavalrahcni** — One of Gracklstugh's four duergar military corps (~200-500 troops), alongside Darkhafts and Xarrorn beyond the 500-strong Stone Guard; reinforces Clan Xundom in mass combat.
- **The Stone Guard** / **Stone Guard** / **Stone Guards** — Duergar military corps of 500 serving the Deepking, patrolling Gracklstugh and guarding the Hold and Overlake Hold under Errde Blackskull.
- **Xarrorn** / **Xarrorns** — One of Gracklstugh's four duergar military corps (~200-500 troops), alongside Darkhafts and Kavalrachni beyond the 500-strong Stone Guard; reinforces Clan Xardelvar in mass combat.

### Governing Bodies

- **Council of Lairds** — Duergar assembly of clan heads where grievances such as Horgar's edicts and hit-list evidence can be raised, potentially triggering civil war.
- **Council of Savants** / **The Council** / **the Council** — Thirty-six-member derro governing body; five members (Narrak, Pliinki, Uskvil, Aliinka, Zubriska) are secretly cult leaders who have won over the rest.

### Cults & Criminal Factions

- **Cult of Demogorgon** / **Narrak's cult** / **the cult** — Derro-led cult worshiping Demogorgon that has infiltrated the Council of Savants and the Gray Ghosts, hoping to summon the demon prince to Gracklstugh.
- **Cult of Orcus** — Necromantic cult foretold to arise from Whorlstone corpses stuffed there if Horgar's derro purge succeeds, fueled by the fallen dead as fodder.
- **Empty-Scabbard Killers** — Loose band of psionic duergar-outcast assassins, secretly overtaken by the mind flayer Qualux; the Deepking uses them to eliminate political and economic rivals.
- **Gray Ghosts** / **The Gray Ghosts** — Thieves' guild founded by three Council of Savants members (Uskvil, Aliinka, Zubriska), secretly serving Narrak's cult; stole the dragon egg and the Thrazgad ore.

### Other Factions

- **Cairngorm Clan** / **Clan Cairngorm** — Clan led by Stonespeaker Hgraam, sworn to the Steelshadows; worried a derro conflict could bring great losses given their territory's proximity.
- **The Keepers of the Flame** / **Keepers of the Flame** — Order loyal to Clan Steelshadow and the Deepking that keeps Themberchaud placated; at war with the Gray Ghosts over the stolen dragon egg.

## Events / concepts

- **Assassins Interrupted** — Encounter (OOTA 62) at the Darklake Docks, triggered when characters arrive unescorted; begins as the party spots Werz.
- **Bar Fight** — Named encounter at the Shattered Spire, referenced only as "See 'Bar Fight' (OOTA 63)."
- **Battle of Blingdenstone** — Upcoming battle for which Blingdenstone's deep gnomes sent the party to Gracklstugh seeking acid-resistant weapons and armor.
- **Chapter 4 - Insurrection!(?)** / **Insurrection** — A future chapter referenced as a forward pointer; the Keepers of the Flame's and Gray Ghosts' reactions to the party's discoveries carry into it.
- **Deep Gnome Merchant** — Named encounter suggested to highlight Gracklstugh's booming trade and the duergar's slaving practices.
- **Drow Pursuit** — Rules for being chased by drow after escaping Velkynvelve; this supplement ignores them since the author's party had already finished that pursuit.
- **Duergar Patrol** — Random patrol of 1d4+2 duergar, all but two invisible; badges of rank from Gartokkar or Errde end encounters peaceably.
- **Merchant Madness** — Named encounter referenced from the original book (OOTA 61); no further detail is given in this supplement.
- **Orc Mercenaries** — Named encounter suggested to highlight Gracklstugh's booming trade and the duergar's slaving practices.
- **Pliinki's Experiments** — Appendix A section detailing the stolen red dragon egg's fate: if not destroyed it hatches into Gorgthrax, a two-headed wyrmling drawn to Demogorgon.
- **Rampaging Giant Encounter** / **Rampaging Giant** — Encounter with the mutated, rampaging Rihuud that draws Keeper-of-the-Flame Gartokkar's attention to the party during their time in Gracklstugh.
- **Rumor Mill** — Named rumor-gathering encounter at the Ghohlbrorn's Lair referenced from the original book (OOTA 64).
- **Slave Caravan** — Recurring named encounter suggested to highlight that Gracklstugh's duergar are slavers.
- **The Downward Spiral** — Prior campaign-book chapter (OOTA 55) describing the madness and corruption spreading through Gracklstugh, expanded here via the Council of Savants' cult infiltration.

## Other / uncategorized

- **Appendix B** / **Duergar Clans, Military, and Other Factions** — Book appendix with bare-bones details on each of the nineteen duergar clans, their numbers, industries, and feelings toward key events.
- **Demogorgonic Abomination** — New creature race introduced in this supplement's Appendix E; only its title appears in this front-matter chunk, with no further description given here.
- **Grackle-lung** — Disease risked by visitors to Gracklstugh's smoke and haze; DC 11 CON save each long rest or gain exhaustion.
- **One Who Watches** — Mysterious figure named in a Whorlstone note claiming the stolen dragon egg is meant for it, not Narrak; identity unrevealed in this chunk.
