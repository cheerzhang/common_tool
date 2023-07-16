import streamlit as st
import pandas as pd

st.title('Dutch Article')
txt = st.text_area('type in the article', ' ')
st.write(txt)


path = 'data/dutch.csv'
voc = pd.read_csv(path)
st.dataframe(voc)

