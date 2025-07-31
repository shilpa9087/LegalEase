from src.pdf_reader import extract_text_from_pdf
from src.summarizer import summarize_text
from src.highlighter import highlight_keywords
import nltk

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Path to PDF file
file_path = r"C:\Users\Dell\Documents\Textsummarizer\data\Kesavananda_Bharati_Sripadagalvaru_vs_State_Of_Kerala_And_Anr_on_24_April_1973.PDF"

# Extract and process
text = extract_text_from_pdf(file_path)
summary = summarize_text(text, num_sentences=7)
highlighted_summary = highlight_keywords(summary)

print("\n--- Highlighted Summary ---\n")
print(highlighted_summary)

import streamlit as st
from src.pdf_reader import extract_text_from_pdf
from src.summarizer import summarize_text

st.title("Legal Document Summarizer")

st.subheader("Upload a legal PDF notice and get a summarized version.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("data/notice1.pdf", "wb") as f: 
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("data/notice1.pdf")

if st.button("Summarize"):
    summary = summarize_text(text, num_sentences=7)
    st.markdown("### Highlighted Summary")
    st.write(summary)
    