import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

def extract_concepts(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    keywords = [w for w in words if w.isalpha() and w.lower() not in stop_words]
    freq = {}
    for w in keywords:
        freq[w] = freq.get(w, 0) + 1
    sorted_terms = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [term for term, _ in sorted_terms[:10]]
