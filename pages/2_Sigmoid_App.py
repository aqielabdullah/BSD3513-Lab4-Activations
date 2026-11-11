import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sigmoid Visualiser")
st.title("2. Sigmoid Activation Function")
st.write("The Sigmoid function maps any input value to a value between 0 and 1, creating an S-shaped curve.")

st.sidebar.header("Settings")
x_min = st.sidebar.slider("X-axis minimum", -10.0, 0.0, -6.0)
x_max = st.sidebar.slider("X-axis maximum", 0.0, 10.0, 6.0)

xgrid = np.linspace(x_min, x_max, 400)
# Sigmoid mathematical operation
ygrid = 1 / (1 + np.exp(-xgrid))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xgrid, ygrid, label="Sigmoid", color="#CC0000", linewidth=2)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.set_title("Sigmoid Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.legend()
ax.grid(True)

st.pyplot(fig)