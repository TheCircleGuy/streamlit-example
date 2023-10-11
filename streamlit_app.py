import streamlit as st
import pandas as pd
import numpy as np

# Input variables
with st.sidebar:
    Profit = st.number_input('Insert desired profit', value=5000, key=None)
    MonthlyCost = st.number_input('Insert Monthly Cost', value=13000, key=None)
    ProjPerManager = st.number_input('Insert Number of Projects per Manager', value=4, key="a1")
    ManagerSalary = st.number_input('Insert Manager Salary', value=500, key="a2")
    ProjPerServer = st.number_input('Insert Number Of Projects per SERVER', value=4, key="a3")
    ServerCost = st.number_input('Insert Server Cost', value=197, key="a4")
    Commision = st.number_input('Insert Commission Percentage', value=0.001, key="a5")
    avgRevLicense = st.number_input('Insert Average Revenue Of License', value=1000, key="a6")
    avgLicensePerClient = st.number_input('Insert Average Licenses per Client', value=10, key="a7")
    price = st.number_input('Insert price to be sold', value=2000, key="a8")
    licenses = st.slider(
        'Select a range of licenses to be sold',
        0, 1000, (60, 150), key="a9")

# Create a table to display the listed variables
table_data = {
    'Variable': ['Monthly Cost', 'Number of Projects per Manager', 'Manager Salary',
                 'Number Of Projects per SERVER', 'Server Cost', 'Commission Percentage',
                 'Average Revenue Of License', 'Average Licenses per Client', 'Price to be sold',
                 'Range of Licenses'],
    'Value': [MonthlyCost, ProjPerManager, ManagerSalary, ProjPerServer, ServerCost,
              Commision, avgRevLicense, avgLicensePerClient, price, f"{licenses[0]} to {licenses[1]}"]
}

st.table(table_data)

# Calculate the revenue, fixed cost, variable cost, and total cost for each quantity
quantities = list(range(licenses[0], licenses[1] + 1))

revenue = [price * q for q in quantities]

fixedCost = [
    MonthlyCost * q
    for q in quantities
]

TotalManagerSalary = [
    ManagerSalary * q if (q // avgLicensePerClient) % ProjPerServer == 0 else ManagerSalary * (q + 1)
    for q in quantities
]

TotalServerCost = [
    ServerCost * q if (q // avgLicensePerClient) % ProjPerServer == 0 else ServerCost * (q + 1)
    for q in quantities
]

VariableCost = np.array(TotalManagerSalary) + np.array(TotalServerCost)

TotalCost = np.array(fixedCost) + VariableCost

# Calculate Target Price
TargetPrice = TotalCost + Profit

# Create a DataFrame to hold the data
data = pd.DataFrame({
    'Quantity': quantities,
    'Fixed Cost': fixedCost,
    'Total Cost': TotalCost,
    'Target Price': TargetPrice,
    'Revenue': revenue
})

# Display the line chart
st.line_chart(data.set_index('Quantity'))

# Display a table of revenue
st.table(data[['Quantity', 'Revenue','TotalCost']])
