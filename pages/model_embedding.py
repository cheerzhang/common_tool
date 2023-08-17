import streamlit as st
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import plotly.graph_objects as go
import random
from util import data_util

st.markdown("# Embedding")

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    return f"{hours}h {minutes}min {seconds}sec"

def plot_after_PCA(df, map_, title):
    labels = df['label'].values
    colors = ['blue' if label == 0 else 'red' for label in labels]
    fig = go.Figure(data=go.Scatter3d(
        x=df['PC1'],
        y=df['PC2'],
        z=df['PC3'],
        mode='markers',
        marker=dict(
            size=5,
            color=colors,
            opacity=0.5
        ),
        text=list(map_.keys())
    ))
    fig.update_layout(
        scene=dict(
            xaxis_title='Principal Component 1 (PC1)',
            yaxis_title='Principal Component 2 (PC2)',
            zaxis_title='Principal Component 3 (PC3)'
        ),
        title=f"PCA of Features ({title})"
    )
    st.plotly_chart(fig)

def get_unique_arr(df_train, column):
    df_train[column] = df_train[column].fillna('UNKNOWN')
    df_train[column] = df_train[column].str.lower()
    df_train[column] = df_train[column].str.replace('NAN', 'UNKNOWN')
    unique_arr = df_train[column].unique().tolist()
    return unique_arr

def get_map(unique_arr):
    if 'UNKNOWN' not in unique_arr:
        n_1percent = round(len(unique_arr)*0.01)
        unknown_index = random.sample(range(len(unique_arr)), n_1percent)
        for i in unknown_index:
            unique_arr[i] = 'UNKNOWN'
    enum_arr = list(enumerate(unique_arr))
    enum_arr = [(i, elem) for i, elem in enum_arr if elem != 'UNKNOWN']
    sorted_arr = sorted(enum_arr, key=lambda x: x[1])
    unique_arr = [elem for i, elem in sorted_arr]
    d = {item: idx+1 for idx, item in enumerate(unique_arr)}
    d['UNKNOWN'] = 0
    return d

class EmbeddingModel(nn.Module):
    def __init__(self, num_embeddings, embedding_dim):
        super().__init__()
        self.embedding = nn.Embedding(num_embeddings, embedding_dim)
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(embedding_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.embedding(x)
        x = self.flatten(x)
        x = self.linear(x)
        x = self.sigmoid(x)
        return x
    
def get_embedding(df_train, column, target='label', embed_size=10, epoch=10):
    arr_ = get_unique_arr(df_train, column)
    map_ = get_map(arr_)
    st.write(f"unique arr: {len(arr_)}, map: {len(map_)}")
    df_train['f_encode'] = df_train[column].apply(lambda x: map_[x] if x in map_.keys() else 0)
    print(f"df_train's shape {df_train.shape}")
    model = EmbeddingModel(len(map_), embed_size)
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters())
    X_train = torch.tensor(df_train['f_encode'].values.astype('int64')).unsqueeze(1)
    y_train = torch.tensor(df_train[target].values).float().unsqueeze(1)
    print(f"train x shape: {X_train.shape}, train y shape: {y_train.shape}")
    for epoch in range(epoch):
        optimizer.zero_grad()
        y_pred = model(X_train)
        loss = criterion(y_pred, y_train)
        loss.backward()
        optimizer.step()
    embeddings = model.embedding.weight.data.numpy()
    return map_, embeddings


def app():
    time_tool = data_util.Time_Tool()
    embdding_df = None
    embeddings_ = None
    map_ = None
    col1, col2 = st.columns(2)
    with col1:
        embdding_size = st.number_input('Insert a number(embedding size)', 3)
    with col2:
        train_epoch = st.number_input('Insert a number(traning epoch)', 100)
    uploaded_file = st.file_uploader("Choose csv file with features and label:", key="file_upload")
    if uploaded_file is not None and embeddings_ is None and map_ is None:
        df = pd.read_csv(uploaded_file)
        with st.expander(f"check the df"):
            st.dataframe(df)
        col3, col4 = st.columns(2)
        with col3:
            column_option = st.selectbox('Which column to embedding?', df.columns.values)
        with col4:
            column_label = st.selectbox('Which column to be the label?', df.columns.values)
        
        with st.spinner(f"Train the Embedding for {column_option} ..."):
            time_tool.start_timer()
            map_, embeddings_ = get_embedding(df, column_option, column_label, embdding_size, train_epoch)
            st.success(f"Processed within {time_tool.end_timer()}")
        st.divider()
        with st.spinner(f"Prpare file to be saved ..."):
            embdding_df = pd.DataFrame(embeddings_)
            map_df = pd.DataFrame({
                    'Name': map_.keys(),
                    'Embedding_Label': map_.values()
                })
            map_df['Name'] = map_df['Name'].astype(str).str.lower()
            embdding_df['Name'] = map_df['Name']
    if uploaded_file is None:
        embdding_df = None
        embeddings_ = None
        map_ = None
    if embdding_df is not None:
        csv_data = convert_df(embdding_df)
        st.download_button(
            label="Download data as CSV",
            data=csv_data,
            file_name=f"[Embedding]{column_option}.csv",
            mime='text/csv',
        )
        with st.expander("save embedding and map"):
            st.dataframe(embdding_df, use_container_width=True)
    st.divider()
    if embeddings_ is not None and map_ is not None:
        with st.spinner("PCA processing..."):
            time_tool.start_timer()
            pca = PCA(n_components=3)
            reduced_embeddings = pca.fit_transform(embeddings_)
            pca_df = pd.DataFrame(data=reduced_embeddings, columns=['PC1', 'PC2', 'PC3'])
            pca_df['Name'] = embdding_df['Name']
            emb_arr = pca_df.drop('Name', axis=1).columns
            merged_df = df[[column_option, 'label']].merge(pca_df, left_on=column_option, right_on='Name', how='left')
            plot_after_PCA(merged_df, map_, column_option)
            st.success(f"Processed within {time_tool.end_timer()}")

if __name__ == '__main__':
    app()
