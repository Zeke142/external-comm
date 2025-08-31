#!/usr/bin/env python3
"""
External Communication Module → GitHub Bridge
Reads /comm/direct_drop.md (Draft), publishes to GitHub (Discussion or Issue),
then appends a log entry to /comm/logs/_index.md.
"""

import os, re, json, pathlib, datetime, sys
import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]  # repo root (contains /comm)
COMM = ROOT / "comm"

# --- Load config (optional) ---
CFG_PATH = COMM / "bridge.config.json"
CFG = {
    "repo": "your-user-or-org/your-repo",
    "mode": "discussion",                 # "discussion" | "issue"
    "discussion_category": "Announcements",
    "issue_labels": ["announcement", "external-comm"],
    "log_path": "comm/logs/_index.md",
    "source_path": "comm/direct_drop.md"
}
if CFG_PATH.exists():
    try:
        CFG.update(json.loads(CFG_PATH.read_text()))
    except Exception as e:
        print(f"Warning: could not parse bridge.config.json: {e}")

REPO = CFG["repo"]
MODE = CFG.get("mode", "discussion").lower()
CATEGORY = CFG.get("discussion_category", "Announcements")
ISSUE_LABELS = CFG.get("issue_labels", [])
LOG_FILE = ROOT / CFG.get("log_path", "comm/logs/_index.md")
SRC_FILE = ROOT / CFG.get("source_path", "comm/direct_drop.md")

API = "https://api.github.com"
TOKEN = os.getenv("GH_TOKEN")

def die(msg: str):
    print(f"Error: {msg}")
    sys.exit(1)

def gh(method: str, url: str, json_body=None):
    if not TOKEN:
        die("Missing GH_TOKEN environment variable.")
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    r = requests.request(method, url, headers=headers, json=json_body)
    if r.status_code >= 300:
        die(f"GitHub API {r.status_code}: {r.text}")
    return r.json()

def read_draft_text(md: str) -> str:
    # capture under 'Draft' header; fallback = first non-empty paragraph
    m = re.search(r"^#{1,3}\s*Draft\s*\n([\s\S]*?)(?:\n#{1,3}\s|\Z)", md, flags=re.M)
    if m:
        text = m.group(1).strip()
        if text:
            return text
    for block in md.split("\n\n"):
        b = block.strip()
        if b and not b.lower().startswith("# external communication module"):
            return b
    die("No draft text found in direct_drop.md")

def first_line_title(text: str, limit: int = 80) -> str:
    first = text.strip().splitlines()[0] if text.strip() else "Update"
    return (first[: limit - 1] + "…") if len(first) > limit else first

def get_discussion_category_id(owner: str, repo: str, name: str):
    data = gh("GET", f"{API}/repos/{owner}/{repo}/discussions/categories")
    for c in data:
        if c["name"].lower() == name.lower():
            return c["id"]
    return None

def create_discussion(owner: str, repo: str, title: str, body: str, cat_id: int):
    return gh("POST", f"{API}/repos/{owner}/{repo}/discussions", {
        "title": title, "body": body, "category_id": cat_id
    })

def create_issue(owner: str, repo: str, title: str, body: str, labels):
    return gh("POST", f"{API}/repos/{owner}/{repo}/issues", {
        "title": title, "body": body, "labels": labels
    })

def append_log(path: pathlib.Path, channel: str, url: str, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    snippet = " ".join(text.split())
    if len(snippet) > 200:
        snippet = snippet[:197] + "…"
    entry = f"- {date} | Channel: {channel} | Link: {url}\n  Text: {snippet}\n"

    if path.exists():
        content = path.read_text(encoding="utf-8")
        if not content.endswith("\n"):
            content += "\n"
        content = content + entry
    else:
        content = "# External Communication Log\n\n" \
                  "This file is the **running archive** of all messages published through the External Communication Module.\n" \
                  "Every entry should include: **date, channel, text snippet, and link**.\n\n" \
                  "## 📜 Log Entries\n\n" \
                  "*(Newest entries go at the top)*\n\n" + entry
    path.write_text(content, encoding="utf-8")

def main():
    if "/" not in REPO:
        die("Config 'repo' must be in the form 'owner/repo'.")
    owner, repo = REPO.split("/", 1)

    if not SRC_FILE.exists():
        die(f"Source file not found: {SRC_FILE}")

    body = read_draft_text(SRC_FILE.read_text(encoding="utf-8"))
    title = first_line_title(body)

    if MODE == "discussion":
        cat_id = get_discussion_category_id(owner, repo, CATEGORY)
        if cat_id:
            res = create_discussion(owner, repo, title, body, cat_id)
            published_url = res.get("html_url")
            channel = f"GitHub Discussion ({CATEGORY})"
        else:
            res = create_issue(owner, repo, title, body, ISSUE_LABELS)
            published_url = res.get("html_url")
            channel = "GitHub Issue (fallback)"
    else:
        res = create_issue(owner, repo, title, body, ISSUE_LABELS)
        published_url = res.get("html_url")
        channel = "GitHub Issue"

    if not published_url:
        die("Publish succeeded but no URL returned from GitHub.")

    append_log(LOG_FILE, channel, published_url, body)
    print(f"Published: {published_url}")

if __name__ == "__main__":
    main()
