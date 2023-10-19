import streamlit as st

# Set the page configuration to "wide"
st.set_page_config(layout="wide")

# Add a logo in the top-left corner
logo_path = 'https://github.com/TheCircleGuy/streamlit-example/blob/d1f324eeb17435412413f340d1cf2f22c50bee51/assets/logo.png'
st.sidebar.image(logo_path, use_column_width=True)

# Create a centered title using Markdown
st.markdown("<h1 style='text-align: center;'>Cost Volume Profit Analysis</h1>", unsafe_allow_html=True)

# Rest of your Streamlit app goes here
# You can add other content below the title, like charts, tables, or interactive elements.
   
