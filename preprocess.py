from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def preprocess(paragraph):
    words = word_tokenize(paragraph)
    words = [w for w in words if w not in punctuation]
    words = [w for w in words if w not in stopwords.words('english')]
    words = [w.lower() for w in words]

    return words
