#!/usr/bin/env python3
"""
Interactive alias review for docs/ensemble/state_dossiers.

Finds duplicate entity names (same person/place under different spellings),
asks the human to confirm each merge, and writes aliases.json for use with
facts_to_state.py --aliases.  Decisions persist across sessions so you never
re-review a pair you've already decided.

Usage:
  python review_aliases.py --review    # interactive prompt for each undecided group
  python review_aliases.py --rebuild   # rebuild aliases.json from saved decisions (no prompts)
  python review_aliases.py --list      # list all candidate groups without prompting
"""

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
CAMPAIGN_DIR = SCRIPT_DIR.parent.parent
DOSSIERS_DIR = SCRIPT_DIR / "state_dossiers"
NPCS_DIR = CAMPAIGN_DIR / "docs" / "npcs"
DECISIONS_FILE = SCRIPT_DIR / ".alias_decisions.json"
ALIASES_FILE = SCRIPT_DIR / "aliases.json"

TITLE_PREFIXES = [
    "the ", "sir ", "sister ", "lady ", "lord ", "ser ",
    "falcon the ", "townmaster ", "town master ",
]


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(path: Path) -> dict:
    """Extract key: value pairs from YAML frontmatter (--- ... ---)."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    result = {}
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith("["):
            try:
                result[k.strip()] = json.loads(v)
            except json.JSONDecodeError:
                result[k.strip()] = v
        else:
            result[k.strip()] = v
    return result


def load_dossiers(dossiers_dir: Path) -> list[dict]:
    """Load display-name metadata from all *.md files in dossiers_dir."""
    out = []
    for path in sorted(dossiers_dir.glob("*.md")):
        fm = parse_frontmatter(path)
        name = fm.get("name", "").strip()
        if not name:
            continue
        out.append({
            "path": path,
            "name": name,
            "type": fm.get("type", ""),
            "n_facts": int(fm.get("n_facts", 0)),
            "chapters": fm.get("chapters", "?"),
        })
    return out


# ---------------------------------------------------------------------------
# Similarity helpers
# ---------------------------------------------------------------------------

def normalize(name: str) -> str:
    n = name.lower()
    n = re.sub(r"[^a-z0-9\s]", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def strip_titles(name: str) -> str:
    n = normalize(name)
    for prefix in TITLE_PREFIXES:
        if n.startswith(prefix):
            n = n[len(prefix):]
    return n.strip()


def levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            curr.append(min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = curr
    return prev[-1]


_MIN_LEN = 4  # ignore names shorter than this for substring/levenshtein checks


def are_similar(a: str, b: str) -> bool:
    na, nb = normalize(a), normalize(b)
    if na == nb:
        return True
    # Substring — both must be long enough to avoid "i" ⊂ "ilvara"-style false hits
    if len(na) >= _MIN_LEN and len(nb) >= _MIN_LEN and (na in nb or nb in na):
        return True
    # Title-strip match
    sa, sb = strip_titles(a), strip_titles(b)
    if sa and sb and len(sa) >= _MIN_LEN and len(sb) >= _MIN_LEN:
        if sa == sb or sa in sb or sb in sa:
            return True
    # Levenshtein ≤ 2 — only meaningful on strings of reasonable length
    if len(na) >= _MIN_LEN and len(nb) >= _MIN_LEN and levenshtein(na, nb) <= 2:
        return True
    return False


# ---------------------------------------------------------------------------
# Group finding (union-find over same-type entities)
# ---------------------------------------------------------------------------

def find_groups(dossiers: list[dict]) -> list[list[dict]]:
    """Return groups of ≥2 dossiers that look like the same entity."""
    # Index-based union-find so same-name different-type entities don't collide
    parent: list[int] = list(range(len(dossiers)))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> None:
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    by_type: dict[str, list[tuple[int, dict]]] = {}
    for i, d in enumerate(dossiers):
        by_type.setdefault(d["type"], []).append((i, d))

    for td in by_type.values():
        for ii, (ia, da) in enumerate(td):
            for ib, db in td[ii + 1:]:
                if are_similar(da["name"], db["name"]):
                    union(ia, ib)

    groups: dict[int, list[dict]] = {}
    for i, d in enumerate(dossiers):
        groups.setdefault(find(i), []).append(d)

    return [g for g in groups.values() if len(g) > 1]


# ---------------------------------------------------------------------------
# npcs/ proposal seeding
# ---------------------------------------------------------------------------

def load_npcs_proposals(name_to_dossier: dict[str, dict]) -> list[list[dict]]:
    """
    Yield candidate groups from docs/npcs/.alias_proposal.json.
    Only includes names that exist in state_dossiers (so display names must match).
    """
    proposal_file = NPCS_DIR / ".alias_proposal.json"
    if not proposal_file.exists():
        return []

    data = json.loads(proposal_file.read_text(encoding="utf-8"))
    by_canonical = data.get("by_canonical", {})
    groups = []

    for stem, entries in by_canonical.items():
        dossier_path = NPCS_DIR / f"{stem}.md"
        if not dossier_path.exists():
            continue
        fm = parse_frontmatter(dossier_path)
        canonical_name = fm.get("name", "").strip()
        if not canonical_name:
            continue
        variants = [e.get("alias", "").strip() for e in entries if e.get("alias")]
        all_names = [canonical_name] + variants
        present = [n for n in all_names if n in name_to_dossier]
        if len(present) >= 2:
            groups.append([name_to_dossier[n] for n in present])

    return groups


# ---------------------------------------------------------------------------
# Decision persistence
# ---------------------------------------------------------------------------

def load_decisions() -> list[dict]:
    if not DECISIONS_FILE.exists():
        return []
    return json.loads(DECISIONS_FILE.read_text(encoding="utf-8")).get("decisions", [])


def save_decisions(decisions: list[dict]) -> None:
    DECISIONS_FILE.write_text(
        json.dumps({"decisions": decisions}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def rebuild_aliases(decisions: list[dict]) -> dict[str, list[str]]:
    aliases: dict[str, list[str]] = {}
    for d in decisions:
        if d["status"] == "approved" and d.get("canonical"):
            canonical = d["canonical"]
            variants = [c for c in d["candidates"] if c != canonical]
            if variants:
                existing = aliases.get(canonical, [])
                aliases[canonical] = list(dict.fromkeys(existing + variants))
    return aliases


def find_decided(group_names: list[str], decisions: list[dict]) -> dict | None:
    gs = set(group_names)
    for d in decisions:
        if set(d["candidates"]) == gs:
            return d
    return None


# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------

def collect_groups(dossiers: list[dict]) -> list[list[dict]]:
    """Collect fuzzy groups + npcs proposal groups, deduplicated."""
    name_to_dossier = {d["name"]: d for d in dossiers}
    groups = find_groups(dossiers)
    group_sets = [frozenset(d["name"] for d in g) for g in groups]

    for proposal_group in load_npcs_proposals(name_to_dossier):
        fs = frozenset(d["name"] for d in proposal_group)
        if not any(fs <= g or g <= fs for g in group_sets):
            groups.append(proposal_group)
            group_sets.append(fs)

    return groups


def review_mode() -> None:
    if not DOSSIERS_DIR.exists():
        print(f"Error: {DOSSIERS_DIR} does not exist.", file=sys.stderr)
        sys.exit(1)

    dossiers = load_dossiers(DOSSIERS_DIR)
    decisions = load_decisions()
    groups = collect_groups(dossiers)

    undecided = [
        g for g in groups
        if not find_decided([d["name"] for d in g], decisions)
    ]

    print(f"Total candidate groups:  {len(groups)}")
    print(f"Already decided:         {len(groups) - len(undecided)}")
    print(f"Undecided (to review):   {len(undecided)}")

    if not undecided:
        print("Nothing to review.")
        _write_aliases(decisions)
        return

    reviewed = 0
    for group in undecided:
        group_sorted = sorted(group, key=lambda d: -d["n_facts"])
        names = [d["name"] for d in group_sorted]
        print()
        print("Merge candidates:")
        for i, d in enumerate(group_sorted, 1):
            print(f"  [{i}] {d['name']}  ({d['n_facts']} facts, ch {d['chapters']})  [{d['type']}]")
        options = "/".join(str(i) for i in range(1, len(group_sorted) + 1))
        print(f"Canonical? [{options}/n(not same)/q(quit)] > ", end="", flush=True)

        try:
            answer = input().strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nInterrupted — saving progress.")
            break

        if answer == "q":
            print("Quitting — progress saved.")
            break
        elif answer == "n":
            decisions.append({
                "candidates": names,
                "canonical": None,
                "status": "rejected",
            })
            print("  → Not merged.")
        elif answer.isdigit() and 1 <= int(answer) <= len(group_sorted):
            canonical = group_sorted[int(answer) - 1]["name"]
            decisions.append({
                "candidates": names,
                "canonical": canonical,
                "status": "approved",
            })
            print(f"  → Canonical: {canonical}")
        else:
            print("  (unrecognized input — skipping this group)")
            continue

        save_decisions(decisions)
        reviewed += 1

    _write_aliases(decisions)
    print(f"\nReviewed {reviewed} group(s) this session.")


def rebuild_mode() -> None:
    decisions = load_decisions()
    _write_aliases(decisions)


def list_mode() -> None:
    dossiers = load_dossiers(DOSSIERS_DIR)
    decisions = load_decisions()
    groups = collect_groups(dossiers)

    print(f"{len(groups)} candidate groups:\n")
    for group in sorted(groups, key=lambda g: -max(d["n_facts"] for d in g)):
        names = [d["name"] for d in sorted(group, key=lambda d: -d["n_facts"])]
        decision = find_decided(names, decisions)
        if decision:
            tag = f"[{decision['status'].upper()}]"
            if decision["status"] == "approved":
                tag += f" canonical={decision['canonical']}"
        else:
            tag = "[undecided]"
        print(f"  {tag}")
        for d in sorted(group, key=lambda d: -d["n_facts"]):
            print(f"    {d['name']}  ({d['n_facts']} facts, ch {d['chapters']})  [{d['type']}]")


def _write_aliases(decisions: list[dict]) -> None:
    aliases = rebuild_aliases(decisions)
    ALIASES_FILE.write_text(
        json.dumps(aliases, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    approved = sum(1 for d in decisions if d["status"] == "approved")
    total_variants = sum(len(v) for v in aliases.values())
    print(f"aliases.json: {approved} canonical entries, {total_variants} total variants → {ALIASES_FILE}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--review", action="store_true",
                   help="Interactive review of undecided duplicate groups")
    g.add_argument("--rebuild", action="store_true",
                   help="Rebuild aliases.json from saved decisions (no prompts)")
    g.add_argument("--list", action="store_true",
                   help="List all candidate groups with their decision status")
    args = p.parse_args()

    if args.review:
        review_mode()
    elif args.rebuild:
        rebuild_mode()
    else:
        list_mode()


if __name__ == "__main__":
    main()
