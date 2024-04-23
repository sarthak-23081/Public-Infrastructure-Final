import streamlit as st
from Hyderabad_office import (
    get_all_offices,
    get_address_by_office_name,
    get_phone_number_by_office_name,
    get_office_name_by_address
)

def run_hyderabad_app():
    # Streamlit UI
    st.title("Hyderabad")

    # Options for different categories
    options = ["Select","Schools", "Banks", "Hospitals", "Public transport","Offices"]
    selected_option = st.selectbox("Choose an option:", options)

    if selected_option == "Offices":
        office_name_1 = st.text_input("Enter the name of the office to get the address:")
    
        if st.button("Get Address"):
            get_address_by_office_name_val = get_address_by_office_name(office_name_1)
            st.write(f"Address of  {office_name_1}:", get_address_by_office_name_val)

        office_name_2 = st.text_input("Enter the name of the office to get the Phone No.:")

        if st.button("Get Phone No. "):
            get_phone_number_by_office_name_val = get_phone_number_by_office_name(office_name_2)
            st.write(f"Phone No. of {office_name_2}:", get_phone_number_by_office_name_val)

        address = st.text_input("Enter the address of the office:")

        if st.button("Get Office Name by Address"):
            get_office_name_by_address_val = get_office_name_by_address(address)
            st.write(f"Get Office Name by Address {address}:", get_office_name_by_address_val)
    
        st.text("Retrieve all the offices")

        if st.button("Get all offices"):
            get_all_offices_val = get_all_offices()
            st.write(f"Get All Offices:", get_all_offices_val)

# Run the Streamlit app
if __name__ == "__main__":
    run_hyderabad_app()
