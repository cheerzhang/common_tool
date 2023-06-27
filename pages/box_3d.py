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

# Create a table
table = go.Mesh3d(
    x=[0, 2, 2, 0, 0],
    y=[1, 1, 2, 2, 1],
    z=[0.5, 0.5, 0.5, 0.5, 0.5],
    color='red',
    opacity=0.7
)

# Combine room walls and roof into a data list
data = room_walls + [room_roof, table]

# Create the 3D layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(visible=True),
        yaxis=dict(visible=True),
        zaxis=dict(visible=True),
        camera=dict(
            eye=dict(x=1, y=1, z=1)  # Set the camera position (adjust the values as needed)
        ),
        # aspectmode="manual",
        # aspectratio=dict(x=room_length, y=room_width, z=room_height)
    ),
    margin=dict(r=0, l=0, b=0, t=0)
)

# Create the figure
fig = go.Figure(data=data, layout=layout)

# Render the figure using Plotly
st.plotly_chart(fig)
