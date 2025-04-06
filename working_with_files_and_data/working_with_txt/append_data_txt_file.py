# This function will append data in txt file
def write_data_txt(file_path, content):
    with open(file_path, 'a', newline='') as file:
        file.write(f'\n{content}')
        print(f'Successfully append in {file_path}')

txt_file_path = 'sample.txt'
content = 'I am a Python developer.'
write_data_txt(txt_file_path, content)