import os

def identify_file(file_path):

    if not os.path.exists(file_path):
        return "File not found"

    extension = os.path.splitext(file_path)[1].lower()

    if extension in ['.jpg', '.jpeg', '.png']:
        return "image"

    elif extension == '.pdf':
        return "pdf"

    elif extension == '.docx':
        return "docx"

    elif extension == '.xlsx':
        return "excel"

    elif extension == '.txt':
        return "text"

    else:
        return "unsupported"