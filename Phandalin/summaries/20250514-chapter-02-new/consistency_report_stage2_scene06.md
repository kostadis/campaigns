- **Location**: Verbatim moments / provisioning; Scene summary; The Day’s March
  - **Issue**: The recap leaves three Goodberry-preparation lines attributed to **UNKNOWN**, even though they describe Soma changing her prepared spells. This makes the speaker identity unnecessarily ambiguous.
  - **Evidence**: Soma is the party’s druid, and the surrounding exchange has her checking the druid spell list. Both `session-summary.md` and `gm-assist.md` attribute the preparation decision to Soma.
  - **Suggested fix**: Attribute “Okay, I could prepare Goodberries” and “I’ll take off… Longstrider” to **Soma**; treat “Oh, good” as Soma if the audio supports it, otherwise retain UNKNOWN for that line alone.

- **Location**: Verbatim moments / map discussion
  - **Issue**: “So let’s go to Icespire Peak” could misleadingly imply that the party’s destination was Icespire Peak rather than the Dwarven Excavation.
  - **Evidence**: AUTHORITATIVE CANON identifies the **Dwarven Excavation** as an ancient settlement 15 miles southwest of Phandalin. The transcript’s subsequent map correction distinguishes the Dwarven Prospectors from the Rock Gnomes, and the party arrives at the excavation—not Icespire Peak.
  - **Suggested fix**: Add a note that this was the GM navigating the regional/Icespire map, not declaring Icespire Peak as the destination.

- **Location**: Verbatim moments throughout
  - **Issue**: Speaker labels inconsistently mix player names and character names, which can obscure who acted or spoke in-world.
  - **Evidence**: `party.md` identifies Wade Brown as Soma’s player, David Mendenhall as Vukradin’s, and Gary Young as Valphine’s for this session; Gary also voiced Brewbarry. Examples include “Wade Brown” for Soma’s map calculation, “Gary Young” for Valphine’s provisioning question, and “Kostadis Roussos” for GM speech.
  - **Suggested fix**: Normalize in-character speech to **Soma**, **Vukradin**, **Valphine**, and **GM** where attribution is clear; retain player names only for table talk or genuinely ambiguous dual-PC lines.

- **Location**: Verbatim moments / provisioning
  - **Issue**: “Valphine Sotorra: Well, at least we have a good look” is a questionable ASR rendering and has no clear meaning in context.
  - **Evidence**: The cleaned transcript contains the same phrase but does not resolve it; `vtt_transcription_corrections.md` provides no canonical correction. The exchange concerns foraging, Goodberry, and the risk that scavenged food or medicine could kill someone.
  - **Suggested fix**: Mark the phrase as unresolved ASR rather than presenting it as reliable verbatim dialogue.

- **Location**: Verbatim moments / arrival
  - **Issue**: Vukradin’s line “There’s no charge around here” is retained despite being an acknowledged garble and may be mistaken for a factual observation.
  - **Evidence**: The cleaned transcript contains the phrase immediately after the GM says nothing unusual happened during the journey; no “charge” is established anywhere in the scene or context.
  - **Suggested fix**: Replace the quotation with `[unclear]` or annotate that it likely responds to the uneventful journey and should not be treated as canon.

- **Location**: Scene summary; The Day’s March
  - **Issue**: “Soma’s shortcut proposal … dies on Vukradin’s honesty” slightly overstates the resolution because Vukradin immediately adds, “Although you do have a point.”
  - **Evidence**: The quoted sequence is: Vukradin calls the proposal dishonest, Soma concedes, then Vukradin acknowledges that she has a point before Soma rejects the shortcut herself on ethical grounds.
  - **Suggested fix**: Say the proposal is abandoned after Vukradin raises the dishonesty and Soma reaffirms her own “heal the land” ethic.