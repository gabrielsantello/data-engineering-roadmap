import pandas as pd
import os
import glob

#Extract and merge jsons
def extract_data_and_merge(folder: str) -> pd.DataFrame:
    files_json = glob.glob(os.path.join(folder, '*.json')) #list of json files in the folder
    df_list = [pd.read_json(file) for file in files_json] #list of read json files - content of the files
    df_total = pd.concat(df_list, ignore_index=True) #merged files
    return df_total

#Test in-file
if __name__ == '__main__':
    folder_argument = 'data'
    print(extract_data_and_merge(folder=folder_argument))