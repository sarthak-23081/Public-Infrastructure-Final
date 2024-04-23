import streamlit as st
from delhistream import run_delhi_app
from Hyderabadstream import run_hyderabad_app

st.title("Public Infrastructure")
# Options for different cities
options = ["Select your city", "Mumbai", "Delhi", "Hyderabad"]
selected_city = st.selectbox("Choose a city:", options)

# Link to the Streamlit app based on the selected city
if selected_city == "Select your city":
    st.write("")
elif selected_city == "Mumbai":
    # run_mumbai_app()
    x = 5
elif selected_city == "Delhi":
    run_delhi_app()
elif selected_city == "Hyderabad":
    run_hyderabad_app()
    
