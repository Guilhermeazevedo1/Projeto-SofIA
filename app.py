import streamlit as st
from utils.db import init_db
from views import cadastro, conteudo, dashboard, documentos, login

init_db()
st.title("🥷 SofIA")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login.show()
else:
    st.sidebar.title("📌 Menu")
    opcao = st.sidebar.radio("Navegação", ["Cadastro", "Dashboard", "Conteúdo", "Documentos"])

    if opcao == "Cadastro":
        cadastro.show()
    elif opcao == "Dashboard":
        dashboard.show()
    elif opcao == "Conteúdo":
        conteudo.show()
    elif opcao == "Documentos":
        documentos.show()