import streamlit as st
import streamlit as st
st.set_page_config(layout="wide")

# Define the URL for your logo image

logo_url = "https://softr-prod.imgix.net/applications/98b27be8-5282-4168-9e63-2aa100dc7626/assets/50f0ea3a-c669-4683-919a-74c4bae9e283.png"

# Use HTML and CSS to create the navigation bar with the logo
navbar_html = f"""
<div style="background-color: #08043d; padding: 10px;">
    <img src="{logo_url}" alt="Logo" style="height: 150px; width: 150px; float: left; margin-right: 10px;">
    <h1 style="color: white; text-align: center;">Pricing Model</h1>
</div> 
"""

# Render the navigation bar
st.markdown(navbar_html, unsafe_allow_html=True)

# Rest of your Streamlit app goes here
# For example:
st.title("Welcome to Your App")
st.write("This is the content of your app.")
