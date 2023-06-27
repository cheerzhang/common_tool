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

# Initialize selected words as an empty list
selected_words = []

# Loop through the words and add hover functionality
for word in words:
    st.markdown(
        f'<span title="Click to save" style="cursor: pointer;" onclick="saveWord(\'{word}\')">{word}</span>',
        unsafe_allow_html=True
    )

# JavaScript function to save the clicked word
save_word_script = """
<script>
function saveWord(word) {
    // Send the word to the server or perform any other desired action
    console.log("Saving word:", word);
}
</script>
"""

# Display the JavaScript code
st.write(save_word_script, unsafe_allow_html=True)
