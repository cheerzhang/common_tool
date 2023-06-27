import streamlit as st

# Sample article
article = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus suscipit nisi eget ex consectetur, ac pharetra massa eleifend. Integer vitae elit efficitur, tempor erat et, malesuada libero. Nulla facilisi. Fusce id mauris at urna congue tincidunt ac sit amet justo. Morbi eu mauris nec purus condimentum tempus at id odio. Vestibulum facilisis, magna non mattis varius, dolor orci volutpat sapien, at gravida elit sem eu arcu. Nulla faucibus viverra quam, in rutrum tellus efficitur non. In nec rutrum lacus. Donec in urna nec purus gravida vestibulum nec id urna. Suspendisse sed diam semper, ultrices odio id, auctor ex. Fusce in ligula sit amet justo iaculis suscipit. Cras congue libero urna, vel tincidunt orci tristique vel.

Sed id mauris vitae ipsum luctus fermentum. In volutpat condimentum nisi, eget tincidunt urna tincidunt vel. Fusce pretium tellus vel mi hendrerit, at feugiat elit consectetur. Nunc venenatis turpis lectus, ut dignissim tortor interdum id. Nullam efficitur libero id lectus auctor, non faucibus mi ultrices. Mauris volutpat est sit amet odio iaculis, nec fermentum nulla fringilla. Aliquam at nisi libero. Quisque et leo vitae turpis facilisis dignissim vel in turpis. Sed sollicitudin ligula id elit euismod auctor. Suspendisse potenti. Nam mollis lectus id turpis semper, et facilisis arcu lobortis.

Praesent id feugiat felis. Nulla tincidunt nisl id mauris rhoncus iaculis. Curabitur volutpat varius augue, eu vulputate sem rhoncus a. Sed euismod, elit id tempor feugiat, enim sem finibus mauris, et dictum tellus sem id nisl. Curabitur fermentum diam et erat tristique, sed condimentum tellus hendrerit. Sed tempus nisl nec tellus malesuada, at dictum nunc fermentum. Morbi auctor justo eget dui ultricies semper. In ac nunc at enim ullamcorper scelerisque id et mi. Cras eget convallis nisi. Integer blandit elit justo, et consequat ligula tincidunt ac. Aliquam ullamcorper congue malesuada. Sed bibendum vulputate lorem, id scelerisque lectus finibus in. Proin in eros mauris. Sed sed libero id purus cursus eleifend.
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
