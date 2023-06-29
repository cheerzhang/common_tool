import streamlit as st

highlighted_text = "Hello, **world**!"

st.markdown(f'<span style="background-color: yellow;">{highlighted_text}</span>', unsafe_allow_html=True)

highlighted_text = "Hello, <mark>world</mark>!"

st.markdown(highlighted_text, unsafe_allow_html=True)
