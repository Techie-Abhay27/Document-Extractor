from database import get_database_schema
from file_handler import identify_file
import os
from image_processor import extract_image_text
from pdf_processor import extract_pdf_text
from docx_processor import extract_docx_text
from excel_processor import extract_excel_data

schema = get_database_schema()

if schema:

    print("\nDATABASE SCHEMA")

    for table, columns in schema.items():

        print(f"\nTable: {table}")

        for column in columns:

            print(f"  - {column}")
            
folder = "uploads"

for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    file_type = identify_file(file_path)

    print(file, "---->", file_type)

#image processing
image_path = "uploads/employee.png"

text = extract_image_text(image_path)

print("\nExtracted Text:")
print("----------------------")

print(text)

#Pdf processing
pdf_path = "uploads/customer.pdf"

text = extract_pdf_text(pdf_path)

print("\nExtracted PDF Text:")
print("----------------------")

print(text)

#word file processing
docx_path = "uploads/supplier.docx"

text = extract_docx_text(docx_path)

print("\nExtracted DOCX Text:")
print("----------------------")

print(text)

#Excel file processing
excel_path = "uploads/data.xlsx"

text = extract_excel_data(excel_path)

print("\nExtracted Excel Text:")
print("----------------------")

print(text)