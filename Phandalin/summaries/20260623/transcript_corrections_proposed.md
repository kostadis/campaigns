# Proposed transcript corrections — ch46 (20260623)

**Not applied.** These are proposals, from CampaignGenerator #250 R1/R3 refusals.
Each one is a place where the *extraction* repaired a word and the *tape* still
carries the garble. R2 says the tape owns the defect — but which word was really
spoken is a judgement about your table, not something a tool should decide.

Approve one by moving its YAML block into `transcript_corrections.yaml`, setting
`verified: true`, then `sd_corrections apply --dir .`. Reject one by deleting it
here. Where the tape is genuinely unclear, **leaving it garbled is the right answer**
— that is what `[inaudible]` is for, and guessing writes fiction into ground truth.

16 proposal(s) covering 15 cues. **Cue 1211 appears twice** — it is both an R1
conflict and an R3 bracket, the intersection the contract doc predicted. The record
refuses two entries on one cue (which would win depends on file order), so merge
them into a single entry whose `now` is the final text.

## cue 224 — R1 (01_return_to_phandalin.md:97)

- **tape** (Gary Young): `I mean, the town has been protected by the strength of the pandemic.`
- **extraction reads**: `The town has been protected by the strength of Lathander.`
- **difference**: neither copy is verbatim (`## Scene summary` near, `## Verbatim moments` near)
- **similarity**: 0.86

```yaml
- id: cue-0224-r1
  cue: 224
  was: 'I mean, the town has been protected by the strength of the pandemic.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R1 refusal at 01_return_to_phandalin.md:97; unconfirmed
```

## cue 245 — R1 (01_return_to_phandalin.md:113)

- **tape** (Stéphane Bourdeaud): `Yeah, but blood can be turned into something soft and wonderful, you know, like a Brewbarry bathroom.`
- **extraction reads**: `Yeah, but blood can be turned into something soft and wonderful, like a Brewbarry bathrobe.`
- **difference**: neither copy is verbatim (`## Scene summary` near, `## Verbatim moments` near)
- **similarity**: 0.93

```yaml
- id: cue-0245-r1
  cue: 245
  was: 'Yeah, but blood can be turned into something soft and wonderful, you know, like a Brewbarry bathroom.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R1 refusal at 01_return_to_phandalin.md:113; unconfirmed
```

## cue 299 — R3 (02_a_hero_s_welcome_at_stonehill_inn.md:92)

- **tape** (David Mendenhall): `We had to kill a dragon, we had to stop an orcan game, I'll see the whole way.`
- **extraction reads**: `We had to kill a dragon, we had to stop an orc campaign, [inaudible — probable "I'll fill you in the whole way"].`
- **difference**: [inaudible — probable "I'll fill you in the whole way"]
- **similarity**: 0.79

```yaml
- id: cue-0299-r3
  cue: 299
  was: "We had to kill a dragon, we had to stop an orcan game, I'll see the whole way."
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 02_a_hero_s_welcome_at_stonehill_inn.md:92; unconfirmed
```

## cue 304 — R3 (02_a_hero_s_welcome_at_stonehill_inn.md:97)

- **tape** (Stéphane Bourdeaud): `Who owns it at Mermaid Steph?`
- **extraction reads**: `Who owns it? [inaudible — probable "It's a mermaid, Steph(ane)"]`
- **difference**: [inaudible — probable "It's a mermaid, Steph(ane)"]
- **similarity**: 0.92

```yaml
- id: cue-0304-r3
  cue: 304
  was: 'Who owns it at Mermaid Steph?'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 02_a_hero_s_welcome_at_stonehill_inn.md:97; unconfirmed
```

## cue 324 — R3 (02_a_hero_s_welcome_at_stonehill_inn.md:142)

- **tape** (Gary Young): `Well, yes, that's our next system.`
- **extraction reads**: `Well, yes, that's our next [stop].`
- **difference**: [stop]
- **similarity**: 0.96

