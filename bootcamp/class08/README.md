# Python ETL with Pandas, JSON, and Parquet

This README provides an overview of essential concepts related to ETL (Extract, Transform, Load) processes using Python. We'll cover the following topics:

1. **ETL with Pandas, JSON, and Parquet**: Learn how to extract data from JSON files, transform it using Pandas, and save the results in Parquet format.

2. **Loguru: A Logging Library for Python**: Explore the benefits of using Loguru, a powerful and user-friendly logging library that simplifies the logging setup process.

3. **Decorators with Loguru**: Discover how decorators can enhance your logging experience when combined with Loguru.

4. **Pydantic**: A data validation and parsing library for Python. It simplifies data validation and serialization/deserialization.

5. **Pandera**: A lightweight data validation library that works well with Pandas DataFrames.

## Table of Contents
1. [ETL with Pandas, JSON, and Parquet](#etl-with-pandas-json-and-parquet)
2. [Loguru: A Logging Solution](#loguru-a-logging-solution)
3. [Benefits of Using Decorators with Loguru](#benefits-of-using-decorators-with-loguru)
4. [Data Validation with Pydantic](#data-validation-with-pydantic)
5. [Data Validation with Pandera](#data-validation-with-pandera)

---

## 1. ETL with Pandas, JSON, and Parquet
- **Pandas**: A popular Python library for data analysis. It provides flexible data structures like DataFrames, making data manipulation and transformation easier.
- **JSON**: A common data format for exchanging structured information. We'll extract data from JSON files.
- **Parquet**: A columnar storage format that offers efficient compression and encoding. We'll save our transformed data in Parquet files.

## 2. Loguru: A Logging Solution
- **Loguru**: A third-party logging framework for Python. It simplifies logging setup and provides useful features.
- Easy to configure and use compared to the default Python logging module.
- Pre-configured handlers for logging to standard error or custom destinations.
- Rich log formatting options.

## 3. Benefits of Using Decorators with Loguru
- **Decorators**: Python functions that modify the behavior of other functions or methods.
- When combined with Loguru, decorators can enhance error tracebacks and provide better insights during debugging.
- Use decorators to catch exceptions, time function execution, or customize log messages.

## 4. Data Validation with Pydantic
- **Pydantic**: A powerful library for data validation and parsing. It allows you to define data models with type hints and validation rules. Use Pydantic to validate input data, serialize/deserialize JSON, and ensure data consistency.

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

## 5. Data Validation with Pandera
- **Pandera**: A lightweight data validation library that integrates well with Pandas DataFrames. It allows you to define schema rules for your data and validate DataFrame columns.

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

Happy coding! 🚀🐍

Source:
(1) How to convert a JSON result to Parquet in python?. https://stackoverflow.com/questions/59141776/how-to-convert-a-json-result-to-parquet-in-python.
(2) Converting JSON Data to Parquet using Python and Pandas. https://towardsdev.com/converting-json-data-to-parquet-using-python-and-pandas-62ba634f6dce.
(3) Transforming JSON to Parquet in Python | by Turkel | Medium. https://medium.com/@turkelturk/tjson-to-parquet-in-python-a3d2a6abc5c6.
(4) Transform json files in directory in parquet files with python & pandas .... https://stackoverflow.com/questions/74811876/transform-json-files-in-directory-in-parquet-files-with-python-pandas.
(5) Building an ETL Pipeline in Python | Integrate.io. https://www.integrate.io/blog/building-an-etl-pipeline-in-python/.
(6) A Complete Guide to Logging in Python with Loguru. https://betterstack.com/community/guides/logging/loguru/.
(7) Python logging with Loguru - Dan Zimmer. https://danzimmer.net/blog/python-logging-with-loguru/.
(8) Python Loguru: A Simple and Efficient Logging Tool - Medium. https://medium.com/@tubelwj/python-loguru-a-simple-and-efficient-logging-tool-21ce925771e5.
(9) python - How to use loguru with standard loggers? - Stack Overflow. https://stackoverflow.com/questions/66769431/how-to-use-loguru-with-standard-loggers.
(10) Create an ETL pipeline in Python with Pandas in 10 minutes. https://towardsdev.com/create-an-etl-pipeline-in-python-with-pandas-in-10-minutes-6be436483ec9.
(11) Aprenda Etl com Python: Guia Completo para Se Tornar um Especialista Em .... https://awari.com.br/aprenda-etl-com-python-guia-completo-para-se-tornar-um-especialista-em-extracao-transformacao-e-carga-de-dados/.
(12) Converter o JSON em Pandas DataFrame | Delft Stack. https://www.delftstack.com/pt/howto/python-pandas/json-to-pandas-dataframe/.
(13) Implementando o processo ETL com Python - Datapeaker. https://datapeaker.com/pt/big--data/proceso-etl-implementacion-del-proceso-etl-con-python/.