import streamlit as st
# from project.mumbaistream import run_mumbai_app
from delhistream import run_delhi_app
# from project.hyedrabadstream import run_hyedrabad_app

st.title("Public Infrastructure")
# Options for different cities
options = ["Select your city", "Mumbai", "Delhi", "Hyderabad"]
selected_city = st.selectbox("Choose a city:", options)

# Link to the Streamlit app based on the selected city
if selected_city == "Select your city":
    st.write("")
   # run_mumbai_app()
   
elif selected_city == "Delhi":
    run_delhi_app()

