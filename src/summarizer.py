from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def summarize_text(text, num_sentences=5):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    freq = {}
    for word in filtered_words:
        freq[word] = freq.get(word, 0) + 1

    sentences = sent_tokenize(text)

    sentence_scores = {}
    for sentence in sentences:
        sentence_words = word_tokenize(sentence.lower())
        sentence_scores[sentence] = sum(freq.get(word, 0) for word in sentence_words)

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return "\n\n".join(summary_sentences)


import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation 
import fitz # PyMuPDF 

nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(file_path):
    text = "" 
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text() 
    return text 

def summarize_text(text, num_sentences=5):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    stop_words = set(stopwords.words("english") + list(punctuation))
    word_frequencies = {}

    for word in words:
        if word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    max_freq = max(word_frequencies.values(), default=1)
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    sentence_scores = {} 
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if word in word_frequencies:
                    sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return " ".join(summary_sentences)          
            
