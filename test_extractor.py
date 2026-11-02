#from text_extractor import extract_text

#file_path = "uploads/employee.png"
#file_path = "uploads/customer.pdf"
#file_path = "uploads/supplier.docx"
# file_path = "uploads/data.xlsx"
# result = extract_text(file_path)

# print("\nExtracted Text:")
# print(result)

# from text_extractor import extract_text

# file_path = input("Enter document path: ")

# result = extract_text(file_path)

# print("\nExtracted Text:")
# print(result)

from text_extractor import extract_text
from attribute_extractor import extract_attributes, identify_document_type,extract_multiple_attributes
from data_validator import validate_attributes
from file_handler import identify_file
from database_operations import insert_record

file_path = input("Enter document path: ")
# Identify file format
file_format = identify_file(file_path)

format_names = {
    "image": "Image",
    "pdf": "PDF",
    "docx": "Word",
    "excel": "Excel",
    "text": "Text"
}

print("File Format:", format_names.get(file_format, "Unknown"))
# Extract text from document
extracted_text = extract_text(file_path)

# Extract employee attributes
attributes = extract_attributes(extracted_text)
# Identify document category
document_type = identify_document_type(extracted_text)

print("Document Category:", document_type.capitalize())


# Select required fields
if document_type == "employee":
    required_fields = ["name", "email", "phone", "department"]

elif document_type == "customer":
    required_fields = ["customer_name", "email", "address"]

elif document_type == "supplier":
    required_fields = ["supplier_name", "contact", "company"]

else:
    required_fields = []


# Process multiple Excel records
if file_format == "excel" and document_type == "supplier":

    records = extract_multiple_attributes(extracted_text)

    print("\nExtracted Supplier Records:")
    print("------------------------------")

    for index, attributes in enumerate(records, start=1):

        print(f"\nSupplier Record {index}:")

        for key, value in attributes.items():
            print(f"{key}: {value}")

        is_valid = validate_attributes(attributes, required_fields)

        if is_valid:
            print("Validation: PASSED")
            insert_record("supplier", attributes)
        else:
            print("Validation: FAILED")


# Process single document
else:

    attributes = extract_attributes(extracted_text)

    if document_type == "unknown":
        is_valid = False
        print("\nUnknown document type!")

    else:
        is_valid = validate_attributes(attributes, required_fields)

    if is_valid:
        print("\nData Validation: PASSED")

        insert_record(document_type, attributes)

    else:
         print("\nData Validation: FAILED")

    print("\nExtracted Attributes:")
    print("------------------------------")

    for key, value in attributes.items():
        print(f"{key}: {value}")
    