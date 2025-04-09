import tarfile

# This function will convert folder into tar
def convert_into_tar(folder_name, file_names):
    with tarfile.open(f"{folder_name}.tar", "w") as tar:
        for file_name in file_names:
            tar.add(f"{folder_name}/{file_name}")
        print(f"Successfully converted '{folder_name}' into '{folder_name}.tar'")

# This function will convert tar folder to normal folder
def untar_folder(folder_name):
    with tarfile.open(f"{folder_name}", "r") as tar:
        tar.extractall('extracted_tar/')
        print(f"Successfully converted {folder_name} into extracted_tar")

if __name__ == "__main__":
    file_name_list = ["file1.txt", "file2.txt"]
    convert_into_tar("folder", file_name_list)

    # calling untar_file()
    # untar_folder("folder.tar")