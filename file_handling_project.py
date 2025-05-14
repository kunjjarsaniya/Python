"""
File Management Script - Beginner Python Tutorial

This script demonstrates how to:
1. Create a file
2. Read a file
3. Update a file (rename, overwrite, append)
4. Delete a file

Author: Your Name
"""

from pathlib import Path
import os


def list_files_and_folders():
    """
    List all files and folders in the current directory and subdirectories.
    """
    path = Path('.')
    items = list(path.rglob('*'))
    print("\n📂 Current Files and Folders:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    print()  # Blank line for spacing


def create_file():
    """
    Create a new text file and write content to it.
    """
    try:
        list_files_and_folders()
        name = input("📄 Enter the name of the new file: ")
        file_path = Path(name)

        if not file_path.exists():
            data = input("✍️  What content would you like to write in the file? ")
            with open(file_path, "w") as file:
                file.write(data)
            print("✅ File created successfully.")
        else:
            print("⚠️  A file with this name already exists.")
    except Exception as err:
        print(f"❌ Error: {err}")


def read_file():
    """
    Read and display the contents of an existing file.
    """
    try:
        list_files_and_folders()
        name = input("📄 Enter the name of the file to read: ")
        file_path = Path(name)

        if file_path.exists() and file_path.is_file():
            with open(file_path, 'r') as file:
                data = file.read()
                print("\n📚 File Content:")
                print(data)
                print("✅ File read successfully.")
        else:
            print("⚠️  The specified file does not exist.")
    except Exception as err:
        print(f"❌ Error: {err}")


def update_file():
    """
    Update an existing file:
    1. Rename it
    2. Overwrite content
    3. Append content
    """
    try:
        list_files_and_folders()
        name = input("✏️  Enter the file name to update: ")
        file_path = Path(name)

        if file_path.exists() and file_path.is_file():
            print("\nChoose an update option:")
            print("1. Rename the file")
            print("2. Overwrite the file content")
            print("3. Append new content")

            option = input("➡️  Enter your choice (1/2/3): ")

            if option == '1':
                new_name = input("📝 Enter the new file name: ")
                file_path.rename(Path(new_name))
                print("✅ File renamed successfully.")

            elif option == '2':
                new_data = input("✍️  Enter the new content to overwrite: ")
                with open(file_path, 'w') as file:
                    file.write(new_data)
                print("✅ Content overwritten successfully.")

            elif option == '3':
                more_data = input("➕ Enter content to append: ")
                with open(file_path, 'a') as file:
                    file.write(" " + more_data)
                print("✅ Content appended successfully.")

            else:
                print("❌ Invalid option selected.")
        else:
            print("⚠️  The specified file does not exist.")
    except Exception as err:
        print(f"❌ Error: {err}")


def delete_file():
    """
    Delete a specified file.
    """
    try:
        list_files_and_folders()
        name = input("🗑️  Enter the name of the file to delete: ")
        file_path = Path(name)

        if file_path.exists() and file_path.is_file():
            os.remove(file_path)
            print("✅ File deleted successfully.")
        else:
            print("⚠️  The specified file does not exist.")
    except Exception as err:
        print(f"❌ Error: {err}")


def main():
    """
    Main menu to let the user choose a file operation.
    """
    print("===== File Management Menu =====")
    print("1. Create a file")
    print("2. Read a file")
    print("3. Update a file")
    print("4. Delete a file")

    choice = input("🧭 Enter your choice (1/2/3/4): ")

    if choice == '1':
        create_file()
    elif choice == '2':
        read_file()
    elif choice == '3':
        update_file()
    elif choice == '4':
        delete_file()
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


# Run the program
if __name__ == "__main__":
    main()
