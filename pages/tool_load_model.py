import streamlit as st
import mlflow
import os, joblib, json

# Set the MLflow tracking URI
with open('config.json') as config_file:
    config = json.load(config_file)
tracking_uri = config["tracking_uri"]
mlflow.set_tracking_uri(tracking_uri)

# Streamlit app
def app():
    st.write('### Load Model from MLflow')
    model_name = st.selectbox(
    'Select Model to load',
    ('logistic_gender', 'countvectorizer_gender'))
    if st.button('Load Model'):
        model_path = f"models:/{model_name}/None"
        loaded_model = mlflow.sklearn.load_model(model_uri=model_path)
        st.success(f"Load model - {model_name} succeed")

        # Save the loaded model to a file (e.g., pickle format)
        model_filename = f"models/{model_name}.pkl"
        joblib.dump(loaded_model, model_filename)

        st.download_button(label='Download Model', data=model_filename, file_name=model_filename)

        # Check if the download button is clicked
        st.write(f"Attempting to delete: {model_filename}")
        if os.path.exists(model_filename):
            os.remove(model_filename)
            st.success(f"Model file '{model_filename}' deleted!")
        else:
            st.error(f"Model file '{model_filename}' not found!")

if __name__ == '__main__':
    app()