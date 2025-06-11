import os
import pdfplumber
import PyPDF2
import pytesseract
import pdf2image
import pypdfium2
import fitz  # PyMuPDF
import pandas as pd
from collections import Counter
from pathlib import Path
import json as js
from dotenv import load_dotenv

# NLP imports
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load environment variables
load_dotenv()

# Download NLTK corpora (silent)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Load stopwords
nltk_stopwords = set(stopwords.words('english'))
stop_words = nltk_stopwords.union({
    "patient", "name", "doctor", "employee", "address", "medications",
    "history", "provider", "care", "phone", "insurance", "today", "date",
    "claim", "company", "report", "record", "exam", "visit", "chart",
    "reason", "summary", "physician", "injury", "worker", "information"
})

# Paths from environment variables
pdf_folder = os.getenv("PDF_INPUT_FOLDER", "./data")
output_csv = os.getenv("OUTPUT_CSV", "./output/keyword_analysis.csv")

# Extraction functions (same fallback order as your original)
def extract_text_pymupdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_doc:
            for page in pdf_doc:
                page_text = page.get_text()
                if page_text:
                    text += page_text + " "
        return text.strip() if text else None
    except:
        return None

def extract_text_with_pdfplumber(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        return text.strip() if text else None
    except:
        return None

def extract_text_pypdfium2(pdf_path):
    text = ""
    try:
        pdf_doc = pypdfium2.PdfDocument(pdf_path)
        for page in pdf_doc:
            page_text = page.get_textpage().get_text_bounded()
            if page_text:
                text += page_text + " "
        return text.strip() if text else None
    except:
        return None

def extract_text_PyPDF2(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        return text.strip() if text else None
    except:
        return None

def extract_text_tesseract_ocr(pdf_path):
    text = ""
    try:
        images = pdf2image.convert_from_path(pdf_path)
        for image in images:
            page_text = pytesseract.image_to_string(image)
            text += page_text
        return text.strip() if text else None
    except:
        return None

def extract_text_from_pdf(pdf_path):
    for extractor in [extract_text_pymupdf, extract_text_with_pdfplumber, extract_text_pypdfium2, extract_text_PyPDF2, extract_text_tesseract_ocr]:
        text = extractor(pdf_path)
        if text:
            return text
    return None

def process_pdfs():
    results = []
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.lower().endswith(".pdf"):
            file_path = os.path.join(pdf_folder, pdf_file)
            text = extract_text_from_pdf(file_path)
            if text:
                tokens = word_tokenize(text.lower())
                filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
                token_freq = Counter(filtered_tokens).most_common(30)
                keywords_dict = dict(token_freq)
            else:
                keywords_dict = {}
            result_entry = {
                "Document": pdf_file,
                "Keywords": js.dumps(keywords_dict)
            }
            results.append(result_entry)

    df = pd.DataFrame(results)
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Keyword analysis saved to {output_csv}")

if __name__ == "__main__":
    process_pdfs()