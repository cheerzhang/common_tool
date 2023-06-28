import streamlit as st
import pandas as pd

# ---------------------------------- article ---------------------------------------
article_1 = """
Tientallen mensen bij stille tocht doodgestoken Antoneta (36) in Den Haag
"""
article_2 = """
Dozens of people stabbed to death in a silent march Antoneta (36) in The Hague
"""
article_3 = """
海牙安东内塔的静默游行中数十人被刺死(36)
"""
st.write(article_1)
# --------------------------------- translate ---------------------------------------
with st.expander("See translation"):
    st.write(article_2)
    st.write(article_3)

# Convert the article into a list of words
words_1 = list(set(word.lower() for word in article_1.split()))
option1 = st.multiselect(
    'Dutch',
    [''] + words_1,
    [])
words_2 = list(set(word.lower() for word in article_2.split()))
option2 = st.multiselect(
    'English',
    [''] + words_2,
    [])
if st.button("Add"):
    selected_dutch_words = ''
    selected_english_words = ''
    for item in option1:
        selected_dutch_words = selected_dutch_words + ' ' + item
    for item in option2:
        selected_english_words = selected_english_words + ' ' + item

df_voc = pd.read_csv('../data/dutch.csv')
data = pd.DataFrame({'dutch': [selected_dutch_words], 'english': [selected_english_words]})
st.dataframe(df_voc)
st.data_editor(df_voc)

