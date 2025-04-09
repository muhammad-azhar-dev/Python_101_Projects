from zipfile import ZipFile

# This function will convert folder into zip
def convert_into_zip(folder_name, file_names):
    with ZipFile(f"{folder_name}.zip", "w") as zip_file:
        for file_name in file_names:
            zip_file.write(f"{folder_name}/{file_name}")
        print(f"Successfully converted '{folder_name}' into '{folder_name}.zip'")

# This function will convert zip folder to normal folder
def unzip_folder(folder_name):
    with ZipFile(f"{folder_name}", "r") as zip_file:
        zip_file.extractall('extracted_zip/')
        print(f"Successfully converted {folder_name} into extracted_zip")

if __name__ == "__main__":
    file_name_list = ["file1.txt", "file2.txt"]
    # convert_into_zip("folder", file_name_list)

    # calling unzip_file()
    # unzip_folder("folder.zip")