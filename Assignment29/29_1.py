import os

filename = input("Enter file name: ")

if os.path.isfile(filename):
    print("File exists")
else:
    print("File does not exist")
