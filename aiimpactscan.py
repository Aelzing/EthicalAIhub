import streamlit as st

st.set_page_config(page_title="AI Impact Scan", page_icon="🤖", layout="centered")

st.title("🤖 AI Impact Scan (v1.0 beta)")
st.markdown("Beoordeel ethische risico’s van je AI-systeem in minder dan 1 minuut.")

# Inputs
use_case = st.text_input("Wat is de toepassing van het algoritme?")
doelgroep = st.selectbox("Wie wordt beïnvloed door dit systeem?", [
    "Burgers", "Bedrijven", "Interne medewerkers", "Kinderen", "Kwetsbare groepen"
])
gevoeligheid = st.slider("Hoe gevoelig zijn de gegevens?", 0, 10, 5)
impact = st.slider("Wat is de potentiële impact van fouten?", 0, 10, 5)
uitlegbaarheid = st.slider("Hoe goed is de werking uitlegbaar?", 0, 10, 5)

# Resultaat tonen
if st.button("🧠 Genereer beoordeling"):
    st.subheader("📊 Resultaat")
    risico_score = (gevoeligheid + impact - uitlegbaarheid)
    advies = ""

    if risico_score >= 15:
        advies = "🚨 Hoog risico – voer een volledige AI Impact Assessment uit."
    elif risico_score >= 8:
        advies = "⚠️ Matig risico – toets dit systeem op transparantie en fairness."
    else:
        advies = "✅ Laag risico – minimale ethische toetsing voldoende."

    st.markdown(f"""
    **Toepassing:** {use_case}  
    **Doelgroep:** {doelgroep}  
    **Score:** {risico_score}/20  
    **Advies:** {advies}
    """)
