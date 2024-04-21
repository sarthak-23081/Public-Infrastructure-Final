import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load data
data = pd.read_excel('project/metro/hyedrabadmetro.xlsx')
region_data = pd.read_excel('Delhi-Regions.xlsx')

# Preprocessing function
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Preprocess the relevant columns and concatenate the text
data['preprocessed_text'] = data[['Station name', 'Station Layout', 'Status', 'Line']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
data['preprocessed_text'] = data['preprocessed_text'].apply(preprocess_text)

region_data['preprocessed_text'] = region_data[['Region', 'Places']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
region_data['preprocessed_text'] = region_data['preprocessed_text'].apply(preprocess_text)

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text
tfidf_matrix = tfidf_vectorizer.fit_transform(data['preprocessed_text'])
region_tfidf_matrix = tfidf_vectorizer.fit_transform(region_data['preprocessed_text'])

# Function to compute cosine similarity between two texts
def compute_cosine_similarity(text1, text2):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)
    text1_tfidf = tfidf_vectorizer.transform([text1])
    text2_tfidf = tfidf_vectorizer.transform([text2])
    similarity = cosine_similarity(text1_tfidf, text2_tfidf)
    return similarity[0][0]

# Function to get layout information for a given area
def get_layout(area):
    max_similarity = -1
    layout = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(area, row['Station Layout'])
        if similarity > max_similarity:
            max_similarity = similarity
            layout = row['Station Layout']
    return layout

# Function to get status information for a given area
def get_status(area):
    max_similarity = -1
    status = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(area, row['Status'])
        if similarity > max_similarity:
            max_similarity = similarity
            status = row['Status']
    return status

# Function to get line information for a given area
def get_line(area):
    max_similarity = -1
    line = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(area, row['Line'])
        if similarity > max_similarity:
            max_similarity = similarity
            line = row['Line']
    return line

# Function to get station names starting with a specific letter
def get_station_names_starting_with(letter):
    matching_stations = data[data['Station name'].str.startswith(letter.upper())]
    return list(matching_stations['Station name'])

# Function to get station names with a specific layout
def get_station_names_with_layout(layout):
    max_similarity = -1
    matching_stations = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(layout, row['Station Layout'])
        if similarity > max_similarity:
            max_similarity = similarity
            matching_stations = [row['Station name']]
        elif similarity == max_similarity:
            matching_stations.append(row['Station name'])
    return matching_stations


# Function to get the line of a given station name
def get_line_of_station(station_name):
    max_similarity = -1
    line = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(station_name, row['Station name'])
        if similarity > max_similarity:
            max_similarity = similarity
            line = row['Line']
    return line

# Function to get station names that run on a given input line
def get_stations_on_line(input_line):
    max_similarity = -1
    matching_stations = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(input_line, row['Line'])
        if similarity > max_similarity:
            max_similarity = similarity
            matching_stations = [row['Station name']]
        elif similarity == max_similarity:
            matching_stations.append(row['Station name'])
    return matching_stations

# Function to get region for a given station name
def get_region_for_station(station_name):
    max_similarity = -1
    region = ""
    for idx, row in region_data.iterrows():
        similarity = compute_cosine_similarity(station_name, row['Places'])
        if similarity > max_similarity:
            max_similarity = similarity
            region = row['Region']
    return region

# Function to get places in a given region
def get_places_in_region(region_name):
    max_similarity = -1
    places = []
    for idx, row in region_data.iterrows():
        similarity = compute_cosine_similarity(region_name, row['Region'])
        if similarity > max_similarity:
            max_similarity = similarity
            places = [row['Places']]
        elif similarity == max_similarity:
            places.append(row['Places'])
    return places

