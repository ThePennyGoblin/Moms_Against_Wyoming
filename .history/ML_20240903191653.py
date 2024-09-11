import pandas as pd
import numpy as np
import tensorflow as tf

Bat = pd.read_csv("Batters2.csv")
Pit = pd.read_csv("Pitchers2.csv")
inj = pd.read_csv("injury_report_combined_years_v4.csv")

# Assuming you have loaded your DataFrames from CSV files

# Step 1: Vertically combine the first two DataFrames
combined_df = pd.concat([df1, df2])

# Step 2: Horizontally join the combined DataFrame with the third DataFrame
# Merging on 'year' column, you can adjust if you have another key
final_df = pd.merge(combined_df, df3, on='year', how='left')

# Save the final combined DataFrame to a new CSV file
final_df.to_csv('combined_file.csv', index=False)
