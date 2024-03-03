import pandas as pd
import os
import glob

#Extract and merge jsons
def extract_data_and_merge(folder: str) -> pd.DataFrame:
    files_json = glob.glob(os.path.join(folder, '*.json')) #list of json files in the folder
    df_list = [pd.read_json(file) for file in files_json] #list of read json files - content of the files
    df_total = pd.concat(df_list, ignore_index=True) #merged files
    return df_total

#Transform
def transform_kpi(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantity'] * df['Sale']
    return df

#Save csv/parquet - this is a "Procedure" because we are saving and not returning something from the function
def load_data(df: pd.DataFrame, format_output: list):
    """
    parameter which choses if it's going to be "csv" or "parquet" or "both"
    """
    for format in format_output:
        if format == 'csv':
            df.to_csv("data.csv", index=False)
        if format == 'parquet':
            df.to_parquet("data.parquet", index=False)


def etl_function(folder_argument: str, format_output: list): #basically it is the test __name__ == __main__ in a function to be called somewhere (pipeline.py)
    data_frame = extract_data_and_merge(folder=folder_argument)
    data_frame_calculated = transform_kpi(data_frame)
    load_data(data_frame_calculated, format_output) #create files csv and parquet