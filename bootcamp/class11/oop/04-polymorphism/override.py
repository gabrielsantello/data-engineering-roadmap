import pandas as pd

class ETLProcess:
    def __init__(self, data_source):
        self.data_source = data_source

    def extract_data(self):
        raise NotImplementedError("The extract_data method must be implemented in child classes.")

    def transform_data(self, data):
        raise NotImplementedError("The transform_data method must be implemented in child classes.")

    def load_data(self, transformed_data):
        raise NotImplementedError("The load_data method must be implemented in child classes.")

    def execute_etl(self):
        extracted_data = self.extract_data()
        transformed_data = self.transform_data(extracted_data)
        self.load_data(transformed_data)


class ETLCSV(ETLProcess):
    def extract_data(self):
        return pd.read_csv(self.data_source)

    def transform_data(self, data):
        # Simple transformation example: convert all letters to uppercase
        return data.applymap(lambda x: x.upper() if isinstance(x, str) else x)

    def load_data(self, transformed_data):
        # Here you can implement logic to load the transformed data from a CSV file
        print("Transformed data (CSV):")
        print(transformed_data)


class ETLExcel(ETLProcess):
    def extract_data(self):
        return pd.read_excel(self.data_source)

    def transform_data(self, data):
        # Simple transformation example: convert all letters to lowercase
        return data.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    def load_data(self, transformed_data):
        # Here you can implement logic to load the transformed data from an Excel file
        print("Transformed data (Excel):")
        print(transformed_data)


# Example usage
if __name__ == "__main__":
    csv_source = 'data.csv'  # Replace 'data.csv' with the path to your CSV file
    etl_csv = ETLCSV(csv_source)
    etl_csv.execute_etl()

    excel_source = 'data.xlsx'  # Replace 'data.xlsx' with the path to your Excel file
    etl_excel = ETLExcel(excel_source)
    etl_excel.execute_etl()