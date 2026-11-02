import os

from database import get_database_schema
from file_handler import identify_file

from text_extractor import extract_text

from attribute_extractor import (
    extract_attributes,
    identify_document_type,
    extract_multiple_attributes
)

from data_validator import validate_attributes
from database_operations import insert_record


# Required fields for each document category
required_fields_map = {
    "employee": ["name", "email", "phone", "department"],
    "customer": ["customer_name", "email", "address"],
    "supplier": ["supplier_name", "contact", "company"]
}


def display_database_schema():

    schema = get_database_schema()

    if schema:

        print("\nDATABASE SCHEMA")
        print("----------------------")

        for table, columns in schema.items():

            print(f"\nTable: {table}")

            for column in columns:
                print(f"  - {column}")


def process_document(file_path):

    if not os.path.isfile(file_path):
        print("File not found!")
        return

    # Identify file format
    file_type = identify_file(file_path)

    format_names = {
        "image": "Image",
        "pdf": "PDF",
        "docx": "Word",
        "excel": "Excel",
        "text": "Text"
    }

    print("\nFile Format:", format_names.get(file_type, "Unknown"))

    if file_type not in format_names:
        print("Unsupported file format!")
        return

    # Extract text
    extracted_text = extract_text(file_path)

    if not extracted_text or not extracted_text.strip():
        print("No text extracted from document!")
        return

    # Identify document category
    document_type = identify_document_type(extracted_text)

    print("Document Category:", document_type.capitalize())

    if document_type not in required_fields_map:
        print("Unknown document category!")
        return

    required_fields = required_fields_map[document_type]

    # Process multiple Excel records
    if file_type == "excel" and document_type == "supplier":

        records = extract_multiple_attributes(extracted_text)

        if not records:
            print("No supplier records found!")
            return

        print("\nExtracted Supplier Records:")
        print("------------------------------")

        for index, attributes in enumerate(records, start=1):

            print(f"\nSupplier Record {index}:")

            for key, value in attributes.items():
                print(f"{key}: {value}")

            # Validate record
            is_valid = validate_attributes(
                attributes,
                required_fields
            )

            if is_valid:

                print("Validation: PASSED")

                insert_record("supplier", attributes)

            else:
                print("Validation: FAILED")

    # Process single document
    else:

        attributes = extract_attributes(extracted_text)

        print("\nExtracted Attributes:")
        print("------------------------------")

        for key, value in attributes.items():
            print(f"{key}: {value}")

        # Validate attributes
        is_valid = validate_attributes(
            attributes,
            required_fields
        )

        if is_valid:

            print("\nData Validation: PASSED")

            insert_record(document_type, attributes)

        else:
            print("\nData Validation: FAILED")


# Main application
if __name__ == "__main__":

    print("================================")
    print("       DOCUMENT EXTRACTOR")
    print("================================")

    display_database_schema()

    file_path = input("\nEnter document path: ").strip()

    process_document(file_path)