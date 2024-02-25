import csv

# Path to the CSV file
file_path = 'example.csv'

# Initializes an empty list to store the data
data = []

# Uses the context manager `with` to open the file
with open(file_path, mode='r', encoding='utf-8') as file:
    # Creates a CSV reader object
    csv_reader = csv.DictReader(file)
    
    # Iterates over the lines of the CSV file
    for line in csv_reader:
        # Adds each line (a dictionary) to the data list
        data.append(line)

# Displays the data read from the CSV file
for record in data:
    print(record)