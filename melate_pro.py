import streamlit as st
import random
from collections import Counter

st.set_page_config(page_title="RetroCore AI 💀", layout="wide")

st.title("🔥 RetroCore AI")

# ======================
# DATA BASE (temporal)
# ======================
if "resultados" not in st.session_state:
    st.session_state.resultados = [
        {"fecha": "2026-04-04", "numeros": [7,12,22,31,37,38]},
        {"fecha": "2026-04-01", "numeros": [4,11,17,22,26,39]},
        {"fecha": "2026-03-28", "numeros": [13,14,24,29,31,35]},
    ]

if "jugadas" not in st.session_state:
    st.session_state.jugadas = [
        {"fecha": "2026-04-04", "numeros": [7,12,22,31,37,47]},
        {"fecha": "2026-04-01", "numeros": [4,7,12,17,22,31]},
    ]

# ======================
# MENU
# ======================
menu = st.sidebar.selectbox("⚙️ Sistema", [
    "📊 Dashboard",
    "🧠 Generador",
    "💀 Mejor Jugada",
    "📈 Evidencia"
])

# ======================
# 📊 DASHBOARD
# ======================
if menu == "📊 Dashboard":

    st.subheader("📊 Rendimiento")

    total_aciertos = 0
    total = 0

    for o in st.session_state.resultados:
        for j in st.session_state.jugadas:
            if o["fecha"] == j["fecha"]:

                aciertos = set(o["numeros"]) & set(j["numeros"])
                total_aciertos += len(aciertos)
                total += 1

                st.write(f"📅 {o['fecha']}")
                st.write(f"Aciertos: {len(aciertos)} → {list(aciertos)}")

    if total > 0:
        st.metric("Promedio", round(total_aciertos/total,2))

# ======================
# 🧠 GENERADOR
# ======================
elif menu == "🧠 Generador":

    st.subheader("Generador Inteligente")

    base = [7,22,31]

    for i in range(3):
        j = set(base)

        while len(j) < 6:
            j.add(random.randint(1,39))

        st.write(f"Jugada {i+1}: {sorted(j)}")

# ======================
# 💀 MEJOR JUGADA
# ======================
elif menu == "💀 Mejor Jugada":

    resultados = st.session_state.resultados

    freq = Counter([n for r in resultados for n in r["numeros"]])

    mejor = sorted([n for n,_ in freq.most_common(6)])

    st.success(f"🔥 Mejor jugada basada en datos: {mejor}")

# ======================
# 📈 EVIDENCIA
# ======================
elif menu == "📈 Evidencia":

    st.subheader("📈 Evidencia del sistema")

    historial = []

    for o in st.session_state.resultados:
        for j in st.session_state.jugadas:
            if o["fecha"] == j["fecha"]:

                aciertos = len(set(o["numeros"]) & set(j["numeros"]))

                historial.append(aciertos)

    if historial:
        st.write("Historial de aciertos:", historial)

        st.line_chart(historial)

        st.metric("Mejor resultado", max(historial))
        st.metric("Promedio", round(sum(historial)/len(historial),2))

    else:
        st.warning("Aún no hay datos suficientes")
