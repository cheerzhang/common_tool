import streamlit as st

# Sample article
article = """
De milieucommissie van het Europees Parlement is het niet gelukt om een compromis te bereiken over de natuurherstelwet van Eurocommissaris Frans Timmermans. Dit betekent dat in het Europees Parlement alles weer open ligt. Over twee weken stemt het voltallig parlement over de wet.
"""

# Convert the article into a list of words
words = article.split()

# Display the article
st.write(article)

# Function to save the selected word
def save_word(word):
    selected_words = st.session_state.get('selected_words', [])
    if word not in selected_words:
        selected_words.append(word)
        st.session_state.selected_words = selected_words

# Loop through the words and add hover functionality
for word in words:
    hover_text = f'<span style="background-color: yellow;">{word}</span>'
    st.markdown(f'<span title="Click to save" style="cursor: pointer;">{hover_text}</span>', unsafe_allow_html=True)
    if st.markdown_clicks():
        save_word(word)

# Display the selected words
st.write("Selected words:", st.session_state.selected_words)
