import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: #080b54;'>Pricing Model</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #0d043b;'>Target Medium Size Businesses: 10 -30 stores</h3>", unsafe_allow_html=True)

 
with st.container():
    st.markdown("<h2 style='text-align: center; color: #0d043b;'>Inputs</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #0d043b;'>Target Profit</h3>", unsafe_allow_html=True)
    Profit = st.number_input('', value=10000, key="a0")
    # st.title('Inputs')
    st.markdown("<h3 style='text-align: center; color: #0d043b;'>Cost Inputs</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col2:
      # st.subheader('Monthly Cost')
      MonthlyCost = st.number_input('Monthly Cost', value=32541, key="a1")  
      st.markdown("<h4 style='text-align: center; color: #0d043b;'>Variable Costs</h4>", unsafe_allow_html=True)
 
    col_1, col_2, col_3, col_4 = st.columns(4)
    with col_1:
    # st.subheader('Projects per Server')
     ProjPerServer = st.number_input('Projects per Server', value=4, key="a4")
     SRAnalyst = st.number_input('Projects per administrator', value=6, key="a21")
     QALeads = st.number_input('Projects per System Admin', value=10, key="a17")

    with col_2:
    # st.subheader('Manager Salary')
     ManagerSalary = st.number_input('Account Manager Salary', value=667, key="a3")
     JRAnalystSalary = st.number_input('Junior Analyst Salary', value=833, key="a20")
     ProductOwnerSalary = st.number_input('Product Owner Cost', value=0, key="a16")

    with col_3:
    # st.subheader('Projects per Manager')
     ProjPerManager = st.number_input('Projects per Account Manager', value=10, key="a2")
     JRAnalyst = st.number_input('Projects per Junior Analyst', value=10, key="a119")
     ProductOwner = st.number_input('Projects per Product Owner', value=0, key="a15")

    with col_4:
    # st.subheader('Server Cost')
     ServerCost = st.number_input('Server Cost', value=193, key="a5")
     SRAnalystSalary = st.number_input('Administrator Salary', value=333, key="a22")
     QALeadsCost = st.number_input('System Admin Cost', value=667, key="a18")

    st.markdown("<h4 style='text-align: center; color: #0d043b;'>Revenue Inputs</h4>", unsafe_allow_html=True)

    coll1, coll2, coll3, coll4, coll5, coll6 = st.columns(6)
    with coll1:
        avgLicensePerClient = st.number_input('Medium Size Clients', value=20, key="a8")   
    with coll2:
        avgTransPerStore = st.number_input('Average Transactions Per Store', value=533, key="a11")
    with coll3:
        Commision = st.number_input('Commision (%)', value=1, key="a6") /100
    with coll4:
        avgTransValue = st.number_input('Average Transaction Value', value=2, key="a7")
    with coll5:
        
        price = st.number_input('Price of Annual License', value=2000, key="a9")
    with coll6:
        competitorPrice = st.number_input('Competitor Annual License Price', value=2500, key="30")
        
    st.markdown("<h4 style='text-align: center; color: #0d043b;'>Sales Volume Range</h4>", unsafe_allow_html=True)
    
    sales = st.slider('', 0, 200, (1, 30), key="a10")

diffbetweenCompetitor = price - competitorPrice    

# Create a table to display the listed variables
table_data = {
    'Inputs': ['Monthly Cost', 'Number of Projects per Manager', 'Manager Salary',
                 'Number Of Projects per SERVER', 'Server Cost', 'Commission Percentage',
                 'Average Revenue Of License', 'Average Licenses per Client', 'Price to be sold',
                 'Range of Licenses', 'Desired Profit'],
    'Value': [MonthlyCost, ProjPerManager, ManagerSalary, ProjPerServer, ServerCost,
              Commision, avgTransValue, avgLicensePerClient, price, f"{sales[0]} to {sales[1]}", Profit]
}

show_last_table = st.checkbox("Show/Hide Inputs Table", value=True)

# Show the last table only if the checkbox is checked
if show_last_table:
    st.table(table_data)

# Calculate the revenue, fixed cost, variable cost, and total cost for each quantity
Sales = list(range(sales[0], (sales[1] + 1) ))


revenue = [(price * avgLicensePerClient * q + Commision * avgTransValue * avgTransPerStore * 12 * 30 * q) for q in Sales]

fixedCost = [MonthlyCost * 12 for q in Sales]
ExpectedProfits = [Profit * 1 for q in Sales]

TotalManagerSalary = []
for q in Sales:
    if q <= ProjPerManager:
        TotalManagerSalary.append(ManagerSalary*12)
    else:
        if (q % ProjPerManager) > 0:
            TotalManagerSalary.append((q // ProjPerManager + 1) * ManagerSalary*12)
        else:
            TotalManagerSalary.append((q // ProjPerManager) * ManagerSalary*12)


TotalServerCost = []
for q in Sales:
    if q <= ProjPerServer:
        TotalServerCost.append(ServerCost*12)
    else:
        if (q % ProjPerManager) > 0:
            TotalServerCost.append((q // ProjPerServer + 1) * ServerCost*12)
        else:
            TotalServerCost.append((q // ProjPerServer) * ServerCost*12)  

TotalProductOwnerCost = []
if ProductOwner > 0 :
 for q in Sales:
     if q <= ProductOwner:
         TotalProductOwnerCost.append(ProductOwnerSalary*12)
     else:
         if (q % ProductOwner) > 0:
             TotalProductOwnerCost.append((q // ProductOwner + 1) * ProductOwnerSalary*12)
         else:
             TotalProductOwnerCost.append((q // ProductOwner) * ProductOwnerSalary*12)  
else:
  for q in Sales:
    TotalProductOwnerCost.append(0)
   
TotalQALeadsCost = []
if QALeads > 0 :
 for q in Sales:
     if q <= QALeads:
         TotalQALeadsCost.append(QALeadsCost*12)
     else:
         if (q % QALeads) > 0:
             TotalQALeadsCost.append((q // QALeads + 1) * QALeadsCost*12)
         else:
             TotalQALeadsCost.append((q // QALeads) * QALeadsCost*12)  
else:
  for q in Sales:
    TotalQALeadsCost.append(0)
   

TotalJRAnalystSalary = []
if JRAnalyst> 0:
 for q in Sales:
     if q <= JRAnalyst:
         TotalJRAnalystSalary.append(JRAnalystSalary*12)
     else:
         if (q % JRAnalyst) > 0:
             TotalJRAnalystSalary.append((q // JRAnalyst + 1) * JRAnalystSalary*12)
         else:
             TotalJRAnalystSalary.append((q // JRAnalyst) * JRAnalystSalary*12)  
else:
  for q in Sales:
    TotalJRAnalystSalary.append(0)
   

TotalSRAnalystSalary = []
if SRAnalyst >0:
 for q in Sales:
     if q <= SRAnalyst:
         TotalSRAnalystSalary.append(SRAnalystSalary*12)
     else:
         if (q % SRAnalyst) > 0:
             TotalSRAnalystSalary.append((q // SRAnalyst + 1) * SRAnalystSalary*12)
         else:
             TotalSRAnalystSalary.append((q // SRAnalyst) * SRAnalystSalary*12)  
else:
  for q in Sales:
    TotalSRAnalystSalary.append(0)
   
VariableCost = np.array(TotalManagerSalary) + np.array(TotalServerCost) + np.array(TotalJRAnalystSalary) + np.array(TotalSRAnalystSalary) + np.array(TotalQALeadsCost) + np.array(TotalProductOwnerCost) 


TotalCost = np.array(fixedCost) + np.array(VariableCost)

TargetCost = np.array(TotalCost) + np.array(ExpectedProfits)

EstimatedProfit = np.array(revenue) - np.array(TotalCost)




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
        # st.write("When Sales =", BreakEvenSales, "; Revenue =", revenue[q], "; Total Cost =", TotalCost[q])
# Target Sales, Target Revenue, Total Cost, Profit, Nearest  competitor, Diff between competitor [Speedpos] )
        col1, col2, col3, col4= st.columns(4)
        with col1:
            col1.metric("Target Sales ", value = BreakEvenSales)

     
        # st.markdown("<h4 class="small-font; style='text-align: center; color: #0d043b;'>Total Cost = Fixed Cost + Variable Cost || Fixed Cost = Monthly Cost x 12 || Variable Cost = Server Cost + Salaries</h4>", unsafe_allow_html=True)
        # st.markdown("<h4 class="small-font"; style='text-align: center; color: #0d043b;'>Revenue = (annual license price x sales x average number of stores) + (average number transactions x average transaction vale)>", unsafe_allow_html=True)
        col2.metric("Target Revenue", value = revenue[q] )
        col3.metric("Total Cost", value = TotalCost[q] )
        col4.metric("Profit", value =  "{:.2f}".format(revenue[q] - TotalCost[q]) )
        st.divider()
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("", "")
        col2.metric("Nearest  competitor price", value = competitorPrice)
        col3.metric("Difference between competitor", value = price-competitorPrice)
        col4.metric("", "")
     
        # col1, col2, col3 = st.columns(3)
        # col1.metric("Target Sales", "70 °F", "1.2 °F")
        # col2.metric("Wind", "9 mph", "-8%")
        # col3.metric("Humidity", "86%", "4%")
    
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

   
st.markdown("<p style='text-align: center; font-size: 12px;'>Total Cost = Fixed Cost + Variable Cost || Fixed Cost = Monthly Cost x 12 || Variable Cost = Server Cost + Salaries</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px;'>Revenue = (annual license price x sales x average number of stores) + (average number transactions x average transaction vale)</p>", unsafe_allow_html=True)

st.divider()    
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
    'Total Cost + Profit Target': TargetCost,
    'Variable Cost': VariableCost,
    'Estimated Profit': EstimatedProfit,

})
st.markdown('<div style="text-align: center;">Price - Volume - Sales Mix</div>', unsafe_allow_html=True)
st.text("")


st.line_chart( data=data.set_index('Quantity')[[ 'Fixed Cost',  'Total Cost',  'Total Cost + Profit Target', 'Revenue']])


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

show_last_table = st.checkbox("Click to see detailed ouputs")

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
