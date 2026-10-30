# Document Extractor

A Python-based document processing project that extracts text and
tabular data from different file formats and connects to a MySQL
database. The project is being developed as an internship project at
Syandrix Infotech.

## Overview

Document Extractor is designed to process documents such as images,
PDFs, Word documents, and Excel spreadsheets. It identifies the file
type and uses an appropriate Python library to extract the available
text or data.

The project also connects to MySQL and can inspect the database schema
so that document information can be matched with the available tables
and columns as the project is extended.

## Current Capabilities

-   Identify supported document types by file extension.
-   Extract text from JPG, JPEG, and PNG images using OpenCV and
    Tesseract OCR.
-   Extract text from text-based PDFs using PyMuPDF.
-   Apply OCR to PDF pages when a page does not contain extractable
    text.
-   Extract paragraphs and table content from DOCX files.
-   Read tabular data from XLSX files using pandas.
-   Connect Python to a MySQL database.
-   Read database tables and their column names dynamically.
-   Keep uploaded test documents out of version control.

## Supported File Formats

  -----------------------------------------------------------------------
  File format             Extension               Processing method
  ----------------------- ----------------------- -----------------------
  Images                  `.jpg`, `.jpeg`, `.png` OpenCV + Tesseract OCR

  PDF                     `.pdf`                  PyMuPDF; OCR fallback
                                                  for scanned pages

  Word                    `.docx`                 python-docx

  Excel                   `.xlsx`                 pandas + openpyxl

  Text                    `.txt`                  Recognized by the file
                                                  handler; processing can
                                                  be extended as needed
  -----------------------------------------------------------------------

## Project Structure

``` text
Document-Extractor/
│
├── uploads/                  # Local input documents (not committed)
│   └── .gitkeep
│
├── main.py                   # Main application entry point
├── database.py               # MySQL connection and schema inspection
├── database_operations.py    # Database operation helpers
├── file_handler.py            # File type identification
├── image_processor.py         # Image preprocessing and OCR
├── pdf_processor.py           # PDF text extraction and OCR fallback
├── docx_processor.py          # DOCX text and table extraction
├── excel_processor.py         # XLSX data extraction
├── attribute_extractor.py    # Attribute extraction logic
├── data_validator.py          # Extracted data validation logic
│
├── requirements.txt           # Python dependencies
├── .env.example               # Example environment configuration
├── .gitignore                 # Files excluded from Git
└── README.md
```

## Technologies Used

-   Python
-   MySQL
-   OpenCV
-   Tesseract OCR / pytesseract
-   Pillow
-   PyMuPDF
-   python-docx
-   pandas
-   openpyxl
-   mysql-connector-python
-   python-dotenv

## Requirements

Before running the project, install or configure:

1.  Python 3.
2.  MySQL Server.
3.  Tesseract OCR for image and scanned-PDF text recognition.
4.  Git (optional, for version control).

## Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/YOUR-USERNAME/Document-Extractor.git
cd Document-Extractor
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

On Windows using Git Bash:

``` bash
python -m venv venv
source venv/Scripts/activate
```

On Windows using Command Prompt:

``` bat
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

### 4. Install and configure Tesseract OCR

Install the Tesseract OCR application on Windows. If it is installed in
the default location, the image processor may use:

``` python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

If Tesseract is installed elsewhere, update this path in
`image_processor.py`.

### 5. Configure MySQL

Create the database in MySQL:

``` sql
CREATE DATABASE document_db;
```

Create a local `.env` file in the project root using `.env.example` as a
guide:

``` env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=document_db
DB_PORT=3306
```

Use the credentials for your own MySQL installation. Do not commit
`.env` or share database passwords.

> The application expects the database tables used by the project to
> exist. If you are setting up a fresh database, create the required
> tables before running database-dependent features.

### 6. Add documents for testing

Place test files in the `uploads/` folder. This folder is ignored by Git
except for `.gitkeep`, so your private or sample documents will remain
local.

### 7. Run the application

``` bash
python main.py
```

## Notes

-   The Tesseract executable must be installed separately; installing
    `pytesseract` with pip alone is not enough.
-   OCR accuracy depends on image quality, text clarity, orientation,
    and language data.
-   The current PDF processor uses direct text extraction where possible
    and OCR for pages without extractable text.
-   The `.env` file contains local credentials and must never be
    committed to GitHub.
-   Update `requirements.txt` whenever project dependencies change:

``` bash
python -m pip freeze > requirements.txt
```

## Security

-   Keep passwords and other secrets in `.env`.
-   Commit `.env.example` with placeholder values only.
-   Do not commit real identity documents, customer records, employee
    records, or other private uploads.
-   Do not commit virtual environments or local cache files.

## Project Status

This README describes the project structure and
document-processing/database components currently present in the
repository. Features and workflows may evolve as development continues.

## Author

Developed as a Python document-extraction internship project.
