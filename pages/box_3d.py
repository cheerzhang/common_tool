import streamlit as st
import plotly.graph_objects as go

# Create room dimensions
room_width = 3.54
room_height = 2.7
room_length = 11.79

# Create room walls
room_walls = [
    go.Mesh3d(
        x=[0, room_width, room_width,   0,           0],
        y=[0, 0,          room_length,  room_length, 0],
        z=[0, 0, 0, 0, 0],
        color='lightgray',
        opacity=0.7
    )
]

# ------------------  Create 1st floor room ----------------------------
room_floor = go.Mesh3d(
    x=[0, room_width, room_width,   0,           0],
    y=[0, 0,          room_length,  room_length, 0],
    z=[0, 0, 0, 0, 0],
    color='lightgray',
    opacity=0.7
)

# add 1 st toelit
toelit_1 = go.Mesh3d(
    x=[0,    0.9,    0.9,   0,    0],
    y=[1.54, 1.54,   2.65,  2.65, 1.54],
    z=[0, 0, 0, 0, 0],
    color='lightblue',
    opacity=0.7
)

# create a kitchen
kitchen = go.Mesh3d(
    x=[0,    room_width,  room_width,   0,              0],
    y=[7.99, 7.99,        room_length,  room_length, 7.99],
    z=[0, 0, 0, 0, 0],
    color='lightyellow',
    opacity=0.7
)

room_1st_floor = [room_floor, toelit_1, kitchen]

# ------------------------ Create a room 2nd floor -------------------------------


# Combine room walls and roof into a data list
data = room_walls + room_1st_floor

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
