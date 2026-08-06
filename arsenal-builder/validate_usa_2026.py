"""Sanity checks on the generated USA 2026 tool files."""
import json
import os

DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "USA", "2026")
FIELDS = ["Tool Name", "Description", "Tracks", "Speakers", "Year", "Github URL", "Location"]


def main():
    issues = 0
    words = []
    files = [f for f in sorted(os.listdir(DEST)) if f.endswith(".json")]
    for f in files:
        d = json.load(open(os.path.join(DEST, f), encoding="utf-8"))
        for k in FIELDS:
            if k not in d:
                print(f"MISSING {k}: {f}")
                issues += 1
        if d.get("Year") != "2026" or d.get("Location") != "USA":
            print(f"BAD meta: {f}")
            issues += 1
        n = len((d.get("Description") or "").split())
        words.append(n)
        if n < 35:
            print(f"SHORT desc ({n}w): {f}")
            issues += 1
        if not d.get("Speakers"):
            print(f"NO speakers: {f}")
            issues += 1
        if not d.get("Tracks"):
            print(f"NO tracks: {f}")
            issues += 1
    print(f"files: {len(files)}  issues: {issues}")
    print(f"description words -> min {min(words)}  max {max(words)}  avg {round(sum(words)/len(words))}")


if __name__ == "__main__":
    main()
