import streamlit as st
import pandas as pd
from util import data_util

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def app():
    st.markdown('# Combind Dataframe')
    time_tool = data_util.Time_Tool()
    df1 = None
    df2 = None
    time_df = st.checkbox("It's time series dataframe")
    upload_df_1 = st.file_uploader("Choose 1st data file:", key="file1_upload")
    upload_df_2 = st.file_uploader("Choose 2nd data file:", key="file2_upload")
    if upload_df_1 is not None and upload_df_2 is not None:
        df1 = pd.read_csv(upload_df_1)
        df2 = pd.read_csv(upload_df_2)
    if df1 is not None and df2 is not None and time_df is True:
        with st.spinner("combineing ..."):
            time_tool.start_timer()
            time_column = st.selectbox('Time Column', df1.columns.values)
            df1[time_column] = pd.to_datetime(df1[time_column], infer_datetime_format=True, errors='coerce')
            st.write(f"file 1 size: :blue[{df1.shape}]")
            st.write(f"file 1 created_at range: :blue[{df1[time_column].min()}] - :blue[{df1[time_column].max()}]")
            df2[time_column] = pd.to_datetime(df2[time_column], infer_datetime_format=True, errors='coerce')
            st.write(f"file 2 size: :blue[{df2.shape}]")
            st.write(f"file 2 created_at range: :blue[{df2[time_column].min()}] - :blue[{df2[time_column].max()}]")
            df_result = pd.concat([df1, df2], axis=0)
            st.write(f"combined dataframe size: {df_result.shape[0]}")
            df_result.drop_duplicates(keep='first', inplace=True)
            st.write(f"combined dataframe size (after drop duplicate): {df_result.shape[0]}")
            st.success(f"combind complated within :blue[{time_tool.end_timer()}]")
            csv = convert_df(df_result)
            file_name = st.text_input('Modify file name', 'combined_df')
            st.download_button( 
                label="Download the combined file",
                data=csv,
                file_name=f'{file_name}.csv',
                mime='text/csv',
            ) 
    if df1 is not None and df2 is not None and time_df is False:
        with st.spinner("combineing ..."):
            time_tool.start_timer()
            st.write(f"file 1 size: :blue[{df1.shape}]")
            st.write(f"file 2 size: :blue[{df2.shape}]")
            df_result = pd.concat([df1, df2], axis=0)
            st.write(f"combined dataframe size: {df_result.shape[0]}")
            df_result.drop_duplicates(keep='first', inplace=True)
            st.write(f"combined dataframe size (after drop duplicate): {df_result.shape[0]}")
            st.write(f'merged: {df_result.shape}')
            st.success(f"combind complated within {time_tool.end_timer()}")
            csv = convert_df(df_result)
            file_name = st.text_input('Modify file name', 'combined_df')
            st.download_button( 
                label="Download the combined file",
                data=csv,
                file_name=f'{file_name}.csv',
                mime='text/csv',
            ) 

if __name__ == '__main__':
    app()