<!--
  Location-scoped race / collective names.

  Bold names in the list below are the payload. facts_to_state.load_known_names
  extracts every doubled-asterisk span in this file, so DO NOT bold anything except the
  payload lists below (races + location-scoped item-species), or the stray span becomes
  a spurious exclude entry.

  Purpose: names passed via `facts_to_state.py --exclude-names` are forced
  location-scoped -- each gets per-place bundles (Derro (Gracklstugh),
  Myconid (Neverlight Grove), Drow (Velkynvelve), ...) instead of one global bundle,
  which is what you want for a race/people that is a distinct faction in each place.

  Item-species (named fungi) that are registered entities but recur across many
  chapters' loot tables are listed here too: a bare registry entity global-bundles and
  vacuums up every incidental loot-table mention into one dossier, so scoping them
  per-place keeps each mention attached to where it actually appears.

  Do NOT register these as bare entities in entity_registry.yaml: a bare race name
  becomes a global "known" bundle that collapses every location into one. facts_to_state
  location-scopes any subject that is not a registry known-name; this file is the
  override for names that are (or were) registered but should still scope by place.
  See the ensemble-type-merge and entity-triage skills.

  Wire it in:
    python ~/src/CampaignGenerator/facts_to_state.py \
      --corpus 'docs/ensemble/per_chapter/*/merged.json' \
      --exclude-names docs/ensemble/location_scoped_races.md --list
-->

# Location-scoped race / collective names

- **Derro**
- **Myconid**
- **Duergar**
- **Drow**
- **Kuo-toa**

# Location-scoped item-species (named fungi)

- **Nilhogg's Nose**
- **Pygmywort**
- **Waterorb**
- **timmask**
