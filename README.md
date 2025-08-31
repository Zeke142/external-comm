# 🛰️ External Communication Module

**Purpose**  
A plug-and-play publisher for outward messages. It runs a simple loop:  
**Draft → Publish → Log.**

This README is all you need to set it up from scratch.

---

## ✅ What you’ll get

- A `/comm/` folder you can drop into any repo.
- A Python bridge that reads your draft and publishes to **GitHub Discussions** (or Issues as fallback).
- An auto-appended log (`/comm/logs/_index.md`) with date + link.
- Optional one-click GitHub Action.

---

## 🧰 Prerequisites (one-time)

1) A GitHub account + a repository (public or private).  
2) (Recommended) Enable **Discussions**:  
   - Repo → **Settings → General → Features** → toggle **Discussions**.  
   - Create a Discussion **category** named **Announcements**.  
3) A **Personal Access Token** (classic or fine-grained) with:
   - `repo`  
   - `discussions:write`  
   Save it as an environment variable named `GH_TOKEN` on your machine, and as a **Repository Secret** in GitHub Actions later.

---

## 📦 Install the module (copy these files)

Create the following files in your repo. You can copy/paste from the blocks below.

### 1) `/comm/instructions.md`

```md
# External Communication Module — Instructions

Use this when you want **speed** and **consistency**:
1) Draft in `/comm/direct_drop.md`
2) Run the bridge (local or GitHub Action)
3) Confirm the link
4) Log is auto-appended in `/comm/logs/_index.md`

Checklist before publishing:
- ≤550 chars if cross-posting
- Links each on a new line
- Tone matches your voice (see system_files.md)