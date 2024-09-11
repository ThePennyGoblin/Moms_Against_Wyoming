import pandas as pd
import numpy as np
import tensorflow as tf

Bat = pd.read_csv("Batters2.csv")
Pit = pd.read_csv("Pitchers2.csv")
inj = pd.read_csv("injury_report_combined_years_v4.csv")

import pandas as pd

# Load your DataFrames from CSV files
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')

# Step 1: Vertically combine the first two DataFrames
combined_df = pd.concat([df1, df2])

# Step 2: Horizontally join the combined DataFrame with the third DataFrame
final_df = pd.merge(combined_df, df3, on='year', how='left')

# Step 3: Remove rows with years between 2015 and 2019
final_df = final_df[~final_df['year'].between(2015, 2019)]

# Save the final combined DataFrame to a new CSV file
final_df.to_csv('combined_file.csv', index=False)

