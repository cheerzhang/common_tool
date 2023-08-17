import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from util import model_ml
import joblib
import mlflow


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

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
        col_option1, col_option2 = st.columns(2)
        with col_option1:
            option_model = st.selectbox('Which model is using?', ['Logistic', 'XGB'])
        with col_option2:
            option_lambda = st.number_input('Insert Lambda', min_value=0.1, value=3.0)
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
            model_logistic_filename = "./models/logistic_gender.pkl"
            joblib.dump(obj_model.model, model_logistic_filename)
            with open(model_logistic_filename, 'rb') as f:
                model_logistic_bytes = f.read()
            st.download_button(label='Download Logistic Model', data=model_logistic_bytes, file_name='logistic_gender.pkl')
        with col_option2:
            model_countvectorizer_filename = "./models/countvectorizer_gender.pkl"
            joblib.dump(obj_model.vectorizer, model_countvectorizer_filename)
            with open(model_countvectorizer_filename, 'rb') as f:
                model_countvectorizer_bytes = f.read()
            experiment_name = st.text_input('Experience Name', 'LogModel')
            # st.download_button(label='Download CountVectorizer Model', data=model_countvectorizer_bytes, file_name='countvectorizer_gender.pkl')
            if st.button('Load CountVectorizer Model'):
                mlflow.set_tracking_uri("http://16.170.205.178:5000")
                experiment = mlflow.get_experiment_by_name(experiment_name)
                if experiment is None:
                    experiment = mlflow.create_experiment(name=experiment_name)
                with mlflow.start_run(experiment_id=experiment.experiment_id) as run:
                    # Log parameters
                    mlflow.log_params({'name': 'countvectorizer_gender'})
                    # Log the model - pytorch
                    # mlflow.pytorch.log_model(model, artifact_path=model_name)
                    # log model - sklearn
                    mlflow.sklearn.log_model(obj_model.vectorizer, 'countvectorizer_gender.pkl')
                    st.success(f"Log model - countvectorizer_gender succeed")
                
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