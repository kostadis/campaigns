# Chapter 52 — recap-removal audit

Date: 2026-09-12
Status: **No recap cut proposed in the current derived documents.**

## Scope and result

Stage 0 and Stage 1 human review are complete. No scene extractions, plan, or narration exist for this session. Reviewed the first scene and Summary in session-summary.md, the source gm-assist.md opening, the recording opening, and the previous session's session-summary.md and session_doc.md in ../20260902.

All three relevant surfaces already start with this session's live tavern encounter:
- Scene list: “The House of a Thousand Faces”; Brewbarry examines the coat and the bartender greets the party.
- Summary prose: opens on the same coat-and-greeting encounter, not the earlier dead-drop investigation.
- Narration framing source: session-summary.md is that same enhanced-summary file, not a separate copy.

The short arrival bridge overlaps the previous chapter's stopping location, but the coat interaction and bartender exchange occur in this recording around 00:22:56 onward. It is scene setup, not a replay of the preceding chapter's investigation. The prior chapter ends with Brewbarry entering; current play has the others deciding to follow him.

**Nothing cut. No files deleted, scenes renumbered, or downstream jobs launched. No VTT or verbatim extraction changed.** No new boundary or rescue destination has been imposed.

## Detection

find_recap.py on session-summary.md returns: no '## Voiced moments' section. **Score unavailable / NOT RUN**, not 0/6. notes/scrub_register_policy.md explicitly records this format limitation and directs a manual three-surface check.

Manual source markers:
- Cleaned VTT 00:16:34: “So when we last left our noble adventurers…”
- 00:18:01: “And so the last thing that happened was that you arrived…”
- 00:21:32: reminder about Soma's familiar in the hole and the Harper documents.
- Around 00:22:05: “So do you guys follow Brewbarry or do you guys stay outside?” followed by player decisions.
- Around 00:22:56: Brewbarry examines the soft coat, followed by the bartender greeting.

These timestamps describe evidence windows, not approved extraction cut boundaries. The pre-00:16:34 recording is social/technical chatter. No such chatter is present in the current summary opening.

## Rescue check

Ran recap_unique.py on an exact diagnostic copy of the enhanced summary's first scene (/tmp/20260908-opening-scene-audit.md), against ../20260902/session-summary.md and ../20260902/session_doc.md (15,507 words).

Tool results: no formatted GM asides, no bookkeeping bullets, no low proper-noun coverage flags. **This is not proof of redundancy**: the same characters and location occur in both chapters. The actual scene content is new live play, as verified above. Raw VTT asides are not formatted annotations and required separate reading.

### GM doctrine explanation — already preserved outside chapter prose

The opening includes a substantial out-of-character explanation, not merely prior-session recap:
- concentrated personal power versus diffuse control through armies;
- Harper opposition to lasting governmental control;
- nature as diffuse power and consequent opposition to naturalists;
- Zhentarim economic control concentrated in a few hands;
- Harpers pursuing freedom rather than simply being good or evil.

Existing destination: ../../notes/neverwinter/harper_doctrine.md, especially “The governing objective,” “Why they hate the Zhentarim,” and “Soma's progression and Lim's outdated understanding.” This note already records these GM rulings. No new canon write or relocation is needed. The transcript's more sweeping spoken shorthand must not silently replace that note's explicit distinction about centralized diffuse power.

The full opening-window dialogue is preserved below so every GM aside, including the opening moral-character jokes and doctrine discussion, remains inspectable. No aside is being deleted from its source.

### Current-chapter bookkeeping

No level-up, gained spell, subclass, or rest was announced in the manually inspected opening through the party's decision to enter. The later confirmed long rest and ability review already remain at session-summary.md:253. Do not remove that later live-state bookkeeping as “recap.”

### Previous-chapter coverage and gaps

The actual repeated beats—Brewbarry entering the House, Soma's familiar passing through the wall/dead drop, and discovery of the Harper office—are present in ../20260902/session-summary.md (Summary and final scene; familiar and Harper discovery around lines 265–275, and Find Familiar/Knock entries). No missing upstream story beat established.

The new explanation of faction doctrine is campaign grounding, not an event to retroactively insert into Chapter 51. It is already preserved in the doctrine note. No upstream repair proposed.

## Policy and next step

