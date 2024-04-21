

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from fuzzywuzzy import process

# Load data
print("Loading data...")
data = pd.read_csv('E:\\reference_S\\BEST_BUS - Sheet1.csv')

# Function to preprocess text
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Preprocess relevant columns
data['preprocessed_depot_name'] = data['Depot Name in English'].apply(preprocess_text)
data['preprocessed_major_operations'] = data['Major Operations'].apply(preprocess_text)
data['preprocessed_bus_route'] = data['Bus Route No.'].apply(preprocess_text)
data['preprocessed_address'] = data['Address'].apply(preprocess_text)

def compute_cosine_similarity(text1, text2):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)
    text1_tfidf = tfidf_vectorizer.transform([text1])
    text2_tfidf = tfidf_vectorizer.transform([text2])
    similarity = cosine_similarity(text1_tfidf, text2_tfidf)
    return similarity[0][0]


# TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text
tfidf_matrix = tfidf_vectorizer.fit_transform(data['preprocessed_depot_name'] + ' ' + data['preprocessed_major_operations'] + ' ' + data['preprocessed_bus_route'] + ' ' + data['preprocessed_address'])

# Function to get buses in a given depot
def get_buses_in_depot(depot_name):
    max_similarity = -1
    best_depot_name = ""
    buses_in_depot = []
    
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(depot_name, data['Depot Name in English'])[0]

    
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(closest_match, row['Depot Name in English'])
        
        if similarity > max_similarity:
            max_similarity = similarity
            best_depot_name = row['Depot Name in English']
            buses_in_depot = [row['Bus Route No.']]
        elif similarity == max_similarity:
            buses_in_depot.append(row['Bus Route No.'])
            
    return buses_in_depot



# Function to count bus stations in a given depot
def count_bus_stations_in_depot(depot_name):
    bus_stations = []
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(depot_name, data['Depot Name in English'])[0]
    
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Depot Name in English'])
        if similarity > 0.8:  # Adjust similarity threshold as needed
            bus_stations.extend(row['Bus Stations'].split(','))
    return len(set(bus_stations))




# Function to get major operations of a depot
def get_major_operations_of_depot(depot_name):
    closest_match = process.extractOne(depot_name, data['Depot Name in English'])[0]
    
    max_similarity = -1
    major_operations = []
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Depot Name in English'])
        if similarity > max_similarity:
            max_similarity = similarity
            major_operations = row['Major Operations']
    return major_operations

# Function to get depot name by depot code
def get_depot_by_code(depot_code):
    # Iterate through each row in the dataset
    for idx, row in data.iterrows():
        # Check if the depot code matches the provided depot code
        if row['Depot Code'] == depot_code:
            # Return the depot name if a match is found
            return row['Depot Name in English']
    
    # If no match is found, return None
    return None



# Function to get bus stations by route
def get_bus_stations_by_route(route_number):
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(route_number, data['Bus Route No.'])[0]
    
    max_similarity = -1
    bus_stations = []
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Bus Route No.'])
        if similarity > max_similarity:
            max_similarity = similarity
            bus_stations = row['Bus Stations']
    return bus_stations

# Function to get buses by major operation (bus station)
def get_buses_by_major_operation(bus_station):
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(bus_station, data['Major Operations'])[0]
    
    max_similarity = -1
    buses = []
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Major Operations'])
        if similarity > max_similarity:
            max_similarity = similarity
            buses = row['Bus Route No.']
    return buses

# Function to get buses starting with a specific letter
def get_buses_starting_with(letter):
    matching_buses = data[data['Bus Route No.'].str.startswith(letter.upper())]['Bus Route No.'].tolist()
    return matching_buses

# Function to count buses in a given region
def count_buses_in_region(region_name):
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(region_name, data['Address'])[0]
    
    max_similarity = -1
    count = 0
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Address'])
        if similarity > max_similarity:
            max_similarity = similarity
            count += 1
    return count

# Function to list bus stations in a given depot
def list_bus_stations_in_depot(depot_name):
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(depot_name, data['Depot Name in English'])[0]
    
    bus_stations = []
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Depot Name in English'])
        if similarity > 0.7:  # Adjusted similarity threshold
            bus_stations.extend(row['Bus Stations'].split(','))
    return list(set(bus_stations))

