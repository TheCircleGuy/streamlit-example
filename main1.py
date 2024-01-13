import streamlit as st
import pandas as pd
import numpy as np

with st.sidebar:
     
     st.title('POS Pricing Model')

     MonthlyCost=  st.number_input('Insert Monthly Cost', value=31530.74)

     ProjPerManager=  st.number_input('Insert Number of Projects per Manager', value = 4, key="a1")

     ManagerSalary=  st.number_input('Insert Manager Salary', value = 681, key="a2")

     ProjPerServer=  st.number_input('Insert Number Of Projects per SERVER', value = 4, key="a3")

     ServerCost=  st.number_input('Insert Server Cost', value = 197, key="a4")

     Commision=  st.number_input('Insert Commission Percentage', value = 0.001, key="a5")

     avgRevLicense = st.number_input('Insert Average Revenue Of License', value = 1000, key="a6")

     avgLicensePerClient = st.number_input('Insert Average Licenses per Client', value = 10, key="a7")

     price=  st.number_input('Insert price to be sold', value = 2000, key="a8")

     licenses = st.slider(
    'Select a range of licenses to be sold',
    0, 1000, (60, 150), key="a9")
    
TotalServerCost = []
TotalManagerSalary = []
x = 2000  # Price per product
a = 100   # Minimum quantity
b = 150   # Maximum quantity
cogs = 500  # Cost of goods sold per product

# Create a list of quantities from a to b
quantities = list(range(a, b + 1))

# Calculate revenue and profit for each quantity
sellRevenue = [(x * q for q in quantities)]
CommisionRevenue = [(avgRevLicense*Commision * q for q in quantities)]
REVENUE = [sellRevenue+CommisionRevenue]
print(REVENUE)

data = pd.DataFrame({'Quantity': quantities, 'Revenue': REVENUE })
# fixedCost = np.full(len(quantities),MonthlyCost*12)

# for q in quantities:
#      if ((q//avgLicensePerClient)%ProjPerServer==0):
#           TotalManagerSalary[q] = ManagerSalary*q
#           TotalServerCost[q] = ServerCost*q
#      else:
#           TotalServerCost[q] = ServerCost*(q+1)
#           TotalManagerSalary[q] = ManagerSalary*(q+1)

# COST = TotalManagerSalary + TotalServerCost +fixedCost

# data = pd.DataFrame({'Quantity': quantities, 'Revenue': revenue, 'COST': COST})


# st.line_chart(data.set_index('Quantity'))



# revenue = price * quantities + %commission*value*quantitities

