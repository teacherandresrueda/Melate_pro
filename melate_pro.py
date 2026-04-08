import streamlit as st
import random
from collections import Counter

st.title("🔥 Melate Retro PRO")

# ======================
# DATA
# ======================
if "resultados" not in st.session_state:
    st.session_state.resultados = [
        {"fecha": "2026-03-17", "numeros": [7,20,21,25,26,30], "rojo": 32},
        {"fecha": "2026-03-21", "numeros": [9,21,24,26,31,35], "rojo": 23},
        {"fecha": "2026-03-24", "numeros": [7,8,16,18,29,33], "rojo": 12},
        {"fecha": "2026-03-28", "numeros": [13,14,24,29,31,35], "rojo": 5},
        {"fecha": "2026-04-01", "numeros": [4,11,17,22,26,39], "rojo": 33},
        {"fecha": "2026-04-04", "numeros": [7,12,22,31,37,38], "rojo": 35}
    ]

if "jugadas" not in st.session_state:
    st.session_state.jugadas = [
        {"fecha": "2026-04-04", "numeros": [7,12,22,30,33,45], "rojo": 0},
        {"fecha": "2026-04-04", "numeros": [7,12,22,31,37,47], "rojo": 0},
        {"fecha": "2026-04-04", "numeros": [7,12,22,31,37,49], "rojo": 0},
        {"fecha": "2026-04-04", "numeros": [7,12,22,33,38,45], "rojo": 0}
    ]

# ======================
# MENU
# ======================
menu = st.sidebar.selectbox("Menú", [
    "Resultados oficiales",
    "Mis jugadas",
    "Dashboard",
    "🧠 Generador PRO",
    "💀 Generador NIVEL DIOS"
])

# ======================
# RESULTADOS
# ======================
if menu == "Resultados oficiales":

    fecha = st.text_input("Fecha")
    nums = st.text_input("Números")
    rojo = st.number_input("Rojo", 0, 99)

    if st.button("Guardar"):
        st.session_state.resultados.append({
            "fecha": fecha,
            "numeros": list(map(int, nums.split(","))),
            "rojo": rojo
        })

# ======================
# JUGADAS
# ======================
elif menu == "Mis jugadas":

    fecha = st.text_input("Fecha jugada")
    nums = st.text_input("Tus números")
    rojo = st.number_input("Tu rojo", 0, 99)

    if st.button("Guardar jugada"):
        st.session_state.jugadas.append({
            "fecha": fecha,
            "numeros": list(map(int, nums.split(","))),
            "rojo": rojo
        })

# ======================
# DASHBOARD
# ======================
elif menu == "Dashboard":

    for o in st.session_state.resultados:
        for j in st.session_state.jugadas:
            if o["fecha"] == j["fecha"]:

                aciertos = set(o["numeros"]) & set(j["numeros"])

                st.subheader(f"📅 {o['fecha']}")
                st.write(f"Aciertos: {len(aciertos)}")
                st.write(list(aciertos))

# ======================
# GENERADOR PRO
# ======================
elif menu == "🧠 Generador PRO":

    cantidad = st.slider("Número de jugadas", 1, 5, 3)

    nucleo = [7,22,31]
    bajos = list(range(1,11))
    medios = list(range(11,21))
    altos = list(range(21,40))

    for i in range(cantidad):
        jugada = set(nucleo)
        jugada.add(random.choice(bajos))
        jugada.add(random.choice(medios))
        jugada.add(random.choice(altos))

        st.write(f"Jugada {i+1}: {sorted(list(jugada)[:6])}")

# ======================
# NIVEL DIOS
# ======================
elif menu == "💀 Generador NIVEL DIOS":

    resultados = st.session_state.resultados
    jugadas = st.session_state.jugadas

    freq_resultados = Counter([n for r in resultados for n in r["numeros"]])
    freq_jugados = Counter([n for j in jugadas for n in j["numeros"]])

    def evaluar(jugada):
        score = 0
        for n in jugada:
            score += freq_resultados.get(n, 0) * 2
            score += freq_jugados.get(n, 0)
        return score

    candidatos = []

    for _ in range(100):
        j = random.sample(range(1,40),6)
        candidatos.append((j, evaluar(j)))

    top = sorted(candidatos, key=lambda x: x[1], reverse=True)[:3]

    for i, (j, s) in enumerate(top):
        st.write(f"Top {i+1} (Score {s}): {sorted(j)}")