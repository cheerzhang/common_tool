import streamlit as st
import plotly.graph_objects as go

# Create room dimensions
room_width = 4
room_length = 5
room_height = 3

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

# Create room floor
room_floor = go.Mesh3d(
   x=[0, room_width, room_width,   0,           0],
   y=[0, 0,          room_length,  room_length, 0],
   z=[0, 0, 0, 0, 0],
   color='lightgray',
   opacity=0.7
)

# create a toilet
toilet = go.Mesh3d(
   x=[0, 1, 1, 0, 0],
   y=[0, 0, 2, 2, 0],
   z=[0, 0, 1, 1, 0],
   color='blue',
   opacity=0.7
)

# Combine room walls and roof into a data list
data = room_walls + [room_floor, toilet]

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



