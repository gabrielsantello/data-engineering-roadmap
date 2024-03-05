# Python Functions and Data Structures Guide

This README provides an overview of essential concepts related to Python functions and data structures. We'll cover the following topics:

1. **Functions in Python**: Learn about defining and using functions, which are reusable blocks of code that perform specific tasks.
2. **Data Structures**: Explore different data structures available in Python, such as lists, dictionaries, tuples, and sets. These structures allow you to organize and manipulate data efficiently.

## Table of Contents
1. [Functions in Python](#functions-in-python)
2. [Common Data Structures](#common-data-structures)

---

## 1. Functions in Python
- **Functions**: In Python, functions are named blocks of code that can be called with specific arguments. They allow you to encapsulate logic, improve code readability, and promote code reusability.

Example:
```python
def greet(name):
    """Print a personalized greeting."""
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```

## 2. Common Data Structures
- **Lists**: Ordered collections of items. Lists can hold elements of different data types and are mutable (modifiable).

Example:
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # Access the first element
fruits.append("grape")  # Add a new fruit
```

- **Dictionaries**: Key-value pairs where keys are unique. Useful for mapping data.

Example:
```python
person = {"name": "Alice", "age": 30}
print(person["name"])  # Access value by key
person["city"] = "New York"  # Add a new key-value pair
```

- **Tuples**: Similar to lists but immutable (cannot be modified after creation).

Example:
```python
coordinates = (10, 20)
print(coordinates[0])  # Access the first value
```

- **Sets**: Unordered collections of unique elements. Useful for removing duplicates.

Example:
```python
colors = {"red", "green", "blue"}
colors.add("yellow")  # Add a new color
```

Happy coding! 🚀🐍

Source: Conversation with Bing, 05/03/2024
(1) A Complete Guide to Logging in Python with Loguru. https://betterstack.com/community/guides/logging/loguru/.
(2) Python logging with Loguru - Dan Zimmer. https://danzimmer.net/blog/python-logging-with-loguru/.
(3) Python Loguru: A Simple and Efficient Logging Tool - Medium. https://medium.com/@tubelwj/python-loguru-a-simple-and-efficient-logging-tool-21ce925771e5.
(4) python - How to use loguru with standard loggers? - Stack Overflow. https://stackoverflow.com/questions/66769431/how-to-use-loguru-with-standard-loggers.
(5) Using Loguru to Prettify Your Python Logs | Pipeline: Your Data .... https://medium.com/pipeline-a-data-engineering-resource/prettify-your-python-logs-with-loguru-a7630ef48d87.
(6) 5. Data Structures — Python 3.12.2 documentation. https://docs.python.org/3/tutorial/datastructures.html.
(7) Data Structures – Real Python. https://realpython.com/tutorials/data-structures/.
(8) Data Structures in Python | List, Tuple, Dict, Sets, Stack, Queue - Edureka. https://www.edureka.co/blog/data-structures-in-python/.
(9) Common Python Data Structures (Guide) – Real Python. https://realpython.com/python-data-structures/.
(10) Python Data Structures - GeeksforGeeks. https://www.geeksforgeeks.org/python-data-structures/.
(11) pandera · PyPI. https://pypi.org/project/pandera/.
(12) Data Validation Made Easy with Pandera Python: A Comprehensive Guide. https://datashark.academy/data-validation-made-easy-with-pandera-python-a-comprehensive-guide/.
(13) Validating Pandas Data with Pandera and Type Hints. https://medium.com/@yuxuzi/validating-pandas-data-with-pandera-and-type-hints-dd46c16fce12.
(14) GitHub - unionai-oss/pandera: A light-weight, flexible, and expressive .... https://github.com/unionai-oss/pandera.
(15) undefined. https://pandera.readthedocs.io.