```yaml
- id: cue-0324-r3
  cue: 324
  was: "Well, yes, that's our next system."
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 02_a_hero_s_welcome_at_stonehill_inn.md:142; unconfirmed
```

## cue 672 — R3 (03_the_universal_basic_treasure_proclamation.md:437)

- **tape** (Wade Brown): `Place the socks go in the dryer.`
- **extraction reads**: `[Same place the] socks go in the dryer.`
- **difference**: [Same place the]
- **similarity**: 1.0

```yaml
- id: cue-0672-r3
  cue: 672
  was: 'Place the socks go in the dryer.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 03_the_universal_basic_treasure_proclamation.md:437; unconfirmed
```

## cue 729 — R3 (04_cheese_business_plans_and_departure_preparations.md:69)

- **tape** (Kostadis Roussos): `Okay, so, and those, and you inform them who they are, those Elaine, the… yeah, alright, alright. Well, then we will absolutely keep them a fine round of our finest cheese, and she, and then she goes, Mr. Brewbarry.`
- **extraction reads**: `Okay, so, and those, and you inform them who they are, [those are Brin and Giles], the… yeah, alright, alright. Well, then we will absolutely keep them a fine round of our finest cheese, and she, and then she goes, Mr. Brewbarry.`
- **difference**: [those are Brin and Giles]
- **similarity**: 0.97

```yaml
- id: cue-0729-r3
  cue: 729
  was: 'Okay, so, and those, and you inform them who they are, those Elaine, the… yeah, alright, alright. Well, then we will absolutely keep them a fine round of our finest cheese, and she, and then she goes, Mr. Brewbarry.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 04_cheese_business_plans_and_departure_preparations.md:69; unconfirmed
```

## cue 747 — R3 (04_cheese_business_plans_and_departure_preparations.md:107)

- **tape** (Stéphane Bourdeaud): `Don't underestimate the power of Gucci's on, you know, the good people.`
- **extraction reads**: `Don't underestimate the power of [the good stuff on] the good people.`
- **difference**: [the good stuff on]
- **similarity**: 0.82

```yaml
- id: cue-0747-r3
  cue: 747
  was: "Don't underestimate the power of Gucci's on, you know, the good people."
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 04_cheese_business_plans_and_departure_preparations.md:107; unconfirmed
```

## cue 781 — R3 (04_cheese_business_plans_and_departure_preparations.md:183)

- **tape** (Stéphane Bourdeaud): `And, and a, you know, a little but, you know, readable.`
- **extraction reads**: `And a little [blurb], readable.`
- **difference**: [blurb]
- **similarity**: 0.61

```yaml
- id: cue-0781-r3
  cue: 781
  was: 'And, and a, you know, a little but, you know, readable.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 04_cheese_business_plans_and_departure_preparations.md:183; unconfirmed
```

## cue 831 — R3 (04_cheese_business_plans_and_departure_preparations.md:281)

- **tape** (Kostadis Roussos): `It literally goes, Shalim Lenny goes, Brewbarry.`
- **extraction reads**: `It literally goes, [so] Linene goes, Brewbarry.`
- **difference**: [so]
- **similarity**: 0.89

```yaml
- id: cue-0831-r3
  cue: 831
  was: 'It literally goes, Shalim Lenny goes, Brewbarry.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 04_cheese_business_plans_and_departure_preparations.md:281; unconfirmed
```

## cue 857 — R3 (04_cheese_business_plans_and_departure_preparations.md:319)

- **tape** (Kostadis Roussos): `That we're phasing in an.`
- **extraction reads**: `That were phasing in and [out].`
- **difference**: [out]
- **similarity**: 0.94

```yaml
- id: cue-0857-r3
  cue: 857
  was: "That we're phasing in an."
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 04_cheese_business_plans_and_departure_preparations.md:319; unconfirmed
```

## cue 1019 — R3 (05_arrival_in_neverwinter.md:108)

