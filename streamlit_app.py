import streamlit as st
import pandas as pd
import numpy as np
from bokeh.models.widgets import Div

# Set the page configuration to 'wide'
st.set_page_config(layout="wide")
# Create a title and logo in the left corner
st.markdown("""
    <style>
        .logo {
            padding: 10px 0px;
            margin: 0px;
            text-align: left;
        }
        .title {
            text-align: center;
            font-size: 36px; /* Larger font size */
        }
        .inputs-header {
            text-align: center;
            font-size: 20px;
        }
    </style>
    <div class="logo">
        <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/fbd4e7f51bfa5d98bb703b3ed81326164734da40/assets/logo.png" alt="Logo" width=100 height=100>
    </div>
    <h1 class="title">Cost Volume Profit Analysis</h1>
    """, unsafe_allow_html=True)
