from torch.utils.data import Dataset, DataLoader
# import datasets
import math
import torch
import torch.nn as nn
from collections import Counter
from tqdm import tqdm
import re
from langdetect import detect
import numpy as np
from collections import Counter
import datasets
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import spacy
from collections import Counter
import re

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nlp = spacy.load('fr_core_news_lg')

def lemmatize_text(row):
    row["text"] = nlp(row["text"])
    return row

def lowerCase(row):
    row['text'] = row['text'].lower()
    return row

def data_clean_pandas(df):
    """Clean the dataframe by filtering and preprocessing the text."""
    # Create a copy to avoid modifying the original
    df_cleaned = df.copy()

    # if 'text' in df_cleaned.columns:
    #     df_cleaned = df_cleaned[~df_cleaned['text'].str.contains(r'= .*? = \n', regex=True)]
    df_cleaned['text'] = df_cleaned['text'].apply(lowerCase)

    # 5- Apply lemmatization if requested
    df_cleaned['text'] = df_cleaned['text'].apply(lemmatize_text)
    
    return df_cleaned
