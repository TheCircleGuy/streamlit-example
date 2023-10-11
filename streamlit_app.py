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
    # ... Your existing sidebar code ...

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
