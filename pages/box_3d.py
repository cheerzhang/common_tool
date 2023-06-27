import streamlit as st
import plotly.graph_objects as go

# Create room dimensions
room_width = 6
room_height = 3
room_length = 8

# Create room walls
room_walls = [
    go.Mesh3d(
        x=[0, room_length, room_length, 0, 0, room_length, room_length, 0],
        y=[0, 0, room_height, room_height, 0, 0, room_height, room_height],
        z=[0, 0, 0, 0, room_width, room_width, room_width, room_width],
        color='lightgray',
        opacity=0.7
    )
]

# Create a chair
chair = go.Mesh3d(
    x=[2, 3, 3, 2, 2, 3, 3, 2, 2.5, 2.5, 3, 3],
    y=[1, 1, 2, 2, 1, 1, 2, 2, 1, 2, 1, 2],
    z=[1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0, 0, 0, 0],
    color='red',
    opacity=0.7
)

# Create the 3D layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="manual",
        aspectratio=dict(x=room_length, y=room_height, z=room_width)
    ),
    margin=dict(r=0, l=0, b=0, t=0)
)

# Combine room walls and chair into a data list
data = room_walls + [chair]

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Render the figure using Plotly
st.plotly_chart(fig)

