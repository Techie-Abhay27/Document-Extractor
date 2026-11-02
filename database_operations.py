from database import get_connection


def insert_record(table_name, data):

    connection = get_connection()

    if connection is None:
        print("Database connection failed!")
        return False

    # Allowed tables and columns
    allowed_tables = {
        "employee": ["name", "email", "phone", "department"],
        "customer": ["customer_name", "email", "address"],
        "supplier": ["supplier_name", "contact", "company"]
    }

    try:

        if table_name not in allowed_tables:
            print("Invalid table name!")
            return False

        allowed_columns = allowed_tables[table_name]

        if not data or not all(key in allowed_columns for key in data):
            print("Invalid data fields!")
            return False

        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))

        query = f"""
            INSERT INTO {table_name} ({columns})
            VALUES ({placeholders})
        """

        cursor = connection.cursor()

        cursor.execute(query, tuple(data.values()))

        connection.commit()

        print(f"Record inserted successfully into {table_name}!")

        return True

    except Exception as error:

        connection.rollback()
        print("Database insertion error:", error)

        return False

    finally:

        if connection.is_connected():
            cursor.close()
            connection.close()