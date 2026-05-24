#!/usr/bin/env python3
"""Extract proper-noun dictionary from docs/background/adventure-t14-5e.json.

Writes a categorised markdown dictionary at
notes/proper_nouns_adventure.md and a flat one-per-line dump at
notes/proper_nouns_adventure.txt suitable for
`vtt-spell-pass/find_unknowns.py --extra-known`.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "background" / "adventure-t14-5e.json"
NPCS_DIR = ROOT / "docs" / "npcs"
OUT_MD = ROOT / "notes" / "proper_nouns_adventure.md"
OUT_TXT = ROOT / "notes" / "proper_nouns_adventure.txt"

# Existing NPC dossier basenames — use as a confirmation set for
# single-word capitalised tokens that would otherwise be ambiguous.
def _load_npc_basenames() -> set[str]:
    if not NPCS_DIR.is_dir():
        return set()
    out = set()
    for p in NPCS_DIR.glob("*.md"):
        stem = p.stem.lower()
        out.add(stem)
        # Also accept the first word — `dren_halveth` → `dren`
        out.add(stem.split("_")[0])
    return out

DOSSIER_NAMES = _load_npc_basenames()

# ---------- 1. Walk the JSON ----------

with SRC.open() as f:
    data = json.load(f)

section_names: list[str] = []
creatures: Counter[str] = Counter()
items_tag: Counter[str] = Counter()
prose: list[str] = []


def walk(node):
    if isinstance(node, dict):
        if isinstance(node.get("name"), str):
            section_names.append(node["name"])
        for v in node.values():
            walk(v)
    elif isinstance(node, list):
        for x in node:
            walk(x)
    elif isinstance(node, str):
        prose.append(node)
        for m in re.finditer(r"\{@creature\s+([^}|]+?)(?:\|[^}]*)?\}", node):
            creatures[m.group(1).strip()] += 1
        for m in re.finditer(r"\{@item\s+([^}|]+?)(?:\|[^}]*)?\}", node):
            items_tag[m.group(1).strip()] += 1


walk(data)


def strip_tags(s: str) -> str:
    return re.sub(r"\{@\w+\s+([^}|]+?)(?:\|[^}]*)?\}", r"\1", s)


corpus = "\n".join(strip_tags(s) for s in prose)


# ---------- 2. Filter section names ----------

GENERIC_HEADERS = {
    "Introduction",
    "Table of Contents",
    "Notes for the Dungeon Master",
    "Getting Started",
    "Other Adventures",
    "Players' Description",
    "Players' Background",
    "Player's Background",
    "Tower & Temple",
    "Dungeon",
    "Dungeon Level Two",
    "Dungeon Level Three",
    "Dungeon Level One",
    "Dungeon Level Four",
    "Dungeon Level Encounter Key",
    "Map",
    "Appendices",
    "Encounter Key",
    "Bestiary",
    "Random Encounters",
    "Wilderness Encounters",
    "Treasure",
    "Wandering Monsters",
    "Concluding the Adventure",
    "Conclusion",
    "Aftermath",
    "Detailed Locations",
    "Key to the Village",
    "Adventure",
    "Adventure Hooks",
    "Adventure Background",
    "Area Descriptions",
    "Brief Area Notes",
    "Assistance and Training",
    "Advanced Official Game Adventure",
    "Defense Strategy",
    "Tactical Notes",
    "Map of Hommlet",
    "Sources",
    "Credits",
    "Acknowledgments",
    # Newly identified noise from first pass
    "First Floor", "Second Floor", "Third Floor", "Upper Floor", "Lower Floor",
    "First Level", "Second Level", "Third Level", "Fourth Level", "Fifth Level",
    "Main Floor", "Parapet Level",
    "First Impressions", "General Information", "General Notes",
    "Combat Notes", "Tactical Notes", "Outdoor Notes", "DM Notes",
    "Map Numbering", "Publication Credits", "Map of Hommlet",
    "Examples of Holy Sayings", "Standard Corridors", "Standard Divine Spell-Like Powers",
    "Spells Memorized", "Spells normally memorized", "Spell Variations",
    "Spell-Like Powers (each usable at will)", "Modifications to Magic",
    "Cleric Spells", "Druid Spells", "Magic-User Spells", "Illusionist Spells",
    "Typical Spells", "Ogre Shaman Spells Memorized",
    "Encounter Details", "Encounter Statistics", "Encounter (5e)",
    "Ceremonial Activity", "Coordinated Efforts",
    "Troop Types", "Troop and Guard Positions",
    "Guard Tactics and Statistics", "Guard Room Notes",
    "Mercenary Table", "Brigand Statistics",
    "Map Numbering", "Special Note, Area 302",
    "Ill Effects", "North Wind Effect",
    "Treasure and Items", "Treasure (Iron Box)", "Table of Magical Treasures",
    "Room Key", "Spellbook (hidden in the portable hole in his wardrobe)",
    "Falrinth's Memorized Spells", "Falrinth's Spellbooks",
    "Kelno the Prefect Spells", "Under-priest 1 Spells", "Under-priest 2 Spells",
    "Players' Historical Notes",
    "Part 2: Nulb and the Ruins",
    "Part 3: Dungeons of Elemental Evil",
    "Part 4: Nodes of Elemental Evil",
    "Elemental Nodes",
    "Elemental Nodes — General Guidelines",
    "Secret History of the Temple",
    "Demoness", "Demigods", "Greater Gods", "Lesser Gods", "Deities & Demigods",
    "DM Notes", "DUNGEON MASTERS GUIDE", "Dungeon Master",
    "New", "New Master", "Supreme", "General Information",
    "Hommlet to Nulb",  # interlude header
    "Map of the Village",
    "Temple Area Descriptions",
    "Tower Area Descriptions", "Tower Exterior",
    "Exterior Notes (for the DM)",
    "Laboratory Materials",
    "Hedrack's Quarters (continued)",
    "Senshock (continued)", "Darley (continued)",
    "Lower Floor (a high basement area, floored)",
    "Spells", "Statistics", "Description", "Details", "Goals", "Clues",
    "Leaders", "Recruits", "Recruiting", "Mercenaries", "Prisoners",
    "Residents", "Special", "Weak", "Capable", "Overwhelming",
}

# Regex for noisy section headers we can drop wholesale.
NOISE_RE = re.compile(
    r"^(?:"
    r"Room,?\s*\d"
    r"|\d+\s*[-x×']"
    r"|GT\s*\d"
    r"|TP\s*\d"
    r"|Cell of the\b"
    r"|Cell of\b"
    r")",
    re.I,
)

# Generic-noun common-words list — drop from single-word bucket unless in DOSSIER_NAMES
COMMON_NOUNS = {
    "Chapel", "Curate", "Door", "Doors", "Pool", "Fountain", "Foyer", "Lounge",
    "Parlor", "Salon", "Grotto", "Stairway", "Stair", "Stairs", "Passage",
    "Corridor", "Study", "Nexus", "Juggernaut", "Mummy", "Beholder", "Dragon",
    "Gorgons", "Salamanders", "Medusa", "Rakshasa", "Wight", "Firetoads",
    "Storoper", "Khargra", "Xaren", "Fragarach",  # creatures — go to creatures bucket
    "Description", "Details", "Goals", "Clues", "Leaders", "Statistics",
    "Spells", "Recruits", "Recruiting", "Mercenaries", "Prisoners", "Residents",
    "Special", "Weak", "Capable", "Overwhelming", "New",
}

# Single-word tokens that are TOEE-canon creatures (not in standard 5e SRD,
# so the @creature scan won't pick them up reliably).
TOEE_CREATURES = {
    "Ascomid", "Ascomoid", "Basidirond", "Basidirond", "Ustilagor", "Zygom",
    "Xaren", "Storoper", "Khargra", "Firetoads", "Phycomid", "Harginn",
    "Harginn Grues",
}

# Generic-room names — drop unless they're a clearly distinctive placename
GENERIC_ROOM_RE = re.compile(
    r"^(Bar|Bedroom|Common Room|Private Room|Kitchen|Pantry|Cellar|Storeroom|"
    r"Storage Chamber|Storage Area|Storage Room|Stable|Barracks|"
    r"Barracks Chamber|Anteroom|Vestibule|Vestry|Audience Chamber|"
    r"Meditation Room|Garbage Room|Torture Chamber|Secret Room|Secret Corridor|"
    r"Ventilation|Armor|Armory|Alchemy Workroom|Bronze Door|Bronze Pit|"
    r"Black Chamber|Black Room|West Vestry|West Wing|West Altar|West Room|"
    r"East Room|North Room|Western Rooms|Western Side Room|Eastern Rooms|"
    r"Inner Chamber|Outer Chamber|Banquet Hall|Great Hall|Grand Entrance|"
    r"Grand Hall|Burial Crypts|Augury Chamber|Burrow Warren|Ashpit|"
    r"Abandoned Storeroom|Altar Curtain|Bar|Bath|Bath Room|Cells|"
    r"Stairs?|Corridor|Hall|Hallway|Latrines?|Closet|Pit|"
    r"Modest Cottage|Average Farm Building|Large Barn|Large Room|"
    r"Small House.*|Modest Cottage.*|Walled Manor House|"
    r"Weatherbeaten Building.*|Well-Kept Dwelling.*|"
    r"Wooden Building.*|Barn-Like House.*|Stone House|"
    r"Two-Storied Tower|Double Fieldstone Walls.*|Tents and Wattle Huts|"
    r"Sturdy New Building.*|Large New Building|Farmer.*Son|Farmer.*Daughter|"
    r"Prosperous Farm Cottage.*|Typical Cottage.*|Modest Farmhouse.*|"
    r"Cottage|Farm Cottage|New Building|Trading Post|Guard Tower|"
    r"Church Library|Chief Priest's Chamber|Assistant Cleric's Chambers|"
    r"Study and Audience Chamber|Processional|Balcony|Hall|Altar and Sanctuary|"
    r"Upper Hall|Watchtower|"
    r"Lower Level.*|Upper Level.*|Approach to.*|Western .*|Eastern .*|"
    r"Northern .*|Southern .*|"
    r"Mercenary Table|Brigand Statistics|Brigands|Bandits|"
    r"Appendix [A-Z]:.*|"
    r"Air Node|Water Node|Earth Node|Fire Node|"  # nodes — keep separately as places
    r"Air Temple|Water Temple|Earth Temple|Fire Temple|Greater Temple|Great Temple|"
    r"West Fire Gate|West Water Gate|Broken Gates|"
    r"Random Encounter.*|"
    r"All Rights Reserved|WORLD OF GREYHAWK.*Setting|"
    r"Concluding.*|Conclusion.*|"
    r"Wand of a Wonder|Hit Dice|Sale Value|"
    r"Old Faith|New Faith|"
    r"GP Sale Value:|XP Value:|"
    r"\d+\s*[A-Z]?\.?\s.*|"  # numeric room labels
    r"[A-Z]\s\d+\.\s.*|"  # C 1. Hall etc.
    r")$",
    re.I,
)

# Some of the above we DO want to keep — re-include after the broad cut:
KEEP_OVERRIDE = {
    "Air Node",
    "Water Node",
    "Earth Node",
    "Fire Node",
    "Air Temple",
    "Water Temple",
    "Earth Temple",
    "Fire Temple",
    "Greater Temple",
    "Trading Post",
}

# Prefix patterns we strip
AREA_RE = re.compile(r"^(?:Area\s+)?\d+[a-z]?\.\s*", re.I)
LETTER_NUM_RE = re.compile(r"^[A-Z]\s*\d+[a-z]?\.\s*")
ROMAN_RE = re.compile(r"^[IVXLC]+\.\s*", re.I)
SINGLE_LETTER_RE = re.compile(r"^[A-Z]\.\s+")


def clean_section(s: str) -> str | None:
    s = s.strip()
    if not s or s in GENERIC_HEADERS:
        return None
    if NOISE_RE.search(s):
        return None
    cleaned = AREA_RE.sub("", s)
    cleaned = LETTER_NUM_RE.sub("", cleaned)
    cleaned = SINGLE_LETTER_RE.sub("", cleaned)
    cleaned = ROMAN_RE.sub("", cleaned).strip()
    if not cleaned:
        return None
    if cleaned in GENERIC_HEADERS:
        return None
    if NOISE_RE.search(cleaned):
        return None
    return cleaned


def strip_paren_suffix(name: str) -> str:
    """Drop ' (whatever)' and ' — descriptor' suffix so bucket dedup works."""
    n = re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()
    n = re.sub(r"\s*—\s+.*$", "", n).strip()
    return n


cleaned_sections = [c for c in (clean_section(n) for n in section_names) if c]

# ---------- 3. Categorise ----------

# Hand-curated TOEE pantheon / extraplanar lords (sourced from the JSON prose
# scan below; included explicitly because some appear only in dialogue, not as
# section headers).
DEITY_SEED = {
    "St. Cuthbert",
    "Iuz",
    "Tharizdun",
    "Lolth",
    "Zuggtmoy",
    "Boccob",
    "Pelor",
    "Heironeous",
    "Hextor",
    "Obad-Hai",
    "Ehlonna",
    "Pholtus",
    "Wee Jas",
    "Erythnul",
    "Nerull",
    "Vecna",
    "Olidammara",
    "Yondalla",
    "Corellon Larethian",
    "Moradin",
    "Gruumsh",
    "Imix",  # Prince of Evil Fire
    "Olhydra",  # Princess of Evil Water
    "Ogremoch",  # Prince of Evil Earth
    "Yan-C-Bin",  # Prince of Evil Air
    "Cryonax",
    "Demogorgon",
    "Orcus",
    "Bahamut",
    "Tiamat",
}

# Realms / regions of Greyhawk that appear in the module
PLACE_SEED = {
    "Hommlet",
    "Nulb",
    "Verbobonc",
    "Velverdyva",  # river
    "Imeryds Run",  # stream
    "Kron Hills",
    "Nyr Dyv",  # lake
    "Wild Coast",
    "Greyhawk",
    "Furyondy",
    "Celene",
    "Veluna",
    "Dyvers",
    "Highfolk",
    "Gnarley Forest",
    "Vesve Forest",
}

# Inline-prose scan for additional proper nouns (multi-word capitalised
# phrases). Use as additive signal on top of section names.
MULTIWORD_RE = re.compile(
    r"\b(?:[A-Z][a-zA-Z']+)(?:\s+(?:of\s+|the\s+|de\s+|von\s+|du\s+)?"
    r"(?:[A-Z][a-zA-Z']+|St\.))+\b"
)
SAINT_RE = re.compile(r"\b(?:St\.|Saint)\s+[A-Z][a-z]+\b")

prose_multi = Counter(m.group(0) for m in MULTIWORD_RE.finditer(corpus))
prose_saints = Counter(m.group(0) for m in SAINT_RE.finditer(corpus))

# Likely-NPC pattern: "Name, the X" or "Name the X" with class/title
NPC_TITLE_RE = re.compile(
    r"\b([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]+)?)\s+(?:the\s+)?"
    r"(?:Mage|Cleric|Druid|Priest|Priestess|Bandit|Brigand|Hierophant|"
    r"Necromancer|Wizard|Fighter|Thief|Ranger|Paladin|Monk|Sorcerer|"
    r"Captain|Commander|Master|Mistress|Hermit|Chief|Elder|Mother|Father|"
    r"Lord|Lady|Sir|Dame|Prefect|Warden|Brother|Sister|Reverend|"
    r"Hammerer|Smith|Innkeeper|Trader|Wainwright)\b"
)
prose_npcs = Counter(m.group(1) for m in NPC_TITLE_RE.finditer(corpus))


# ---------- 4. Bucket ----------

DEITY_KEYWORDS = re.compile(
    r"(god|deity|elder|prince of evil|princess of evil|demoness|"
    r"lord of|patron|saint|hierophant)",
    re.I,
)

PLACE_HINTS = re.compile(
    r"(Village|Tower|Castle|Keep|Fort|Manor|Inn|Tavern|Temple|Shrine|"
    r"Church|Citadel|Lake|River|Stream|Run|Wood|Forest|Hills?|Mountains?|"
    r"Coast|Pass|Hamlet|Ruins|Moathouse|Node|Plane)",
)

PERSON_HINTS = re.compile(
    r"\b(Mother|Father|Sir|Lord|Lady|Dame|Captain|Commander|Prefect|"
    r"Brother|Sister|Elder|Chief|Reverend|Master|Mistress|Hierophant|"
    r"Barmaid|Barman|the\s+(?:Mage|Cleric|Priest|Druid|Fighter|Wizard))",
    re.I,
)

ITEM_HINTS = re.compile(
    r"\b(Orb|Sword|Wand|Staff|Rod|Ring|Cloak|Helm|Shield|Tome|Crown)\b"
)

buckets: dict[str, set[str]] = defaultdict(set)


def bucket(name: str, category: str):
    # Normalize: strip "(continued)" / paren-suffix and trailing whitespace
    n = strip_paren_suffix(name)
    if not n:
        return
    if n in GENERIC_HEADERS:
        return
    buckets[category].add(n)


# Seeds
for d in DEITY_SEED:
    if d in corpus or d.replace("-", "") in corpus.replace("-", ""):
        bucket(d, "deities")
for p in PLACE_SEED:
    if p in corpus:
        bucket(p, "places")

# Section names → categorise
for s in cleaned_sections:
    # Skip pure noise
    if GENERIC_ROOM_RE.match(s) and s not in KEEP_OVERRIDE:
        continue
    # NPC pattern: "Role: Name" or "Name, the X"
    if ":" in s and len(s.split(":")) == 2:
        role, person = (x.strip() for x in s.split(":"))
        if len(person.split()) <= 3 and person[:1].isupper():
            bucket(person, "npcs")
            continue
    if "," in s and PERSON_HINTS.search(s):
        # "Burne, 'His Most Worshipful Mage of Hommlet'"
        first = s.split(",")[0].strip()
        if 1 <= len(first.split()) <= 3:
            bucket(first, "npcs")
            continue
    if DEITY_KEYWORDS.search(s):
        bucket(s, "deities")
        continue
    if ITEM_HINTS.search(s) and "of" in s:
        bucket(s, "items")
        continue
    if PLACE_HINTS.search(s):
        bucket(s, "places")
        continue
    # Default: if it looks like a single-word proper noun, route smartly.
    if " " not in s and s[:1].isupper() and s.isalpha():
        if s in COMMON_NOUNS and s.lower() not in DOSSIER_NAMES:
            continue  # drop generic-noun residue
        if s in TOEE_CREATURES:
            bucket(s, "creatures")
            continue
        if s.lower() in {c.lower() for c in creatures}:
            bucket(s, "creatures")
            continue
        if s.lower() in DOSSIER_NAMES:
            bucket(s, "npcs")
            continue
        # Looks like a name but no dossier — surface as candidate
        bucket(s, "candidates")
        continue
    bucket(s, "places")

# Creatures
for c in creatures:
    # Title-case canonical form
    bucket(" ".join(w.capitalize() for w in c.split()), "creatures")

# Inline saints / multiword that aren't already captured
for s in prose_saints:
    bucket(s, "deities")

for phrase, count in prose_multi.most_common():
    if count < 3:
        continue
    if phrase in GENERIC_HEADERS:
        continue
    if any(phrase in v for v in buckets.values()):
        continue
    if PLACE_HINTS.search(phrase) or "of" in phrase.split():
        # Looks place-ish or named-item-ish
        if ITEM_HINTS.search(phrase):
            bucket(phrase, "items")
        else:
            bucket(phrase, "places")
    elif PERSON_HINTS.search(phrase):
        bucket(phrase, "npcs")

# NPCs from prose-title pattern (only multi-occurring)
for name, count in prose_npcs.most_common():
    if count < 2:
        continue
    if name in GENERIC_HEADERS:
        continue
    bucket(name, "npcs")


# ---------- 5. Write outputs ----------

CATEGORY_ORDER = [
    ("deities", "Deities & Divine Powers"),
    ("places", "Places, Realms & Notable Locations"),
    ("npcs", "NPCs (named in module + cross-referenced with docs/npcs/)"),
    ("creatures", "Creatures"),
    ("items", "Named Magic Items"),
    ("candidates", "Unconfirmed candidates (single-word capitalised, no dossier yet — review before promoting)"),
]

# Pure-room generic place labels — drop from places bucket.
GENERIC_PLACE_RE = re.compile(
    r"^(The\s+)?("
    r"Anteroom|Bar|Bath|Bath Room|Bedroom|Bedchamber|"
    r"Cellar|Cells|Chamber|Closet|Common Room|Corner Room|"
    r"Corridor|Crooked Corridor|Crypts|Empty .*|Empty Bedchamber|"
    r"Foyer|Frescoed Corridor|Garbage Room|Grand Hall|Grand Staircase|"
    r"Great Hall|Green Corridor|Grim Chamber|"
    r"Hall|Hallway|Hexagonal Chamber|Hexagonal Room|Hidden Room|"
    r"High Altar|Huge Casks|Inky Chamber|Inner Chamber|"
    r"Junk Room|Kitchen|L-Shaped Room|Large Barn.*|"
    r"Level One|Level Two|Level Three|Level Four|"
    r"Lieutenant's Quarters|Light Chamber|Littered .*|"
    r"Locked Storage|Low.*|Main Cellar|Main Room|"
    r"Meditation Room|Modest Cottage|Modest Farmhouse|Museum Room|"
    r"North.*Room|North Storeroom|North.*Room|Northeast Room|"
    r"Octagonal Chamber|Odd Side Room|Old Storeroom|"
    r"Opulent Bedchamber|Outer Chamber|Padlocked Door|"
    r"Pantry|Parchment Message|Parlor|Passage|Pearlescent Room|"
    r"Pillared Hall|Pit|Pit Chamber|Pleasure Chamber|"
    r"Prison Room|Private Room|Private Suite|Processional Corridor|"
    r"Reception Room|Scarlet Room|Sealed Doors?|Secret Corridor|"
    r"Secret Door|Secret Passage|Secret Room|Secured Door|"
    r"Serving Barmaid Room|Side Chamber|Side Room|"
    r"Sitting Room|Sleeping Apartment|Small Door|Small Room|"
    r"South.*Room|Spare Room|Spiral Stair|Square Chamber|"
    r"Stable|Stair|Stairs|Stairway|Stairway Arch|Stairway Up|"
    r"Storeroom|Storage Chamber|Storage Room|Study|"
    r"Summer Kitchen|Sunlit Room|"
    r"Tower|Trading Post|Triangular Chamber|"
    r"Undetected Trap|Upper Floor|Vault|Ventilation|Vestibule|Vestry|"
    r"Walled Manor House|Watchtower|"
    r"East .*|West .*|North .*|South .*|"
    r"Side .*|Inner .*|Outer .*|Lower .*|Upper .*|"
    r"Dais.*|Dining .*|Domed .*|Dormitory .*|"
    r"Earth-Floored .*|Exercise .*|Bedroom"
    r")$",
    re.I,
)

# Bestiary "Type, Adjective" patterns (e.g., "Pudding, Black", "Giants, Fire").
BESTIARY_LIST_RE = re.compile(
    r"^(Pudding|Slime|Mold|Giants?|Dragons?|Elementals?|Eyes|Fungi|Ooze|"
    r"Fire Bats?|Fire Snakes?|Ice Lizards?|Rock Reptiles?|Harginn Grues?|"
    r"Dragon Turtles?|Other Swords of Answering),?\s",
    re.I,
)

# Post-process: dedup across buckets (later buckets lose to earlier),
# move bestiary-list entries from places to creatures, strip generic-place noise.
PRIORITY = ["deities", "npcs", "places", "creatures", "items", "candidates"]
seen: set[str] = set()
seen_keys: set[str] = set()

def key(name: str) -> str:
    """Normalised lookup key for cross-bucket dedup."""
    k = re.sub(r"^The\s+", "", name, flags=re.I)
    return k.lower().strip()

for cat in PRIORITY:
    if cat not in buckets:
        continue
    cur = sorted(buckets[cat])
    keep = set()
    for name in cur:
        # Move bestiary-list entries to creatures
        if cat == "places" and BESTIARY_LIST_RE.match(name):
            buckets["creatures"].add(name)
            continue
        # Drop generic-place residue
        if cat == "places" and GENERIC_PLACE_RE.match(name):
            continue
        k = key(name)
        if k in seen_keys:
            continue
        keep.add(name)
        seen_keys.add(k)
    buckets[cat] = keep

with OUT_MD.open("w") as f:
    f.write("# TOEE Adventure — Proper-Noun Dictionary\n\n")
    f.write(
        f"Extracted from `docs/background/adventure-t14-5e.json` "
        f"({len(cleaned_sections)} cleaned section names, "
        f"{len(creatures)} unique `@creature` tags, "
        f"{len(prose)} prose strings scanned).\n\n"
    )
    f.write(
        "Categorisation is heuristic — review and prune before promoting. "
        "Flat one-per-line dump for `vtt-spell-pass --extra-known` lives "
        "alongside this file at `proper_nouns_adventure.txt`.\n\n"
    )
    for key, title in CATEGORY_ORDER:
        items = sorted(buckets.get(key, set()))
        f.write(f"## {title} ({len(items)})\n\n")
        for it in items:
            f.write(f"- {it}\n")
        f.write("\n")

# Flat dump — every canonical, deduped
flat = set()
for items in buckets.values():
    flat.update(items)
with OUT_TXT.open("w") as f:
    for n in sorted(flat):
        f.write(n + "\n")

print(f"Wrote {OUT_MD}")
print(f"Wrote {OUT_TXT}  ({len(flat)} canonical names)")
for key, title in CATEGORY_ORDER:
    print(f"  {key}: {len(buckets.get(key, set()))}")
