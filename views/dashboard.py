import streamlit as st
import pandas as pd
from utils.db import get_connection

def show():
    st.title("📊 Dashboard Escolar")

    # Conexão com o banco
    conn = get_connection()

    # 1️⃣ Total de Estudantes
    total_estudantes = conn.execute("SELECT COUNT(*) FROM estudantes").fetchone()[0]

    # 2️⃣ Total de Documentos
    total_documentos = conn.execute("SELECT COUNT(*) FROM documentos").fetchone()[0]

    st.metric("Total de Estudantes", total_estudantes)
    st.metric("Total de Documentos", total_documentos)

    # 3️⃣ Gráfico de distribuição de estudantes por inicial do nome
    df_estudantes = pd.read_sql("SELECT nome, nota FROM estudantes", conn)

    if not df_estudantes.empty:
        st.subheader("Distribuição de Notas dos Estudantes")
        st.bar_chart(df_estudantes.set_index('nome')['nota'])
    else:
        st.info("Nenhum estudante cadastrado ainda para gerar gráfico.")

    # 4️⃣ Lista interativa de estudantes
    st.subheader("Lista de Estudantes")
    if not df_estudantes.empty:
        st.dataframe(df_estudantes[['nome']])
    else:
        st.info("Nenhum estudante cadastrado.")

    conn.close()
