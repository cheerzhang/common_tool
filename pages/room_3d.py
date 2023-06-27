import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyvista as pv

# Create 3D coordinates for the box
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Set up the Streamlit app
st.title("3D Image Viewer")
st.write("Displaying a 3D box using Matplotlib")

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, edgecolor='black')

# Show the plot in Streamlit
st.pyplot(fig)


# Create a simple 3D box
mesh = pv.Box()

# Set up the Streamlit app
st.title("3D Image Viewer")
st.write("Displaying a 3D box")

# Render the 3D image
st.pyvista_plot(mesh)

