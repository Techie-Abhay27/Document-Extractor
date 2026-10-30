import mysql.connector

def get_connection():

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Abhay@1234",
            database="document_db",
            port=3306
        )

        if connection.is_connected():
            print("Database connected successfully!")

        return connection

    except mysql.connector.Error as error:

        print("Database connection failed:", error)
        return None
    
def get_database_schema():

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    schema = {}

    try:

        # Fetch all tables
        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall()

        for table in tables:

            table_name = table[0]

            # Fetch table columns
            cursor.execute(
                f"DESCRIBE `{table_name}`"
            )

            columns = cursor.fetchall()

            column_names = []

            for column in columns:
                column_names.append(column[0])

            schema[table_name] = column_names

        return schema

    finally:
        cursor.close()
        connection.close()