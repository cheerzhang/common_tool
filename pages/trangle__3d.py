import streamlit as st
import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Define the vertices of the triangle
vertices = [[0, 0, 0], [1, 0, 0], [0.5, 0.5, 1]]

# Create the triangular roof shape
for i, vertex in enumerate(vertices):
    fig.add_trace(go.Scatter3d(
        x=[vertex[0]], y=[vertex[1]], z=[vertex[2]],
        mode='text',
        text=f'Vertex {i+1}',
        textposition='top center',
        textfont=dict(size=12, color='black')
    ))

# Set layout
fig.update_layout(
    scene=dict(
        xaxis=dict(range=[-1, 2], autorange=False),
        yaxis=dict(range=[-1, 2], autorange=False),
        zaxis=dict(range=[-1, 2], autorange=False),
        aspectratio=dict(x=1, y=1, z=0.8),
        camera=dict(
            up=dict(x=0, y=0, z=1),
            eye=dict(x=0, y=2, z=0)
        ),
    ),
)

# Render the figure using Streamlit
st.plotly_chart(fig)
