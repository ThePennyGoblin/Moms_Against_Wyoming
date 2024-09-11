import pandas as pd

# Load the CSV files
batters_df = pd.read_csv('Batters2.csv')
pitchers_df = pd.read_csv('Pitchers2.csv')
injury_report_df = pd.read_csv('injury_report_combined_years_v4.csv')

# Function to reformat 'last_name, first_name' to 'First Last'
def reformat_name(name):
    if pd.isna(name):
        return ''
    last_first = name.split(", ")
    if len(last_first) == 2:
        return f"{last_first[1]} {last_first[0]}"
    return name

# Apply the reformatting function to the 'last_name, first_name' columns in batters and pitchers data
batters_df['Name'] = batters_df['last_name, first_name'].apply(reformat_name)
pitchers_df['Name'] = pitchers_df['last_name, first_name'].apply(reformat_name)

# Drop the original 'last_name, first_name' columns since the 'Name' column will be used for merging
batters_df.drop(columns=['last_name, first_name'], inplace=True)
pitchers_df.drop(columns=['last_name, first_name'], inplace=True)

# Filter batters and pitchers data to include only records from 2020 and later
batters_df_filtered = batters_df[batters_df['year'] >= 2020]
pitchers_df_filtered = pitchers_df[pitchers_df['year'] >= 2020]

# Combine the filtered batters and pitchers dataframes vertically
combined_filtered_df = pd.concat([batters_df_filtered, pitchers_df_filtered], ignore_index=True)

# Merge the filtered combined dataframe with the injury report on the 'Name' column
merged_filtered_df = pd.merge(combined_filtered_df, injury_report_df, on='Name', how='left')

# Save or display the merged filtered DataFrame
merged_filtered_df.to_csv('.csv', index=False)




