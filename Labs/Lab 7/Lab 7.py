import os
import hashlib

def menu():
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            Folder = input("Enter specific directory to search:")
            os.path.isdir(Folder)


def find_duplicates(directory):
    # search os.walk(directory):
    FileDict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file in FileDict:
                FileDict[file].append(file_path)
            else:
                FileDict[file] = [file_path]
    return FileDict
    # use a dictionary to store file names and paths
    # compare files with the same name

def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

