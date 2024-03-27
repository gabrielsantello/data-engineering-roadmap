import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.filtered_df = None

    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df  # Return the DataFrame after loading

    def filter_by(self, columns, attributes):
        if len(columns) != len(attributes):
            raise ValueError("Number of columns and attributes must be the same")
        
        if len(columns) == 0:
            return self.df
        
        current_column = columns[0]
        current_attribute = attributes[0]

        filtered_df = self.df[self.df[current_column] == current_attribute]

        if len(columns) == 1:
            return filtered_df
        else:
            return self.filter_by(columns[1:], attributes[1:])