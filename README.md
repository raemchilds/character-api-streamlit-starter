# 🤖 Character API — Context-Aware Joke Generator

**Status:** Prototype Complete · **Stack:** Python 3.10, Streamlit, Dataclasses  

---

### 🧩 Overview  
This project is part of **Glowlock Labs**, exploring the intersection of AI and comedy writing.  
The **Character API** generates jokes based on character traits — *Blind Spot, Flaw, Attitude,* and *Agenda* — and dynamically places characters in **ironic situations** for maximum humor.  

Each joke preserves the character’s voice and tone while adapting to new contexts.  
Demo character: **Queen Margaret 👑**

---

### 🎯 Goal  
To build a lightweight joke engine that keeps **character voice consistent** while adapting humor to **contextual irony**.

---

### 💡 Use Case  
- Writers’-room humor generator for sitcoms and animation  
- Character-consistent dialogue tests for AI agents  
- Prototyping tone and persona for story-based products  

---

### 🔧 Tech Stack  
- **Language:** Python 3.10  
- **Libraries:** Streamlit, Dataclasses, Typing, Random  
- **Environment:** macOS / Streamlit Cloud  

**Run locally:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

🧪 Sprint Outcome

✅ Trait-aware irony logic for contextual joke generation
✅ Generated 50+ unique jokes with consistent tone
✅ Ready for deployment via Streamlit Cloud
✅ Reusable codebase for Glowlock Labs humor systems

📄 Example Output

Input Traits:
Oblivious privilege · Neurotic / indecisive · Polite / manipulative
Agenda: maintain power · Catchphrases: “Oh dear!”, “Surely, you jest!”

Generated:

Ironic Situation: hosting a charity event for the poor
Joke: Queen Margaret smiles nervously and says,
“Oh dear!—I do hope they don’t notice the diamond-encrusted donation box!”

🚀 Live Demo

👉 View the Character API on Streamlit

🧠 Next Steps

Add “Archetype Packs” (Royal, Rebel, Fool, Bureaucrat)

Integrate with LyricSmith for punchline rhythm testing

Add visual generation via Glowlock Sensory Engine

✨ Developed by Glowlock Labs — exploring narrative systems through AI and creative computation.
