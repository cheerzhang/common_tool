import streamlit as st
import plotly.graph_objects as go

# Create room dimensions
room_width = 6
room_height = 3
room_length = 8

# Create room walls
room_walls = [
    go.Mesh3d(
        x=[0, 3.7, 3.7,   0, 0],
        y=[0, 0,   11.79, 11.79, 0],
        z=[0, 0, 0, 0, 0],
        color='lightgray',
        opacity=0.7
    )
]

# Create room floor
room_floor = go.Mesh3d(
    x=[0, 3.7, 3.7,   0, 0],
    y=[0, 0,   11.79, 11.79, 0],
    z=[0, 0, 0, 0, 0],
    color='lightgray',
    opacity=0.7
)

# create a kitchen
room_kitchen = go.Mesh3d(
    x=[0,    3.7,  3.7,   0,     0],
    y=[7.99, 7.99, 11.79, 11.79, 0],
    z=[0, 0, 0, 0, 0],
    color='orange',
    opacity=0.7
)

# Create a room roof
room_roof_1 = go.Mesh3d(
    x=[0, 3.7, 3.7,   0, 0],
    y=[0, 0,   11.79, 11.79, 0],
    z=[3, 3, 3, 3, 3],
    color='lightgray',
    opacity=0.7
)
room_roof_2 = go.Mesh3d(
    x=[0, room_length, room_length, 0, 0],
    y=[0, 0, 0, 0, 0],
    z=[6, 6, 6, 6, 6],
    color='lightgray',
    opacity=0.7
)

# Create a table
table = go.Mesh3d(
    x=[0, 0, 2, 2, 0],
    y=[0, 2, 2, 0, 0],
    z=[0.5, 0.5, 0.5, 0.5, 0.5],
    color='red',
    opacity=0.7
)

# Combine room walls and roof into a data list
data = room_floor + [room_roof_1, room_roof_2, room_kitchen]

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
