import streamlit as st
import plotly.graph_objects as go

# Create room dimensions
room_width = 6
room_height = 3
room_length = 8

# Create a 3D room figure
fig = go.Figure()

# Add room walls
fig.add_trace(go.Mesh3d(
    x=[0, room_length, room_length, 0, 0, 0, room_length, room_length, room_length, room_length, 0, 0],
    y=[0, 0, room_height, room_height, 0, 0, 0, room_height, room_height, 0, 0, room_height],
    z=[0, 0, 0, 0, 0, room_width, room_width, room_width, 0, 0, 0, 0],
    color='lightgray',
    opacity=0.7
))

# Add a table in the room
table_width = 2
table_height = 0.8
table_length = 4
table_x = (room_length - table_length) / 2
table_y = (room_height - table_height) / 2
table_z = (room_width - table_width) / 2

fig.add_trace(go.Mesh3d(
    x=[table_x, table_x + table_length, table_x + table_length, table_x, table_x, table_x, table_x + table_length, table_x + table_length, table_x + table_length, table_x + table_length, table_x, table_x],
    y=[table_y, table_y, table_y + table_height, table_y + table_height, table_y, table_y, table_y, table_y + table_height, table_y + table_height, table_y, table_y, table_y + table_height],
    z=[table_z, table_z, table_z, table_z, table_z, table_z + table_width, table_z + table_width, table_z + table_width, table_z, table_z, table_z, table_z],
    color='brown',
    opacity=0.7
))

# Add table legs
table_leg_height = table_height / 2
table_leg_width = table_width / 10
table_leg_length = table_length / 10
table_leg_x = [table_x, table_x + table_length, table_x, table_x + table_length]
table_leg_y = [table_y, table_y, table_y + table_height, table_y + table_height]
table_leg_z = [table_z, table_z, table_z, table_z]

for i in range(4):
    fig.add_trace(go.Mesh3d(
        x=[table_leg_x[i], table_leg_x[i], table_leg_x[i] + table_leg_width, table_leg_x[i] + table_leg_width, table_leg_x[i]],
        y=[table_leg_y[i], table_leg_y[i] + table_leg_length, table_leg_y[i] + table_leg_length, table_leg_y[i], table_leg_y[i]],
        z=[table_leg_z[i], table_leg_z[i], table_leg_z[i], table_leg_z[i], table_leg_z[i]],
        color='black',
        opacity=0.7
    ))

# Set figure layout
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectratio=dict(x=1, y=1, z=1),
        camera_eye=dict(x=1.5, y=-1.5, z=0.8),
        annotations=[]
    ),
    scene_camera=dict(up=dict(x=0, y=0, z=1))
)

# Display the 3D room
st.plotly_chart(fig)
