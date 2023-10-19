import streamlit as st
st.set_page_config(layout="wide")



# Define the URL for your logo image
logo_url = "https://example.com/your-logo-image.png"

# Use HTML and CSS to create the navigation bar with the logo and centered text
navbar_html = f"""
<div style="background-color: #08043d; padding: 10px;">
    <img src="{logo_url}" alt="Logo" style="height: 50px; width: 50px; float: left; margin-right: 10px;">
    <h1 style="color: white; text-align: center;">Pricing Model</h1>
</div>
"""



# Render the navigation bar
st.markdown(navbar_html, unsafe_allow_html=True)

# Rest of your Streamlit app goes here
# For example:
st.title("Welcome to Your App")
st.write("This is the content of your app.")
