# Registry slug-only entries — report only, not edited

`docs/entity_inventory.md` is generated from `docs/entity_registry.yaml`.
These entries carry only a filename-derived slug and no readable display name, so the
spell pass cannot match the spoken form and every correctly-spelled mention orphans as
an unknown candidate. Measured cost this batch: `Orc Raider` (17 corpus occurrences),
`Orc Scout` (8) and `Orc Brigand` (3) pulled 7 distinct wrong-form families into
spurious clusters before they were added to the known set by hand.

Fix by adding a display name in `entity_registry.yaml`, then `registry.py project`.

| inventory line | slug | suggested display name |
|---|---|---|
| 552 | `aletra` | Aletra |
| 553 | `backes_dunfield` | Backes Dunfield |
| 555 | `cooragh_struckt` | Cooragh Struckt |
| 556 | `corbin` | Corbin |
| 557 | `daran_edermath_silverleaf` | Daran Edermath Silverleaf |
| 558 | `delaan_winterhound` | Delaan Winterhound |
| 561 | `elara` | Elara |
| 562 | `jarek` | Jarek |
| 563 | `jax` | Jax |
| 564 | `locutus` | Locutus |
| 566 | `lord_halueth_verres` | Lord Halueth Verres |
| 567 | `lyra` | Lyra |
| 568 | `marian` | Marian |
| 569 | `martisha_vinetalker` | Martisha Vinetalker |
| 570 | `out_of_phase_dwarves_axelholm_inhabitants` | Out of Phase Dwarves Axelholm Inhabitants |
| 571 | `qelline_alderleaf` | Qelline Alderleaf |
| 574 | `runa` | Runa |
| 575 | `skippy` | Skippy |
| 577 | `sridar` | Sridar |
| 579 | `teega_the_smith` | Teega the Smith |
| 580 | `the_anchorite_half_orc` | the Anchorite Half Orc |
| 581 | `the_cult_fanatic` | the Cult Fanatic |
| 582 | `the_dwarven_king` | the Dwarven King |
| 583 | `the_orc_scout` | the Orc Scout |
| 584 | `the_stag` | the Stag |
| 585 | `thomas` | Thomas |
