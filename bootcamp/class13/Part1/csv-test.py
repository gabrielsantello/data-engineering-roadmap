import pandas as pd

# Load the first CSV file
df = pd.read_csv('./example.csv')

# Filter by 'state' column with value 'SP'
df_filtered = df[df['state'] == 'SP']

# Filter by 'price' column with value '10.50'
df_filtered = df[df['price'] == '10.50']

print(df_filtered)

print("#########################")

# Load the second CSV file
df2 = pd.read_csv('./example2.csv')

# Filter by 'state' column with value 'DF'
df_filtered2 = df2[df2['state'] == 'DF']

# Filter by 'price' column with value '10.50'
df_filtered2 = df2[df2['price'] == '10.50']

print(df_filtered2)