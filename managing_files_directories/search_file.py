import glob

# Search file by extension and return list
def search_file(file_path, file_extension):
    txt_files = glob.glob(f"{file_path}/*{file_extension}")
    if txt_files:
        print(f"{len(txt_files)} files are found")
        print(txt_files)
    else:
        print(f"files with this extension '{file_extension}' are not found!")

search_file("folder", ".txt")