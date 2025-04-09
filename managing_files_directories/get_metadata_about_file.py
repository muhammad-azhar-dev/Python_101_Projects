"""
What is metadata?
it's all about file details like file-size, last-modified-time, and more...
"""

import os
from datetime import datetime

file_name = "main.py"

# Get file info by file name
file_info = os.stat(file_name)

# Get file size in bytes
size = file_info.st_size
print(f"{size} bytes")

# Get last modified time of file
last_modified_time = file_info.st_mtime
# Format this time in readable formaat
formatted_time = datetime.fromtimestamp(last_modified_time)
print(f"Last modified time: {formatted_time}")