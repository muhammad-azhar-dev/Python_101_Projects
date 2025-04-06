# This function will create a txt file and write content in it
def write_data_txt(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        print(f'Successfully Write in {file_path}')

txt_file_path = 'sample.txt'
content = 'This is my txt file.'
write_data_txt(txt_file_path, content)