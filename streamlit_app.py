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

# Create space below the title
st.write(" ")


# Create four columns for input fields
col1, col2, col3, col4 = st.columns(4)

# Input fields in the first column
with col1:
    fixed_costs = st.number_input("Fixed Monthly Costs", value=100000, key="fixed_costs")
    
# Input fields in the second column
with col2:
    variable_cost_per_sale = st.number_input("Variable Cost per Sale", value=603, key="variable_cost_per_sale")
    
# Input fields in the third column
with col3:
    target_profit = st.number_input("Target Profit", value=50000, key="target_profit")

# Input fields in the fourth column
with col4:
    price_to_be_sold = st.number_input("Price to be sold", value=999, key="price_to_be_sold")

# Create slider input for "Quantity"
quantity_range = st.slider("Quantity", 100, 500, (100, 500))

# Calculate the optimal price to achieve the target profit




# Calculate the "Target Price" based on total cost and target profit
sales = list(range(quantity_range[0], quantity_range[1] + 1))
total_cost_values = [fixed_costs + variable_cost_per_sale * s for s in sales]
target_price_values = [total_cost + target_profit for total_cost in total_cost_values]

# Calculate the revenue as the product of sales and price
revenue_values = [sales[i] * price_to_be_sold for i in range(len(sales))]

# Calculate the break-even number of sales
break_even_sales = None
for i in range(len(sales)):
    if revenue_values[i] - target_price_values[i] >= 0:
        break_even_sales = sales[i]
        break
        


url = 'https://www.dias-advisors.com/'
if st.button('Connect with Dias'):
    webbrowser.open_new_tab(url)
