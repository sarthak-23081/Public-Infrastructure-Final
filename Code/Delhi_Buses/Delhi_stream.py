#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
# from project.metro.delhimetro import get_layout, get_status, get_station_names_starting_with, get_station_names_with_layout
# from project.metro.delhimetro import  get_line_of_station, get_stations_on_line
# from project.school.delhischool import get_schools_in_region, count_schools_in_region, get_school_levels_in_region
# from project.school.delhischool import get_schools_and_levels_in_region
# from project.school.delhischool import get_zone_of_school, get_schools_by_zone, get_school_names_starting_with
# from project.school.delhischool import get_school_names_with_level, get_phone_number_of_school
# from Mumbai_buses import get_buses_in_depot,count_bus_stations_in_depot,get_major_operations_of_depot,get_depot_by_code,get_bus_stations_by_route,get_buses_by_major_operation,get_buses_starting_with,count_buses_in_region,list_bus_stations_in_depot
from Delhi_buses import get_source_by_code,get_destination_by_code,get_route_by_code,count_buses_in_source,count_buses_in_destination,list_buscodes_matching_code,list_bus_numbers_from_source,list_bus_numbers_to_destination

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
        st.title("Bus Station Information")
            
        depot_route = st.text_input("Enter the code of bus whose source station you want:")
        if st.button("Source By Code"):
            answer = get_source_by_code(depot_route)
            st.write("Answer:", answer)

        depot_name = st.text_input("Enter the code of bus whose destination station you want:")
        if st.button("Destination By Code"):
            answer2 = get_destination_by_code(depot_name)
            st.write("Answer:", answer2)
            
        depot_name2 = st.text_input("Enter the code of bus whose route you want:")
        if st.button("Get Route By Code"):
            answer3 = get_route_by_code(depot_name2)
            st.write("Answer:", answer3)
            
        depot_name3 = st.text_input("Enter the source station to get its bus count:")
        if st.button("Source Station Bus Count"):
            answer4 = count_buses_in_source(depot_name3)
            st.write("Answer:", answer4)
            
        depot_name4 = st.text_input("Enter the destination station to get its bus count:")
        if st.button("Destination Station Bus Count"):
            answer5 = count_buses_in_destination(depot_name4)
            st.write("Answer:", answer5)
            
        depot_name5 = st.text_input("Enter the bus code to get similar codes:")
        if st.button("Similar Bus Codes"):
            answer6 = list_buscodes_matching_code(depot_name5)
            st.write("Answer:", answer6)
            
        depot_name6 = st.text_input("Enter the source station whose buses you want")
        if st.button("Bus from Source"):
            answer7 = list_bus_numbers_from_source(depot_name6)
            st.write("Answer:", answer7)

        depot_name7 = st.text_input("Enter the destination station whose buses you want")
        if st.button("Bus from Destination"):
            answer8 = list_bus_numbers_to_destination(depot_name7)
            st.write("Answer:", answer8)

       
        
    elif selected_option == "Airport":
        st.write("Airport information will be displayed here.")

def run_delhi_app():
    # Streamlit UI
    st.title("Delhi")

    # Options for different categories
    options = ["Select","Schools", "Banks", "Hospitals", "Public transport"]
    selected_option = st.selectbox("Choose an option:", options)

    # Show relevant options based on user selection
    if selected_option == "Public transport":
        run_public_transport()

    # Add functionality for other options
    elif selected_option == "Schools":
        st.title("Schools Information")
        # Load the school data and display the relevant information
        # You can directly call the functions from school_functions.py
        
        region_name = st.text_input("Enter the region to get schools information:")
        if st.button("Get Schools in Region"):
            schools_in_region = get_schools_in_region(region_name)
            st.write(f"Schools in {region_name}:", schools_in_region)

        region_name_count = st.text_input("Enter the region to get count of schools:")
        if st.button("Get Count of Schools in Region"):
            count = count_schools_in_region(region_name_count)
            st.write(f"Count of Schools in {region_name_count}:", count)

        region_name_levels = st.text_input("Enter the region to get school levels:")
        if st.button("Get School Levels in Region"):
            levels = get_school_levels_in_region(region_name_levels)
            st.write(f"School Levels in {region_name_levels}:", levels)

        region_name_details = st.text_input("Enter the region to get schools and their levels:")
        if st.button("Get Schools and Levels in Region"):
            schools_and_levels = get_schools_and_levels_in_region(region_name_details)
            st.write(f"Schools and Levels in {region_name_details}:", schools_and_levels)


        school_name_zone = st.text_input("Enter the school name to get zone:")
        if st.button("Get Zone of School"):
            zone = get_zone_of_school(school_name_zone)
            st.write(f"Zone of {school_name_zone}:", zone)

        zone_name = st.text_input("Enter the zone to get schools:")
        if st.button("Get Schools by Zone"):
            schools_by_zone = get_schools_by_zone(zone_name)
            st.write(f"Schools in {zone_name} zone:", schools_by_zone)

        starts_with_letter_school = st.text_input("Enter a letter to find school names starting with that letter (e.g., A):")
        if starts_with_letter_school:
            school_starts_with = get_school_names_starting_with(starts_with_letter_school)
            st.write(f"School Names Starting with {starts_with_letter_school}:", school_starts_with)

        school_level = st.text_input("Enter the school level to get school names:")
        if school_level:
            school_names_by_level = get_school_names_with_level(school_level)
            st.write(f"School Names with Level '{school_level}':", school_names_by_level)

        school_name_phone = st.text_input("Enter the school name to get phone number:")
        if st.button("Get Phone Number of School"):
            phone_number = get_phone_number_of_school(school_name_phone)
            st.write(f"Phone Number of {school_name_phone}:", phone_number)

    elif selected_option == "Banks":
        st.write("Banks information will be displayed here.")

    elif selected_option == "Hospitals":
        st.write("Hospitals information will be displayed here.")

        

