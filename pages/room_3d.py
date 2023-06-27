import streamlit as st
import pythreejs as p3

# Create room dimensions
room_width = 6
room_height = 3
room_length = 8

# Create a 3D scene
scene = p3.Scene()

# Add room walls
room_walls = p3.Mesh(
    p3.BoxGeometry(room_length, room_height, room_width),
    p3.MeshLambertMaterial(color='lightgray', opacity=0.7, transparent=True),
    position=[room_length / 2, room_height / 2, room_width / 2]
)
scene.add(room_walls)

# Add a table in the room
table_width = 2
table_height = 0.8
table_length = 4
table_x = (room_length - table_length) / 2
table_y = (room_height - table_height) / 2
table_z = (room_width - table_width) / 2

table = p3.Mesh(
    p3.BoxGeometry(table_length, table_height, table_width),
    p3.MeshLambertMaterial(color='brown', opacity=0.7, transparent=True),
    position=[table_x + table_length / 2, table_y + table_height / 2, table_z + table_width / 2]
)
scene.add(table)

# Add table legs
table_leg_height = table_height / 2
table_leg_width = table_width / 10
table_leg_length = table_length / 10

table_legs = [
    p3.Mesh(
        p3.BoxGeometry(table_leg_width, table_leg_length, table_leg_height),
        p3.MeshLambertMaterial(color='black', opacity=0.7, transparent=True),
        position=[
            table_x + table_length / 2,
            table_y + table_leg_length / 2,
            table_z + table_width / 2 - table_leg_width / 2
        ]
    ),
    p3.Mesh(
        p3.BoxGeometry(table_leg_width, table_leg_length, table_leg_height),
        p3.MeshLambertMaterial(color='black', opacity=0.7, transparent=True),
        position=[
            table_x + table_length / 2,
            table_y + table_height - table_leg_length / 2,
            table_z + table_width / 2 - table_leg_width / 2
        ]
    ),
    p3.Mesh(
        p3.BoxGeometry(table_leg_width, table_leg_length, table_leg_height),
        p3.MeshLambertMaterial(color='black', opacity=0.7, transparent=True),
        position=[
            table_x + table_length / 2 - table_leg_width / 2,
            table_y + table_leg_length / 2,
            table_z + table_width / 2 + table_leg_width / 2
        ]
    ),
    p3.Mesh(
        p3.BoxGeometry(table_leg_width, table_leg_length, table_leg_height),
        p3.MeshLambertMaterial(color='black', opacity=0.7, transparent=True),
        position=[
            table_x + table_length / 2 - table_leg_width / 2,
            table_y + table_height - table_leg_length / 2,
            table_z + table_width / 2 + table_leg_width / 2
        ]
    )
]

for leg in table_legs:
    scene.add(leg)

# Create a 3D renderer
renderer = p3.Renderer(scene, camera='perspective', width=800, height=600)

# Display the 3D room
st.pythreejs(renderer)



