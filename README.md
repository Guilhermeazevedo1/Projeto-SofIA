# SofIA - Sistema de Gestão Escolar com IA

O **SofIA** é um projeto em Python utilizando **Streamlit** para criar um sistema escolar interativo, integrado com **IA generativa** via LangChain e Groq. O sistema permite:

- Cadastrar estudantes (com notas).
- Gerenciar documentos (PDFs, Excel).
- Consultar e gerar conteúdo educativo usando IA.
- Visualizar um dashboard com métricas e gráficos reais dos estudantes e documentos.

---

## 💻 Tecnologias usadas

- Python 3.11+
- Streamlit
- SQLite (banco local `escola.db`)
- Pandas
- PyPDF2 (para leitura de PDFs)
- OpenAI / LangChain / LangChain-Groq (IA generativa)
- FAISS (indexação vetorial para documentos)

---

## 📁 Estrutura do projeto

```
sofia/
├─ app.py # Arquivo principal do Streamlit
├─ data/
│ └─ escola.db # Banco de dados SQLite
├─ controllers/ # Funções que manipulam dados no banco
│ └─ estudante_controller.py
├─ models/ # Models do projeto
│ ├─ estudante_model.py
│ └─ documento_model.py
├─ utils/ # Funções auxiliares
│ ├─ db.py
│ ├─ file_loader.py
│ ├─ limpar_resposta.py
│ └─ qa_chain_groq.py
└─ views/ # Páginas do Streamlit
├─ cadastro.py
├─ conteudo.py
├─ dashboard.py
├─ documentos.py
└─ login.py
```

---

## ⚙️ Configuração do ambiente

1. Criar o ambiente virtual:

```bash
python -m venv venv
```

2. Ativar o ambiente:

**Windows**

```bash
.\venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

3. Atualizar o pip:

```bash
python.exe -m pip install --upgrade pip
```

4. Instalar as dependências:

```bash
pip install load_dotenv streamlit langchain openai pandas PyPDF2 faiss-cpu tiktoken openpyxl langchain-groq langchain-community
```

5. Gerar `requirements.txt` (opcional):

```bash
pip freeze > requirements.txt
```

## 🚀 Rodando o projeto

Certifique-se de que o arquivo `data/escola.db` não está corrompido.

Se estiver, delete o arquivo e o banco será recriado automaticamente.

Rodar o Streamlit:

```bash
streamlit run app.py
```

Navegue pelo menu lateral:

- **Login**: Use `admin` como usuário e `1234` como senha para acessar o sistema.
- **Cadastro**: adicionar estudantes e suas notas.
- **Dashboard**: ver métricas e gráficos de estudantes e documentos.
- **Conteúdo**: gerar conteúdos educativos com IA. **Requer chave Groq configurada.**
- **Documentos**: enviar PDFs ou Excel e conversar com os documentos usando IA. **Requer chave Groq configurada.**

## 📊 Funcionalidades do Dashboard

- Total de Estudantes e Documentos (métricas rápidas).
- Gráfico de distribuição de estudantes por inicial do nome.
- Gráfico de notas dos estudantes.
- Tabela interativa com lista de estudantes e suas notas.

Exemplo de código para gráfico de notas:

```python
df_estudantes = pd.read_sql("SELECT nome, nota FROM estudantes", conn)
if not df_estudantes.empty:
    st.subheader("Distribuição de Notas dos Estudantes")
    st.bar_chart(df_estudantes.set_index(\'nome\')[\'nota\'])
else:
    st.info("Nenhum estudante cadastrado ainda para gerar gráfico.")
```

## 📝 Observações

- As notas só funcionam se a coluna `nota` estiver presente no banco.
- Para reiniciar o banco (desenvolvimento), delete `data/escola.db` e rode o app.
- A integração com IA requer chave da Groq fornecida pelo usuário na interface.

## 🔗 Referências

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq AI](https://groq.com/)

## 📸 Sugestões de melhoria

- Adicionar filtros interativos no dashboard (por notas, letras iniciais, documentos).
- Criar gráficos por faixa de notas ou documentos por tipo.
- Incluir login de usuário para controlar acesso às páginas.
- Melhorar a interface com Streamlit Components ou bibliotecas como Plotly.

---

Se você quiser, eu posso fazer **uma versão final do README com imagens/screenshot do dashboard e do cadastro**, totalmente pronta para colocar no GitHub, que deixa o projeto **profissional e visualmente bonito**.

Quer que eu faça isso também?
