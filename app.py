import streamlit as st
from auth import *
import random

st.set_page_config(page_title="Melate AI System 💀", layout="wide")

crear_tabla()

# ======================
# LOGIN
# ======================
menu = st.sidebar.selectbox("Acceso", ["Login", "Registro"])

if menu == "Registro":
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Crear cuenta"):
        registrar(user, password)
        st.success("Cuenta creada")

elif menu == "Login":
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Entrar"):
        if login(user, password):
            st.session_state["login"] = True
        else:
            st.error("Datos incorrectos")

# ======================
# SISTEMA PRINCIPAL
# ======================
if st.session_state.get("login"):

    st.title("🔥 Melate AI Premium")

    seccion = st.sidebar.selectbox("Sistema", [
        "Dashboard",
        "Generador Inteligente",
        "Top Jugada"
    ])

    # ======================
    # GENERADOR
    # ======================
    if seccion == "Generador Inteligente":

        st.subheader("🧠 Generador basado en tu patrón")

        base = [7,22,31]

        jugadas = []

        for _ in range(5):
            j = set(base)
            while len(j) < 6:
                j.add(random.randint(1,39))
            jugadas.append(sorted(list(j)))

        for j in jugadas:
            st.write(j)

    # ======================
    # TOP JUGADA
    # ======================
    if seccion == "Top Jugada":

        mejor = sorted(random.sample(range(1,40),6))

        st.success(f"🔥 Mejor jugada sugerida: {mejor}")

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #00ffcc;
}
</style>
""", unsafe_allow_html=True)
