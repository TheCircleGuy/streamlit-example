import streamlit as st
import pandas as pd
import numpy as np
import gspread


sa= gspread.service_account()
sh= sa.open(" bybit api")

wks = sh.worksheet("Analysis")

pnl_value = wks.acell('C17').value
positions_value = wks.acell('C13').value
trades_value = wks.acell('C14').value
pnl = int(float(pnl_value))
percent = 50/100

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

st.markdown('<img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/master/banner.png" style="width:100%;" />', unsafe_allow_html=True)


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

st.markdown("<h1 style='text-align: center;'>Trading Dashboard</h1>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<h3 style='text-align: center;'>PNL và tỉ lệ chia cho Tân hiện tại = 50%</h3>", unsafe_allow_html=True)
st.write("")
# Create four columns for input fields
col1, col2, col3, col4 = st.columns(4)

# Input fields in the first column
with col1:
    fixed_costs = st.number_input("PNL ($)", value=float(pnl_value), key="fixed_costs")*12
    
# Input fields in the second column
with col2:
    variable_cost_per_sale = st.number_input("Positions", value=float(positions_value), key="variable_cost_per_sale")
    
# Input fields in the third column
with col3:
    target_profit = st.number_input("cho Chú", value=(pnl * (1-percent)), key="target_profit")

# Input fields in the fourth column
with col4:
    price_to_be_sold = st.number_input("cho Tân", value=percent , key="price_to_be_sold")

st.divider()
# Create slider input for "Quantity"
# quantity_range = st.slider("Quantity", 100, 5000, (100, 500))

# Calculate the optimal price to achieve the target profit




# Calculate the "Target Price" based on total cost and target profit
# sales = list(range(quantity_range[0], quantity_range[1] + 1))
# total_cost_values = [fixed_costs + variable_cost_per_sale * s for s in sales]
# target_price_values = [total_cost + target_profit for total_cost in total_cost_values]

# Calculate the revenue as the product of sales and price
# revenue_values = [sales[i] * price_to_be_sold for i in range(len(sales))]

# Calculate the break-even number of sales
break_even_sales = float(pnl_value)


st.markdown("<div style='text-align: center; background-color: #f89d13; padding: 20px; border-radius: 10px;'><h3 style='color: #161638;'>Lợi Nhuận Ròng</h3><h1 style='color: #161638;'>{}</h1></div>".format(break_even_sales), unsafe_allow_html=True)
st.write("")
st.divider()
st.write("")

# Line chart with vertical axis as price and horizontal axis as sales
# Showing Total Cost, Target Price, and Revenue


# Chart 1
st.markdown("""
<div class="chart-container">
    <iframe width="700" height="371" seamless frameborder="0" scrolling="no" 
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTV3KRzGqbMxwP4J6oRQdEU36VizRh580pdXQTZLkiMN_SfYH_pNawhJlWo6MQu1sDVHT9P4VPRLFoL/pubchart?oid=89569499&amp;format=interactive"></iframe>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("""
<div class="chart-container">
    <iframe width="700" height="371" seamless frameborder="0" scrolling="no" 
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTV3KRzGqbMxwP4J6oRQdEU36VizRh580pdXQTZLkiMN_SfYH_pNawhJlWo6MQu1sDVHT9P4VPRLFoL/pubchart?oid=1103638229&amp;format=interactive"></iframe>
</div>
""", unsafe_allow_html=True)

URL_STRING = "https://docs.google.com/spreadsheets/d/1uDBMmH5jwKhPbXYhGlfZG5uYJJ7L7NsisPMQip0stFc/edit#gid=280897894"

coll1, coll2, coll3, coll4, coll5 = st.columns(5)
with coll3:
    st.markdown(f'<a href="{URL_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #f89d13; color: black; text-align: center; text-decoration: none; font-size: 15px; border-radius: 4px;"><strong>Xem data</strong></a>', unsafe_allow_html=True
    )