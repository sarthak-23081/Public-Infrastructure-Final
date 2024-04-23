import streamlit as st
from gpt4all import GPT4All

def generate_text(prompt):
    model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf')  # replace with the model you want to use
    with model.chat_session():
        response = model.generate(prompt, temp=0.5)
    message = response.strip()
    return message

st.title('Public Infrastructure Chat')

prompt = st.text_input('Enter your prompt:', 'Type here...')
if st.button('Generate'):
    with st.spinner('Generating text...'):
        generated_text = generate_text(prompt)
    st.text_area('Generated Text:', generated_text,height=200)
