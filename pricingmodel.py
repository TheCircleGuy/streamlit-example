import streamlit as st
import pandas as pd
import numpy as np

st.balloons()

# Input variables
with st.sidebar:
    Profit = st.number_input('Insert Desired Profit Constant', value=10000, key="a0")

    MonthlyCost = st.number_input('Insert Monthly Cost', value=31530, key="a1")

    ProjPerManager = st.number_input('Insert Number of Projects per Manager', value=4, key="a2")

    ManagerSalary = st.number_input('Insert Manager Salary', value=681, key="a3")

    ProjPerServer = st.number_input('Insert Number Of Projects per SERVER', value=4, key="a4")

    ServerCost = st.number_input('Insert Server Cost', value=197, key="a5")

    Commision = st.number_input('Insert Commission Percentage', value=0.01, key="a6")

    avgTransValue = st.number_input('Insert Average Transaction Value ', value=2, key="a7")

    avgTransPerStore = st.number_input('Insert Average Transactions Per Store', value=533, key="a11")

    avgLicensePerClient = st.number_input('Medium Size Clients (Number of Stores per sales)', value=20, key="a8")

    price = st.number_input('Insert price to be sold', value=2000, key="a9")

    sales = st.slider(
        'Sales Volume',
        0, 200, (1, 30), key="a10")

# Create a table to display the listed variables
table_data = {
    'Inputs': ['Monthly Cost', 'Number of Projects per Manager', 'Manager Salary',
                 'Number Of Projects per SERVER', 'Server Cost', 'Commission Percentage',
                 'Average Revenue Of License', 'Average Licenses per Client', 'Price to be sold',
                 'Range of Licenses', 'Desired Profit'],
    'Value': [MonthlyCost, ProjPerManager, ManagerSalary, ProjPerServer, ServerCost,
              Commision, avgTransValue, avgLicensePerClient, price, f"{sales[0]} to {sales[1]}", Profit]
}



# Calculate the revenue, fixed cost, variable cost, and total cost for each quantity
Sales = list(range(sales[0], (sales[1] + 1) ))


revenue = [(price * avgLicensePerClient * q + Commision * avgTransValue * avgTransPerStore * 12 * 30 * q) for q in Sales]

fixedCost = [MonthlyCost * 12 for q in Sales]
ExpectedProfits = [Profit * 1 for q in Sales]

# TotalManagerSalary = [
#     ManagerSalary * q if (q // avgLicensePerClient) % ProjPerServer == 0 else ManagerSalary * (q + 1)
#     for q in Sales
# ]

