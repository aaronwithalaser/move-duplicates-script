import os
import shutil
import hashlib
import sys

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicate_files(folder_path):
    files_hash = {}
    duplicate_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)

            if file_hash not in files_hash:
                files_hash[file_hash] = [file_path]
            else:
                files_hash[file_hash].append(file_path)
                duplicate_files.append(file_path)

    return duplicate_files

def move_duplicate_files(duplicate_files, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for file_path in duplicate_files:
        shutil.move(file_path, os.path.join(dest_folder, os.path.basename(file_path)))

def main():
    folder_path = input("Enter the folder path to search for duplicate files: ")
    dest_folder = os.path.join(folder_path, "duplicates")

    duplicate_files = find_duplicate_files(folder_path)
    move_duplicate_files(duplicate_files, dest_folder)

    print(f"{len(duplicate_files)} duplicate files moved to {dest_folder}")

if __name__ == "__main__":
    main()
