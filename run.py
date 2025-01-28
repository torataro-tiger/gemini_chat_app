import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("Gemini Chat App")

with st.sidebar:
    api_key = st.text_input("API key", type="password")
    model_name = st.selectbox(
        "Model Select",
        ("gemini-1.5-flash", "gemini-1.5-pro"),
    )
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.10, step=0.01, format="%.2f")
    top_p = st.slider("Top_p", min_value=0.0, max_value=1.0, value=0.10, step=0.01, format="%.2f")
    top_k = st.slider("Top_k", min_value=1, max_value=10, value=5, step=1, format="%.2f")

if api_key:
    llm = ChatGoogleGenerativeAI(
        model=model_name,
        api_key=api_key,  # type: ignore
        top_p=top_p,
        top_k=top_k,
        temperature=temperature,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()

    chain = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
    )
else:
    st.info("APIキーをセットしてください。")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("何か聞いてください")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        res = chain(prompt)
        res_message = res["response"]
        print(res_message)
        st.markdown(res_message)
        st.session_state.messages.append({"role": "assistant", "content": res_message})
