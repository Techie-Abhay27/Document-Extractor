import pandas as pd


def extract_excel_data(file_path):

    try:

        # Read Excel file
        df = pd.read_excel(file_path)

        print("Excel Data:")
        print(df)

        # Convert data into text
        extracted_text = df.to_string(index=False)

        return extracted_text

    except Exception as error:

        print("Excel processing error:", error)

        return None