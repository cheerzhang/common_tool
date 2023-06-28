import streamlit as st
import pandas as pd

# ---------------------------------- article ---------------------------------------
article_1 = """
Mourinho ook in Italië geschorst na beledigen arbiter; in totaal zes duels toekijken.
"""
article_2 = """
Mourinho also suspended in Italy after insulting referee; watch a total of six matches.
"""
article_3 = """
穆里尼奥在意大利也因侮辱裁判而被禁赛； 总共观看六场比赛.
"""
st.write(article)
# --------------------------------- translate ---------------------------------------
with st.expander("See translation"):
    st.write(article_2)
    st.write(article_3)

# Convert the article into a list of words
words_1 = list(set(word.lower() for word in article_1.split()))
words_2 = list(set(word.lower() for word in article_2.split()))
words_3 = list(set(word.lower() for word in article_3.split()))
with st.beta_container():
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        option1 = st.selectbox('Dutch', words_1)
    with col2:
        option2 = st.selectbox('English', words_2)
    with col3:
        option3 = st.selectbox('Chinese', words_3)



# Select a word using a selectbox
selected_word = st.selectbox("Select a word", [''] + words)

# Enter a memo for the selected word
memo = st.text_input("Enter a memo")

# Button to trigger saving the word-memo pair
if st.button("Save"):
    # Store the selected word and memo in a dictionary
    word_memo = {selected_word: memo}

    # Store the word-memo pairs in a list
    selected_words = st.session_state.get('selected_words', [])
    selected_words.append(word_memo)
    st.session_state.selected_words = selected_words

    # Reset the selected_word and memo variables
    selected_word = ''
    memo = ''

# Display the selected words and memos in a table
st.write("Selected words:",  st.session_state.selected_words)
