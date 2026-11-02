import pandas as pd


def extract_excel_data(file_path):

    try:

        # Read Excel file
        df = pd.read_excel(file_path)

        print("Excel Data:")
        print(df)

        # Convert each row into labelled text
        extracted_text = ""

        for index, row in df.iterrows():

            for column in df.columns:
                column_name = str(column).strip()
                extracted_text += f"{column_name}: {row[column]}\n"

            extracted_text += "\n"

        return extracted_text

    except Exception as error:

        print("Excel processing error:", error)

        return None