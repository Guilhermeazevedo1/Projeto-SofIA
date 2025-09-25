import streamlit as st

def show():
    st.title("🔑 Login")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        with st.form("login_form"):
            user = st.text_input("Usuário")
            pwd = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar")

        if submit:
            # Exemplo simples de usuário/senha
            if user == "admin" and pwd == "1234":
                st.session_state.logged_in = True
                st.success("✅ Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("❌ Usuário ou senha inválidos")
    else:
        st.info("Você já está logado.")
        if st.button("Sair"):
            st.session_state.logged_in = False
            st.rerun()
