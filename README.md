## This project is aimed at creating an information retreival system for public infrastructure
We have collected public infrastructure related data of 3 major cities:
1. Delhi
2. Mumbai
3. Hyderabad

We have considered data about several public infrastructures in these cities:
1. Buses
2. Trains
3. Metro
4. Airport
5. Schools
6. Colleges
7. Hospitals

For each city-infrastructure, we have created 3 files:
1. app.py: this is used to run the code using the streamlit architecture
2. city-infrastructurestream.py: this is used so that user can navigate through options where they want to make a query
3. city-infrastructure.py: this is used to handle the query and give results based on cosine similarity
In case of no free text in queries, we navigate queries to GPT for which we have used GPT4All

# The dependencies required to run this project are as follows:
```
import streamlit as st
from gpt4all import GPT4All
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from fuzzywuzzy import process
```

# To run the project following command can be used in the terminal

```
streamlit run app.py
```
