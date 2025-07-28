# LegalEase - Legal Notice Summarizer 

**LegalEase** is an intelligent legal document summarization tool that extracts key information from lengthy legal notices (PDFs) and generates concise summaries using advanced NLP techniques. It features a user-friendly Streamlit interface, supports PDF uploads, and allows exporting summaries to PDF.

---

## Features 

**Upload legal PDF** documents 

**Text extraction** using PyMuPDF

**Summarization** using frequency-based 

**Streamlit UI** for interactive use

**Export summary** to PDF 

Modular code structure

---

## Project Structure

#### Textsummarizer/
#### │
#### ├── app.py # Streamlit app
#### ├── requirements.txt # Project dependencies
#### ├── README.md # Project documentation
#### │
#### ├── data/
#### │ ├── The Indian Contract Act, 1872.pdf # Sample legal PDF
#### │ └── notice.pdf # Exported summary
#### │
#### └── src/
#### ├── init.py
#### ├── pdf_reader.py # PDF extraction logic
#### ├── summarizer.py # Summarization logic
#### └── highlighter.py # Summary-to-PDF utility

--- 

## How to run this Project

1. **Clone the Repository** 
```bash
git clone https://github.com/shilpa9087/LegalEase.git
cd LegalEase

# Install Dependencies
pip install -r requirements.txt 

# Run the app 
streamlit run app.py

# Built With 
Python 3.9+ 
Streamlit 
PyMuPDF (fitz) 
NLTK 
ReportLab 

# Future Improvements 

* Add BERT or LLM-based summarization 
* Include keyword/entity highlighting 
* Integrate HuggingFace Transformers 
* Deploy to Streamlit Cloud 

# Author 
Shilpashree C M
https://github.com/shilpa9087/shilpa9087.git
www.linkedin.com/in/shilpashree-c-m-28021a28a

