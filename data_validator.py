import re


def validate_email(email):

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(pattern, email):
        return True
    else:
        return False
    
def validate_phone(phone):

    pattern = r"^[0-9]{10}$"

    if re.fullmatch(pattern, phone):
        return True
    else:
        return False


def validate_required_fields(attributes, required_fields):

    for field in required_fields:

        if field not in attributes or not attributes[field]:

            print(f"Missing required field: {field}")
            return False

    return True

def validate_attributes(attributes, required_fields):

    # Check required fields
    if not validate_required_fields(attributes, required_fields):
        return False

    # Validate email if available
    if "email" in attributes:
        if not validate_email(attributes["email"]):
            print("Invalid email address!")
            return False

    # Validate phone if available
    if "phone" in attributes:
        if not validate_phone(attributes["phone"]):
            print("Invalid phone number!")
            return False

    # Validate supplier/customer contact if available
    if "contact" in attributes:
        if not validate_phone(attributes["contact"]):
            print("Invalid contact number!")
            return False

    return True
    
