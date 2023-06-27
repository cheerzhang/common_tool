import streamlit as st
import pyvista as pv

# Create a simple 3D box
mesh = pv.Box()

# Set up the Streamlit app
st.title("3D Image Viewer")
st.write("Displaying a 3D box")

# Render the 3D image
st.pyvista_plot(mesh)
