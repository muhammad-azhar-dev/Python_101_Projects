import openpyxl

# This function will append values in excel file
def append_values(file_path, sheet_name, values):
    work_book = openpyxl.load_workbook(file_path)
    sheet = work_book.create_sheet(sheet_name)
    for row in values:
        sheet.append(row)
    work_book.save(file_path)
    print(f'Successfully append values in {file_path} in sheet: {sheet_name}')

excel_file_path = 'new_test.xlsx'  # Replace with your Excel file path
new_values = [
    ['Ali', 26],
    ['Usama', 30]
]
append_values(excel_file_path, 'Sheet1', new_values)