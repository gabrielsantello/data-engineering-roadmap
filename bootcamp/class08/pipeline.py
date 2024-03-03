from etl import etl_function

folder_argument: str = 'data'
format_output: list = ["csv", "parquet"]

etl_function(folder_argument, format_output)