Existing campaign policy already says to omit resolved prior-chapter retellings and preceding unrelated chatter, while preserving live-state resumes and bookkeeping. No new standing ruling or policy edit needed.

Recommendation: leave the current first scene and Summary intact. A future scene extraction must still be reviewed for accidental reintroduction of the recording's opening recap; no automated boundary has been authorized here.

## Separate repair of an already-approved edit

During this audit, discovered that the earlier Stage 1 patch had attached the GM speaker label to the bargaining quote instead of the one-egg joke. Corrected the application to match the approved s1-02 decision: bargaining quote is Vukradin; one-egg joke is “GM, joking in the Rift Weaver Prime's voice.” Quote text unchanged. This is not a recap-removal edit.

## Verbatim opening-window evidence

Source: GMT20260909-040128_Recording.transcript.vtt, original speaker labels and wording. Window 00:16:34–00:23:25, chosen for inspection only. ASR spellings here are preserved, not new canon. Includes every GM aside in that window and surrounding player responses.

### 00:16:39.300 --> 00:16:40.630

> Kostadis Roussos: And Soma, actually.

### 00:16:41.300 --> 00:16:42.479

> Wade Brown: Yeah, I'm not…

### 00:16:42.480 --> 00:16:44.190

> David Mendenhall: Someone's doing pretty well.

### 00:16:44.190 --> 00:16:46.790

> Kostadis Roussos: Yeah, and Soma, that's at Bukradin and Soma, yes?

### 00:16:47.400 --> 00:16:48.810

> Wade Brown: She's not greedy.

### 00:16:48.810 --> 00:16:54.840

> Kostadis Roussos: Oh, no, she's actually, she's actually moving the needle. She's, you know, she's… she's embraced…

### 00:16:54.980 --> 00:16:57.600

> Kostadis Roussos: Her inner goodness, right? Concern for the.

### 00:16:57.600 --> 00:17:00.460

> David Mendenhall: I mean, she's still pro-treasure, but, you know, nobody's.

### 00:17:00.460 --> 00:17:04.579

> Kostadis Roussos: I said, I said Vukradin and Sova.

### 00:17:05.050 --> 00:17:07.590

> Kostadis Roussos: They're good along different dimensions.

### 00:17:09.079 --> 00:17:11.159

> Wade Brown: Moral relativism.

### 00:17:11.589 --> 00:17:14.229

> Gary Young: Y'all need to get on any dimensions, maybe?

### 00:17:15.420 --> 00:17:19.629

> Kostadis Roussos: Valfine is currently offering people options.

### 00:17:19.819 --> 00:17:24.629

> Wade Brown: Rouss are just inherently evil, don't you know that? Like, all… in all of Kostadis' campaigns, Drous are just…

### 00:17:24.630 --> 00:17:29.810

> David Mendenhall: You say that you support Lathander, on the other hand, Lathander is dead. But, you know…

### 00:17:29.810 --> 00:17:32.509

> Kostadis Roussos: No, no, no, this is, like, God is dead. This is the.

### 00:17:32.510 --> 00:17:37.779

> David Mendenhall: I know, I know, that is one… I know the Nietzsche angle, I thought of all the angles.

### 00:17:37.780 --> 00:17:38.600

> Kostadis Roussos: He's…

### 00:17:38.600 --> 00:17:40.020

> Wade Brown: Get ahead of you, man.

### 00:17:40.050 --> 00:17:46.680

> Kostadis Roussos: I know that. I'm aware. I'm aware. Yes, alright. So, let's see here, roll 20…

### 00:17:48.090 --> 00:17:50.289

> Kostadis Roussos: Okay, let me get to my roommate.

### 00:18:01.170 --> 00:18:07.549

> Kostadis Roussos: And… So, the last thing that happened was that you arrived at the Tavern of the Thousand Faces.

### 00:18:07.550 --> 00:18:10.469

> Wade Brown: Oh, right, we were poking our holes through the wall. Right.

### 00:18:10.470 --> 00:18:16.949

> Kostadis Roussos: And Brewberry had gone in, and you guys knew that inside the tavern, was,

### 00:18:17.200 --> 00:18:20.150

> Kostadis Roussos: what's his name? Was a Harp… was a Harper hangout.

### 00:18:20.350 --> 00:18:21.290

> Wade Brown: Yeah.

### 00:18:23.220 --> 00:18:26.519

> Kostadis Roussos: That's the, critical, detail.

