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
    data = {'dutch': selected_dutch_words, 'english': selected_english_words}
    st.data_editor(data)
# Display the selected options
st.write('Selected Options:')
st.write('Option 1:', option1)
st.write('Option 2:', option2)



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
