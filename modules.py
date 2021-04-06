import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import csv

class QuestionAnalyzer:
 def __init__(self):
  print("Start question analyzer")
 
class DocumentRetriever:
 def __init__(self):
  print("Start document retriever")
 
 def load_corpus(file_path):
  return pd.read_csv(file_path)
 
 def build_index(self, dataset_name, source_path, dest_path):
  raw_docs = load_corpus(source_path)
  stem_docs = 
  
 
class AnswerExtractor:
 def __init__(self):
  print ("Start answer extractor")
  
class Preprocess:
 def __init__(self):
  nltk.download('punkt')
  
 def stemming(docs):
  porter = PorterStemmer()
  if(type(docs) is list):
    new_doc = []
    for doc in docs:
      words = word_tokenize(doc)
      new_word = ""

      for word in words:
        stem = porter.stem(word)
        new_word = new_word + " " + stem 
      new_doc.append(new_word)
    return new_doc
  else:
     words = word_tokenize(docs)
     new_word = ""
     for word in words:
      stem = porter.stem(word)
      new_word = new_word + " " + stem 
  return new_word