### 00:18:28.280 --> 00:18:30.689

> Wade Brown: And somehow you think Harpers are bad, so…

### 00:18:31.010 --> 00:18:38.020

> Kostadis Roussos: No, okay, so I actually spent some time thinking about it, because I felt like, you know, I owed you guys better than Harper's Bad. So, I mean…

### 00:18:38.230 --> 00:18:42.070

> Kostadis Roussos: No, I mean, the only person I owed it to is myself, just to be clear.

### 00:18:43.640 --> 00:18:47.189

> Kostadis Roussos: I decided that the problem with, the… so the Harpers…

### 00:18:47.700 --> 00:18:57.000

> Kostadis Roussos: So, there's 3 levels of power in my campaign. There is concentrated power and diffused power. Diffuse power are armies that can occupy areas.

### 00:18:58.520 --> 00:19:03.540

> Kostadis Roussos: Concentrated power are, like, high-powered individuals, gods, etc, right?

### 00:19:03.910 --> 00:19:09.909

> Kostadis Roussos: So, any government has to have both assets for concentrated power and diffuse power.

### 00:19:10.140 --> 00:19:17.990

> Kostadis Roussos: Right? And you… and so, the Harpers believe that diffuse power is intrinsically evil, because it imposes control.

### 00:19:19.300 --> 00:19:21.660

> Kostadis Roussos: We didn't die. That's right, so there are.

### 00:19:21.660 --> 00:19:22.130

> Wade Brown: perspective.

### 00:19:22.130 --> 00:19:24.729

> Kostadis Roussos: Yeah, their perspective.

### 00:19:24.730 --> 00:19:25.869

> Gary Young: What did she say?

### 00:19:26.200 --> 00:19:28.610

> Wade Brown: He wants Dave to die.

### 00:19:29.170 --> 00:19:35.369

> Kostadis Roussos: No shit, nobody died. That's what she said. Nobody. God, immediately, you think the worst of people.

### 00:19:35.370 --> 00:19:36.330

> David Mendenhall: It's okay.

### 00:19:36.330 --> 00:19:38.460

> Wade Brown: She always wished Seth on Dave!

### 00:19:38.460 --> 00:19:40.000

> David Mendenhall: It's not the worst, it's just padded record.

### 00:19:40.000 --> 00:19:40.690

> Wade Brown: Meganism.

### 00:19:40.690 --> 00:19:42.989

> Kostadis Roussos: No, no, she says TPK. She's actually telling you.

### 00:19:42.990 --> 00:19:44.530

> David Mendenhall: She wants everybody to die.

### 00:19:44.530 --> 00:20:02.289

> Kostadis Roussos: She wants everybody… she wants me to be quiet, that's what she wants. All right, so the Harpers believe that diffuse power is intrinsically dangerous, and they're opposed to it. They believe that individuals with concentrated power are only the only guarantee of peace, because they can't control large numbers of people.

### 00:20:04.680 --> 00:20:23.329

> Kostadis Roussos: So they're opposed to governments for that reason. They're also opposed to the naturalists, because the naturalists believe, like, the most important diffuse power is nature. And they also hate the Zantarim, because the Zantarim believe that, no, no, concentrated power can rule, have diffuse power, as long as it uses other means, like economic power.

### 00:20:25.650 --> 00:20:26.389

> Gary Young: I kind of looks terrible.

### 00:20:26.390 --> 00:20:27.270

> Wade Brown: Pretty hypocritical.

### 00:20:27.960 --> 00:20:28.600

> Kostadis Roussos: What?

### 00:20:29.560 --> 00:20:31.880

> Gary Young: Economic power is also diffuse power.

### 00:20:32.390 --> 00:20:37.749

> Kostadis Roussos: Yes, yes, yes. But it can be concentrated in the hands of a small number of people.

### 00:20:38.420 --> 00:20:44.960

> Kostadis Roussos: That's why they hate the Zantarim. The Zantarim believe in concentrated… people with concentrated power having to fuse power through…

### 00:20:45.080 --> 00:20:45.640

> Kostadis Roussos: You know.

### 00:20:45.920 --> 00:20:49.699

> Wade Brown: So, the harbors are Bitcoin bros, is what I'm hearing.

### 00:20:49.700 --> 00:20:52.479

> Kostadis Roussos: Yeah, I guess so, you could call them that, right? But, but…

