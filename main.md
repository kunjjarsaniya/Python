# 📘 Python Tutorial Guide

Welcome to this beginner-friendly Python tutorial repository! This guide complements the `main.py` script and is designed to help you understand the concepts through written explanations, examples, and exercises.

## 📂 Sections Overview

This guide breaks the tutorial into the following conceptual topics:

- ✅ [Variables & Data Types](#1-variables--data-types)
- ✅ [Strings & Input](#2-strings--input)
- ✅ [Arithmetic & Logical Operations](#3-arithmetic--logical-operations)
- ✅ [Conditional Statements](#4-conditional-statements)
- ✅ [Loops](#5-loops)
- ✅ [Functions](#6-functions)
- ✅ [Lists, Tuples, Sets, Dictionaries](#7-lists-tuples-sets-dictionaries)
- ✅ [File Handling](#8-file-handling)
- ✅ [Exception Handling](#9-exception-handling)
- ✅ [Advanced Python Concepts](#10-advanced-python-concepts)
- ✅ [Pattern Printing & Logic Exercises](#11-pattern-printing--logic-exercises)

---

## 1. Variables & Data Types

### 🧠 Concept

A variable is a name that refers to a value. In Python, you don’t need to declare the type of variable.

```python
age = 25            # Integer
price = 99.99       # Float
is_online = True    # Boolean
name = "Alice"      # String
```

### 🧪 Try It Yourself

* Declare a variable for your name and age.
* Print them using `print()` and `f-string` formatting.

---

## 2. Strings & Input

### 🧠 Concept

Use `input()` to receive input from the user, and use `f-strings` for formatting.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### 🧪 Try It Yourself

* Ask the user for their city and print a welcome message.

---

## 3. Arithmetic & Logical Operations

### 🧠 Concept

Basic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`

Logical operators: `and`, `or`, `not`

```python
print(3 + 5)          # 8
print(10 > 5 and 2 < 4)  # True
```

---

## 4. Conditional Statements

### 🧠 Concept

Use `if`, `elif`, and `else` to control the flow.

```python
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Too young to vote")
```

---

## 5. Loops

### 🧠 Concept

Use `for` or `while` to repeat actions.

```python
for i in range(5):
    print(i)
```

### 🧪 Try It Yourself

* Print numbers from 1 to 10.
* Print multiplication table of a given number.

---

## 6. Functions

### 🧠 Concept

Functions help reuse code.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

## 7. Lists, Tuples, Sets, Dictionaries

### Lists

```python
fruits = ["apple", "banana", "cherry"]
```

### Dictionary

```python
person = {"name": "Bob", "age": 30}
```

---

## 8. File Handling

```python
with open("example.txt", "w") as f:
    f.write("Hello, file!")
```

### 🧪 Try It Yourself

* Create a file and write your name into it.

---

## 9. Exception Handling

```python
try:
    a = int(input("Enter number: "))
    result = 10 / a
except ZeroDivisionError:
    print("❌ Cannot divide by zero")
```

---

## 10. Advanced Python Concepts

* Lambda functions
* Decorators
* Dictionary & List comprehensions
* `map()`, `filter()`

---

## 11. Pattern Printing & Logic Exercises

```python
for i in range(1, 6):
    print("* " * i)
```

### 🔁 Practice Problems

* Check if a number is prime
* Reverse a string without using slicing
* Count vowels in a string

---

## ✅ Conclusion

This guide gives you a strong foundation in Python. Explore the `main.py` file to see full working examples.

Happy coding! 🚀
