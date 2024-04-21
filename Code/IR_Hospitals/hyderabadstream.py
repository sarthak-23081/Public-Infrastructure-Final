
import streamlit as st
# from project.school.delhischool import get_schools_in_region, count_schools_in_region, get_school_levels_in_region
# from project.school.delhischool import get_schools_and_levels_in_region
# from project.school.delhischool import get_zone_of_school, get_schools_by_zone, get_school_names_starting_with
# from project.school.delhischool import get_school_names_with_level, get_phone_number_of_school
from Hyderabad_Hospitals import get_hospitals_in_zone, count_hospitals_in_zone
from Hyderabad_Hospitals import get_hospitals_and_addresses_with_department, get_hospitals_in_category
from Hyderabad_Hospitals import get_address_of_hospital, get_hospitals_with_department
from Hyderabad_Hospitals import get_department_of_hospital, get_hospitals_starting_with
from Hyderabad_Hospitals import get_category_of_hospital, get_zone_of_hospital

def run_public_transport():
    st.title("Public Transport Information")

    # Options for different modes of public transport
    options = ["Metro", "Railways", "Buses", "Airport"]
    selected_option = st.selectbox("Choose a mode of public transport:", options)

    # Show relevant options based on user selection
    if selected_option == "Metro":
        st.title("Metro Station Information")
        # Load the metro data and display the relevant information
        # You can directly call the functions from hyedrabadmetro.py
        desired_area_layout = st.text_input("Enter the area to get the layout information:")
        if st.button("Get Layout Information"):
            layout_answer = get_layout(desired_area_layout)
            st.write("Layout Answer:", layout_answer)

        desired_area_status = st.text_input("Enter the area to get the status information:")
        if st.button("Get Status Information"):
            status_answer = get_status(desired_area_status)
            st.write("Status Answer:", status_answer)

        starts_with_letter = st.text_input("Enter a letter to find station names starting with that letter (e.g., A):")
        if starts_with_letter:
            starts_with_answer = get_station_names_starting_with(starts_with_letter)
            st.write(f"Station Names Starting with {starts_with_letter}:", starts_with_answer)
            
        
        
        desired_station = st.text_input("Enter the station name to know line:")
        if st.button("Get Station Line"):
            line = get_line_of_station(desired_station)
            st.write(f"Line of {desired_station}: {line}")

        desired_line = st.text_input("Enter the line (e.g. Blue line):")
        if st.button("Get Stations on Line"):
            stations = get_stations_on_line(desired_line)
            st.write(f"Stations on {desired_line} line: {stations}")

        desired_lay = st.text_input("Enter the desired status to find station names with that layout (e.g., Elevated):")
        if desired_lay:
            status_match_answer = get_station_names_with_layout(desired_lay)
            st.write(f"Station Names with Layout '{desired_lay}':", status_match_answer)

    elif selected_option == "Railways":
        st.write("Railways information will be displayed here.")

    elif selected_option == "Buses":
        st.write("Bus information will be displayed here.")

    elif selected_option == "Airport":
        st.write("Airport information will be displayed here.")

def run_hyderabad_app():
    # Streamlit UI
    st.title("Hyedrabad")

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
        
        zone_name = st.text_input("Enter the zone to get hospitals:")
        if st.button("Get Hospitals in Zone"):
            hospitals_in_zone = get_hospitals_in_zone(zone_name)
            st.write(f"Hospitals in {zone_name} zone:", hospitals_in_zone)

        zone_name_count = st.text_input("Enter the zone to get count of hospitals:")
        if st.button("Get Count of Hospitals in Zone"):
            count = count_hospitals_in_zone(zone_name_count)
            st.write(f"Count of Hospitals in {zone_name_count}:", count)

        department_name = st.text_input("Enter the department to get hospitals and addresses:")
        if st.button("Get Hospitals and Addresses with Department"):
            hospitals_and_addresses = get_hospitals_and_addresses_with_department(department_name)
            st.write(f"Hospitals and Addresses with Department '{department_name}':", hospitals_and_addresses)

        category_name = st.text_input("Enter the category to get hospitals:")
        if st.button("Get Hospitals in Category"):
            hospitals_in_category = get_hospitals_in_category(category_name)
            st.write(f"Hospitals in Category '{category_name}':", hospitals_in_category)

        hospital_name = st.text_input("Enter the hospital name to get address:")
        if st.button("Get Address of Hospital"):
            address = get_address_of_hospital(hospital_name)
            st.write(f"Address of {hospital_name}:", address)

        department_name_hospital = st.text_input("Enter the department to get hospitals:")
        if st.button("Get Hospitals with Department"):
            hospitals_with_department = get_hospitals_with_department(department_name_hospital)
            st.write(f"Hospitals with Department '{department_name_hospital}':", hospitals_with_department)

        starts_with_letter_hospital = st.text_input("Enter a letter to find hospital names starting with that letter (e.g., A):")
        if starts_with_letter_hospital:
            hospitals_starts_with = get_hospitals_starting_with(starts_with_letter_hospital)
            st.write(f"Hospital Names Starting with {starts_with_letter_hospital}:", hospitals_starts_with)

        hospital_name_zone = st.text_input("Enter the hospital name to get zone:")
        if st.button("Get Zone of Hospital"):
            zone = get_zone_of_hospital(hospital_name_zone)
            st.write(f"Zone of {hospital_name_zone}:", zone)

        hospital_name_category = st.text_input("Enter the hospital name to get category:")
        if st.button("Get Category of Hospital"):
            category = get_category_of_hospital(hospital_name_category)
            st.write(f"Category of {hospital_name_category}:", category)

        hospital_name_department = st.text_input("Enter the hospital name to get department:")
        if st.button("Get Department of Hospital"):
            department = get_department_of_hospital(hospital_name_department)
            st.write(f"Department of {hospital_name_department}:", department)

        