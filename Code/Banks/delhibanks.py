import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load bank data
data = pd.read_excel('Delhi_banks.xlsx')

# Function to preprocess text
def preprocess_text(text):
    if pd.isna(text):
        return ''
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

data['preprocessed_text'] = data[['Bank Name', 'Branch Name', 'Zone', 'IFSC Code', 'Address']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)
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

# Function to get branch name by address
def get_branch_name_by_address(input_address):
    max_similarity = -1
    branch_name = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(input_address, row['Address'])
        if similarity >= max_similarity:
            max_similarity = similarity
            branch_name.append(row['Branch Name'])
            if similarity == 1:
                return branch_name[-1]
    return branch_name


# Function to get IFSC code of a bank by entering address
def get_ifsc_code_by_address(input_address):
    max_similarity = -1
    ifsc_code = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(input_address, row['Address'])
        if similarity >= max_similarity:
            max_similarity = similarity
            ifsc_code.append(row['IFSC Code'])
            if similarity == 1:
                return ifsc_code[-1]
    return ifsc_code


# Function to get IFSC code of a given bank branch
def get_ifsc_code_of_branch(branch_name):
    max_similarity = -1
    ifsc_code = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(branch_name, row['Branch Name'])
        if similarity >= max_similarity:
            max_similarity = similarity
            ifsc_code.append(row['IFSC Code'])
            if similarity == 1:
                return ifsc_code[-1]
    return ifsc_code

# Function to get address of a given bank branch
def get_address_of_branch(branch_name):
    max_similarity = -1
    address = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(branch_name, row['Branch Name'])
        if similarity >= max_similarity:
            max_similarity = similarity
            address.append(row['Address'])
            if similarity == 1:
                return address[-1]
    return address

# Function to get address by entering the IFSC code
def get_address_by_ifsc_code(input_ifsc):
    max_similarity = -1
    address = []
    full_ifsc_code =[]
    for idx, row in data.iterrows():
        ifsc_code = row['IFSC Code']
        similarity = compute_cosine_similarity(input_ifsc, ifsc_code)
        if similarity >= max_similarity:
            max_similarity = similarity
            address.append(row['Address'])
            full_ifsc_code.append(ifsc_code)
            if similarity == 1:
                return address[-1],full_ifsc_code[-1]
    return address,full_ifsc_code

# Function to get branch name and IFSC code by entering IFSC code
def get_branch_name_and_ifsc_by_partial_ifsc(input_ifsc):
    max_similarity = -1
    branch_name = []
    full_ifsc_code = []
    for idx, row in data.iterrows():
        ifsc_code = row['IFSC Code']
        similarity = compute_cosine_similarity(input_ifsc, ifsc_code)
        if similarity >= max_similarity:
            max_similarity = similarity
            branch_name.append(row['Branch Name'])
            full_ifsc_code.append(ifsc_code)
            if similarity == 1:
                return branch_name[-1],full_ifsc_code[-1]
    return branch_name, full_ifsc_code

#function to get bank details in delhi
def get_branch_details_by_zone(input_zone):
    max_similarity = -1
    bank_details = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(input_zone, row['Zone'])
        if similarity >= max_similarity:
            max_similarity = similarity
            bank_details.append({
                'Bank Name': row['Bank Name'],
                'Zone': row['Zone'],
                'Branch Name': row['Branch Name'],
                'IFSC Code': row['IFSC Code'],
                'Address': row['Address']
            })
    return bank_details


# Function to get bank details by entering branch name
def get_bank_details_by_branch(branch_name):
    max_similarity = -1
    bank_details = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(branch_name, row['Branch Name'])
        if similarity >= max_similarity:
            max_similarity = similarity
            bank_details.append({
                'Bank Name': row['Bank Name'],
                'Zone': row['Zone'],
                'Branch Name': row['Branch Name'],
                'IFSC Code': row['IFSC Code'],
                'Address': row['Address']
            })
            
            if similarity == 1:
                return bank_details[-1]
    
    return bank_details

# Function to get bank details by entering IFSC code 
def get_bank_details_by_ifsc(partial_ifsc_code):
    max_similarity = -1
    bank_details = []
    
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(partial_ifsc_code, row['IFSC Code'])
        
        if similarity >= max_similarity:
            max_similarity = similarity 
            
            bank_details.append({
                'Bank Name': row['Bank Name'],
                'Zone': row['Zone'],
                'Branch Name': row['Branch Name'],
                'IFSC Code': row['IFSC Code'],
                'Address': row['Address']
            })
            
            if similarity == 1:
                return bank_details[-1]  # Return the last bank detail if it's a perfect match
    
    return bank_details[-1] 


# Function to get bank details by entering address
def get_bank_details_by_address(input_address):
    max_similarity = -1
    bank_details = []
    for idx, row in data.iterrows():
        similarity = compute_cosine_similarity(input_address, row['Address'])
        if similarity >= max_similarity:
            max_similarity = similarity
            bank_details.append({
                'Bank Name': row['Bank Name'],
                'Zone': row['Zone'],
                'Branch Name': row['Branch Name'],
                'IFSC': row['IFSC Code'],
                'Address': row['Address']
            })

            if similarity == 1:
                return bank_details[-1]
            
    return bank_details


