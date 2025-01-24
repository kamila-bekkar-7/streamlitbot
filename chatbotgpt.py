import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

 # Display assistant response in chat message container
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            max_tokens = 200,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

    st.header('st.selectbox')

option = st.selectbox(
     'What is your GPT model?',
     ('gpt-3.5-turbo', 'gpt-3.5-turbo-instruct', 'gpt-3.5-turbo-1106','gpt-3.5-turbo-0125'))

st.write('What is your GPT model?', option)

from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Token Limit Slider')

max_tokens = st.slider('Select the maximum number of tokens for GPT generation', 0, 500, 100)
st.write("Maximum tokens selected:", max_tokens)
