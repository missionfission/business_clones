import pandas as pd

# Read the CSV file
df = pd.read_csv('CB-Insights_Global-Unicorn-Club_2024.csv')
print("Column names:", df.columns.tolist())

# Drop the 'Select Investors' column
df = df.drop('Select Investors', axis=1)

# Save the modified dataframe to a new CSV file
df.to_csv('CB-Insights_Global-Unicorn-Club_2024_no_investors.csv', index=False) 