import streamlit as st 
import os
import pandas as pd
from dotenv import load_dotenv
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI



load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')



llm = OpenAI(api_token=api_key)

st.title("Prompt-driven analysis with PandasAI")
uploaded_file = st.file_uploader("Upload a csv file for analisis", type=['csv'])

def text():
    prompt = st.text_area("Enter your prompt:")
    return prompt

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(3))
    prompt = text()
    if st.button("Generate"):
        if prompt:
            with st.spinner('Genereting response...'):
                pandas_ai = SmartDataframe(df, config={"llm": llm})
                response = pandas_ai.chat(prompt)
                st.write(response)
        else:
            st.warning("Please enter a prompt.")


