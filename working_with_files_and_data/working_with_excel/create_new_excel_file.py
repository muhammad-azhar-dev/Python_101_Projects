import openpyxl

# This function will create a new excel file
def create_excel_file(file_path):
    work_book = openpyxl.Workbook()
    work_book.save(file_path)

new_file_path = 'new_test.xlsx'  # Replace with your new Excel file path
create_excel_file(new_file_path)