import streamlit as st
import pandas as pd
import re

st.title('Dutch Article')
txt = st.text_area('type in the article', ' ')

path = 'data/dutch.csv'
voc = pd.read_csv(path)
add_words = []
add_translates = []

def clean(word):
    pattern = r"[.,']"
    cleaned_text = re.sub(pattern, '', word)
    return cleaned_text

def get_unknow_word(word, voc):
    word_ = clean(word)
    if word_ not in voc['word'].unique():
        add_words.append(word_)
        add_translates.append(word)
        return f"({word}:xxx)"
    else:
        translate = voc[voc['word'] == word_]['translate'].values[0]
        return word

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

words = txt.split()
str_new = ' '.join(get_unknow_word(w, voc) for w in words)
st.write(str_new)
if st.button('Add all words'):
    add_df = pd.DataFrame({'word': add_words, 'translate': add_translates})
    new_df = pd.concat([voc, add_df], axis=0)
    csv_df = convert_df(new_df)
    st.download_button(
      label="Download data as CSV",
      data=csv_df,
      file_name='dutch.csv', 
      mime='text/csv',
    )
    st.ballons()