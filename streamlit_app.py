import streamlit as st

# Set the page configuration to 'wide'
st.set_page_config(layout="wide")

# Create a title and logo in the left corner
st.markdown("""
    <style>
        .logo {
            padding: 10px 0px;
            margin: 0px;
            text-align: left;
            height: 2.15px;
            width: 5.3px;
        }
        .title {
            text-align: center;
        }
    </style>
    <div class="logo">
        <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/fbd4e7f51bfa5d98bb703b3ed81326164734da40/assets/logo.png?raw=true" alt="Logo" width=100 height=100>
    </div>
    <h1 class="title">Cost Volume Profit Analysis</h1>
    """, unsafe_allow_html=True)


# Create three columns for input fields
col1, col2, col3 = st.columns(3)

# Input fields
with col1:
    fixed_costs = st.number_input("Fixed Monthly Costs", value=1000.0)

with col2:
    variable_costs = st.number_input("Variable Costs per Sale", value=10.0)

with col3:
    target_profit = st.number_input("Target Profit", value=500.0)

# Add your content here
st.write("Welcome to the Cost Volume Profit Analysis dashboard!")

# You can continue adding more content and functionality to your 
