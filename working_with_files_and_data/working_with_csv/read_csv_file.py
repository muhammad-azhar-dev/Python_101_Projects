import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data  

csv_file_path = 'sample.csv'   # replace with your csv file path
csv_data = read_csv(csv_file_path)
print(csv_data)