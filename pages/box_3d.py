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
room_floor_1 = go.Mesh3d(
    x=[0, room_width, room_width,   0,           0],
    y=[0, 0,          room_length,  room_length, 0],
    z=[0, 0, 0, 0, 0],
    color='lightgray',
    opacity=0.7
)
# add 1 st sofa
sofa_1 = go.Mesh3d(
    x=[0,    1.8,    1.8,   0,    0],
    y=[5.99, 5.99,   7.99,  7.99, 5.99],
    z=[0, 0, 0, 0, 0],
    color='lightpink',
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
toelit_1_wall_1_config_x = [0,    0.9,    0.9,   0,    0]
toelit_1_wall_1_config_y = [1.54, 1.54,   1.64,  1.64, 1.54]
toelit_1_wall = []
for item in range(0, 27, 1):
    toelit_1_wall.append(go.Mesh3d(x=toelit_1_wall_1_config_x, y=toelit_1_wall_1_config_y, z=[item*0.1,item*0.1,item*0.1,item*0.1,item*0.1], color='lightblue', opacity=0.7))
toelit_1_wall_2_config_x = [0,    0.1,    0.1,   0,    0]
toelit_1_wall_2_config_y = [1.54, 1.54,   2.65,  2.65, 1.54]
for item in range(0, 27, 1):
    toelit_1_wall.append(go.Mesh3d(x=toelit_1_wall_2_config_x, y=toelit_1_wall_2_config_y, z=[item*0.1,item*0.1,item*0.1,item*0.1,item*0.1], color='lightblue', opacity=0.7))
toelit_1_wall_3_config_x = [0,    0.9,    0.9,   0,    0]
toelit_1_wall_3_config_y = [2.65, 2.65,   2.75,  2.75, 2.65]
for item in range(0, 27, 1):
    toelit_1_wall.append(go.Mesh3d(x=toelit_1_wall_3_config_x, y=toelit_1_wall_3_config_y, z=[item*0.1,item*0.1,item*0.1,item*0.1,item*0.1], color='lightblue', opacity=0.7))


# create a kitchen
kitchen = go.Mesh3d(
    x=[0,    room_width,  room_width,   0,              0],
    y=[7.99, 7.99,        room_length,  room_length, 7.99],
    z=[0, 0, 0, 0, 0],
    color='lightyellow',
    opacity=0.7
)

room_1st_floor = [room_floor_1, toelit_1, kitchen, sofa_1] + toelit_1_wall

# ------------------------ Create a room 2nd floor -------------------------------
room_floor_2 = go.Mesh3d(
    x=[0, room_width, room_width,   0,           0],
    y=[0, 0,          8.01,         8.01,        0],
    z=[room_height, room_height, room_height, room_height, room_height],
    color='lightgray',
    opacity=0.7
)
room_2nd_room_1 = go.Mesh3d(
    x=[0, room_width, room_width,   0,           0],
    y=[0, 0,          2.46,         2.46,        0],
    z=[room_height, room_height, room_height, room_height, room_height],
    color='lightpink',
    opacity=0.7
)
room_2nd_floor = [room_floor_2, room_2nd_room_1]


# Combine room walls and roof into a data list
data = room_walls + room_1st_floor + room_2nd_floor

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
