import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load hospital data
hospital_data = pd.read_excel('mumbai-healthcare .xlsx')

# Function to preprocess text
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

hospital_data['preprocessed_text'] = hospital_data[['NAME OF HOSPITAL', 'ADDRESS']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
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

# Function to get hospitals starting with a specific letter using cosine similarity
def get_hospitals_starting_with(letter):
    max_similarity = -1
    matching_hospitals = []
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(letter, row['NAME OF HOSPITAL'][0])
        if similarity > max_similarity:
            max_similarity = similarity
            matching_hospitals = [row['NAME OF HOSPITAL']]
        elif similarity == max_similarity:
            matching_hospitals.append(row['NAME OF HOSPITAL'])
    return matching_hospitals


# Function to get the contact number of a given hospital using cosine similarity
def get_contact_of_hospital(hospital_name):
    max_similarity = -1
    contact = None
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(hospital_name, row['NAME OF HOSPITAL'])
        if similarity > max_similarity:
            max_similarity = similarity
            contact = row['CONTACT NO']
    return contact if contact is not None else None

# Function to get the number of beds in a given hospital using cosine similarity
def get_beds_of_hospital_using_similarity(hospital_name):
    max_similarity = -1
    beds = None
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(hospital_name, row['NAME OF HOSPITAL'])
        if similarity > max_similarity:
            max_similarity = similarity
            beds = row['No. of beds']
    return beds if beds is not None else None


# Function to get hospital names by address
def get_hospitals_by_address(address):
    max_similarity = -1
    hospitals_by_address = []
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(address, row['ADDRESS'])
        if similarity > max_similarity:
            max_similarity = similarity
            hospitals_by_address = [row['NAME OF HOSPITAL']]
        elif similarity == max_similarity:
            hospitals_by_address.append(row['NAME OF HOSPITAL'])
    return hospitals_by_address


# Function to get hospital names and addresses with a specific keyword
def get_hospitals_and_addresses_with_keyword(keyword):
    max_similarity = -1
    hospitals_and_addresses = {}
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(keyword, row['NAME OF HOSPITAL'])
        if similarity > max_similarity:
            max_similarity = similarity
            hospitals_and_addresses[row['NAME OF HOSPITAL']] = row['ADDRESS']
        elif similarity == max_similarity:
            hospitals_and_addresses[row['NAME OF HOSPITAL']] = row['ADDRESS']
    return hospitals_and_addresses


# Function to count the number of hospitals at a particular address
def count_hospitals_at_address(target_address):
    max_similarity = -1
    count = 0
    for idx, row in hospital_data.iterrows():
        similarity = compute_cosine_similarity(target_address, row['ADDRESS'])
        if similarity > 0.8:  # Adjust similarity threshold as needed
            count += 1
    return count