TotalManagerSalary = []
for q in Sales:
    if q < 5:
        TotalManagerSalary.append(ManagerSalary*12)
    else:
        if (q % ProjPerManager) > 0:
            TotalManagerSalary.append((q // ProjPerManager + 1) * ManagerSalary*12)
        else:
            TotalManagerSalary.append((q // ProjPerManager) * ManagerSalary*12)

TotalServerCost = []
for q in Sales:
    if q < 5:
        TotalServerCost.append(ServerCost*12)
    else:
        if (q % ProjPerManager) > 0:
            TotalServerCost.append((q // ProjPerServer + 1) * ServerCost*12)
        else:
            TotalServerCost.append((q // ProjPerServer) * ServerCost*12)  
            
VariableCost = np.array(TotalManagerSalary) + np.array(TotalServerCost)

TotalCost = np.array(fixedCost) + np.array(VariableCost)

TargetCost = np.array(TotalCost) + np.array(ExpectedProfits)

EstimatedProfit = np.array(revenue) - np.array(TotalCost)


show_last_table = st.checkbox("Show/Hide Inputs Table")

# Show the last table only if the checkbox is checked
if show_last_table:
    st.table(table_data)

# BreakEvenSales = None
# for q in range(len(Sales)):
#     if revenue[q] - TotalCost[q] >= 0:
#         BreakEvenSales = Sales[q]
#         break

# if BreakEvenSales is not None:
#     st.write("When Sales =", BreakEvenSales, "; Revenue =", revenue[q], "; Total Cost =", TotalCost[q])
# else:
#     st.write("No Break-Even Sales found. Searching for optimal price and sales to break even.")

#     optimal_price = None
#     optimal_sales = None
#     found = False

#     for new_price in range(price, 10000, 100):  # Change the range and step size as needed
#         for new_sales in range(1, 1000):  # Change the range as needed
#             new_revenue = (new_price * avgLicensePerClient * new_sales + Commision * avgTransValue * avgTransPerStore * 12 * 30 * new_sales)
#             new_total_cost = (MonthlyCost * 12 + new_sales * ManagerSalary + new_sales * ServerCost)
#             if new_revenue - new_total_cost >= 0:
#                 optimal_price = new_price
#                 optimal_sales = new_sales
#                 found = True
#                 break
#         if found:
#             break

#     if optimal_price and optimal_sales:
#         st.write("Optimal Price:", optimal_price)
#         st.write("Optimal Sales Volume:", optimal_sales)
#     else:
#         st.write("No optimal price and sales combination found to break even.")

# Check for Break-Even Sales
BreakEvenSales = None
for q in range(len(Sales)):
    if revenue[q] - TotalCost[q] >= 0:
        BreakEvenSales = Sales[q]
        break

st.text("")
st.text("")
st.text("")

# Display loading section
with st.spinner("Wait A Sec, Dan!"):
    if BreakEvenSales is not None:
        st.write("When Sales =", BreakEvenSales, "; Revenue =", revenue[q], "; Total Cost =", TotalCost[q])
    else:
        # Find the 5 most optimal price and sales pairs to break even
        st.write("No exact Break-Even Sales found. Finding 5 most optimal price and sales pairs to break even...")

        optimal_pairs = []
        max_combinations = 5  # You can change this to get more or fewer combinations

        for p in range(500, 2500000, 100):
            for s in range(1, 200):
                revenue = p * avgLicensePerClient * s + Commision * avgTransValue * avgTransPerStore * 12 * 30 * s
                fixed_cost = MonthlyCost * 12
                variable_cost = ManagerSalary * s if s < 5 else (s // ProjPerManager + 1) * ManagerSalary
                total_cost = fixed_cost + variable_cost
                expected_profit = revenue - total_cost
                if expected_profit >= Profit:
                    optimal_pairs.append((p, s, revenue, total_cost))
                    if len(optimal_pairs) >= max_combinations:
                        break
            if len(optimal_pairs) >= max_combinations:
                break

        st.write("5 Most Optimal Price and Sales Pairs to Break Even:")
        for i, pair in enumerate(optimal_pairs):
            st.write(f"Option {i + 1}: Price: {pair[0]}, Sales: {pair[1]}, Revenue: {pair[2]}, Total Cost: {pair[3]}")


st.text("")
st.text("")
st.text("")

st.write("Note that: _Total_Cost = _Fixed_Cost + _Variable_Cost. And Variable Cost is small comparing to the Revenue. Thus you will see the _Total_Cost and _Fixed_Cost almost coincide. Zoom to see clearly 2 lines ")
st.text("")
st.text("")
st.text("")
st.text("")

# Create a DataFrame to hold the data
data = pd.DataFrame({
    'Quantity': Sales,
    'Fixed Cost': fixedCost,
    'Total Cost': TotalCost,
    'Revenue': revenue,
    'ServerCost': TotalServerCost,
    #'Desired Profit': [Profit] * len(Sales) + TotalCost,
    'Target Cost': TargetCost,
    'Variable Cost': VariableCost,
    'Estimated Profit': EstimatedProfit,

})

# Create a line chart for Fixed Cost, Total Cost, Target Cost, and Revenue
st.markdown('<div style="text-align: center;">MODEL CALCULATION</div>', unsafe_allow_html=True)
st.text("")
st.line_chart(data.set_index('Quantity')[[
    'Fixed Cost', 
    'Total Cost', 
    'Target Cost',
    'Revenue',
    # 'ServerCost',
    # 'Variable Cost',
    # 'Estimated Profit'
    
    ]])





data = pd.DataFrame({
    'Quantity': Sales,
    'Fixed Cost': fixedCost,
    'Total Cost': TotalCost,
    'Revenue': revenue,
    'Estimated Profit': EstimatedProfit,
    'Desired Profit': [Profit] * len(Sales),
    'Variable Cost': VariableCost,
    'Total Salary': TotalManagerSalary,
    
})

st.text("")
st.text("")
st.text("")

show_last_table = st.checkbox("Show/Hide Variables Table")

# Show the last table only if the checkbox is checked
if show_last_table:
    st.markdown('<div style="text-align: center;">Variable Table</div>', unsafe_allow_html=True)
    st.text("")
    st.table(data[[
        'Quantity',
        'Fixed Cost',
        'Total Cost',
        'Revenue',
        'Estimated Profit',
        'Desired Profit',
        'Variable Cost',
        'Total Salary',
    ]])
