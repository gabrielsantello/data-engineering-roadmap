# Python Tools and Libraries Guide

This README provides an overview of essential Python tools and libraries. We'll cover the following topics:

1. **Decorators**: A powerful feature in Python that allows you to modify or enhance functions and methods dynamically.
2. **Loguru Logger**: A user-friendly logging library for Python that simplifies logging setup and provides rich formatting options.
3. **Pandera**: A lightweight data validation library that integrates well with Pandas DataFrames.
4. **Pydantic**: A versatile library for data validation, parsing, and serialization/deserialization.

## Table of Contents
1. [Decorators](#decorators)
2. [Loguru Logger](#loguru-logger)
3. [Data Validation with Pandera](#data-validation-with-pandera)
4. [Data Validation with Pydantic](#data-validation-with-pydantic)

---

## 1. Decorators
- **Decorators**: Python functions that modify the behavior of other functions or methods.
- Use decorators to add functionality to existing functions, such as logging, timing, or authentication checks.

Example:
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 2. Loguru Logger
- **Loguru**: A third-party logging framework for Python.
- Simplifies logging setup and provides useful features.
- Easy to configure and use compared to the default Python logging module.

Example:
```python
from loguru import logger

logger.info("This is an info message.")
logger.error("An error occurred: %s", "Something went wrong")
```

## 3. Data Validation with Pandera
- **Pandera**: A lightweight data validation library that works well with Pandas DataFrames.
- Define schema rules for your data and validate DataFrame columns.

Example:
```python
import pandas as pd
import pandera as pa

schema = pa.DataFrameSchema({
    "name": pa.Column(pa.String),
    "age": pa.Column(pa.Int, checks=pa.Check.greater_than(0)),
})

data = pd.DataFrame({"name": ["Alice", "Bob"], "age": [25, -10]})
validated_data = schema.validate(data)
print(validated_data)
```

## 4. Data Validation with Pydantic
- **Pydantic**: A powerful library for data validation and parsing.
- Define data models with type hints and validation rules.
- Use Pydantic for input validation, serialization/deserialization, and more.

Example:
```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str

user_data = {"username": "john_doe", "email": "john@example.com"}
user = User(**user_data)
print(user)
```

Happy coding! 🚀🐍

Source:
(1) . https://www.athenapaas.com/documentation/blueprint/blueprint-logging.html.
(2) . https://cuthbertsonlaird.ie/power-loggers/183-fluke-1736-three-phase-power-logger.html.
(3) . http://www.ei5di.com/sdscreen.html.
(4) . https://www.pinterest.ie/pin/oscar-the-grouch-no-carve-pumpkin--331225747573013846/.
(5) . https://cuthbertsonlaird.ie/power-loggers/571-fluke-1734-three-phase-electrical-energy-logger.html.
(6) . https://rshydro.ie/mx1101-pr-855.html.
(7) Support for pydantic attribute validation · Issue #408 · Delgan/loguru. https://github.com/Delgan/loguru/issues/408.
(8) Implementing Log Decorators in Python | by Hima Mahajan - Medium. https://medium.com/swlh/add-log-decorators-to-your-python-project-84094f832181.
(9) Validation Decorator - Pydantic. https://docs.pydantic.dev/latest/concepts/validation_decorator/.
(10) GitHub - Delgan/loguru: Python logging made (stupidly) simple. https://github.com/Delgan/loguru.