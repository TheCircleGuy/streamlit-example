import streamlit as st
import pandas as pd
import numpy as np

# Input variables
with st.sidebar:
    st.title('Inputs')
    st.header('Target Profit')
    Profit = st.number_input('', value=10000, key="a0")
    st.divider()   
    st.header('Cost Input')
    st.subheader('Monthly Cost')
    MonthlyCost = st.number_input('', value=31530, key="a1")
    st.subheader('Projects per Manager')
    ProjPerManager = st.number_input('', value=4, key="a2")
    st.subheader('Manager Salary')
    ManagerSalary = st.number_input('', value=681, key="a3")
    st.subheader('Projects per Server')
    ProjPerServer = st.number_input('', value=4, key="a4")
    st.subheader('Server Cost')
    ServerCost = st.number_input('', value=197, key="a5")
    st.divider()
    st.header('Revenue Inputs')
    st.subheader('Commision perentage')
    Commision = st.number_input('', value=0.01, key="a6")
    st.subheader('Average Transaction Value')
    avgTransValue = st.number_input('', value=2, key="a7")
    st.subheader('Average Transactions Per Store')
    avgTransPerStore = st.number_input('', value=533, key="a11")
    st.subheader('Medium Size Clients')
    avgLicensePerClient = st.number_input('', value=20, key="a8")
    st.subheader('price to be sold')
    price = st.number_input('', value=2000, key="a9")
    st.subheader('Sales Volume')
    sales = st.slider(
        '',
        0, 200, (1, 30), key="a10")


st.markdown("<h1 style='text-align: center; color: #080b54;'>Pricing Model</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #0d043b;'>Target Medium Size Businesses: 10 -30 stores</h3>", unsafe_allow_html=True)

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
# Target Sales, Target Revenue, Total Cost, Profit, Nearest  competitor, Diff between competitor [Speedpos] )
        # col1, col2, col3 = st.columns(4)
        #     col1.metric("Target Sales", value = BreakEvenSales )
        #     col2.metric("Target Revenue", value = revenue[q] )
        #     col3.metric("Total Cost", value = TotalCost[q] )
        #     col3.metric("Profit", value =  revenue[q] - TotalCost[q] )
        #  st.divider()
        # col1, col2, col3 = st.columns(2)
        #     col1.metric("Nearest  competitor price", value = 2000)
        #     col2.metric("Diff between competitor", value = 0 )

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.metric("Temperature", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")
        col4.metric("Humidity", "86%", "4%")
        col5.metric("Humidity", "86%", "4%")
        col6.metric("Humidity", "86%", "4%")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.metric("Temperature", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")
        col4.metric("Humidity", "86%", "4%")
        col5.metric("Humidity", "86%", "4%")
        col6.metric("Humidity", "86%", "4%")

    
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
