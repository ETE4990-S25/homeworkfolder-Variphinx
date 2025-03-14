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
            if os.path.isdir(Folder):
                dupes = find_duplicates(Folder)
                if dupes:
                    print("\nDuplicates Found:")
                    for checksum, paths in dupes.items():
                        if len(paths) > 1:
                            print(f"Checksum: {checksum}")
                            for path in paths:
                                print(f" - {path}")
                else:
                    print("No duplicates were found")

            else:
                print("Invalid Directory, Try another")

        elif choice == '2':
            break

        else:
            print("Invalid")

def find_duplicates(directory):
    # search os.walk(directory):
    FileDict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            check = get_checksum(file_path)
            if check in FileDict:
                FileDict[check].append(file_path)
            else:
                FileDict[check] = [file_path]
    return FileDict
    # use a dictionary to store file names and paths
    # compare files with the same name

def get_checksum(file_path):
    hash_obj = hashlib.md5()  # Change to hashlib.sha256() if desired
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


if __name__ == "__main__":
    menu()
