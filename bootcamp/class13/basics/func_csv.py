import pandas as pd

def load_csv_and_filter(csv_file, state):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Check and remove empty cells
    df = df.dropna()
    
    # Filter rows by the 'state' column
    filtered_df = df[df['state'] == state]
    
    return filtered_df

csv_file = './example.csv'  # Replace with the path to your CSV file
filtered_state = 'SP'  # State you want to filter
filtered_df = load_csv_and_filter(csv_file, filtered_state)

print(filtered_df)