# Voice fixes — session 20260902

Review: `voice-critic:20260902:20260907-r1`

Decision record: `decisions.json`, saved `2026-09-07 00:13 UTC`.

## Result

All seven findings were approved. Eighteen frozen target spans were applied to
six files: the raw and scrubbed forms of scenes 03, 04, and 05. Scenes 01 and 02
were unchanged. Locked dialogue was preserved, including the raw `Colorado` and
scrubbed `Daggerford` variants in scene 04.

| Finding | Status | Destinations |
|---|---|---|
| VC-001 | applied | raw + scrubbed scene 03 |
| VC-002 | applied | raw + scrubbed scene 04 |
| VC-003 | applied | raw + scrubbed scene 04 |
| VC-004 | applied | raw + scrubbed scene 04 |
| VC-005 | applied | raw + scrubbed scene 05 |
| VC-006 | applied | raw + scrubbed scene 05 |
| VC-007 | applied | raw + scrubbed scene 05 |

## Hash ledger

| File | Original SHA-256 | Result SHA-256 |
|---|---|---|
| scene 03 raw | `ebea9b4ad55a20bc6471e5159ebe7c19267dd6371f7fdce4596ac39b8d0c1968` | `eed2f6da61d28fed0bcc1f8f1fa24040b71976b9cc9a5dfab352f60a0735f3c8` |
| scene 03 scrubbed | `aa437191ee80b821819d1925343b2c393a5bc2a47901e7eac023f6458ced4a30` | `c20e0bd316e0e1f80c4bc65bda11a672430751e261de8d6bf89f7d2d5f9ceb99` |
| scene 04 raw | `60b2669c0ef593a6112ae80181d931e88a96beb762e6896580b3a58cca51833b` | `dfa148c54d86b3af5cf1c02b745843588b79847d55d352ce1871074f45cb7769` |
| scene 04 scrubbed | `2f5a1d8d90fe475e0113b4f92bc7d1ba13581d62ecaaea8f1f955ec8bdc473e5` | `121da991d24f13d0af366098d65434287d9567e78db70f93b5994a2068a754db` |
| scene 05 raw | `d51155477a5dd3e8a0634fd0cf6daeaac17a66ba951dfdf87138bba65107b6ac` | `df077e7fd3912f2fb40c2958fde73a05e0dfe78c414abfba111f5472e4dea13d` |
| scene 05 scrubbed | `956549deaabba80480f9f4ac6821c5a6fadebdd545d5ba1cdae95fc1a4ad5de5` | `1d0c7385d9d8cd58efd9bde6903d37469e414095f59293430dbc8b5e6dba3aa0` |

## Before and after

- Vukradin abstract balanced closers: 4 → 1 (cap 1).
- Soma abstract balanced closers: 2 → 1 (cap 1).
- Selected-corpus prose words: 5,922 → 5,850.
- Dialogue words: 3,705 → 3,705.
- Installed lint: 0 errors / 0 warnings before and after. The unchanged config
  note says `extra_tics` is ignored; those families remain not mechanically checked.

Affected paragraphs and joins were reread. No stranded grammar, chronology change,
or lost attribution was found. Collision review found `My jaw tightens` in an
excluded alternate scene 05 render, also narrated by Soma; it does not collide
across narrators or within the effective selected corpus.
