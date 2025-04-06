import pandas as pd

# This function will read specific data from an excel file
def read_excel(file_path, selected_columns):
    df = pd.read_excel(file_path, usecols=selected_columns)
    return df

excel_file_path = 'test.xlsx'  # Replace with your Excel file path
selected_columns = ['id','first name']
selected_data = read_excel(excel_file_path, selected_columns)
print(selected_data)