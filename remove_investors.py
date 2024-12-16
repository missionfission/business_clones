import pandas as pd

# Read the CSV file
df = pd.read_csv('2023-02-27-yc-companies.csv')
print("Column names:", df.columns.tolist())

# Drop the 'Select Investors' column
df = df.drop('long_description', axis=1)

# Save the modified dataframe to a new CSV file
df.to_csv('yc-companies.csv', index=False) 