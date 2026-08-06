"""Turn the scraped USA 2026 session list into per-tool JSON files.

Sessions repeat across days, so dedupe by tool name and merge speakers/tracks.
Track names on the BH site drift slightly between events — normalize to the
canonical names already used across this repo.
"""
import json
import os
import re

SRC = "Data/USA/us-26_arsenal_schedule_index.html.json"
DEST = "../tools/USA/2026"

TRACK_ALIASES = {
    "WebAppSec": "Web AppSec",
    "Threat Hunting & Incident Response": "Threat Hunting and Incident Response",
}


def sanitize_filename(name, max_length=120):
    return re.sub(r'[\\/*?:"<>|]', "_", name).strip()[:max_length]


def main():
    sessions = json.load(open(SRC, encoding="utf-8"))
    merged = {}
    for s in sessions:
        name = s["tool_name"].strip()
        entry = merged.setdefault(name, {
            "Tool Name": name,
            "Description": (s.get("description") or "").strip(),
            "Tracks": [],
            "Speakers": [],
            "Year": "2026",
            "Github URL": "",
            "Location": "USA",
        })
        for tr in (s.get("tracks") or []):
            tr = TRACK_ALIASES.get(tr, tr)
            if tr not in entry["Tracks"]:
                entry["Tracks"].append(tr)
        for sp in (s.get("speakers") or []):
            if sp not in entry["Speakers"]:
                entry["Speakers"].append(sp)
        # Keep the longest description seen for a repeated session
        desc = (s.get("description") or "").strip()
        if len(desc) > len(entry["Description"]):
            entry["Description"] = desc

    os.makedirs(DEST, exist_ok=True)
    for name, entry in merged.items():
        path = os.path.join(DEST, sanitize_filename(name) + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(entry, f, indent=2, ensure_ascii=False)
    print(f"💾 Wrote {len(merged)} tools to {DEST}")


if __name__ == "__main__":
    main()
