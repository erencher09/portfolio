import os
directory = "./test"
for root, dirs, files in os.walk(directory):
   for file in files:
      file_path = os.path.join(root, file)
      file_size = os.path.getsize(file_path)
      print(f"{file_path}: {file_size} bytes")