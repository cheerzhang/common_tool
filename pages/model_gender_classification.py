import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from util import model_ml
import joblib
import mlflow
import json

with open('config.json') as config_file:
    config = json.load(config_file)

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def log_mdoel(model_name, model, experiment_name = 'LogModel'):
    tracking_uri = config["tracking_uri"]
    mlflow.set_tracking_uri(tracking_uri)
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        experiment = mlflow.create_experiment(name=experiment_name)
    with mlflow.start_run(experiment_id=experiment.experiment_id) as run:
        # Log parameters
        mlflow.log_params({'name': model_name})
        mlflow.sklearn.log_model(model, model_name)
        return f"Log model - {model_name} succeed"

def app():
    st.markdown('# Gender Classification Model')
    df_file = st.file_uploader("Choose 'gender' file :", key="gender_file_upload")
    df_pred = st.file_uploader("Choose file for predict gender :", key="gender_predict_file_upload")
    if df_file is not None:
        df = pd.read_csv(df_file)
        with st.expander(f"check dataset size {df.shape}"):
            col_data, col_pie = st.columns(2)
            with col_data:
                st.dataframe(df)
            with col_pie:
                fig, ax = plt.subplots()
                num_boys, num_girls = df[df['gender_code'] == 'M'].shape[0], df[df['gender_code'] == 'F'].shape[0]
                ax.pie([num_girls, num_boys], labels=['Female', 'Male'], autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                st.pyplot(fig)
        df['gender_code'] = df['gender_code'].map({'M': 1, 'F': 0})
        # Split the dataset into training and testing sets (80% train, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(df['first_name'], df['gender_code'], test_size=0.2, random_state=42)


        experiment_name = st.text_input('Experience Name', 'LogModel')

        col_option1, col_option2 = st.columns(2)
        with col_option1:
            option_model = st.selectbox('Which model is using?', ['Logistic', 'XGB'])
        with col_option2:
            option_lambda = st.number_input('Insert Lambda', min_value=0.1, value=1.0)
        if option_model == 'XGB':
            obj_model = model_ml.XGB_Gender(lambda_c = option_lambda)
        if option_model == 'Logistic':
            obj_model = model_ml.Logistic_Gender(lambda_c = option_lambda)
        obj_model.train(X_train, y_train, X_test, y_test)
        # Evaluate the model's accuracy on the test set
        # train set
        accuracy_tr, recall_tr, precision_tr = obj_model.metric(X_train, y_train)
        # test set
        accuracy_te, recall_te, precision_te = obj_model.metric(X_test, y_test)
        reesult = {'0': ['train set', 'test set'], 
                   'accuracy': [accuracy_tr, accuracy_te],
                   'precision': [precision_tr, precision_te],
                   'recall': [recall_tr, recall_te]}
        st.dataframe(reesult)
        # download model
        with col_option1:
            if st.button('Log logistic_gender Model'):
                msg = log_mdoel('logistic_gender.pkl', obj_model.model)
                st.success(msg)
        with col_option2:
            if st.button('Log CountVectorizer Model'):
                msg = log_mdoel('countvectorizer_gender.pkl', obj_model.vectorizer)
                st.success(msg)
                
        if df_pred is not None:
            df_p = pd.read_csv(df_pred)
            st.dataframe(df_p)
            # df_p = df_p.dropna()
            df_p = df_p.fillna("")
            # Predict gender for new names
            option_column = st.selectbox('Which column is first name?', df_p.columns.values)
            new_names = df_p[option_column].values
            predictions = obj_model.predict(new_names)
            # Convert numerical predictions back to gender labels
            predicted_genders = ['M' if pred == 1 else 'F' for pred in predictions]
            df_p['pred_gender'] = predicted_genders
            st.markdown("### Prediction")
            col_dataf, col_pie = st.columns(2)
            with col_dataf:
                st.dataframe(df_p[[option_column, 'pred_gender']])
            with col_pie:
                num_boys, num_girls = df_p[df_p['pred_gender'] == 'M'].shape[0], df_p[df_p['pred_gender'] == 'F'].shape[0]
                fig, ax = plt.subplots()
                ax.pie([num_girls, num_boys], labels=['Female', 'Male'], autopct='%1.1f%%', startangle=90)
                ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                st.pyplot(fig)

if __name__ == '__main__':
    app()