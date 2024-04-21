import streamlit as st
# from project.mumbaistream import run_mumbai_app
from hyderabadstream import run_hyderabad_app
# from project.hyedrabadstream import run_hyedrabad_app

st.title("Public Infrastructure")
# Options for different cities
options = ["Select your city", "Mumbai", "Delhi", "Hyderabad"]
selected_city = st.selectbox("Choose a city:", options)

# Link to the Streamlit app based on the selected city
if selected_city == "Select your city":
    st.write("")
elif selected_city == "Hyderabad":
     run_hyderabad_app()

# elif selected_city == "Mumbai":
#     run_mumbai_app()
# elif selected_city == "Delhi":
#     run_delhi_app()
# elif selected_city == "Hyderabad":
#     run_hyedrabad_app()
#     st.write("Streamlit app for Hyderabad is not available yet.")
