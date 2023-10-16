import streamlit as st

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
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

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
