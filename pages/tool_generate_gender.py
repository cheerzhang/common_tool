import streamlit as st
import pandas as pd


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


def app():
    st.markdown('# Gender Data Preparing')
    df_exist_file = st.file_uploader("Choose 'exist gender' file :", key="gender_exist_file_upload")
    
    df_file = st.file_uploader("Choose 'gender' file :", key="gender_file_upload")
    if df_file is not None and df_exist_file is not None:
        df_gender = pd.read_csv(df_file)
        first_name_column = st.selectbox('Select first name column', df_gender.columns.values)
        df_exist = pd.read_csv(df_exist_file)
        # remove duplicate
        existing_first_names = set(df_exist['first_name'])
        df_gender = df_gender.rename(columns={first_name_column: 'first_name'})

        df_gender_filtered = df_gender[~df_gender['first_name'].isin(existing_first_names)]
        df_gender_filtered = df_gender_filtered[df_gender_filtered['first_name'].str.len() > 2]
        # 
        df_gender_filtered['gender'] = False
        df_gender_for_girl = df_gender_filtered
        df_gender_for_boy = df_gender_filtered
        st.write(f"data to fill: {df_gender_filtered.shape}")
        col_f, col_m = st.columns(2)
        with col_f:
            st.markdown("Label for Female")
            df_girl = st.data_editor(
                df_gender_for_girl[['first_name', 'gender']],
                column_config={
                    "gender": st.column_config.CheckboxColumn(
                        "Female?",
                        help="Select gender",
                        default=False,
                    )
                },
                disabled=['first_name'],
                hide_index=True,
                key = 'for_girl'
            ) 
            df_girl_ = df_girl[df_girl['gender']==True]
            st.write(f"girls have {df_girl_.shape}")
        with col_m:
            st.markdown("Label for Male")
            df_boy = st.data_editor(
                df_gender_for_boy[['first_name', 'gender']],
                column_config={
                    "gender": st.column_config.CheckboxColumn(
                        "Male?",
                        help="Select gender",
                        default=False,
                    )
                },
                disabled=['first_name'],
                hide_index=True,
                key = 'for_boy'
            ) 
            df_boy_ = df_boy[df_boy['gender']==True]
            st.write(f"boys have {df_boy_.shape}")
        df_girl_['gender_code'] = 'F'
        df_boy_['gender_code'] = 'M'
        result_df = pd.concat([df_girl_, df_boy_], axis=0)
        result_df = result_df[['first_name', 'gender_code']]
        st.dataframe(result_df)
        csv = convert_df(result_df)
        file_name = st.text_input('Modify file name', 'gender_train.csv')
        st.download_button(
            label="Download the result CSV",
            data=csv,
            file_name=file_name,
            mime='text/csv',
        )
if __name__ == '__main__':
    app()