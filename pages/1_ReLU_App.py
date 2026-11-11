import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ReLU Visualiser")
st.title("1. Rectified Linear Unit (ReLU)")
st.write("The ReLU function outputs the input directly if it is positive; otherwise, it outputs zero.")

# Sidebar controls for interactivity
st.sidebar.header("Settings")
x_min = st.sidebar.slider("X-axis minimum", -10.0, 0.0, -6.0)
x_max = st.sidebar.slider("X-axis maximum", 0.0, 10.0, 6.0)

# Generate data
xgrid = np.linspace(x_min, x_max, 400)
# ReLU mathematical operation
ygrid = np.maximum(0, xgrid)

# Plotting using matplotlib as referenced in foundation_nn.py
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xgrid, ygrid, label="ReLU", color="#007700", linewidth=2)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.set_title("ReLU Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.legend()
ax.grid(True)

# Display in Streamlit
st.pyplot(fig)