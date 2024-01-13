import streamlit as st
import pandas as pd
import numpy as np

with st.sidebar:
# Input variables
    MonthlyCost = st.number_input('Insert Monthly Cost', value=31530.74)
    ProjPerManager = st.number_input('Insert Number of Projects per Manager', value=4, key="a1")
    ManagerSalary = st.number_input('Insert Manager Salary', value=681, key="a2")
    ProjPerServer = st.number_input('Insert Number Of Projects per SERVER', value=4, key="a3")
    ServerCost = st.number_input('Insert Server Cost', value=197, key="a4")
    Commision = st.number_input('Insert Commission Percentage', value=0.001, key="a5")
    avgRevLicense = st.number_input('Insert Average Revenue Of License', value=1000, key="a6")
    avgLicensePerClient = st.number_input('Insert Average Licenses per Client', value=10, key="a7")
    ProductPrice = st.number_input('Insert price to be sold', value=2000, key="a8")
    quantity_range = st.slider('Select a range of quantities to be sold', 0, 1000, (60, 150), key="a9")

# Calculate FixedCost
FixedCost = MonthlyCost * 12

# Calculate Revenue and Fixed Cost for each quantity
quantities = np.arange(quantity_range[0], quantity_range[1] + 1)
Revenue = ProductPrice * quantities + Commision * avgRevLicense * quantities
FixedCosts = np.full_like(quantities, FixedCost)

# Create a DataFrame for plotting
import pandas as pd
data = pd.DataFrame({'Quantity': quantities, 'Revenue': Revenue, 'FixedCost': FixedCosts})

# Create a line chart
st.line_chart(data.set_index('Quantity'))
