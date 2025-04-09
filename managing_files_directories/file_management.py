import os
import shutil

class FileHandler():

    # check file exists or not
    def check_file_exist(self, file_name):
        current_dir = os.getcwd()
        if file_name in os.listdir(current_dir):
            return True
        else:
            return False

    # create file
    def create_file(self, file_name, file_content):
        # check file exists or not
        if self.check_file_exist(file_name):
            print(f"File {file_name} is Already exist!")
        else:
            with open(file_name, 'w') as file:
                file.write(file_content)
                print(f"Successfully created File: {file_name}")

    # copy file
    def copy_file(self, file_name, copied_path):
        # check file exists or not
        if self.check_file_exist(file_name):
            shutil.copy(file_name, copied_path)
            print(f"Successfully copied {file_name} in {copied_path}")
        else:
            print(f"File: {file_name} Doesn't Exists! please first create it.")

    # move file
    def move_file(self, file_name, moved_path):
        # check file exists or not
        if self.check_file_exist(file_name):
            shutil.move(file_name, moved_path)
            print(f"Successfully moved {file_name} in {moved_path}")
        else:
            print(f"File: {file_name} Doesn't Exists! please first create it.")

    # rename file
    def rename_file(self, file_name, new_file_name):
        # check file exists or not
        if self.check_file_exist(file_name):
            os.rename(file_name, new_file_name)
            print(f"Successfully Renamed file {file_name} to {new_file_name}")
        else:
            print(f"File: {file_name} Doesn't Exists! please first create it.")

    # delete file
    def delete_file(self, file_name):
        # check file exists or not
        if self.check_file_exist(file_name):
            os.remove(file_name)
            print(f"Successfully Deleted {file_name}")
        else:
            print(f"File: {file_name} Doesn't Exists! please first create it.")