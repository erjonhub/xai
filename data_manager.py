import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

# Load the FAISS index and the dataframes
index = faiss.read_index('data/faiss_index')
questions_df = pd.read_csv('data/questions.csv', index_col='Id')
answers_df = pd.read_csv('data/answers.csv', index_col='Id')

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_data():
    return index, questions_df, answers_df, model