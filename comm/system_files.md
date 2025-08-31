# External Communication Module — System Files

This file is the **complete framework** for how external communication is managed inside a project folder.  
It ensures **consistency, portability, and completeness**.

---

## 📂 File Layout

    comm/
      ├─ instructions.md      # Quick how-to guide
      ├─ system_files.md      # This full framework doc
      ├─ direct_drop.md       # Working draft to publish
      ├─ logs/
      │   └─ _index.md        # Archive of published messages
      └─ bridges/
          └─ github_bridge.md # Example bridge for GitHub

---

## 🔄 Core Loop

1. **Draft** → message is written in `/comm/direct_drop.md`.  
2. **Publish** → bridge pushes it to an external platform (GitHub, LinkedIn, etc.).  
3. **Log** → bridge appends a permanent entry to `/comm/logs/_index.md`.

---

## 🛠 File Purposes

### `instructions.md`
- Lightweight guide for users.  
- Step-by-step “Draft → Publish → Log” workflow.

### `system_files.md`
- This full framework reference.  
- Explains all moving parts and how they connect.  

### `direct_drop.md`
- Where you actually type your outbound draft.  
- Structured with three sections:
  - **Draft**: message text.  
  - **Publish**: checklist before pushing.  
  - **Log**: space where the bridge will append confirmation.

### `logs/_index.md`
- Running log of every external message published.  
- Each entry includes:  
  - Date  
  - Channel (GitHub, LinkedIn, etc.)  
  - Text snippet  
  - Link  

### `bridges/`
- Each file here is a connector to a specific external device/platform.  
- Examples:
  - `github_bridge.md` → pushes to GitHub Discussions or Issues.  
  - `linkedin_bridge.md` → would push to LinkedIn (future).  

---

## 🧭 Principles

- **Portable**: copy `/comm` into any repo to enable comms instantly.  
- **Complete**: everything required to draft, publish, and log lives here.  
- **Consistent**: same workflow no matter the platform.  

---

## 🚀 Extending the Module

- Add more bridges for other platforms.  
- Hook into automation tools (GitHub Actions, Zapier, n8n).  
- Expand logging rules if you need analytics or tagging.  

---

## ✅ Success Criteria

- You can draft in one place (`direct_drop.md`).  
- Publishing always creates an external post.  
- Logs are never skipped — every outbound message has a durable entry.

