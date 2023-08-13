import streamlit as st
import pandas as pd

def get_dataframe():
    uploaded_file = st.file_uploader("Choose a file for training")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        with st.expander('Original Dataframe'):
            st.dataframe(df)

if __name__ == "__main__":
    get_dataframe()
