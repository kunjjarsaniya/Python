"""
=============================================================
📘 PYTHON LEARNING TUTORIAL (Beginner Friendly)
=============================================================
Author: Your Name
GitHub: https://github.com/yourusername/yourrepo

🎯 GOAL: This file teaches Python fundamentals with examples.

📂 SECTIONS COVERED:
1. Variable Naming & Data Types
2. Strings & User Input
3. Arithmetic & Logical Operations
4. Conditionals (if/elif/else)
5. Loops (for, while)
6. Functions
7. Lists, Tuples, Sets, Dictionaries
8. File Handling
9. Exception Handling
10. Advanced Concepts: Decorators, Lambda, Comprehensions
11. Pattern Printing & Logical Exercises
=============================================================
"""

# --------------------------
# 1. VARIABLE NAMING & TYPES
# --------------------------

def variable_naming_examples():
    # Variable Naming Styles
    PascalCase = "StudentName"
    camelCase = "studentName"
    snake_case = "student_name"  # Preferred in Python

    # Data Types
    int_val = 10
    float_val = 3.14
    complex_val = 2 + 3j
    bool_val = True
    string_val = "Hello!"

    print("✅ Variable and Data Type Examples:")
    print(type(int_val), type(float_val), type(complex_val), type(bool_val), type(string_val))

# variable_naming_examples()

# --------------------------
# 2. STRINGS & USER INPUT
# --------------------------

def string_examples():
    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    print(f"👋 Hello {name}, you are {age} years old.")

# string_examples()

# --------------------------
# 3. ARITHMETIC OPERATIONS
# --------------------------

def arithmetic_operations():
    a = 10
    b = 3
    print(f"Addition: {a + b}\nSubtraction: {a - b}\nMultiplication: {a * b}")
    print(f"Division: {a / b}\nFloor Division: {a // b}\nModulo: {a % b}\nPower: {a ** b}")

# arithmetic_operations()

# --------------------------
# 4. CONDITIONAL STATEMENTS
# --------------------------

def check_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("✅ You are eligible to vote.")
    else:
        print("❌ You are not eligible to vote.")

# check_eligibility()

# --------------------------
# 5. LOOPS
# --------------------------

def print_table():
    number = int(input("Enter a number to print its multiplication table: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# print_table()

# --------------------------
# 6. FUNCTIONS
# --------------------------

def greet(name):
    return f"Hello, {name}! Welcome to Python."

# print(greet("Alice"))

# --------------------------
# 7. LISTS & TUPLES
# --------------------------

def list_and_tuple_examples():
    fruits = ["apple", "banana", "cherry"]
    numbers = (1, 2, 3)
    print("🍎 Fruits:", fruits)
    print("🔢 Numbers:", numbers)

# list_and_tuple_examples()

# --------------------------
# 8. SETS & DICTIONARIES
# --------------------------

def set_and_dict_examples():
    unique_nums = {1, 2, 2, 3, 4}
    user_info = {"name": "Alice", "age": 25}
    print("📌 Unique Numbers:", unique_nums)
    print("👤 User Info:", user_info)

# set_and_dict_examples()

# --------------------------
# 9. FILE HANDLING
# --------------------------

def write_file():
    with open("example.txt", "w") as f:
        f.write("This is an example file.")
    print("✅ File written successfully.")

# write_file()

# --------------------------
# 10. EXCEPTION HANDLING
# --------------------------

def safe_division():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print("Result =", result)
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except ValueError:
        print("❌ Please enter valid numbers.")

# safe_division()

# --------------------------
# 11. ADVANCED CONCEPTS
# --------------------------

def use_lambda_map_filter():
    nums = list(range(1, 11))
    squares = list(map(lambda x: x ** 2, nums))
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("🔢 Squares:", squares)
    print("🧮 Evens:", evens)

# use_lambda_map_filter()

# --------------------------
# 12. PATTERN PRINTING
# --------------------------

def print_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

# print_triangle(5)

# --------------------------
# 13. PRACTICE EXERCISES
# --------------------------

"""
🧠 Challenge 1: Ask the user for two numbers and print the greater one.
🧠 Challenge 2: Count how many vowels are in a string.
🧠 Challenge 3: Write a function to check if a number is prime.
🧠 Challenge 4: Create a dictionary that stores subjects and marks, and calculate the average.
🧠 Challenge 5: Read a file and count how many lines it has.
"""

# ==========================
# MAIN EXECUTION POINT
# ==========================

if __name__ == "__main__":
    print("✅ Python tutorial module loaded. Uncomment function calls to run examples.")
