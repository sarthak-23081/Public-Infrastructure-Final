import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma

# Set your OpenAI API key
OPENAI_API_KEY = os.getenv('Chhatrapati_Shivaji_Maharaj_International_Airport (1).pdf')

# Define the path to your PDF document
DOC_PATH = "path_to_your_pdf.pdf"

# Define the name of your vector database
CHROMA_PATH = "your_db_name"

# Load your PDF document
loader = PyPDFLoader(DOC_PATH)
pages = loader.load()

# Split the document into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(pages)

# Get OpenAI Embedding model
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Embed the chunks as vectors and load them into the database
db_chroma = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
