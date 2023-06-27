import streamlit as st
import pandas as pd

# Sample article
article = """
De milieucommissie van het Europees Parlement is het niet gelukt om een compromis te bereiken over de natuurherstelwet van Eurocommissaris Frans Timmermans. Dit betekent dat in het Europees Parlement alles weer open ligt. Over twee weken stemt het voltallig parlement over de wet.
"""

# Convert the article into a list of words
words = list(set(word.lower() for word in article.split()))

# Display the article
st.write(article)

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
