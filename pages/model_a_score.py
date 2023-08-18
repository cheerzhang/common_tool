import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time, datetime
from datetime import date, timedelta
from util import model_ml, data_util

def app():
    st.markdown("New User Score [Fraud]")
    uploaded_fraud_file = st.file_uploader("Choose 'fraud_' csv file:", key="fraud_file_upload")
    uploaded_embedding_file_email_host = st.file_uploader("Choose '[Embedding]email_host' for embedding csv file:", key="email_host_embedding_upload")
    uploaded_embedding_file_email_server = st.file_uploader("Choose '[Embedding]email_server' for embedding csv file:", key="email_server_embedding_upload")
    uploaded_embedding_file_d_street = st.file_uploader("Choose '[Embedding]customer_delivery_street' for embedding csv file:", key="d_street_embedding_upload")
    uploaded_embedding_file_d_city = st.file_uploader("Choose '[Embedding]customer_delivery_city' for embedding csv file:", key="d_city_embedding_upload")
    if uploaded_embedding_file_email_host is not None \
    and uploaded_embedding_file_email_server is not None \
    and uploaded_embedding_file_d_street is not None \
    and uploaded_embedding_file_d_city is not None:
        with st.expander("EDA"):
            dftr_fe = st.session_state['dftr_fe']
            dfva_fe = st.session_state['dfva_fe']
            dfte_fe = st.session_state['dfte_fe']
            st.write(f"train data: size :blue[{dftr_fe.shape}], start from :blue[{dftr_fe['created_at'].min()}] to :blue[{dftr_fe['created_at'].max()}]")
            st.write(f"valid data: size :blue[{dfva_fe.shape}], start from :blue[{dfva_fe['created_at'].min()}] to :blue[{dfva_fe['created_at'].max()}]")
            st.write(f"test data: size :blue[{dfte_fe.shape}], start from :blue[{dfte_fe['created_at'].min()}] to :blue[{dfte_fe['created_at'].max()}]")
            st.write(f"""train bad radio: :blue[{round(dftr_fe[dftr_fe['label']==1].shape[0]/dftr_fe.shape[0], 4) * 100} %] , 
                        valid bad radio: :blue[{round(dfva_fe[dfva_fe['label']==1].shape[0]/dfva_fe.shape[0], 4) * 100} %] ,
                        test bad radio: :blue[{round(dfte_fe[dfte_fe['label']==1].shape[0]/dfte_fe.shape[0], 4) * 100} %]""")
            st.write(f"train size: :blue[{dftr_fe.shape}], valid size: :blue[{dfva_fe.shape}], test size: :blue[{dfte_fe.shape}]")



if __name__ == '__main__':
    app()