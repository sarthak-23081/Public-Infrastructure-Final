import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load data
data = pd.read_excel('Delhi_govt_new.xlsx')

# Function to clean the contact person column
def clean_contact_person(contact_person):
    cleaned_name = contact_person.replace("Contact Person:", "").strip()
    return cleaned_name

# Function to clean the Tele No. column
def clean_tele_no(tele_no):
    cleaned_tele_no = tele_no.replace("Tel:", "").strip()
    return cleaned_tele_no

# Apply cleaning functions to the 'Contact Person' and 'Tele No.' columns
data['Contact Person'] = data['Contact Person'].apply(clean_contact_person)
data['Tele No.'] = data['Tele No.'].apply(clean_tele_no)

# Function to preprocess text
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

data['preprocessed_text'] = data[['List of Govt. Offices','Address','Contact Person']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
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

# Function to get addresses based on a government office
SIMILARITY_THRESHOLD=0.8
def get_addresses_from_govt_office(office_name):
    addresses = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(office_name, row['List of Govt. Offices'])
        if similarity > SIMILARITY_THRESHOLD:  # Adjust threshold as needed
            addresses.append(row['Address'])
    return ", ".join(addresses)

# Function to get a list of all government offices in delhi
def get_list_of_all_govt_offices():
    govt_offices = data['List of Govt. Offices'].unique().tolist()
    return govt_offices

# Function to get government office name of the person
def get_govt_offices_for_person(person):
    max_similarity = -1
    govt_offices = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(person, row['Contact Person'])
        if similarity >= max_similarity:
            if similarity > max_similarity:
                max_similarity = similarity
                govt_offices = []
            govt_offices.append(row['List of Govt. Offices'])
    return "".join(govt_offices)

# Function to get the deatails of position and Tele No.
def find_details_for_contact_person(contact_person_name):
    max_similarity = -1
    details = {}
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(contact_person_name, row['Contact Person'])
        if similarity > max_similarity:
            max_similarity = similarity
            details['Position'] = row['Position']
            details['Tele No.'] = row['Tele No.']
    if max_similarity < 0.5 or not details['Position'] or not details['Tele No.']:  # Adjust the threshold as needed
        return "Data not available."
    return details

# Function to get all the names of officials with their offices
def get_govt_office_person_association():
    govt_office_person_mapping = {}
    for idx, row in data.iterrows():
        govt_office = row['List of Govt. Offices']
        person = row['Contact Person']
        if govt_office not in govt_office_person_mapping:
            govt_office_person_mapping[govt_office] = [person]
        else:
            govt_office_person_mapping[govt_office].append(person)
    return govt_office_person_mapping

# Function to find the name of contacted official in the government office
def get_contact_person_for_govt_office(office_name):
    max_similarity = -1
    contact_person = ""
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(office_name, row['List of Govt. Offices'])
        if similarity > max_similarity:
            max_similarity = similarity
            contact_person = row['Contact Person']
    return contact_person
