from interface.classes.csv_class import CsvProcessor
# import pandas as pd

csv_file = './example.csv'
filter_column = 'state'
limit_value = 'SP'

csv_processor = CsvProcessor(csv_file)
csv_processor.load_csv()  # Load the CSV
print(csv_processor.filter_by(['state', 'price'], ['SP', '10.50']))
# print(csv_processor.df)
print("#########################")
# csv_file2 = './example2.csv'
# filter_column2 = 'state'  # Changed to filter_column2
# limit_value2 = 'DF'

# csv_processor2 = CsvProcessor(csv_file2)
# csv_processor2.load_csv()  # Load the CSV
# print(csv_processor2.filter_by(filter_column2, limit_value2))  # Changed to filter_column2
# print(csv_processor2.sub_filter('price', '10.50'))