import streamlit as st
import plotly.graph_objects as go

# Create room walls
room_walls = [
    go.Mesh3d(
        x=[0, 5, 5, 0, 0],
        y=[0, 0, 5, 5, 0],
        z=[0, 0, 0, 0, 0],
        color='lightgray',
        opacity=0.1
    )
]

# ------------------------------- Create room floor -----------------------------
room_floor = go.Mesh3d(
   x=[0, 2.3, 2.3, 0, 0],
   y=[0, 0, 5, 5, 0],
   z=[0, 0, 0, 0, 0],
   color='lightgray',
   opacity=0.7
)
room_wall = [
    go.Mesh3d(x=[0, 0.01, 0.01,0,0],y=[0,0,5,5,0],z=[0,2,2,0,0], color='lightgray', opacity=0.7), # left
    go.Mesh3d(x=[2.29,2.3,2.3,2.29,2.29], y=[0,0,5,5,0], z=[2,0,0,2,2], color='lightgray', opacity=0.7), # right
    go.Mesh3d(x=[0,2.3,2.3,0,0], y=[0,0,0.01,0.01,0], z=[0,0,2,2,0], color='lightgray', opacity=0.7), # back
    go.Mesh3d(x=[0,2.3,2.3,0,0], y=[4.99,4.99,5,5,4.99], z=[2,2,0,0,2], color='lightgray', opacity=0.7), # front
]

floor_1 = [room_floor] + room_wall
# --------------------------- stair ---------------------------------



# Combine room walls and roof into a data list
data = room_walls + floor_1

# Create the 3D layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(visible=True),
        yaxis=dict(visible=True),
        zaxis=dict(visible=True),
        camera=dict(
            eye=dict(x=0.5, y=0.5, z=1)  # Set the camera position (adjust the values as needed)
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
