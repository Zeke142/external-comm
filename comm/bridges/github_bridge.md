# GitHub Bridge — External Communication Module

This bridge connects the **External Communication Module** to **GitHub**.  
It takes the text in `/comm/direct_drop.md`, publishes it to this repository (as a **Discussion** or **Issue**), and then appends a log entry in `/comm/logs/_index.md`.

## Requirements
- GitHub token with scopes: `repo`, and `discussions:write` (if using Discussions).
- Python 3.10+ (only if running locally; not needed for GitHub Actions).

## How to use
1) Edit `/comm/direct_drop.md` under **Draft**.  
2) Either:
   - Run the local script: `python comm/publish_to_github.py`, or
   - Let GitHub Actions run automatically on commit (see workflow).

The bridge will create a Discussion (or Issue fallback) and append to `/comm/logs/_index.md`.
