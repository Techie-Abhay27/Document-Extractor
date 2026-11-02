import re

def extract_attributes(text):

    attributes = {}

    # Extract Employee Name
    name = re.search(r"Employee Name:\s*(.+)", text)

    if name:
        attributes["name"] = name.group(1).strip()

    # Extract Email
    email = re.search(r"Email:\s*(\S+)", text)

    if email:
        attributes["email"] = email.group(1).strip()
        
    # Extract Customer Name
    customer_name = re.search(r"Customer Name:\s*(.+)", text)

    if customer_name:
        attributes["customer_name"] = customer_name.group(1).strip()

    # Extract Address
    address = re.search(r"Address:\s*(.+)", text)

    if address:
        attributes["address"] = address.group(1).strip()
        
        # Extract Supplier Name
    supplier_name = re.search(r"Supplier Name:\s*(.+)", text)

    if supplier_name:
        attributes["supplier_name"] = supplier_name.group(1).strip()

    # Extract Contact
    contact = re.search(r"Contact:\s*(\d{10})", text)

    if contact:
        attributes["contact"] = contact.group(1)

    # Extract Company
    company = re.search(r"Company:\s*(.+)", text)

    if company:
        attributes["company"] = company.group(1).strip()

    # Extract Phone
    phone = re.search(r"Phone:\s*(\d{10})", text)

    if phone:
        attributes["phone"] = phone.group(1)

    # Extract Department
    department = re.search(r"Department:\s*(.+)", text)

    if department:
        attributes["department"] = department.group(1).strip()

    return attributes


def identify_document_type(text):

    if not text:
        return "unknown"

    if all(keyword in text for keyword in [
        "Employee Name:",
        "Email:",
        "Phone:",
        "Department:"
    ]):
        return "employee"

    elif all(keyword in text for keyword in [
        "Customer Name:",
        "Email:",
        "Address:"
    ]):
        return "customer"

    elif all(keyword.lower() in text.lower() for keyword in [
    "Supplier Name",
    "Contact",
    "Company"
]):
        return "supplier"

    else:
        return "unknown"

def extract_multiple_attributes(text):

    records = []

    # Split text into separate records
    rows = re.split(r"\n\s*\n", text.strip())

    for row in rows:

        if not row.strip():
            continue

        attributes = extract_attributes(row)

        if attributes:
            records.append(attributes)

    return records
