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
            font-size: 36px;
        }
        .inputs-header {
            text-align: center;
            font-size: 20px;
        }
        .footer {
            position: absolute;
            bottom: 10px;
            left: 0;
            padding: 10px 0;
        }
    </style>
    <div class="logo">
        <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/fbd4e7f51bfa5d98bb703b3ed81326164734da40/assets/logo.png" alt="Logo" width=100 height=100>
    </div>
    <h1 class="title">Cost Volume Profit Analysis</h1>
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
quantity_range = st.slider("Quantity", 100, 500, (100, 500))

# Calculate the optimal price to achieve the target profit
optimal_price = (fixed_costs + target_profit) / variable_cost_per_sale

st.markdown(f"<h3 style='text-align: center; color: #0d043b;'>Optimal Price to Achieve Target Profit: ${optimal_price:.2f}</h3>", unsafe_allow_html=True)

# Calculate the "Target Price" based on total cost and target profit
sales = list range(quantity_range[0], quantity_range[1] + 1)
total_cost_values = [fixed_costs + variable_cost_per_sale * s for s in sales]
target_price_values = [total_cost + target_profit for total_cost in total_cost_values]

# Line chart with vertical axis as price and horizontal axis as sales
# Showing Fixed Cost, Variable Cost, Total Cost, and Target Price
chart_data = pd.DataFrame({
    'Sales': sales,
    'Fixed Cost': [fixed_costs] * len(sales),
    'Variable Cost': [variable_cost_per_sale * s for s in sales],
    'Total Cost': total_cost_values,
    'Target Price': target_price_values
})

st.markdown("<h3 style='text-align: center; color: #0d043b;'>Price vs. Sales</h3>", unsafe_allow_html=True)
st.line_chart(chart_data.set_index('Sales')[['Fixed Cost', 'Variable Cost', 'Total Cost', 'Target Price']])

# Footer
st.markdown("""
    <div class="footer">
        <div class="logo">
            <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/fbd4e7f51bfa5d98bb703b3ed81326164734da40/assets/logo.png" alt="Logo" width=60 height=60>
        </div>
        <a href="#">Our Story</a> |
        <a href="#">Solutions</a> |
        <a href="#">Team</a> |
        <a href="#">Portfolio</a> |
        <a href="#">Find Investors</a> |
        <a href="#">XCHANGE</a> |
        <a href="#">Contact</a>
    </div>
    """, unsafe_allow_html=True)
