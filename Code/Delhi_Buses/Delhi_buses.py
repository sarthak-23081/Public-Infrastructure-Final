import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from fuzzywuzzy import process

# Load data
print("Loading data...")
data = pd.read_csv("E:\Delhi_Buses\Buses_Delhi.xlsx - Sheet1.csv")

# Function to preprocess text
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Preprocess relevant columns
data['preprocessed_source'] = data['Source'].apply(preprocess_text)
data['preprocessed_destination'] = data['Destination'].apply(preprocess_text)

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
tfidf_matrix = tfidf_vectorizer.fit_transform(data['preprocessed_source'] + ' ' + data['preprocessed_destination'])


# Function to get source location by depot code
def get_source_by_code(depot_code):
    # Iterate through each row in the dataset
    for idx, row in data.iterrows():
        # Check if the depot code matches the provided depot code
        if row['Bus No.'] == depot_code:
            # Return the source location if a match is found
            return row['Source']
    
    # If no match is found, return None
    return None

# Function to get destination location by depot code
def get_destination_by_code(depot_code):
    # Iterate through each row in the dataset
    for idx, row in data.iterrows():
        # Check if the depot code matches the provided depot code
        if row['Bus No.'] == depot_code:
            # Return the destination location if a match is found
            return row['Destination']
    
    # If no match is found, return None
    return None

# Function to get source destination by route number
def get_route_by_code(route_code):
    # Iterate through each row in the dataset
    for idx, row in data.iterrows():
        # Check if the route code matches the provided code
        if row['Bus No.'] == route_code:
            # Return the source and destination concatenated
            return row['Source'] + ' -> ' + row['Destination']
    
    # If no match is found, return None
    return None


# Function to count buses in a given source region
def count_buses_in_source(region_name):
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(region_name, data['Source'])[0]
    
    count = 0
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Source'])
        if similarity > 0.7:  # Adjusted similarity threshold
            count += 1
    return count

# Function to count buses in a given destination region
def count_buses_in_destination(region_name):
    # Fuzzy matching to find the closest match
    closest_match = process.extractOne(region_name, data['Destination'])[0]
    
    count = 0
    for idx, row in data.iterrows():
        # Check if the similarity is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Destination'])
        if similarity > 0.7:  # Adjusted similarity threshold
            count += 1
    return count

# Function to list bus stations in a given bus route
def list_buscodes_matching_code(bus_route):
    matching_buscodes = []

    # Check for exact matches
    exact_matches = data[data['Bus No.'] == bus_route]['Bus No.'].tolist()
    matching_buscodes.extend(exact_matches)

    # Fuzzy matching to find similar matches
    closest_matches = process.extract(bus_route, data['Bus No.'], limit=5)
    for match in closest_matches:
        if match[1] > 80:  # Adjusted similarity threshold
            matching_buscodes.append(match[0])

    return list(set(matching_buscodes))


# Function to list bus numbers for a given source location
def list_bus_numbers_from_source(source):
    # Fuzzy matching to find the closest match for the source
    closest_match = process.extractOne(source, data['Source'])[0]
    
    bus_numbers = []
    for idx, row in data.iterrows():
        # Check if the similarity of the source is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Source'])
        if similarity > 0.7:  # Adjusted similarity threshold
            bus_numbers.append(row['Bus No.'])
    return bus_numbers

# Function to list bus numbers for a given destination location
def list_bus_numbers_to_destination(destination):
    # Fuzzy matching to find the closest match for the destination
    closest_match = process.extractOne(destination, data['Destination'])[0]
    
    bus_numbers = []
    for idx, row in data.iterrows():
        # Check if the similarity of the destination is above a certain threshold
        similarity = compute_cosine_similarity(closest_match, row['Destination'])
        if similarity > 0.7:  # Adjusted similarity threshold
            bus_numbers.append(row['Bus No.'])
    return bus_numbers

