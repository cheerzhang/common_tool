import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time, datetime
from datetime import date, timedelta
from util import model_ml, data_util

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def app():
    time_tool = data_util.Time_Tool()
    st.markdown("New User Score [Fraud]")
    d2 = st.date_input(
        "Select created_at start date for prediction",
        datetime.datetime.today() - timedelta(days=1)
    )
    uploaded_fraud_file = st.file_uploader("Choose 'fraud_' csv file:", key="fraud_file_upload")
    uploaded_embedding_file_email_host = st.file_uploader("Choose '[Embedding]email_host' for embedding csv file:", key="email_host_embedding_upload")
    uploaded_embedding_file_email_server = st.file_uploader("Choose '[Embedding]email_server' for embedding csv file:", key="email_server_embedding_upload")
    uploaded_embedding_file_d_street = st.file_uploader("Choose '[Embedding]customer_delivery_street' for embedding csv file:", key="d_street_embedding_upload")
    uploaded_embedding_file_d_city = st.file_uploader("Choose '[Embedding]customer_delivery_city' for embedding csv file:", key="d_city_embedding_upload")
    if uploaded_embedding_file_email_host is not None \
    and uploaded_embedding_file_email_server is not None \
    and uploaded_embedding_file_d_street is not None \
    and uploaded_embedding_file_d_city is not None:
        obj_item = data_util.Fraud_FE()
        df = obj_item.get_label(df, d2)
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
            random_seed = st.number_input('Insert random seed', value=42, step=1)
            train_, validtest_ = obj_item.split_data(df, 'id', 0.8, random_seed)
            valid_, test_ = obj_item.split_data(validtest_, 'id', 0.5, random_seed)
            st.write(f"""train bad radio: {round(train_[train_['label']==1].shape[0]/train_.shape[0], 4) * 100} %, 
                        valid bad radio: {round(valid_[valid_['label']==1].shape[0]/valid_.shape[0], 4) * 100} %,
                        test bad radio: {round(test_[test_['label']==1].shape[0]/test_.shape[0], 4) * 100} %""")
            st.write(f"train size: {train_.shape}, valid size: {valid_.shape}, test size: {test_.shape}")
            st.success(f"Processed within {time_tool.end_timer()}")
        st.divider()
        st.subheader('FE and Feature Selection for Model')
        with st.spinner("Feature Engineering..."):
            start_time = time.time()
            dftr_fe = obj_item.get_features(train_)
            dfva_fe = obj_item.get_features(valid_)
            dfte_fe = obj_item.get_features(test_)
            st.success(f"Processed within {time_tool.end_timer()}")
            with st.expander("After FE, train set can be used to train embedding"):
                st.dataframe(dftr_fe)
            csv = convert_df(dftr_fe)
            st.download_button(
                label="Download the result CSV",
                data=csv,
                file_name='[Embedding]with_label.csv',
                mime='text/csv',
            )
            st.success(f"FE for train, valid, test dataframe Done! time using: {time_tool.end_timer()}")
        with st.spinner("Embedding processing..."):
            time_tool.start_timer()
            emb_fe_arr = []
            df_emb_customer_email_host = pd.read_csv(uploaded_embedding_file_email_host)
            df_emb_customer_email_server = pd.read_csv(uploaded_embedding_file_email_server)
            df_emb_d_street = pd.read_csv(uploaded_embedding_file_d_street)
            df_emb_d_city = pd.read_csv(uploaded_embedding_file_d_city)
            emb_df = {
                'email_host': df_emb_customer_email_host,
                'email_server': df_emb_customer_email_server,
                'customer_delivery_street': df_emb_d_street,
                'customer_delivery_city': df_emb_d_city
            }
            obj_item = data_ml.Fraud_FE()
            for name in emb_df.keys():
                arr_, df_ = obj_item.map_embedding(dftr_fe, emb_df[name], name)
                _, df_va = obj_item.map_embedding(dfva_fe, emb_df[name], name)
                _, df_te = obj_item.map_embedding(dfte_fe, emb_df[name], name)
                dftr_fe = df_
                dfva_fe = df_va
                dfte_fe = df_te
                emb_fe_arr = emb_fe_arr + arr_
            st.success(f"Embedding processed within {time_tool.end_timer()}")

if __name__ == '__main__':
    app()