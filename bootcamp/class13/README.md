# Data Processing and Scheduling Project

This project includes several Python scripts for data processing and scheduling tasks. The main components of the project are described below.

## CsvProcessor

The `CsvProcessor` class is used to load and filter data from a CSV file. It includes methods to load a CSV file into a pandas DataFrame and filter the DataFrame based on specified columns and attributes.

## AbstractDataSource

The `AbstractDataSource` class is an abstract base class that defines the interface for a data source. It includes abstract methods for starting the data source, getting data, transforming data to a DataFrame, and saving data.

## CsvSource, JsonSource, and TxtSource

These classes inherit from `AbstractDataSource` and implement the abstract methods for CSV, JSON, and TXT data sources, respectively.

## Scheduling

The script uses the `schedule` library to periodically check for new files in the data sources. The `check_for_new_files` function is scheduled to run every 10 seconds.

## Data Consolidation

The script consolidates data from CSV and TXT files located in specified folders. It initializes an empty DataFrame and appends data from each file to the DataFrame.

## Usage

To use the `CsvProcessor` class, create an instance and call the `load_csv` method to load a CSV file. Then, call the `filter_by` method to filter the DataFrame.

To use the scheduling functionality, create instances of `CsvSource`, `JsonSource`, and `TxtSource`, and run the main loop with `schedule.run_pending()`.

To consolidate data, specify the paths to the CSV and TXT folders and run the script. The consolidated DataFrame will be printed to the console.