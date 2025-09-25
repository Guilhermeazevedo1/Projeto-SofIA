import streamlit as st
from controllers.estudante_controller import adicionar_estudante, listar_estudantes

def show():
    st.title("📚 Cadastro de Estudantes")
    
    with st.form("cadastro_form"):
        nome = st.text_input("Nome")
        nota = st.number_input("Nota", min_value=0.0, max_value=10.0, step=0.1)
        submitted = st.form_submit_button("Cadastrar")

    if submitted:
        adicionar_estudante(nome, nota)  # alterar função para receber a nota
        st.success("✅ Estudante cadastrado com sucesso!")
    
    st.subheader("Lista de Estudantes")
    estudantes = listar_estudantes()
    for e in estudantes:
        st.write(f"👤 {e.nome}")
