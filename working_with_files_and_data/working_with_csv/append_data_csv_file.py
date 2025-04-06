import csv

def create_csv_file(file_path, data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        print(f'Successsfully added data in {file_path}')

csv_file_path = 'sample.csv'   # replace with your csv file path
new_data = [5, 'Sikander', 29]
create_csv_file(csv_file_path, new_data)