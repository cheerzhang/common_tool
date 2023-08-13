import streamlit as st

# main 2 column
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Tools")
    with st.expander("[gender data tools](https://commontool-7p2wajolwr.streamlit.app/gender_data)"):
        st.markdown("Goal: Generate a dataset of first names and predict the likely gender associated with each name.")

with col2:
    st.markdown("### Models")

