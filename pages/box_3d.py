import streamlit as st
import plotly.graph_objects as go

# Create room walls
room_walls = [
    go.Mesh3d(
        x=[0, 3.54, 3,54,   0,           0],
        y=[0, 0,    11.79,  11.79, 0],
        z=[0, 0, 0, 0, 0],
        color='lightgray',
        opacity=0.7
    )
]

# ------------------------------- Create room floor -----------------------------
room_floor = go.Mesh3d(
   x=[0, 3.54, 3,54,   0,           0],
   y=[0, 0,    11.79,  11.79, 0],
   z=[0, 0, 0, 0, 0],
   color='lightgray',
   opacity=0.7
)
room_wall = [
    go.Mesh3d(x=[0, 0.01, 0.01,0,0],y=[0, 0,11.79,11.79, 0],z=[0,2.7,2.7,0, 0], color='lightgray', opacity=0.7),
    go.Mesh3d(x=[3.53, 3.54, 3.54, 3.53, 3.53], y=[0, 0, 11.79,11.79, 0], z=[2.7, 0,  0, 2.7, 2.7], color='lightgray', opacity=0.7)
]
kitchen_wall = [
    go.Mesh3d(x=[0,0.5,0.5,0,0],y=[7.98,7.98,7.99,7.99,7.98],z=[0,0,2.7,2.7,0], color='lightgray', opacity=0.7),
]
kitchen = [
    go.Mesh3d(x=[0,1,1,0,0],y=[8, 8, 8.5, 8.5, 8],z=[0.5,0.5,0.5,0.5,0.5], color='lightpink', opacity=0.7),
    go.Mesh3d(x=[0,0.7,0.7,0,0],y=[8.5, 8.5, 11.78, 11.78, 8.5],z=[0.5,0.5,0.5,0.5,0.5], color='lightpink', opacity=0.7),
]

floor_1 = [room_floor] + room_wall + kitchen_wall + kitchen
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
