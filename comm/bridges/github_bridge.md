# GitHub Bridge — External Communication Module

This bridge connects the **External Communication Module** to **GitHub**.  
It takes the text in `/comm/direct_drop.md`, publishes it to this repository (as a **Discussion** or **Issue**), and then appends a log entry in `/comm/logs/_index.md`.

---

## ⚙️ Requirements

- A GitHub repository (this one).  
- GitHub token with:
  - `repo` (for Issues)  
  - `discussions:write` (for Discussions)  
- Python 3.10+ installed locally.  

---

## 🚀 Workflow

1. Write your message in `/comm/direct_drop.md` under **Draft**.  
2. Run the Python bridge:

   ```bash
   export GH_TOKEN=your_token_here
   python comm/publish_to_github.py
