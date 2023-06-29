import streamlit as st
import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Define the vertices of the triangle
vertices = [[0, 0, 0], [1, 0, 0], [0.5, 0.5, 1]]

# Create the triangular roof shape
fig.add_trace(go.Mesh3d(
    x=[v[0] for v in vertices],
    y=[v[1] for v in vertices],
    z=[v[2] for v in vertices],
    color='lightblue',
    opacity=0.7
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
