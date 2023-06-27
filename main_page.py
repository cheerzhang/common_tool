import pandas as pd
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Anything ",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.markdown("# Main page ")
st.sidebar.markdown("# Main page 🎈")
