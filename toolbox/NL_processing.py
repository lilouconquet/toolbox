import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
import unidecode


def clean_text(text,
               punctuation=True,
               lower_case=True,
               remove_stopwords=True,
               accents=True,
               numbers=True,
               emails=True,
               lemmatize=True,
               language='english'):
    if emails:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        text = re.sub(regex, '', text)

    if punctuation:
        text = ''.join(char for char in text if not char in string.punctuation)

    if lower_case:
        text = text.lower()

    if numbers:
        text = ''.join(char for char in text if not char.isdigit())

    if accents:
        text = unidecode.unidecode(text)

    if remove_stopwords:
        stop_words = set(stopwords.words(language))
        word_tokens = word_tokenize(text)
        text = ' '.join(char for char in word_tokens if not char in stop_words)

    if lemmatize:
        text = word_tokenize(text)
        lemmatizer = WordNetLemmatizer()
        lemmatized = [lemmatizer.lemmatize(char) for char in text]
        text = ' '.join(lemmatized)

    return text
