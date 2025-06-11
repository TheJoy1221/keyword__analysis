# Keyword Extraction Engine

A multi-layer PDF keyword extraction pipeline that parses scanned and text-based documents using a stack of PDF extraction libraries and OCR fallbacks. Processes extracted text using NLP tokenization and stopword filtering to output document-level keyword frequency counts.

---

## Features

- 📄 Supports both scanned and text-based PDFs.
- 🧹 Multiple fallback text extraction methods: PyMuPDF, pdfplumber, pypdfium2, PyPDF2, and Tesseract OCR.
- 🧠 NLP keyword extraction using NLTK.
- 🔑 Custom stopword filtering to isolate meaningful keywords.
- 📊 Outputs clean CSV keyword files for analysis or downstream ML usage.

---

## 📂 Project Structure

keyword-extraction/
│
├── src/
│   └── keyword_extraction.py
│
├── .env.example
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---

## ⚙️ Setup Instructions

### Clone the Repository

git clone https://github.com/your-username/keyword-extraction.git
cd keyword-extraction

## Install Dependencies
- Ensure you’re using Python 3.10+ (tested on 3.10.x).
pip install -r requirements.txt

-## Configure Environment Variables
Create your .env file using the provided example:
cp .env.example .env

- ## Then edit .env with your actual input and output paths for PDF processin
PDF_INPUT_FOLDER=./data
OUTPUT_CSV=./output/keyword_analysis.csv

-## Run the script
python src/keyword_extraction.py

---

Notes
	•	This pipeline automatically attempts multiple PDF extraction methods: PyMuPDF → pdfplumber → pypdfium2 → PyPDF2 → Tesseract OCR.
	•	Ensure Tesseract is installed and properly configured in your system PATH if OCR is needed.
	•	All keyword extraction uses NLTK tokenization with custom stopword filtering.
	•	The script is designed to process batch PDF folders automatically.
