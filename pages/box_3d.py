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

