import pandas as pd

# This function extracts column names from an Excel file using pandas
def extract_column_names(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    # Extract column names
    column_names = df.columns.tolist()
    return column_names

if __name__ == "__main__":
    excel_file_path = 'test.xlsx'  # Replace with your Excel file path
    column_names = extract_column_names(excel_file_path)
    print("Column names:", column_names)