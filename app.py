
import streamlit as st
import random

# Simulated avatars
avatars = {
    "Beleidsmaker": "🧑‍💼",
    "Developer": "👨‍💻",
    "Burger": "🧍",
    "Onderzoeker": "🔬"
}

st.set_page_config(page_title="AI & Ethiek Playground", layout="centered")

st.title("🎡 AI & Ethiek Playground")
st.markdown("Ervaar de ethiek van AI-toepassingen interactief.")

if "avatar" not in st.session_state:
    st.session_state.avatar = None

# Avatar keuze
if st.session_state.avatar is None:
    st.subheader("👤 Kies je rol")
    choice = st.radio("Wie ben jij vandaag?", list(avatars.keys()))
if st.button("Start"):
    st.session_state.avatar = choice
    st.success("Avatar gekozen. Herlaad de pagina om verder te gaan.")
    st.stop()  # Voorkomt verdere uitvoer in deze sessie
else:
    st.success(f"Welkom, {st.session_state.avatar}! {avatars[st.session_state.avatar]}")

    st.header("🏘️ Dilemma: AI voor woningtoewijzing")
    st.image("images/woning_ai_retro.png", caption="Een retro visual van woningdata-analyses")
    st.markdown("Een gemeente wil AI inzetten voor woningtoewijzing. "
                "De AI voorspelt wie langdurig en zonder overlast blijft wonen.")
    keuze = st.radio("Mag de AI gezinsgrootte, inkomen en woonhistorie meewegen?",
                     ["✅ Ja", "⚠️ Alleen anoniem", "❌ Nee, risico op uitsluiting"])

    if keuze:
        st.subheader("💡 Analyse")
        if keuze.startswith("✅"):
            st.markdown("**Impact:** Meer stabiliteit, maar mogelijk indirecte discriminatie.")
        elif keuze.startswith("⚠️"):
            st.markdown("**Impact:** Privacy beter geborgd, maar lagere voorspelkracht.")
        else:
            st.markdown("**Impact:** Minimale bias, maar misschien inefficiënt toewijzingsmodel.")

    st.header("📊 AI Impact Scan")
    transparantie = st.slider("Transparantie", 0, 10, 5)
    uitlegbaarheid = st.slider("Uitlegbaarheid", 0, 10, 5)
    bias = st.slider("Bias-gevoeligheid", 0, 10, 5)
    governance = st.slider("Governance", 0, 10, 5)
    impact = st.slider("Publieke impact", 0, 10, 5)
    beheersbaarheid = st.slider("Beheersbaarheid", 0, 10, 5)

    if st.button("Toon resultaat"):
        score = (transparantie + uitlegbaarheid + bias + governance + impact + beheersbaarheid) / 6
        st.subheader("🧠 Ethiek Profiel")
        if score >= 7:
            st.success("Je AI-project is robuust en verantwoord opgezet. Profiel: Zorgvuldige Innovator")
        elif score >= 4:
            st.warning("Je AI-toepassing is redelijk, maar verdient verbetering. Profiel: Voorzichtige Verkenner")
        else:
            st.error("Hoge risico’s! Profiel: Ethiek Alarmfase Rood")

        st.markdown("📩 Wil je je resultaten ontvangen of bespreken? Klik hieronder:")
        st.markdown("[Plan een gesprek](https://calendly.com/adrikelzing)")

