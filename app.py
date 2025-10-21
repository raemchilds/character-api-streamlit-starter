import streamlit as st
from character_logic import generate_joke, pick_ironic_situation, Character, SITUATIONS

st.set_page_config(page_title="Character API — Joke Generator", page_icon="🤖")
st.title("🤖 Character API — Joke Generator")

st.markdown(
    "Enter a character's traits, then generate an ironic situation and a joke in their voice."
)

with st.sidebar:
    st.header("Settings")
    seed = st.number_input("Random seed (optional)", value=0, step=1)
    force_context = st.selectbox("Force situation (optional)", ["", *SITUATIONS])

st.subheader("Character")
name = st.text_input("Name", value="Queen Margaret")
blind_spot = st.text_input("Blind Spot", value="Oblivious to her own privilege")
flaw = st.text_input("Flaw", value="Neurotic and indecisive")
attitude = st.text_input("Attitude", value="Overly polite but secretly manipulative")
agenda = st.text_input("Agenda", value="Maintain power at all costs")
catchphrases = st.text_input("Catchphrases (comma-separated)", value="Oh dear!, Surely, you jest!")

if st.button("Generate Joke"):
    c = Character(
        name=name.strip(),
        blind_spot=blind_spot.strip(),
        flaw=flaw.strip(),
        attitude=attitude.strip(),
        agenda=agenda.strip(),
        catchphrases=[p.strip() for p in catchphrases.split(",") if p.strip()],
    )
    situation = force_context or None
    result = generate_joke(c, seed=seed if seed != 0 else None, force_context=situation)
    st.success(f"Ironic Situation: **{result['situation']}**")
    st.write(result["joke"])

st.divider()
st.caption("Glowlock Labs · Streamlit prototype")
