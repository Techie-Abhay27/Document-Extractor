from file_handler import identify_file

from image_processor import extract_image_text
from pdf_processor import extract_pdf_text
from docx_processor import extract_docx_text
from excel_processor import extract_excel_data


def extract_text(file_path):

    file_type = identify_file(file_path)

    if file_type == "image":
        return extract_image_text(file_path)

    elif file_type == "pdf":
        return extract_pdf_text(file_path)

    elif file_type == "docx":
        return extract_docx_text(file_path)

    elif file_type == "excel":
        return extract_excel_data(file_path)

    elif file_type == "text":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    else:
        print("Unsupported file format!")
        return None