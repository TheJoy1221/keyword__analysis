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

```bash
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
