import pandas as pd

# This function will read the Excel file and return a DataFrame
def read_excel_file(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path, index_col=None, engine='openpyxl')
    return df

if __name__ == "__main__":
    excel_file_path = 'test.xlsx'  # Replace with your Excel file path
    print("DataFrame:\n", read_excel_file(excel_file_path))