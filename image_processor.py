import cv2
import pytesseract


# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_image_text(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded!")
        return None

    # Convert image into grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Apply thresholding
    processed = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(
        processed
    )

    return extracted_text