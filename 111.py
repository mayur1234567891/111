import os
import shutil

from_dir="C:/Users/malli/Downloads"
to_dir="C:/Users/malli/Documents"
list_of_file=os.listdir(from_dir)
print(list_of_file)
for file_name in list_of_file:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
