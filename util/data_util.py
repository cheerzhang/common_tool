import pandas as pd
import time, random

class DATA_PROCESS:
    def __init__(self, name="data function"):
        self.name = name
    
    def remove_duplicate(self, df, unique_id = 'id'):
        df.drop_duplicates(subset=unique_id, keep='first', inplace=True)
        return df

    def combine_df_up_down(self, df1, df2, unique_id = 'id'):
        df_new = pd.concat([df1, df2], axis=0)
        df_new = self.remove_duplicate(df_new, unique_id)
        return df_new 

class Time_Tool:
    def __init__(self, name='time_tool'):
        self.name = name
        self._start_time = time.time()
        self._end_time = None

    def format_duration(self, duration):
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        return f"{hours}h {minutes}min {seconds}sec"

    def start_timer(self):
        start_time = time.time()
        self._start_time = start_time

    def end_timer(self):
        end_time = time.time()
        self._end_time = end_time
        msg = self.format_duration(self._end_time - self._start_time)
        return msg

class Fraud_FE:
    def __init__(self, name = 'fraud'):
        self.name = name
    def split_data(self, df, uid = 'id', ratio_train = 0.8, random_seed = 42):
        random.seed(random_seed)
        uniq_ = df[uid].unique()
        n_all = len(uniq_)
        n_20p_v = round(n_all * (1 - ratio_train))
        valid_user = random.choices(uniq_, k=n_20p_v)
        train_user = [item for item in uniq_ if item not in valid_user]
        df_train = df[df[uid].isin(train_user)]
        df_valid = df[df[uid].isin(valid_user)]
        # X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
        # X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
        return df_train, df_valid
    def get_features(self, df):
        to_lower_list = ['company_name', 'customer_postcode',
                         'customer_first_name', 'customer_last_name', 'customer_initials', 'customer_email',
                         'customer_street', 'customer_house_extension', 'customer_city', 'customer_country_code',
                         'customer_delivery_street', 'customer_delivery_house_extension', 'customer_delivery_city']
        super().lower_string_for_column(df, to_lower_list)
        # name features
        df['first_name_len'] = df['customer_first_name'].str.len()
        df['last_name_len'] = df['customer_last_name'].str.len()
        df['initials_len'] = df['customer_initials'].str.len()
        df['A_first_name'] = df['customer_first_name'].str[0:1]
        df['A_last_name'] = df['customer_last_name'].str[0:1]
        # 
        df['customer_first_name'] = df['customer_first_name'].fillna('unknown')
        df['customer_last_name'] = df['customer_last_name'].fillna('unknown')
        df['customer_initials'] = df['customer_initials'].fillna('unknown')
        #
        df['initials'] = df['customer_initials'].str.replace('.', '').str.extract(r'([a-zA-Z])')[0]
        df['same_as_first_name'] = df.apply(lambda row: 1 if row['initials'] == row['A_first_name'] else 0, axis=1)
        # gender features
        df['customer_sex'] = df['customer_sex'].fillna('U')
        gender_map = {'U': 0, 'O': 0, 'unknown': 0,
                      'M': 1, 'mr': 1,
                      'W': 2, 'V': 2, 'F': 2, 'mrs': 2}
        df['gender'] = df['customer_sex'].map(gender_map)
        # age features
        df['age'] = super().calculate_age(df, 'customer_birthdate')
        df['birth_month'] = df['customer_birthdate'].dt.month
        df['birth_day'] = df['customer_birthdate'].dt.day
        df['birth_week'] = df['customer_birthdate'].dt.dayofweek
        # email
        df['email_host'] = df['customer_email'].str.split('.').str[-1]
        df['email_server'] = df['customer_email'].str.split('@').str[-1].str.split('.').str[0]
        # phone
        # delivery address - address
        df = super().process_typo(df, 'customer_postcode')
        df['postcode_2'] = pd.to_numeric(df['customer_postcode'].str[0:2], errors='coerce').astype(float)
        df['postcode_4'] = pd.to_numeric(df['customer_postcode'].str[0:4], errors='coerce').astype(float)
        df['postcode_2str'] = 'P_'+df['customer_postcode'].str[0:2]
        df['postcode_4str'] = 'P_'+df['customer_postcode'].str[0:4]
        if df['customer_house_number'].dtype == 'object':
            df['house_number'] = df['customer_house_number'].str.extract(r'(\d+)', expand=False).astype(float)
        else:
            df['house_number'] = df['customer_house_number']
        df['same_as_street'] = df.apply(lambda row: 1 if row['customer_street'] == row['customer_delivery_street'] else 0, axis=1)
        df['same_as_city'] = df.apply(lambda row: 1 if row['customer_city'] == row['customer_delivery_city'] else 0, axis=1)
        if df['customer_delivery_house_number'].dtype == 'object':
            df['d_house_number'] = df['customer_delivery_house_number'].str.extract(r'(\d+)', expand=False).astype(float)
        else:
            df['d_house_number'] = df['customer_delivery_house_number']
        df['same_as_house_number'] = df.apply(lambda row: 1 if row['customer_house_number'] == row['customer_delivery_house_number'] else 0, axis=1)
        df['same_as_house_extension'] = df.apply(lambda row: 1 if row['customer_house_extension'] == row['customer_delivery_house_extension'] else 0, axis=1)
        # company information - name
        df['client_idstr'] = 'C_' + df['client_id'].astype(str)
        # company information - address
        # company - size ...
        # order amount
        # order time
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        df['order_month'] = df['created_at'].dt.month
        df['order_day']   = df['created_at'].dt.day
        df['order_week']  = df['created_at'].dt.dayofweek
        df['order_hour']  = df['created_at'].dt.hour
        return df