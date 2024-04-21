import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load data
data = pd.read_excel('project\school\delhischool.xlsx')

# Function to preprocess text
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

data['preprocessed_text'] = data[['Region', 'Zone', 'School ID', 'UDISE Code', 'School Name', 'Address', 'SchoolLevel', 'Gender', 'Phone', 'Hos Name']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
data['preprocessed_text'] = data['preprocessed_text'].apply(preprocess_text)

# Function to compute cosine similarity between two texts
def compute_cosine_similarity(text1, text2):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)
    text1_tfidf = tfidf_vectorizer.transform([text1])
    text2_tfidf = tfidf_vectorizer.transform([text2])
    similarity = cosine_similarity(text1_tfidf, text2_tfidf)
    return similarity[0][0]

tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the preprocessed text
tfidf_matrix = tfidf_vectorizer.fit_transform(data['preprocessed_text'])

# Function to get school names in a given region
# Function to get school names in a given region
def get_schools_in_region(region_name):
    max_similarity = -1
    schools_in_region = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(region_name, row['Region'])
        if similarity > max_similarity:
            max_similarity = similarity
            schools_in_region = [row['School Name']]
        elif similarity == max_similarity:
            schools_in_region.append(row['School Name'])
    return schools_in_region

# Function to count the number of schools in a given region
def count_schools_in_region(region_name):
    return len(get_schools_in_region(region_name))

# Function to get school level(s) in a given region
def get_school_levels_in_region(region_name):
    schools_in_region = get_schools_in_region(region_name)
    school_levels = set()
    for school in schools_in_region:
        for idx, row in data.iterrows():
            if row['School Name'] == school:
                school_levels.add(row['SchoolLevel'])
    return list(school_levels)

# Function to get all schools and their levels in a given region
def get_schools_and_levels_in_region(region_name):
    schools_in_region = get_schools_in_region(region_name)
    schools_and_levels = {}
    for school in schools_in_region:
        for idx, row in data.iterrows():
            if row['School Name'] == school:
                schools_and_levels[school] = row['SchoolLevel']
    return schools_and_levels

# Function to get the zone of a given school
def get_zone_of_school(school_name):
    max_similarity = -1
    zone = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(school_name, row['School Name'])
        if similarity > max_similarity:
            max_similarity = similarity
            zone = row['Zone']
    return zone

# Function to get schools by zone
def get_schools_by_zone(zone):
    max_similarity = -1
    schools_in_zone = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(zone, row['Zone'])
        if similarity > max_similarity:
            max_similarity = similarity
            schools_in_zone = [row['School Name']]
        elif similarity == max_similarity:
            schools_in_zone.append(row['School Name'])
    return schools_in_zone

# Function to get school names starting with a specific letter
def get_school_names_starting_with(letter):
    matching_schools = data[data['School Name'].str.startswith(letter.upper())]['School Name'].tolist()
    return matching_schools

# Function to get school names with a specific school level
def get_school_names_with_level(level):
    max_similarity = -1
    matching_schools = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(level, row['SchoolLevel'])
        if similarity > max_similarity:
            max_similarity = similarity
            matching_schools = [row['School Name']]
        elif similarity == max_similarity:
            matching_schools.append(row['School Name'])
    return matching_schools

# Function to get the phone number of a given school
def get_phone_number_of_school(school_name):
    max_similarity = -1
    phone_number = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(school_name, row['School Name'])
        if similarity > max_similarity:
            max_similarity = similarity
            phone_number = row['Phone']
    return phone_number