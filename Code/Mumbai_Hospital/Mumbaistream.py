import streamlit as st
from Mumbai_Hospitals import get_hospitals_starting_with
from Mumbai_Hospitals import get_beds_of_hospital_using_similarity
from Mumbai_Hospitals import get_contact_of_hospital, get_hospitals_and_addresses_with_keyword
from Mumbai_Hospitals import get_hospitals_by_address,count_hospitals_at_address

def run_Mumbai_app():
    # Streamlit UI
    st.title("Mumbai")

    # Options for different categories
    options = ["Select","Schools", "Banks", "Hospitals", "Public transport"]
    selected_option = st.selectbox("Choose an option:", options)

    # # Show relevant options based on user selection
    # if selected_option == "Public transport":
    #     run_public_transport()

    # Add functionality for other options
   

    if selected_option == "Hospitals":
        st.write("Hospitals information will be displayed here.")
        # Load the hospital data and display the relevant information
        # You can directly call the functions from Hyderabad_Hospitals.py

        hospital_name = st.text_input("Enter the Hospital name to get the contact of hospitals:")
        if st.button("Get Contact Information of the hospital"):
            contact = get_contact_of_hospital(hospital_name)
            st.write(f"Count of Hospitals in {hospital_name}:", contact)

        hospital_name = st.text_input("Enter the hospital name to get the number of beds available:")
        if st.button("Get the number of beds available of the named Hospital"):
            beds = get_beds_of_hospital_using_similarity(hospital_name)
            st.write(f"Hospitals and Addresses with Department '{hospital_name}':", beds)

        address = st.text_input("Enter the address to get hospitals:")
        if st.button("Get Hospitals from the address"):
            hospitals_by_address = get_hospitals_by_address(address)
            st.write(f"Hospitals in Category '{address}':", hospitals_by_address)

        hospital_name = st.text_input("Enter the hospital name to get address:")
        if st.button("Get Address of Hospital"):
            address = get_hospitals_and_addresses_with_keyword(hospital_name)
            st.write(f"Address of {hospital_name}:", address)

        address = st.text_input("Enter the address to get the count of the hospitals available at that address:")
        if st.button("Get Hospitals with Department"):
            hospitals_with_department = count_hospitals_at_address(address)
            st.write(f"Hospitals with Department '{address}':", hospitals_with_department)

        starts_with_letter_hospital = st.text_input("Enter a letter to find hospital names starting with that letter (e.g., A):")
        if starts_with_letter_hospital:
            hospitals_starts_with = get_hospitals_starting_with(starts_with_letter_hospital)
            st.write(f"Hospital Names Starting with {starts_with_letter_hospital}:", hospitals_starts_with)

        