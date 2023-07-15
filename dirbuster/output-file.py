import os

path = input("File Path: \n")
if os.path.exists(path):
    file = open(path, "r")
    print(file)
    content = file.read()
    print(content)

