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
floor_1_wall_1 = go.Mesh3d(
   x=[0, 2.5, 2.5, 2.5, 0],
   y=[3, 3,   3.1, 3.1, 3],
   z=[0, 0,   2.7, 2.7, 0],
   color='lightgray',
   opacity=0.7
)
room_floor_2 = go.Mesh3d(
   x=[0, room_width, room_width,   0,           0],
   y=[0, 0,          room_length,  room_length, 0],
   z=[2.7, 2.7, 2.7, 2.7, 2.7],
   color='lightgray',
   opacity=0.7
)

# --------------------------- create a toilet ----------------------------------
toilet = go.Mesh3d(
   x=[3, 4, 4, 3, 3],
   y=[0, 0, 2, 2, 0],
   z=[0, 0, 0, 0, 0],
   color='lightblue',
   opacity=0.7
)
toilet_wall_1 = go.Mesh3d(
   x=[3, 3.1, 3.1, 3, 3],
   y=[0, 0.1, 1.9, 2, 0],
   z=[0, 2.7, 2.7, 0, 0],
   color='lightblue',
   opacity=0.7
)
toilet_wall_2 = go.Mesh3d(
   x=[3.9, 4, 4, 3.9, 3.9],
   y=[0.1, 0, 2, 1.9, 0.1],
   z=[2.7, 0, 0, 2.7, 2.7],
   color='lightblue',
   opacity=0.7
)
toilet_wall_3 = go.Mesh3d(
   x=[3, 4, 3.9, 3.1, 3],
   y=[0, 0, 0.1, 0.1, 0],
   z=[0, 0, 2.7, 2.7, 0],
   color='lightblue',
   opacity=0.7
)
toilet_wall_4 = go.Mesh3d(
   x=[3, 4, 3.9, 3.1, 3],
   y=[2, 2, 1.9, 1.9, 2],
   z=[0, 0, 2.7, 2.7, 0],
   color='lightblue',
   opacity=0.7
)
toilet_floor = go.Mesh3d(
   x=[3.1, 3.9, 3.9, 3.1, 3.1],
   y=[0.1, 0.1, 1.9, 1.9, 0.1],
   z=[2.7, 2.7, 2.7, 2.7, 2.7],
   color='lightblue',
   opacity=0.7
)
toilet_ = [toilet, toilet_wall_1, toilet_wall_2, toilet_wall_3, toilet_wall_4]

# ----------------------------  create a bed  ---------------------------------
bed = go.Mesh3d(
   x=[0.1,   1.9,   1.9,   0.1,   0.1],
   y=[0.1,   0.1,   1.7,   1.7,   0.1],
   z=[0.5,   0.5,   0.5,   0.5,   0.5],
   color='pink',
   opacity=0.7
)
bed_head = go.Mesh3d(
   x=[0,   0.1,   0.1,  0,   0],
   y=[0,   0,     1.8,  1.8, 0],
   z=[1,   0.5,   0.5,  1,   1],
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
   y=[0.1, 0,  1.8, 1.7,   0.1],
   z=[0.5, 0,  0,   0.5,   0.5],
   color='pink',
   opacity=0.7
)
bed_ = [bed, bed_leg_1, bed_leg_2, bed_leg_3, bed_leg_4, bed_head]

# --------------------------- Create a bookshelf -----------------------------
shelf_1 = go.Mesh3d(
   x=[2.5, 3, 3, 2.5, 2.5],
   y=[0,   0,  3,  3,   0],
   z=[0,   0,  0,  0,   0],
   color='lightyellow',
   opacity=0.7
)
shelf_2 = go.Mesh3d(
   x=[2.5, 3,   3,   2.5, 2.5],
   y=[0,   0,   3,   3,   0],
   z=[0.5, 0.5, 0.5, 0.5, 0.5],
   color='lightyellow',
   opacity=0.7
)
shelf_3 = go.Mesh3d(
   x=[2.5, 3,   3,   2.5, 2.5],
   y=[0,   0,   3,   3,   0],
   z=[1,   1,   1,   1,   1],
   color='lightyellow',
   opacity=0.7
)
shelf_4 = go.Mesh3d(
   x=[2.5, 3,   3,   2.5, 2.5],
   y=[0,   0,   3,   3,   0],
   z=[1.5, 1.5, 1.5, 1.5, 1.5],
   color='lightyellow',
   opacity=0.7
)
shelves_ = [shelf_1, shelf_2, shelf_3, shelf_4]

# Combine room walls and roof into a data list
data = room_walls + [room_floor, room_floor_2, floor_1_wall_1] + bed_ + toilet_ + shelves_ 

# Create the 3D layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(visible=True),
        yaxis=dict(visible=True),
        zaxis=dict(visible=True),
        camera=dict(
            eye=dict(x=2, y=2, z=1)  # Set the camera position (adjust the values as needed)
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



