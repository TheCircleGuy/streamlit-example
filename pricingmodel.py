import streamlit as st
import pandas as pd
import numpy as np

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
            font-size: 24px;
        }
        .inputs-header {
            text-align: center;
            font-size: 20px;
        }
    </style>
    <div class="logo">
        <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/fbd4e7f51bfa5d98bb703b3ed81326164734da40/assets/logo.png" alt="Logo" width=100 height=100>
    </div>
    <h1 class="title">Pricing Model</h1>
    """, unsafe_allow_html=True)

# Create space below the title
st.write(" ")

# Input fields
st.markdown("<h3 style='text-align: center; color: #0d043b;'>Input Variables</h3>", unsafe_allow_html=True)

fixed_costs = st.number_input("Fixed Monthly Costs", value=10000, key="fixed_costs")
variable_cost_per_sale = st.number_input("Variable Cost per Sale", value=10, key="variable_cost_per_sale")
target_profit = st.number_input("Target Profit", value=5000, key="target_profit")

# Create slider inputs for "Price to be sold" and "Quantity"
price_range = st.slider("Price to be sold", 1000, 5000, (1000, 5000))
quantity_range = st.slider("Quantity", 100, 500, (100,
