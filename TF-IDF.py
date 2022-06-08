from sklearn.feature_extraction.text import TfidfVectorizer
import json
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import numpy as np


with open('f1iran.json',encoding="utf8") as f:
    corpus = json.load(f)

docs = [d['summary'] for d in corpus]


# tf-idf
vectorizer = TfidfVectorizer()
tfidf_docs = vectorizer.fit_transform(docs)

tfidf_docs.shape, len(vectorizer.vocabulary_)

list(vectorizer.vocabulary_.keys())[:10]


# query
query ='تکنولوژی'
tfidf_query = vectorizer.transform([query])[0]

# similarities
cosines = []
for d in tqdm(tfidf_docs):
  cosines.append(float(cosine_similarity(d, tfidf_query)))

# sorting
k = 10
sorted_ids = np.argsort(cosines)
for i in range(k):
  cur_id = sorted_ids[-1]
print(docs[cur_id], cosines[cur_id]) 




