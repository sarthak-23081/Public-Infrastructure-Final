
import streamlit as st
from project.metro.hyedrabadmetro import get_layout, get_status, get_station_names_starting_with, get_station_names_with_status
from project.metro.hyedrabadmetro import get_status_of_station, get_line_of_station, get_stations_on_line


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
            
        desired_sta = st.text_input("Enter the station name to get status:")
        if st.button("Get Station Status"):
            status = get_status_of_station(desired_sta)
            st.write(f"Status of {desired_sta}: {status}")
        
        desired_station = st.text_input("Enter the station name to know line:")
        if st.button("Get Station Line"):
            line = get_line_of_station(desired_station)
            st.write(f"Line of {desired_station}: {line}")

        desired_line = st.text_input("Enter the line:")
        if st.button("Get Stations on Line"):
            stations = get_stations_on_line(desired_line)
            st.write(f"Stations on {desired_line} line: {stations}")

        desired_lay = st.text_input("Enter the desired status to find station names with that layout (e.g., Elevated):")
        if desired_lay:
            status_match_answer = get_station_names_with_status(desired_lay)
            st.write(f"Station Names with Layout '{desired_lay}':", status_match_answer)

    elif selected_option == "Railways":
        st.write("Railways information will be displayed here.")

    elif selected_option == "Buses":
        st.write("Bus information will be displayed here.")

    elif selected_option == "Airport":
        st.write("Airport information will be displayed here.")

def run_hyedrabad_app():
    # Streamlit UI
    st.title("Hyedrabad")

    # Options for different categories
    options = ["Select","Schools", "Banks", "Hospitals", "Public transport"]
    selected_option = st.selectbox("Choose an option:", options)

    # Show relevant options based on user selection
    if selected_option == "Public transport":
            
        run_public_transport()
        