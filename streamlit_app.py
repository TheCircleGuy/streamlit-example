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
            height: 5px;
            width: 20px;
        }
        .title {
            text-align: center;
        }
    </style>
    <div class="logo">
        <img src="https://raw.githubusercontent.com/TheCircleGuy/streamlit-example/b4003f268d65134df7e3015f6090d6e79e601fbb/logo.png" alt="Logo" width=100 height=100>
    </div>
    <h1 class="title">Cost Volume Profit Analysis</h1>
    """, unsafe_allow_html=True)


# Create three columns for inputs
col1, col2, col3 = st.beta_columns(3)

# Input for Fixed monthly costs
fixed_costs = col1.number_input("Fixed monthly costs", min_value=0.0, step=1.0)

# Input for Variable costs per sale
variable_costs = col2.number_input("Variable costs per sale", min_value=0.0, step=1.0)

# Input for Target profit
target_profit = col3.number_input("Target profit", min_value=0.0, step=1.0)

# You can use these input values for further calculations or
