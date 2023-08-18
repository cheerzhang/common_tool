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