- **tape** (Kostadis Roussos): `Like, do you want to ask about it, or, like, Vugrid, you're, like, cut, or just keep moving on.`
- **extraction reads**: `Valphine, you immediately recognized the music. It was Vukradin's old music. Like, do you want to ask about it, or, like, Vukradin, you're, like, [continue?], or just keep moving on.`
- **difference**: [continue?]
- **similarity**: 0.68

```yaml
- id: cue-1019-r3
  cue: 1019
  was: "Like, do you want to ask about it, or, like, Vugrid, you're, like, cut, or just keep moving on."
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 05_arrival_in_neverwinter.md:108; unconfirmed
```

## cue 1106 — R3 (05_arrival_in_neverwinter.md:171)

- **tape** (Kostadis Roussos): `In honor of the liberators of the Orning, through whose courage and through the combined strength of the Lord's Alliance, the giant kingdoms were restored to order to north, and the secured.`
- **extraction reads**: `As you walk through the Protector's Enclave, mounted on a building, at eye level, is a carved stone plaque. In honor of the liberators of the Ordning, through whose courage and through the combined strength of the Lord's Alliance, the giant kingdoms were restored to order in the north, and [kept] secured. And then it says, beside it is a Lord's Alliance Herald in blue and gold livery distributing a broadsheet.`
- **difference**: [kept]
- **similarity**: 0.62

```yaml
- id: cue-1106-r3
  cue: 1106
  was: "In honor of the liberators of the Orning, through whose courage and through the combined strength of the Lord's Alliance, the giant kingdoms were restored to order to north, and the secured."
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 05_arrival_in_neverwinter.md:171; unconfirmed
```

## cue 1211 — R3 (06_the_exotic_armorer_of_neverwinter.md:154)

- **tape** (Stéphane Bourdeaud): `works for no one, but Brewbarry has much respect for the thunder, yes.`
- **extraction reads**: `Brewbarry works for no one, but Brewbarry has much respect for [Lathander], yes.`
- **difference**: [Lathander]
- **similarity**: 0.85

```yaml
- id: cue-1211-r3
  cue: 1211
  was: 'works for no one, but Brewbarry has much respect for the thunder, yes.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R3 refusal at 06_the_exotic_armorer_of_neverwinter.md:154; unconfirmed
```

## cue 1173 — R1 (06_the_exotic_armorer_of_neverwinter.md:50)

- **tape** (Kostadis Roussos): `Are you… are you the drow that Brother Aldrich speaks of? The one who converted to the blessed teachings of the Morning Lord?`
- **extraction reads**: `Are you… are you the drow that Brother Aldric speaks of? The one who converted to the blessed teachings of the Morning Lord?`
- **difference**: neither copy is verbatim (`## Scene summary` near, `## Verbatim moments` near)
- **similarity**: 1.0

```yaml
- id: cue-1173-r1
  cue: 1173
  was: 'Are you… are you the drow that Brother Aldrich speaks of? The one who converted to the blessed teachings of the Morning Lord?'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R1 refusal at 06_the_exotic_armorer_of_neverwinter.md:50; unconfirmed
```

## cue 1211 — R1 (06_the_exotic_armorer_of_neverwinter.md:154)

- **tape** (Stéphane Bourdeaud): `works for no one, but Brewbarry has much respect for the thunder, yes.`
- **extraction reads**: `Brewbarry works for no one, but Brewbarry has much respect for [Lathander], yes.`
- **difference**: neither copy is verbatim (`## Scene summary` near, `## Verbatim moments` unverified)
- **similarity**: 0.85

```yaml
- id: cue-1211-r1
  cue: 1211
  was: 'works for no one, but Brewbarry has much respect for the thunder, yes.'
  now: 'REPLACE ME - what was actually said'
  recorded: 2026-08-10
  verified: false
  note: proposed from a R1 refusal at 06_the_exotic_armorer_of_neverwinter.md:154; unconfirmed
```
