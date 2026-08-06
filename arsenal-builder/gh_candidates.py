"""Query the GitHub search API for candidate repos matching each USA 2026 tool."""
import json
import os
import re
import subprocess
import sys
import time

TOOLS_DIR = "../tools/USA/2026"
OUT = "Data/USA/us-26_gh_candidates.json"


def short_name(name):
    """Take the part of the session title that reads like a project name."""
    n = re.split(r"[:–—]| - | \(| – ", name)[0].strip()
    n = re.sub(r"[^\w .+#&-]", " ", n).strip()
    return n or name


def gh_search(q, per_page=6):
    try:
        out = subprocess.run(
            ["gh", "api", "-X", "GET", "search/repositories",
             "-f", f"q={q}", "-f", f"per_page={per_page}", "-f", "sort=stars"],
            capture_output=True, text=True, timeout=40,
        )
        if out.returncode != 0:
            return {"error": out.stderr.strip()[:200]}
        data = json.loads(out.stdout)
        return [
            {
                "full_name": r["full_name"],
                "url": r["html_url"],
                "stars": r["stargazers_count"],
                "desc": (r.get("description") or "")[:220],
                "updated": r.get("pushed_at"),
            }
            for r in data.get("items", [])
        ]
    except Exception as e:
        return {"error": f"{e.__class__.__name__}: {e}"}


def main():
    results = {}
    if os.path.exists(OUT):
        results = json.load(open(OUT, encoding="utf-8"))

    files = sorted(f for f in os.listdir(TOOLS_DIR) if f.endswith(".json"))
    for i, f in enumerate(files, 1):
        d = json.load(open(os.path.join(TOOLS_DIR, f), encoding="utf-8"))
        name = d["Tool Name"]
        if name in results:
            continue
        key = short_name(name)
        results[name] = {"query": key, "candidates": gh_search(key)}
        print(f"{i:3d}/{len(files)}  {key}")
        time.sleep(2.2)  # search API: 30 req/min authenticated
        if i % 10 == 0:
            json.dump(results, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    json.dump(results, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"💾 {len(results)} entries -> {OUT}")


if __name__ == "__main__":
    main()
