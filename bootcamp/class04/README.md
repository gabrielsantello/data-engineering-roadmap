# Python Basics: Type Hints, Complex Types, File Reading, and Functions

## Introduction
This README provides an overview of essential Python concepts related to type hints, complex data types (such as dictionaries, DataFrames, tables, and Excel), file reading (including the `with` statement), and functions. Whether you're a beginner or an experienced developer, understanding these concepts is crucial for writing efficient and maintainable Python code.

## Table of Contents
1. [Type Hints](#type-hints)
2. [Complex Data Types](#complex-data-types)
3. [File Reading](#file-reading)
4. [Functions](#functions)

---

## 1. Type Hints
Type hints allow you to annotate function parameters and return values with their expected data types. Although Python is dynamically typed, type hints improve code readability and help catch potential errors early.

Example:
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## 2. Complex Data Types
### - Dictionaries
Dictionaries are key-value pairs, where each value is associated with a unique key. They are useful for organizing and retrieving data efficiently.

### - DataFrames (Pandas)
DataFrames are two-dimensional, tabular data structures provided by the Pandas library. They resemble tables and allow data manipulation and analysis.

### - Tables (SQL)
Tables are structured data representations used in SQL databases. They store data in rows and columns, making them suitable for querying and joining data.

### - Excel Spreadsheets
Python can read and write data from Excel spreadsheets using libraries like Pandas or openpyxl.

## 3. File Reading (including the `with` statement)
Python provides various methods to read data from files, such as `open()`, `read()`, and `readlines()`. The `with` statement ensures proper resource management and automatically closes the file when done.

Example:
```python
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
```

## 4. Functions (including 3 examples)
Functions are reusable blocks of code that perform specific tasks. They improve code organization and maintainability.

### Example 1: Adding Two Numbers
```python
def add(a: int, b: int) -> int:
    return a + b

result = add(5, 3)
print(f"Sum: {result}")
```

### Example 2: Greeting Function
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))
```

### Example 3: Checking Even or Odd
```python
def check_even_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(7))
print(check_even_odd(12))
```

---

Happy coding! 🚀🐍

Source:
(1) Python Functions (With Examples) - Programiz. https://www.programiz.com/python-programming/function.
(2) Python Functions – How to Define and Call a Function - freeCodeCamp.org. https://www.freecodecamp.org/news/python-functions-define-and-call-a-function/.
(3) 16 Python Functions Exercises and Examples – Pythonista Planet. https://pythonistaplanet.com/python-functions-examples/.
(4) Functions - Learn Python - Free Interactive Python Tutorial. https://www.learnpython.org/en/Functions.
(5) Python Functions - W3Schools. https://www.w3schools.com/python/python_functions.asp.
(6) Reading and Writing Files in Python (Guide) – Real Python. https://realpython.com/read-write-files-python/.
(7) Python File Open - W3Schools. https://www.w3schools.com/python/python_file_open.asp.
(8) Python File Operation (With Examples) - Programiz. https://www.programiz.com/python-programming/file-operation.
(9) File Reading and Writing Using Python: Easy Examples. https://codeblockhub.com/python/python-file-reading-writing/.
(10) How to read from a file in Python - GeeksforGeeks. https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/.
(11) Python Examples | Programiz. https://www.programiz.com/python-programming/examples.
(12) 7 Python Function Examples with Parameters, Return and Data Types. https://www.thegeekstuff.com/2019/06/python-function-examples/.
(13) Python Reading and Writing Files (With Examples). https://machinelearningtutorials.org/python-reading-and-writing-files-with-examples/.
(14) Reading Files with Python - Stack Abuse. https://stackabuse.com/reading-files-with-python/.