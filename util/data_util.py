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

class IV:
    def __init__(self, name='iv'):
        self.name = name
    
    def calculate_woe_iv(self, df, bin_col, target_col, num_bins = 10, data_range=None, show_report=False):
        # Input validation
        if bin_col not in df.columns:
            raise ValueError(f"{bin_col} is not a column in df")
        if target_col not in df.columns:
            raise ValueError(f"{target_col} is not a column in df")
        if not isinstance(num_bins, int) or num_bins < 1:
            raise ValueError("num_bins must be a positive integer")   
        
        # Get the min and max values of the column
        min_value = data_range[0] if data_range else (df[bin_col].min()-1)
        max_value = data_range[1] if data_range else df[bin_col].max()
        # Generate the bin edges
        bin_edges = np.linspace(min_value, max_value, num=num_bins+1)
        # Cut the data into bins
        df['bins'] = pd.cut(df[bin_col], bins=bin_edges)
        counts = df.groupby(['bins', target_col])[target_col].count().unstack()
        good_class_name = counts.columns[1]
        bad_class_name = counts.columns[0]
        if show_report:
            print('good: ', good_class_name)
            print('bad: ', bad_class_name)
        counts = counts.rename(columns={good_class_name: 'Good', bad_class_name: 'Bad'})
        counts['sum_good'] = counts['Good'].sum() #df[target_col].value_counts()[good_class_name]
        counts['sum_bad'] = counts['Bad'].sum() #df[target_col].value_counts()[bad_class_name]
        counts['ratio_good'] = (counts['Good']) / counts['sum_good']
        counts['ratio_bad'] = (counts['Bad']) / counts['sum_bad']
        counts['woe'] = np.log(counts['ratio_good'] / counts['ratio_bad'])
        counts['good-bad'] = counts['ratio_good'] - counts['ratio_bad']
        counts['iv'] = counts['good-bad'] * counts['woe']
        pd.options.display.float_format = '{:.4f}'.format
        iv = counts['iv'].replace([np.inf, -np.inf, np.nan], 0).sum()
        return iv, counts
    
    def get_iv_tab(self, x):
        if float(x) >= 0.5:
            return 'Suspicious'
        if float(x) >= 0.3:
            return 'Strong'
        if float(x) >= 0.1:
            return 'Moderate'
        if float(x) >= 0.02:
            return 'Weak'
        return 'No predictive power'