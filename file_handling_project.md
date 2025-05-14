
# 📁 Python File Management Tutorial

Welcome to this beginner-friendly Python tutorial!  
This repository helps you understand how to manage files in Python — create, read, update, and delete them — through a hands-on command-line interface.

---

## 🚀 What You’ll Learn

This script introduces core Python concepts such as:

- 📂 Listing files and folders using `pathlib`
- 📝 Creating and writing to text files
- 📖 Reading content from existing files
- ✏️ Renaming, overwriting, and appending to files
- 🗑️ Deleting files from the filesystem
- ⚠️ Exception handling using `try-except`
- ✅ Structuring Python code with functions and `if __name__ == "__main__"`

---

## 🧰 Requirements

- Python 3.6 or higher
- No external packages needed

---

## ▶️ How to Run the Script

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kunjjarsaniya/python.git
   cd file_handling_project
   ```

2. **Run the script:**

   ```bash
   python main.py
   ```

3. **Choose an option from the menu:**

   ```
   1. Create a file
   2. Read a file
   3. Update a file
   4. Delete a file
   ```

---

## 📘 Code Overview

### `main.py` Functions:

| Function               | Purpose                                               |
|------------------------|-------------------------------------------------------|
| `list_files_and_folders()` | Lists all files/folders in the current directory   |
| `create_file()`        | Creates a new file and writes user input to it        |
| `read_file()`          | Displays the contents of an existing file             |
| `update_file()`        | Allows renaming, overwriting, or appending to a file  |
| `delete_file()`        | Deletes a selected file from the directory            |
| `main()`               | Provides an interactive menu                          |

---

## 🧠 Concepts Covered

| Concept        | Explanation |
|----------------|-------------|
| `pathlib.Path` | Modern, object-oriented file and folder paths |
| File Modes     | `'w'` = write, `'r'` = read, `'a'` = append |
| `try-except`   | Error handling for invalid input or missing files |
| `os.remove()`  | Deletes files from the OS |
| `Path.rename()`| Renames files using the `pathlib` module |

---

## 🧪 Suggested Exercises

To expand this tutorial, try implementing these enhancements:

1. **🗃️ Directory Creation**  
   Add support for creating new folders alongside files.

2. **🛠️ Work in Any Directory**  
   Allow users to specify the directory to operate in.

3. **📂 File Backup**  
   Before overwriting, create a `.bak` version of the file.

4. **🧾 View File Metadata**  
   Show size, creation date, and file type before reading.

5. **🧰 CLI Version**  
   Use `argparse` to create a command-line version of this tool.

6. **💡 Mini-Project:**  
   Build a text-based note-taking app using this file system logic.

---

## 🔗 Useful Resources

- [`pathlib` documentation](https://docs.python.org/3/library/pathlib.html)
- [`open()` function](https://docs.python.org/3/library/functions.html#open)
- [`os` module](https://docs.python.org/3/library/os.html)
- [`try-except` blocks](https://docs.python.org/3/tutorial/errors.html)

---

## 👨‍🏫 About the Author

Created by `KUNJ` 
Contributions and sugestions are welcome! Fork this project or open an issue to collaborate.

---
