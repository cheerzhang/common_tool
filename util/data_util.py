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
        return df_train, df_valid
    
    def get_label(self, df, d2):
        d = 90
        d2_timestamp = pd.Timestamp(d2)
        df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        df['paid_at'] = pd.to_datetime(df['paid_at'], errors='coerce')
        condition_good_df = df[(df['paid_at'] - df['created_at']).dt.days <= d]
        remaining_indices = df.index.difference(condition_good_df.index)
        condition_bad_df = df.loc[remaining_indices][(df.loc[remaining_indices]['paid_at'].isnull()) & ((d2_timestamp - df.loc[remaining_indices]['created_at']).dt.days > d)]
        condition_good_df['category'] = 'Good'
        condition_bad_df['category'] = condition_bad_df['category'].fillna('Unknown')
        combind_df = pd.concat([condition_bad_df, condition_good_df], axis=0)
        label_maps = {'Good': 0, 'Fraude op naam': 1, 'Adres fraude': 2, 'Handelsonbekwaam': 3, 'Unknown': 4}
        combind_df['class_labels'] = combind_df['category'].map(label_maps)
        combind_df['label'] = combind_df['class_labels'].apply(lambda x: 1 if x>0 else 0)
        return combind_df
    
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
    
    def map_embedding(self, df, emb_df, column_name):
        emb_arr = emb_df.drop('Name', axis=1).columns
        merged_df = df.merge(emb_df, 
                                  left_on=column_name, 
                                  right_on='Name', 
                                  how='left')
        merged_df = merged_df.drop(columns=['Name'])
        for item in emb_arr:
            new_column_name = f"emb_{column_name}_{item}" 
            merged_df.rename(columns={item: new_column_name}, inplace=True)
        emb_fe_arr = [f"emb_{column_name}_{item}"  for item in emb_arr]
        return emb_fe_arr, merged_df