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
   x=[3, 4, 4, 3, 3],
   y=[0, 0, 2, 2, 0],
   z=[0, 0, 0, 0, 0],
   color='blue',
   opacity=0.7
)
# ----------------------------  create a bed  ---------------------------------
bed = go.Mesh3d(
   x=[0.1,   1.9,   1.9,   0.1,   0.1],
   y=[0.1,   0.1,   1.7,   1.7,   0.1],
   z=[0.5, 0.5, 0.5,   0.5, 0.5],
   color='pink',
   opacity=0.7
)
bed_leg_1 = go.Mesh3d(
   x=[0, 2, 1.9, 0.1, 0],
   y=[0, 0, 0.1, 0.1, 0],
   z=[0, 0, 0.5, 0.5, 0.5],
   color='pink',
   opacity=0.7
)
bed_leg_2 = go.Mesh3d(
   x=[0,   2,   1.9, 0.1,   0],
   y=[1.8, 1.8, 1.7, 1.7,   1.8],
   z=[0,   0,   0.5, 0.5,   0.5],
   color='pink',
   opacity=0.7
)
bed_leg_3 = go.Mesh3d(
   x=[0,   0.1,   0.1,  0,   0],
   y=[0,   0.1,   1.7,  1.9,   0],
   z=[0,   0.5,   0.5,  0,   0],
   color='pink',
   opacity=0.7
)
bed_leg_4 = go.Mesh3d(
   x=[1.9, 2,  2,   1.9,   1.9],
   y=[0,   0,  1.8, 1.8,   0],
   z=[0.5, 0,  0,   0.5, 0.5],
   color='pink',
   opacity=0.7
)

# Combine room walls and roof into a data list
bed_ = [bed, bed_leg_1, bed_leg_2, bed_leg_3, bed_leg_4]
data = room_walls + [room_floor, toilet] + bed_

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



