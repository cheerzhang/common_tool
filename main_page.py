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
    with st.expander(" [[Tool] Graydon](/tool_graydon)"):
        st.markdown("""
            The task involves checking the number of API calls made to the 'Dragen' service in the past year. 
            """)
    with st.expander(" [[Tool] Gender](/tool_generate_gender)"):
        st.markdown("""
            The task is to prepare gender classification model. 
            """)
    with st.expander(" [[Tool] Plot with file](/tool_plot_with_file)"):
        st.markdown("""
            The task is to plot data from a file.
            """)
    with st.expander(" [[Tool] Save model](/tool_save_model)"):
        st.markdown("""Save model from ML """)

# Second title: Modeling
st.markdown("## Modeling")
col4, col5, col6 = st.columns(3)
with col4:
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
with col5:
    with st.expander(" [[Model] A score](/model_a_score)"):
        st.markdown("""
        Application(check) Score for new users
        """)
    with st.expander(" [[Predict] A score](/predict_a_score)"):
        st.markdown("""
        Application(check) Score Model Prediction Page
        """)
with col6:
    with st.expander(" [[Model] B score(sub)](/model_b_score_sub)"):
        st.markdown("""
        Bahavior(payment) Score for existing users (sub model)
        """)
    with st.expander(" [[Model] B score](/model_b_score)"):
        st.markdown("""
        Bahavior(payment) Score for existing users (final model)
        """)
    with st.expander(" [[Predict] B score](/predict_b_score)"):
        st.markdown("""
        Bahavior(payment) Score Model Prediction Page
        """)

st.markdown("## Data Tools")
st.markdown("## Data Analysis Task")
col7, col8, col9 = st.columns(3)
with col7:
    with st.expander(" [[DA] 25-35 Female](/da_25_baseline)"):
        st.markdown("""
        Baseline of 25-35 female users' activities
        """)
