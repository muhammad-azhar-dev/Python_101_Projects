import os

# Check file path exists or not
def check_file_path_exists(file_path):
    # check file path exists or not
    if os.path.exists(file_path):
        print(f"{file_path} Exist")
    else:
        print(f"{file_path} Doesn't Exist")

# Check both file names are same or not
def compare_two_file_names(path1, path2):
    # compare two files names (not their data) are same or not
    if os.path.samefile(path1, path2):
        print("paths refers to the same file")
    else:
        print("paths do not refer to the same file")

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "folder", "file1.txt")
    # check_file_path_exists(file_path)

    path1 = f"{os.getcwd()}/folder/file1.txt"
    path2 = f"{os.getcwd()}/folder/file2.txt"
    compare_two_file_names(path1, path2)