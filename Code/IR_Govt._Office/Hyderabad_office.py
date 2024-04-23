import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load data
office_data = pd.read_excel('Hyderabad_data.xlsx')

# Function to preprocess text
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

office_data['preprocessed_text'] = office_data.apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
office_data['preprocessed_text'] = office_data['preprocessed_text'].apply(preprocess_text)

# Function to compute cosine similarity between two texts
def compute_cosine_similarity(text1, text2):
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)
    text1_tfidf = tfidf_vectorizer.transform([text1])
    text2_tfidf = tfidf_vectorizer.transform([text2])
    similarity = cosine_similarity(text1_tfidf, text2_tfidf)
    return similarity[0][0]

# Fit and transform the preprocessed text
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(office_data['preprocessed_text'])


# Function to get address by office name using cosine similarity
def get_address_by_office_name(office_name):
    max_similarity = -1
    address = ""
    for idx, row in office_data.iterrows():
        similarity = compute_cosine_similarity(office_name, row['Office Names'])
        if similarity > max_similarity:
            max_similarity = similarity
            address = row['Address']
    return address

# Function to get phone number by office name using cosine similarity
def get_phone_number_by_office_name(office_name):
    max_similarity = -1
    phone_number = ""
    for idx, row in office_data.iterrows():
        similarity = compute_cosine_similarity(office_name, row['Office Names'])
        if similarity > max_similarity:
            max_similarity = similarity
            phone_number = row['Phone No.']
    return phone_number

# Function to get office name by address using cosine similarity
def get_office_name_by_address(address):
    max_similarity = -1
    office_name = ""
    for idx, row in office_data.iterrows():
        similarity = compute_cosine_similarity(address, row['Address'])
        if similarity > max_similarity:
            max_similarity = similarity
            office_name = row['Office Names']
    return office_name

# Function to get list of all offices in a dictionary
def get_all_offices():
    offices = {}
    for idx, row in office_data.iterrows():
        offices[row['Office Names']] = {'Address': row['Address'], 'Phone': row['Phone No.']}
    return offices

