import streamlit as st
import pandas as pd
import numpy as np


# Set the page configuration to 'wide'
# st.set_page_config(layout="wide")
# Set the theme to dark

# st.set_page_config(
#     page_title="Dias - Cost Volume Profit Analysis",
#     page_icon="🧊",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'website': 'https://www.extremelycoolapp.com/help',
#         'Linkedin': "https://www.linkedin.com/in/svenroering/",
#     }
# )

st.set_page_config(
    page_title="Dias - Cost Volume Profit Analysis",
    page_icon="🧊",

    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/svenroering/',
        'Report a bug': "https://www.linkedin.com/in/svenroering/",
        'About': "https://www.linkedin.com/in/svenroering/"
    }
)

st.markdown('<img src="https://raw.githubusercontent.com/TanNguyenDiasAdvisors/PriceAnalysis/main/assets/banner.png" style="width:100%;" />', unsafe_allow_html=True)


# Create a title and logo in the left corner
# st.markdown("""
#     <style>
#         .logo {
#             padding: 10px 0px;
#             margin: 0px;
#             text-align: left;
#         }
#         .title {
#             text-align: center;
#             font-size: 36px; /* Larger font size */
#         }
#         .inputs-header {
#             text-align: center;
#             font-size: 20px;
#         }
#     </style>
#     <div class="logo">
#         <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/fbd4e7f51bfa5d98bb703b3ed81326164734da40/assets/logo.png" alt="Logo" width=100 height=100>
#     </div>
#     <h1 class="title">Cost Volume Profit Analysis</h1>
#     """, unsafe_allow_html=True)



# Create space below the title
st.write(" ")

st.markdown("<h1 style='text-align: center;'>Cost Volume Profit Analysis</h1>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<h3 style='text-align: center;'>Update the Inputs below to determine your target monthly sales volume</h3>", unsafe_allow_html=True)
st.write("")
# Create four columns for input fields
col1, col2, col3, col4 = st.columns(4)

# Input fields in the first column
with col1:
    fixed_costs = st.number_input("Fixed Monthly Costs", value=2000, key="fixed_costs")*12
    
# Input fields in the second column
with col2:
    variable_cost_per_sale = st.number_input("Variable Cost per Sale", value=200, key="variable_cost_per_sale")
    
# Input fields in the third column
with col3:
    target_profit = st.number_input("Target Profit", value=30000, key="target_profit")

# Input fields in the fourth column
with col4:
    price_to_be_sold = st.number_input("Price to be sold", value=350, key="price_to_be_sold")

st.divider()
# Create slider input for "Quantity"
quantity_range = st.slider("Quantity", 100, 5000, (100, 500))

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

st.markdown("<div style='text-align: center; background-color: #f89d13; padding: 20px; border-radius: 10px;'><h3 style='color: #161638;'>Target Number of Sales</h3><h1 style='color: #161638;'>{}</h1></div>".format(break_even_sales), unsafe_allow_html=True)
st.write("")
st.divider()
st.write("")

# Line chart with vertical axis as price and horizontal axis as sales
# Showing Total Cost, Target Price, and Revenue
chart_data = pd.DataFrame({
    'Sales': sales,
    'Total Cost': total_cost_values,
    'Total Cost + Profit  Target': target_price_values,
    'Revenue': revenue_values
})

st.markdown("<h3 style='text-align: center; color: #f89d13;'>Y-axis = currency, X-axis = sales volume</h3>", unsafe_allow_html=True)
st.line_chart(chart_data.set_index('Sales')[['Total Cost', 'Total Cost + Profit  Target', 'Revenue']])

URL_STRING = "https://www.linkedin.com/in/svenroering/"

coll1, coll2, coll3, coll4, coll5 = st.columns(5)
with coll3:
    st.markdown(f'<a href="{URL_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #f89d13; color: black; text-align: center; text-decoration: none; font-size: 15px; border-radius: 4px;"><strong>Connect With Dias</strong></a>', unsafe_allow_html=True
    )
