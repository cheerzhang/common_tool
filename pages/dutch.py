import streamlit as st
import pandas as pd

# Sample article
article = """
De milieucommissie van het Europees Parlement is het niet gelukt om een compromis te bereiken over de natuurherstelwet van Eurocommissaris Frans Timmermans. Dit betekent dat in het Europees Parlement alles weer open ligt. Over twee weken stemt het voltallig parlement over de wet.
"""

# Convert the article into a list of words
words = article.split()

# Display the article
st.write(article)

# Select a word using a selectbox
selected_word = st.selectbox("Select a word", words)

# Store the selected word in an array
selected_words = st.session_state.get('selected_words', [])
if selected_word not in selected_words:
    selected_words.append(selected_word)
    st.session_state.selected_words = selected_words

# Display the selected words
st.write("Selected words:", selected_words)
