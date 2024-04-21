import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load data
data = pd.read_excel('project\metro\hyedrabadmetro.xlsx')

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

# Initialize TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text
tfidf_matrix = tfidf_vectorizer.fit_transform(data['preprocessed_text'])

# Function to get layout information for a given area
def get_layout(area):
    question = f"What is the layout at {area}?"
    question = preprocess_text(question)
    question_tfidf = tfidf_vectorizer.transform([question])
    similarity = cosine_similarity(question_tfidf, tfidf_matrix)
    most_similar_index = similarity.argmax()
    layout = data.loc[most_similar_index, 'Station Layout']
    return layout

# Function to get status information for a given area
def get_status(area):
    question = f"What is the status of {area}?"
    question = preprocess_text(question)
    question_tfidf = tfidf_vectorizer.transform([question])
    similarity = cosine_similarity(question_tfidf, tfidf_matrix)
    most_similar_index = similarity.argmax()
    status = data.loc[most_similar_index, 'Status']
    return status

# Function to get line information for a given area
def get_line(area):
    question = f"What is the line of {area}?"
    question = preprocess_text(question)
    question_tfidf = tfidf_vectorizer.transform([question])
    similarity = cosine_similarity(question_tfidf, tfidf_matrix)
    most_similar_index = similarity.argmax()
    line = data.loc[most_similar_index, 'Line']
    return line

# Function to get station names starting with a specific letter
def get_station_names_starting_with(letter):
    matching_stations = data[data['Station name'].str.startswith(letter.upper())]
    return list(matching_stations['Station name'])

# Function to get station names with a specific status
def get_station_names_with_status(layout):
    matching_stations = data[data['Station Layout'].str.lower() == layout.lower()]
    return list(matching_stations['Station name'])

# Function to get the status of a given station name
def get_status_of_station(station_name):
    station = data[data['Station name'].str.lower() == station_name.lower()]
    if not station.empty:
        return station.iloc[0]['Status']
    else:
        return "Station not found."

# Function to get the line of a given station name
def get_line_of_station(station_name):
    station = data[data['Station name'].str.lower() == station_name.lower()]
    if not station.empty:
        return station.iloc[0]['Line']
    else:
        return "Station not found."

# Function to get station names that run on a given input line
def get_stations_on_line(input_line):
    stations_on_line = data[data['Line'].str.lower() == input_line.lower()]
    if not stations_on_line.empty:
        return list(stations_on_line['Station name'])
    else:
        return "No stations found for the given line."
