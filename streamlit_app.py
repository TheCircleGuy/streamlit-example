import streamlit as st
import pandas as pd
import numpy as np
st.write("TEST")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["colxx", "col2", "col3"])

st.line_chart(
   chart_data, x="colxx", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)
