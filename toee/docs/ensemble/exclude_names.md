# ToEE excluded names (for facts_to_state.py --exclude-names)

Companion to `known_names.md`, but inverted: forces these normalised names to
stay anonymous/location-scoped even though the new npc-known-by-default rule
in `facts_to_state.py` would otherwise treat them as unique named individuals.

Populated 2026-07-04 from a full `--types npc --min-facts 1 --list` review.
Most generic npc role-phrases (`Ghoul`, `Warlock`, `Ogre`, `Dryad`, `The
Wraith`, ...) are already caught automatically because the same subject also
appears as `type: monster` somewhere in the corpus — those don't need an
entry here. This file is only for the residual cases with no monster-type
match: bare role/title phrases with no distinguishing name attached.

Bold spans are what `load_known_names` reads (same loader as known_names.md).

## Generic role phrases (npc-typed, no personal name)

- **Bandit Chief**
- **the freed prisoner**
- **Gnome guard**
- **Fire Cleric**
- **Commander**
- **Sergeant**
- **Village Elder**
- **Captive Monk**

Iterate the same way as known_names.md: run `--list --types npc` periodically
as the campaign continues, and add anything that's clearly a role/title
without a name attached to it.
