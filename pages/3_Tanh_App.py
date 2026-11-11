import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tanh Visualiser")
st.title("3. Hyperbolic Tangent (Tanh)")
st.write("The Tanh function maps input values to a range between -1 and 1.")

st.sidebar.header("Settings")
x_min = st.sidebar.slider("X-axis minimum", -10.0, 0.0, -6.0)
x_max = st.sidebar.slider("X-axis maximum", 0.0, 10.0, 6.0)

xgrid = np.linspace(x_min, x_max, 400)
# Tanh mathematical operation
ygrid = np.tanh(xgrid)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xgrid, ygrid, label="Tanh", color="#0000CC", linewidth=2)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output (y)")
ax.legend()
ax.grid(True)

st.pyplot(fig)