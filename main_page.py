import streamlit as st

# Title: Data Scientist Work Note
st.markdown("# Data Scientist Work Note")

# First title: Data Task
st.markdown("## Quick Data Task")

# Pages under Data Task
col1, col2 = st.columns(2)
with col1:
    with st.expander(" [[Tool] Combind dataframe](/tool_combine_df)"):
        st.markdown("""
        This tool for combind 2 dataframe concat and drop the duplicate rows (by id)
        """)
    with st.expander(" [[Tool] Plot with custmized data](/tool_plot_with_data)"):
        st.markdown("""
        This tool line chart with customized data and column names
        """)
with col2:
    with st.expander(" [[Tool] Gender](/tool_generate_gender)"):
        st.markdown("""
            The task is to prepare gender classification model. 
            """)
    with st.expander(" [[Tool] Plot with file](/tool_plot_with_file)"):
        st.markdown("""
            The task is to plot data from a file.
            """)

# Second title: Modeling
st.markdown("## Modeling")
col3, col4 = st.columns(2)
with col3:
    with st.expander(" [[Model] Membedding](/model_embedding)"):
        st.markdown("""
        Embedding model for binary classification task
        """)
    with st.expander(" [[Model] Regression](/model_regression)"):
        st.markdown("""
        Regression Model for future prediction
        """)
    with st.expander(" [[Model] Gender](/model_gender_classification)"):
        st.markdown("""
        Classify the gender by first name
        """)
with col4:
    with st.expander(" [[Model] Gender](/model_gender_classification)"):
        st.markdown("""
        Classify the gender by first name
        """)

