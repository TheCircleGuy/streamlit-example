import streamlit as st
import pandas as pd
import numpy as np



with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")
        MonthlyCost=  st.number_input('Insert Monthly Cost')
        st.write('The current number is ', MonthlyCost)

        AnnualCost = MonthlyCost *12

        ProjPerManager=  st.number_input('Insert Number of Projects per Manager',key="a1")
        st.write('The current number is ', ProjPerManager)

        ManagerSalary=  st.number_input('Insert Manager Salary',key="a2")
        st.write('The current number is ', ManagerSalary)

        ProjPerServer=  st.number_input('Insert Number Of Projects per SERVER',key="a3")
        st.write('The current number is ', ProjPerServer)

        ServerCost=  st.number_input('Insert Server Cost',key="a4")
        st.write('The current number is ', ServerCost)

with st.spinner("Loading..."):
    time.sleep(5)
    st.success("Done!")





st.title('POS Pricing Model')
chart_data = pd.DataFrame(
   {
       "col1": list(range(20)) * 3,
       "col2": np.random.randn(60),
       "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
   }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")
