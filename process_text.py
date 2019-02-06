from nltk.tokenize import TweetTokenizer
from nltk import WordNetLemmatizer
import nltk
import string


def process(txt):
    # txt = input.strip(string.punctuation)
    print("this equals:" + txt)
    tTokenizer = TweetTokenizer()
    tokenised = tTokenizer.tokenize(txt)
    print('Tokenised: ', tokenised)
    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    words = [w for w in tokenised if w.lower() not in stopwords]
    print('Stopwords: ', words)
    #  lemmatise
    #  removes prefixes: dis-, in-, re-, and suffixes: -ed, -ing, -ly, and -es
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(t) for t in words]
    print('Lemmatised: ', lemmas)
    process_completed = " ".join(lemmas)
    print("processed text:" + process_completed)
    return process_completed
