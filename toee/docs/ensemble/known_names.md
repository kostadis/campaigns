# ToEE known-named entities (for facts_to_state --known-names)

Curated from proper_nouns_adventure.md CLEAN sections + PCs.
Excludes the heuristic-noisy Places section and all Creatures (kept location-scoped).
Bold spans are what load_known_names reads.

2026-07-04: reclaimed 9 real NPCs that the extraction heuristic had misfiled into
the noisy Places section (Jaroo, Skole, Captain Tolub confirmed against corpus
fact counts; Commander Hedrack, Prince Thrommel, Furnok of Ferd, Grud Squinteye,
Mother Screng, Smigmal Redhand pre-staged, not yet seen in play).

2026-07-04: facts_to_state.py now treats every npc-typed subject as known by
default (see CampaignGenerator docs/cli/fact-to-state-data-files.md) — named
NPCs no longer need curating here at all. This file's NPC section is now only
for **overrides**: Airgid and Snej are added because their names also show up
as type=="monster" facts elsewhere in the corpus (Airgid is unmasked as a
silver dragon; Snej apparently fights under a monster stat block), which
would otherwise wrongly auto-exclude them. See docs/ensemble/exclude_names.md
for the opposite override (generic role-phrases forced anonymous).

## Player Characters

- **Zephyr**
- **Sequoia**
- **Zinnia**
- **Calmer**

## Deities & Divine Powers (17)

- **Boccob**
- **Ehlonna**
- **Erythnul**
- **Heironeous**
- **Hextor**
- **Iuz**
- **Lolth**
- **Nerull**
- **Obad-Hai**
- **Olidammara**
- **Orcus**
- **Pelor**
- **Pholtus**
- **St. Cuthbert**
- **Tharizdun**
- **Wee Jas**
- **Zuggtmoy**

## NPCs (named in module + cross-referenced with docs/npcs/) (20)

- **Airgid**
- **Captain Tolub**
- **Commander Hedrack**
- **Dala**
- **Dick Rentsch**
- **Elmo**
- **Furnok of Ferd**
- **Grud Squinteye**
- **Hartsch**
- **Jaroo**
- **Kelno**
- **Mother Screng**
- **Pearl**
- **Prince Thrommel**
- **Romag**
- **Rufus**
- **Skole**
- **Smigmal Redhand**
- **Snej**
- **Wat**

## Named Magic Items (1)

- **Orb of Golden Death**

## Named Locations

- **Hommlet**
- **Nulb**
- **Sheernobb**
- **Kron Hills**
- **Gnarley Forest**
- **Greenway Valley**
- **Lotrimil mountains**
- **Emiry Meadows**
- **Bronze Wood Glade**
- **Moathouse**
- **Temple of Elemental Evil**
- **Burne and Rufus's tower interior**
- **Water Temple**
- **Air Temple**
- **Earth Temple**
- **Fire Temple**
- **Hall of Trophies and Elemental Strife**
- **Hall of the Scarlet Moon**
- **Labyrinthine Library**
- **Abbey of Allitur**
- **Abbey of Beory**
- **Temple of St. Cuthbert**
- **Church of St. Cuthbert**
- **Inn of the Welcome Wench**
- **Honey Haven Tavern**
- **Boatman’s Tavern**
- **The Cheap Forester**
- **Waterside Hostel**
- **Moot Hall**
- **Sheernobb Moothall**
- **Drowned Cottage**
- **Iron Lash**
- **Nulb Stables**
- **Rhennee Encampment**
- **Boatwright**
- **Gallows Corner**
- **Gallows Square**
- **Pasmarie’s Beehives**
- **Elder Kenter’s compound**
- **Jaroo's grove**
