import streamlit as st
import openai
import os

response = False

# Verifica se a chave de API do OpenAI foi definida corretamente
if "OPENAI_API_KEY" not in os.environ: 
    st.error("A chave de API do OpenAI não foi definida corretamente. Verifique se você definiu a variável de ambiente 'OPENAI_API_KEY' com sua chave de API do OpenAI.")
    st.stop()

def make_request(question_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{question_input}"},
        ]
    )
    return response


# Render Streamlit page
st.write("# Brainstorming! 🧠")
st.sidebar.success("Insira as informações nos campos correspondentes e clique em Executar.")

st.markdown(
    """
    O Brainstorming é um App desenvolvido para ajudar os estudantes de Python a desenvolverem projetos para o seu portfólio. Esta aplicação foi desenvolvida como exemplo de possibilidades de desenvolvimento com Python + Streamlit + OpenAi API.
    """
)

st.markdown("""---""")


col1, col2 = st.columns(2)
with col1:
    tipo = st.selectbox("Escolha o tipo de projeto", ("Python", "Data Science"))

with col2:
    nivel = st.selectbox("Selecione o nível do projeto", ("Iniciante", "Intermediário", "Avançado"))


quantidade = st.slider("Quantidade de Ideias", 1, 5, 3)

contexto = st.text_area(
    label="Contexto de aplicação (opcional)",
    placeholder="Gostaria de projetos para o contexto do agronegócio...", height=200
)

# Cria o prompt personalizado
prompt = f"Olá, gostaria que você me sugerisse {quantidade} projeto(s) de {tipo} para compor meu portfólio. Meu nível de conhecimento é {nivel}. Considere o contexto {contexto} e me ajude com ideias."

rerun_button = st.button("Executar!")

if rerun_button:
    response = make_request(prompt)
    print(prompt)
else:
    pass

if response:
    st.write("Response:")
    st.write(response["choices"][0]["message"]["content"])