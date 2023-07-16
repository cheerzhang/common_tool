import streamlit as st
import pandas as pd
import re

st.title('Dutch Article')
txt = st.text_area('type in the article', ' ')

path = 'data/dutch.csv'
voc = pd.read_csv(path)

def clean(word):
    pattern = r"[.,']"
    cleaned_text = re.sub(pattern, '', word)
    return cleaned_text

def get_unknow_word(word, voc):
    word_ = clean(word)
    if word_ not in voc['word'].unique():
        return f"({word}:xxx)"
    else:
        translate = voc[voc['word'] == word_]['translate'].values[0]
        return word

words = txt.split()
str_new = ' '.join(get_unknow_word(w, voc) for w in words)
st.write(str_new)
if st.button('Add all words'):
    st.bollon()