import streamlit as st
from Delhi_office import (
    get_addresses_from_govt_office,
    get_list_of_all_govt_offices,
    get_govt_offices_for_person,
    find_details_for_contact_person,
    get_govt_office_person_association,
    get_contact_person_for_govt_office
)

from Hyderabad_office import (
    get_all_offices,
    get_address_by_office_name,
    get_phone_number_by_office_name,
    get_office_name_by_address
)

def run_public_transport():
    # Define the function for public transport information here
    print("blah")

def run_delhi_app():
    # Streamlit UI
    st.title("Delhi")

    # Options for different categories
    options = ["Select","Schools", "Banks", "Hospitals", "Public transport","Offices"]
    selected_option = st.selectbox("Choose an option:", options)

    # Show relevant options based on user selection
    if selected_option == "Public transport":
        run_public_transport()

    # Add functionality for other options
    elif selected_option == "Schools":
        # Define the functionality for schools information here
        x = 5

    elif selected_option == "Banks":
        x = 5
        # Define the functionality for banks information here

    elif selected_option == "Hospitals":
        # Define the functionality for hospitals information here
        x = 5

    elif selected_option == "Offices":
        st.title("Government Offices Information")


        # Collect user input for person's name
        person_name = st.text_input("Enter the name of the person:")

        # Button to trigger getting government offices for person
        if st.button("Get Government Offices for Person"):
            govt_offices_for_person = get_govt_offices_for_person(person_name)
            st.write(f"Government offices associated with {person_name}:", govt_offices_for_person)

        # Collect user input
        office_type = st.text_input("Enter the type of government office (e.g., Post Office, Police Station):")

        # Button to trigger the data retrieval
        if st.button("Get Addresses"):
            office_addresses = get_addresses_from_govt_office(office_type)
            st.write(f"Addresses of {office_type}:", office_addresses)


        # Collect user input for contact person's name
        contact_person_name = st.text_input("Enter the name of the contact person:")

        # Button to trigger getting contact person's details
        if st.button("Get Contact Person's Details"):
            contact_person_details = find_details_for_contact_person(contact_person_name)
            st.write("Contact Person's Details:")
            st.write(contact_person_details)

        

        # Collect user input for government office name
        govt_office_name = st.text_input("Enter the name of the government office:")

        # Button to trigger getting contact person for government office
        if st.button("Get Contact Person for Government Office"):
            contact_person_for_govt_office = get_contact_person_for_govt_office(govt_office_name)
            st.write(f"Contact person for {govt_office_name}:", contact_person_for_govt_office)



        # Button to get the list of all government offices
        if st.button("Get List of Government Offices"):
            st.subheader("List of Government Offices")
            all_govt_offices = get_list_of_all_govt_offices()
            st.write(all_govt_offices)

        # Button for getting government office - contact person association
        if st.button("Get Government Office - Contact Person Association"):
            st.subheader("Government Office - Contact Person Association")
            govt_office_person_association = get_govt_office_person_association()
            st.write(govt_office_person_association)

        

# Run the Streamlit app
if __name__ == "__main__":
    run_delhi_app()


def run_hyedrabad_app():
    # Streamlit UI
    st.title("Hyderabad")

    if st.button("Get all offices"):
        get_all_offices_val = get_all_offices()
        st.write(f"Get All Offices:", get_all_offices_val)

    office_name = st.text_input("Enter the name of the office:")
    
    if st.button("Get Address by Office Name"):
        get_address_by_office_name_val = get_address_by_office_name(office_name)
        st.write(f"Get Address by Office Name {office_name}:", get_address_by_office_name_val)

    if st.button("Get Phone No. by Office Name"):
        get_phone_number_by_office_name_val = get_phone_number_by_office_name(office_name)
        st.write(f"Get Phone No. by Office Name {office_name}:", get_phone_number_by_office_name_val)

    address = st.text_input("Enter the address of the office:")

    if st.button("Get Office Name by Address"):
        get_office_name_by_address_val = get_office_name_by_address(address)
        st.write(f"Get Office Name by Address {address}:", get_office_name_by_address_val)

# Run the Streamlit app
if __name__ == "__main__":
    run_hyedrabad_app()

