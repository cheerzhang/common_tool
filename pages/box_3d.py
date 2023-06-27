import streamlit as st
import plotly.graph_objects as go

# Create room dimensions
room_width = 6
room_height = 3
room_length = 8

# Create room walls
room_walls = [
    go.Mesh3d(
        x=[0, room_length, room_length, 0, 0],
        y=[0, 0, room_height, room_height, 0],
        z=[0, 0, 0, 0, 0],
        color='lightgray',
        opacity=0.7
    )
]

# Create a room roof
room_roof = go.Mesh3d(
    x=[0, room_length, room_length, 0, 0],
    y=[0, 0, 0, 0, 0],
    z=[room_width, room_width, room_width, room_width, room_width],
    color='lightgray',
    opacity=0.7
)

# Combine room walls and roof into a data list
data = room_walls + [room_roof]

# Create the 3D layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="manual",
        aspectratio=dict(x=room_length, y=room_width, z=room_height)
    ),
    margin=dict(r=0, l=0, b=0, t=0)
)

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Render the figure using Plotly
st.plotly_chart(fig)
