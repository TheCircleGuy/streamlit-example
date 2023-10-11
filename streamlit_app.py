from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
"""
# Pricing Model

Somethingcool-Somethingcool-Somethingcool-Somethingcool-Somethingcool-Somethingcool-Somethingcool-Somethingcool-Somethingcool-Somethingcool
"""

# Sidebar
with st.sidebar:
    st.title("Sidebar")
    MonthlyCost = st.number_input('Insert Monthly Cost', value=13000)
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

# Main content
    st.title("Main Content")

# Calculate TotalManagerSalary, TotalServerCost, and VariableCost
quantities = range(0, 1001)
TotalManagerSalary = [
    ManagerSalary * q if (q // avgLicensePerClient) % ProjPerServer == 0 else ManagerSalary * (q + 1)
    for q in quantities
]
TotalServerCost = [
    ServerCost * q if (q // avgLicensePerClient) % ProjPerServer == 0 else ServerCost * (q + 1)
    for q in quantities
]
VariableCost = [TotalServerCost[i] + TotalManagerSalary[i] for i in range(len(quantities))]

# Calculate Fixedcost and TotalCost
Fixedcost = MonthlyCost * 12
TotalCost = [Fixedcost + VariableCost[i] for i in range(len(quantities))]

# Create a line chart
st.line_chart(
    np.column_stack((quantities, Fixedcost, TotalCost, VariableCost)),
    use_container_width=True,
)
st.write("Line Chart Explanation:")
st.write("X-axis: Number of Licenses")
st.write("Y-axis: Cost (Price)")
st.write("Blue Line: Fixed Cost")
st.write("Orange Line: Total Cost")
st.write("Green Line: Variable Cost")