### 00:20:52.480 --> 00:20:54.180

> Wade Brown: Yeah, they're evil, we gotta kill them.

### 00:20:54.460 --> 00:21:00.019

> Kostadis Roussos: They're not evil. They're just… As they have a particular point of view.

### 00:21:00.490 --> 00:21:03.590

> Kostadis Roussos: That, you know, big government's bad.

### 00:21:05.380 --> 00:21:07.459

> Wade Brown: Yes, Bitcoin bro's gotta die.

### 00:21:07.730 --> 00:21:13.940

> Kostadis Roussos: Okay, this was not where I thought this was gonna go, but apparently I better roll up some character sheets.

### 00:21:17.330 --> 00:21:18.350

> Kostadis Roussos: Alright.

### 00:21:19.420 --> 00:21:21.110

> Kostadis Roussos: Let me see… okay.

### 00:21:31.180 --> 00:21:32.610

> Wade Brown: Excuse me.

### 00:21:32.610 --> 00:21:39.049

> Gary Young: So we had also taken, Wade's Familiar, Soma's Familiar, and shoved it in the hole.

### 00:21:39.460 --> 00:21:40.080

> Kostadis Roussos: Yes.

### 00:21:40.080 --> 00:21:45.869

> Wade Brown: It was relayed… it's what relayed back to us that there were Harper documents and stuff inside.

### 00:21:46.820 --> 00:21:47.520

> Kostadis Roussos: Yep.

### 00:21:48.070 --> 00:21:51.759

> Wade Brown: And Brubbery found ale inside at the front door, so there's that.

### 00:21:54.390 --> 00:21:54.940

> Gary Young: Yeah.

### 00:21:55.380 --> 00:21:59.009

> Gary Young: I guess we know where he's gonna be during this, this session.

### 00:21:59.320 --> 00:21:59.810

> Wade Brown: Oh, yeah.

### 00:21:59.810 --> 00:22:00.310

> Kostadis Roussos: Yes.

### 00:22:00.860 --> 00:22:08.139

> Kostadis Roussos: Okay, all right. So, is, so does Brewberry… so do you guys follow Brewery, or do you guys stay outside?

### 00:22:13.440 --> 00:22:14.160

> Wade Brown: I…

### 00:22:14.550 --> 00:22:15.970

> Gary Young: I'll go with brewberry.

### 00:22:16.210 --> 00:22:16.910

> Kostadis Roussos: Right.

### 00:22:16.910 --> 00:22:19.509

> David Mendenhall: Yeah… Let's go.

### 00:22:19.920 --> 00:22:22.779

> Wade Brown: Yeah, I mean, we know it's… we know it's in the back room, I guess.

### 00:22:22.990 --> 00:22:25.890

> Wade Brown: Doesn't really tell us much to stay outside anymore.

### 00:22:25.890 --> 00:22:27.350

> Kostadis Roussos: Okay. Interesting. Okay.

### 00:22:28.920 --> 00:22:33.929

> Kostadis Roussos: So for various inside, he's wearing one of his, prototypes,

### 00:22:33.930 --> 00:22:34.280

> Wade Brown: For sure.

### 00:22:36.410 --> 00:22:40.830

> David Mendenhall: You guys want me to… find the room stealthily?

### 00:22:43.260 --> 00:22:44.490

> Gary Young: You wanna do what again?

### 00:22:44.490 --> 00:22:53.069

> Kostadis Roussos: Well, hold on, let… just give you… give me a second to describe the scene, and then you can do whatever you want. Yes. Just give me a second, then you can…

### 00:22:55.400 --> 00:22:59.309

> Kostadis Roussos: He's staring at a mannequin, wearing a coat.

### 00:22:59.800 --> 00:23:04.190

> Kostadis Roussos: That's… and muttering, this is so… Soft.

### 00:23:06.710 --> 00:23:08.010

> David Mendenhall: Blueberry's doing this?

### 00:23:08.010 --> 00:23:13.740

> Kostadis Roussos: Yes, he's holding the lining of the coat, and is very impressed with the softness of the lining.

### 00:23:15.330 --> 00:23:16.989

> Wade Brown: Charmin would be proud.

### 00:23:16.990 --> 00:23:25.199

> Kostadis Roussos: Right, he's, he's, Lenain… he's thinking… he's wanting to know where that came from.
