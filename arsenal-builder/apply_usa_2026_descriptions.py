"""Replace the scraped USA 2026 abstracts with polished third-person descriptions."""
import glob
import json
import os

DEST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "USA", "2026")
SRC_GLOB = (
    "/private/tmp/claude-501/-Users-TheBrain-Documents-githubArsenal-awesome-blackhat-arsenal/"
    "e98f478b-0291-4870-95de-ba8dc3cfdc10/scratchpad/desc_batch*.json"
)


def main():
    polished = {}
    for path in sorted(glob.glob(SRC_GLOB)):
        polished.update(json.load(open(path, encoding="utf-8")))

    applied = set()
    for f in sorted(os.listdir(DEST)):
        if not f.endswith(".json"):
            continue
        path = os.path.join(DEST, f)
        d = json.load(open(path, encoding="utf-8"))
        new = polished.get(d["Tool Name"])
        if new:
            d["Description"] = new
            applied.add(d["Tool Name"])
            json.dump(d, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    unmatched = set(polished) - applied
    if unmatched:
        print("⚠️  Polished text with no matching tool file:")
        for m in sorted(unmatched):
            print("   ", m)
    print(f"✅ Applied {len(applied)} descriptions")


if __name__ == "__main__":
    main()
