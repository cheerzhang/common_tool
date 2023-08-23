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
    uploaded_fraud_file = st.file_uploader("Choose 'fraud_traning' csv file:", key="fraud_file_tr_upload")
    uploaded_fraud_va_file = st.file_uploader("Choose 'fraud_valiation' csv file:", key="fraud_file_va_upload")
    uploaded_fraud_te_file = st.file_uploader("Choose 'fraud_test' csv file:", key="fraud_file_te_upload")
    uploaded_embedding_file_email_host = st.file_uploader("Choose '[Embedding]email_host' for embedding csv file:", key="email_host_embedding_upload")
    uploaded_embedding_file_email_server = st.file_uploader("Choose '[Embedding]email_server' for embedding csv file:", key="email_server_embedding_upload")
    uploaded_embedding_file_d_street = st.file_uploader("Choose '[Embedding]customer_delivery_street' for embedding csv file:", key="d_street_embedding_upload")
    uploaded_embedding_file_d_city = st.file_uploader("Choose '[Embedding]customer_delivery_city' for embedding csv file:", key="d_city_embedding_upload")
    uploaded_embedding_file_post_code_2 = st.file_uploader("Choose '[Embedding]postcode_2str' for embedding csv file:", key="post_2_embedding_upload")
    uploaded_embedding_file_city = st.file_uploader("Choose '[Embedding]customer_city' for embedding csv file:", key="city_embedding_upload")
    if uploaded_embedding_file_email_host is not None \
    and uploaded_embedding_file_email_server is not None \
    and uploaded_embedding_file_d_street is not None \
    and uploaded_embedding_file_d_city is not None \
    and uploaded_embedding_file_post_code_2 is not None \
    and uploaded_embedding_file_city is not None:
        df_tr = pd.read_csv(uploaded_fraud_file)
        df_va = pd.read_csv(uploaded_fraud_va_file)
        df_te = pd.read_csv(uploaded_fraud_te_file)
        with st.expander('split data'):
            time_tool.start_timer()
            st.write(f"""train bad radio: {round(df_tr[df_tr['label']==1].shape[0]/df_tr.shape[0], 4) * 100} %, 
                        valid bad radio: {round(df_va[df_va['label']==1].shape[0]/df_va.shape[0], 4) * 100} %,
                        test bad radio: {round(df_te[df_te['label']==1].shape[0]/df_te.shape[0], 4) * 100} %""")
            st.write(f"train size: {df_tr.shape}, valid size: {df_va.shape}, test size: {df_te.shape}")
            st.success(f"Processed within {time_tool.end_timer()}")
        st.divider()
        st.subheader('FE and Feature Selection for Model')
        with st.spinner("Feature Engineering..."):
            time_tool.start_timer()
            with st.expander("After FE, train set can be used to train embedding"):
                st.dataframe(df_tr)
            st.success(f"FE for train, valid, test dataframe Done! time using: {time_tool.end_timer()}")
        with st.spinner("Embedding processing..."):
            obj_item = data_util.Fraud_FE()
            time_tool.start_timer()
            emb_fe_arr = []
            df_emb_customer_email_host = pd.read_csv(uploaded_embedding_file_email_host)
            df_emb_customer_email_server = pd.read_csv(uploaded_embedding_file_email_server)
            df_emb_d_street = pd.read_csv(uploaded_embedding_file_d_street)
            df_emb_d_city = pd.read_csv(uploaded_embedding_file_d_city)
            df_emb_post_2 = pd.read_csv(uploaded_embedding_file_post_code_2)
            df_emb_city = pd.read_csv(uploaded_embedding_file_city)
            emb_df = {
                'email_host': df_emb_customer_email_host,
                'email_server': df_emb_customer_email_server,
                'customer_delivery_street': df_emb_d_street,
                'customer_delivery_city': df_emb_d_city,
                'postcode_2str': df_emb_post_2,
                'customer_city': df_emb_city
            }
            for name in emb_df.keys():
                arr_, dftr_fe = obj_item.map_embedding(df_tr, emb_df[name], name)
                _, dfva_fe = obj_item.map_embedding(df_va, emb_df[name], name)
                _, dfte_fe = obj_item.map_embedding(df_te, emb_df[name], name)
                emb_fe_arr = emb_fe_arr + arr_
            st.success(f"Embedding processed within {time_tool.end_timer()}")
        st.divider()
        with st.spinner("check IV and L1..."):
            fe_columns = ['first_name_len', 'last_name_len', 'initials_len', 'same_as_first_name',
                                            'gender', 'age', 'birth_month', 'birth_day', 'birth_week',
                                            'postcode_2', 'postcode_4',
                                            'same_as_street', 'same_as_city', 'house_number', 'd_house_number',
                                            'same_as_house_number', 'same_as_house_extension',
                                            'total_price_inc_vat', 'client_id',
                                            'order_month', 'order_day', 'order_week', 'order_hour']
            numeric_features = emb_fe_arr + fe_columns
            st.dataframe(dftr_fe, use_container_width=True)
            with st.expander('IV'):
                iv_arr = []
                iv_train_df = dftr_fe[numeric_features + ['label']]
                iv_train_df = iv_train_df.fillna(-1)
                iv_obj = data_util.IV()
                for item in numeric_features:
                    iv, counts = iv_obj.calculate_woe_iv(df = iv_train_df,  bin_col = item, target_col = 'label', num_bins = 10, data_range=None, show_report=False)
                    iv_arr.append(iv)
                data = pd.DataFrame({'feature': numeric_features,'iv_value': iv_arr})
                data['tab'] = data['iv_value'].apply(lambda x: iv_obj.get_iv_tab(x))

if __name__ == '__main__':
    app()