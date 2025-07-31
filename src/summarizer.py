import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords 
import string

nltk.download("punkt")
nltk.download("stopwords")

def summarize_text(text, num_sentences=7):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    # Remove stopwords and punctuation 
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words and word not in string.punctuation]

    # Calculate word frequencies
    freq_dist = FreqDist(words)

    # Score each sentence based on word frequencies
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq_dist:
                if sent not in sentence_scores:
                    sentence_scores[sent] = freq_dist[word]
                else:
                    sentence_scores[sent] += freq_dist[word]

    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]

    # Return as numbered list
    pointwise_summary = "\n".join([f"{i+1}. {sent}" for i, sent in enumerate(top_sentences)])

    return pointwise_summary
           








