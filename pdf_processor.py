import pymupdf
import os
from image_processor import extract_image_text


def extract_pdf_text(pdf_path):

    document = pymupdf.open(pdf_path)

    extracted_text = ""

    for page_number, page in enumerate(document):

        print(f"Processing page: {page_number + 1}")

        # Extract direct text
        text = page.get_text()

        if text.strip():

            extracted_text += text + "\n"

        else:

            # Scanned PDF: Convert page into image
            pix = page.get_pixmap(dpi=300)

            image_path = f"uploads/temp_page_{page_number}.png"

            pix.save(image_path)

            # Apply OCR
            ocr_text = extract_image_text(image_path)

            if ocr_text:
                extracted_text += ocr_text + "\n"

            # Remove temporary image
            os.remove(image_path)

    document.close()

    return extracted_text