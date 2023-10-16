import streamlit as st

st.markdown("<h1 style='text-align: center; color: #080b54;'>Pricing Model</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #0d043b;'>Target Medium Size Businesses: 10 -30 stores</h3>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Inputs", "Dashboard"])

with tab1:
    st.markdown("<h2 style='text-align: center; color: #0d043b;'>Inputs</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #0d043b;'>Target Profit</h3>", unsafe_allow_html=True)
    Profit = st.number_input('', value=10000, key="a0")
    # st.title('Inputs')
    st.markdown("<h3 style='text-align: center; color: #0d043b;'>Cost Inputs</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col2:
      # st.subheader('Monthly Cost')
      MonthlyCost = st.number_input('Monthly Cost', value=31530, key="a1")  

    st.markdown("<h4 style='text-align: center; color: #0d043b;'>Variable Costs</h4>", unsafe_allow_html=True)

    
    col_1, col_2, col_3, col_4 = st.columns(4)
    with col_1:
      
      # st.subheader('Projects per Manager')
      ProjPerManager = st.number_input('Projects per Manager', value=4, key="a2")
      ProductOwner = st.number_input('Projects per Product Owner', value=4, key="a15")
      JRAnalyst = st.number_input('Projects per Junior Analyst ', value=4, key="a119")
        
     
     
      
        
    with col_2:
      # st.subheader('Manager Salary')
      ManagerSalary = st.number_input('Manager Salary', value=681, key="a3")
      ProductOwnerSalary = st.number_input('Product Owner Cost', value=4, key="a16")
      JRAnalystSalary = st.number_input('Junior Analyst Salary', value=4, key="a20")
        
     

    with col_3:
      # st.subheader('Projects per Server')
      ProjPerServer = st.number_input('Projects per Server', value=4, key="a4")
      QALeads = st.number_input('Projects per QA Lead', value=4, key="a17") 
      SRAnalyst = st.number_input('Projects per Senior Analyst', value=4, key="a21")

    with col_4:
      # st.subheader('Server Cost')
      ServerCost = st.number_input('Server Cost', value=197, key="a5")
      QALeadsCost = st.number_input('QA Lead Cost', value=200, key="a18") 
      SRAnalystSalary = st.number_input('Senior Analyst Salary', value=4, key="a22")

col1, col2, col3 = st.columns(3)
    with col2:
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
