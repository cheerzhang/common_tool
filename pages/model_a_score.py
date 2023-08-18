import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time, datetime
from datetime import date, timedelta
from util import model_ml, data_util

def app():
    time_tool = data_util.Time_Tool()
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
        df = pd.read_csv(uploaded_fraud_file)
        with st.expander('get labels'):
            st.dataframe(df.head(5))
            bar_ = df.groupby(['category'])['id'].count()
            st.bar_chart(data = bar_, use_container_width=True)
            st.dataframe(bar_)
            pie_ = df.groupby(['label'])['id'].count()
            fig, ax = plt.subplots()
            ax.pie(pie_.values, labels=pie_.index, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.pyplot(fig)
            st.write(f"total data size: {df.shape[0]}, bad transcations size: {df[df['label']==1].shape[0]}")
        with st.expander('split data'):
            obj_item = data_util.Fraud_FE()
            random_seed = st.number_input('Insert random seed', value=42, step=1)
            train_, validtest_ = obj_item.split_data(df, 'id', 0.8, random_seed)
            valid_, test_ = obj_item.split_data(validtest_, 'id', 0.5, random_seed)
            st.write(f"""train bad radio: {round(train_[train_['label']==1].shape[0]/train_.shape[0], 4) * 100} %, 
                        valid bad radio: {round(valid_[valid_['label']==1].shape[0]/valid_.shape[0], 4) * 100} %,
                        test bad radio: {round(test_[test_['label']==1].shape[0]/test_.shape[0], 4) * 100} %""")
            st.write(f"train size: {train_.shape}, valid size: {valid_.shape}, test size: {test_.shape}")
            st.success(f"Processed within {time_tool.end_timer()}")
        st.divider()

if __name__ == '__main__':
    app()