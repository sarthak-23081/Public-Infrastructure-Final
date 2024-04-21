import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load hospital data
hospital_data = pd.read_excel('Hyderabad_health_facilities.xlsx')

# Function to preprocess text
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

hospital_data['preprocessed_text'] = hospital_data[['Zone', 'Hospital Name', 'Category', 'Department', 'Address']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
hospital_data['preprocessed_text'] = hospital_data['preprocessed_text'].apply(preprocess_text)

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
tfidf_matrix = tfidf_vectorizer.fit_transform(hospital_data['preprocessed_text'])

# Function to get hospitals in a given zone with all details
def get_hospitals_in_zone(zone_name):
    max_similarity = -1
    hospitals_in_zone = []
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(zone_name, row['Zone'])
        if similarity > max_similarity:
            max_similarity = similarity
            hospitals_in_zone = [(row['Hospital Name'], row['Category'], row['Department'], row['Address'])]
        elif similarity == max_similarity:
            hospitals_in_zone.append((row['Hospital Name'], row['Category'], row['Department'], row['Address']))
    return hospitals_in_zone

# Function to count the number of hospitals in a given zone
def count_hospitals_in_zone(zone_name):
    count = 0
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(zone_name, row['Zone'])
        if similarity > 0.5:  # Adjust similarity threshold as needed
            count += 1
    return count

# Function to get hospitals in a given category
def get_hospitals_in_category(category_name):
    max_similarity = -1
    hospitals_in_category = []
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(category_name, row['Category'])
        if similarity > max_similarity:
            max_similarity = similarity
            hospitals_in_category = [row['Hospital Name']]
        elif similarity == max_similarity:
            hospitals_in_category.append(row['Hospital Name'])
    return hospitals_in_category

# Function to get hospitals with a specific department
def get_hospitals_with_department(department_name):
    max_similarity = -1
    hospitals_with_department = []
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(department_name, row['Department'])
        if similarity > max_similarity:
            max_similarity = similarity
            hospitals_with_department = [row['Hospital Name']]
        elif similarity == max_similarity:
            hospitals_with_department.append(row['Hospital Name'])
    return hospitals_with_department

# Function to get hospitals starting with a specific letter
def get_hospitals_starting_with(letter):
    matching_hospitals = hospital_data[hospital_data['Hospital Name'].str.startswith(letter.upper())]['Hospital Name'].tolist()
    return matching_hospitals

# Function to get the zone of a given hospital
def get_zone_of_hospital(hospital_name):
    max_similarity = -1
    zone = ""
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(hospital_name, row['Hospital Name'])
        if similarity > max_similarity:
            max_similarity = similarity
            zone = row['Zone']
    return zone

# Function to get the category of a given hospital
def get_category_of_hospital(hospital_name):
    max_similarity = -1
    category = ""
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(hospital_name, row['Hospital Name'])
        if similarity > max_similarity:
            max_similarity = similarity
            category = row['Category']
    return category

# Function to get the department of a given hospital
def get_department_of_hospital(hospital_name):
    max_similarity = -1
    department = ""
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(hospital_name, row['Hospital Name'])
        if similarity > max_similarity:
            max_similarity = similarity
            department = row['Department']
    return department

# Function to get the address of a given hospital
def get_address_of_hospital(hospital_name):
    max_similarity = -1
    address = ""
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(hospital_name, row['Hospital Name'])
        if similarity > max_similarity:
            max_similarity = similarity
            address = row['Address']
    return address

# Function to get hospital names and addresses with a specific department
def get_hospitals_and_addresses_with_department(department_name):
    max_similarity = -1
    hospitals_and_addresses = {}
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(department_name, row['Department'])
        if similarity > max_similarity:
            max_similarity = similarity
            hospitals_and_addresses[row['Hospital Name']] = row['Address']
        elif similarity == max_similarity:
            hospitals_and_addresses[row['Hospital Name']] = row['Address']
    return hospitals_and_addresses
