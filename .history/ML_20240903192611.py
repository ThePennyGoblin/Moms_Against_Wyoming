import pandas as pd
import numpy as np
import tensorflow as tf
import pandas as pd

# Load your DataFrames from CSV files
df1 = pd.read_csv('Batters2.csv')
df2 = pd.read_csv('Pitchers2.csv')
df3 = pd.read_csv('injury_report_combined_years_v4.csv')

# Step 1: Combine first and last names in the original format "Last, First"
df1['full_name'] = df1['last_name'] + ', ' + df1['first_name']
df2['full_name'] = df2['last_name'] + ', ' + df2['first_name']

# Step 2: Convert the "Last, First" format to "First Last"
df1['full_name'] = df1['full_name'].apply(lambda x: ' '.join(x.split(', ')[::-1]))
df2['full_name'] = df2['full_name'].apply(lambda x: ' '.join(x.split(', ')[::-1]))

# Drop the original name columns as they are now combined and formatted
df1 = df1.drop(columns=['first_name', 'last_name'])
df2 = df2.drop(columns=['first_name', 'last_name'])

# Step 3: Vertically combine the first two DataFrames
combined_df = pd.concat([df1, df2])

# Step 4: Horizontally join the combined DataFrame with the third DataFrame
final_df = pd.merge(combined_df, df3, on='year', how='left')

# Step 5: Remove rows with years between 2015 and 2019
final_df = final_df[~final_df['year'].between(2015, 2019)]

# Save the final combined DataFrame to a new CSV file
final_df.to_csv('combined_file.csv', index=False)

