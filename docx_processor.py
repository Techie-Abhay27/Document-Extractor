from docx import Document


def extract_docx_text(file_path):

    document = Document(file_path)

    extracted_text = ""

    # Extract paragraphs
    for paragraph in document.paragraphs:

        extracted_text += paragraph.text + "\n"

    # Extract tables
    for table in document.tables:

        for row in table.rows:

            for cell in row.cells:

                extracted_text += cell.text + " "

            extracted_text += "\n"

    return extracted_text