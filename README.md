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

###
[![Open in Streamlit](https://character-api-app-starter-pbpbw4akspk2qbnfxrxtus.streamlit.app/)



#### Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

