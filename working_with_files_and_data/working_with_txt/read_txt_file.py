# This function will read txt file and return content
def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content
    
txt_file_path = 'sample.txt'
data = read_txt_file(txt_file_path)
print(data)