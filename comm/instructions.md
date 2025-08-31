# External Communication Module — Instructions

This module turns any project folder into a **plug-and-play communication hub**.  
It manages the loop: **Draft → Publish → Log**.

---

## 📖 How to Use

1. **Draft**  
   - Open `/comm/direct_drop.md`.  
   - Write your outbound message under the **Draft** section.  
   - Keep it short (≤550 characters for LinkedIn, ≤280 for X).  
   - Place links on their own line.

2. **Publish**  
   - Run the bridge (e.g., `/comm/publish_to_github.py`).  
   - The bridge pushes your draft to the external platform (GitHub Discussion or Issue).  
   - Alternative: use `/comm/bridges/github_bridge.md` to connect via no-code automation.

3. **Log**  
   - The bridge automatically appends a new entry in `/comm/logs/_index.md`.  
   - Each log entry includes:  
     - Date  
     - Channel (where published)  
     - Full text (or snippet)  
     - Link to the external post  

---

## 🛠 Components

- `instructions.md` → this file, quick guide.  
- `system_files.md` → full framework docs.  
- `direct_drop.md` → staging area for each draft.  
- `logs/_index.md` → running history of all published messages.  
- `bridges/` → scripts or configs to push to external platforms (GitHub, LinkedIn, etc.).

---

## 🧭 Notes

- You can add more bridges (e.g., `linkedin_bridge.md`, `twitter_bridge.md`).  
- Always keep `/comm/logs/_index.md` updated — it’s your source of truth.  
- For automation, hook into GitHub Actions or Zapier/n8n to run the bridge when `direct_drop.md` changes.  
- This module is **portable**: copy `/comm` into any repo to instantly enable external comms.
