import streamlit as st
import pandas as pd

st.title('Dutch Article')
txt = st.text_area('type in the article', ' ')
st.write(txt)


path = 'data/dutch.csv'
voc = pd.read_csv(path)
st.dataframe(voc)


for v in txt.split():
    if v.strip("'") not in voc['word'].unique():
        st.write(f"unknown word : {v}")