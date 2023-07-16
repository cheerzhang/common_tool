import streamlit as st
import pandas as pd

st.title('Dutch Article')
txt = st.text_area('type in the article', ' ')
st.write(txt)


path = 'data/dutch.csv'
voc = pd.read_csv(path)
st.dataframe(voc)

def get_unknow_word(word, voc):
    if word.strip("'") not in voc['word'].unique():
        st.write(f"unknown word : {word}")
    else:
        translate = voc[voc['word'] == word]['translate'].values[0]
        st.write(f"word : {word} - {translate}")

str_new = ''
for v in txt.split():
    str_new = str_new + get_unknow_word(v, voc)


st.write(str_new)