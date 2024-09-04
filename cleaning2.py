import pandas as pd

# Load your dataset
combined_bpi_df_new = pd.read_csv('CombinedBPI.csv')

# Define a function to clean names by removing special characters and extra spaces
def clean_name(name):
    if pd.isna(name):
        return ''
    # Remove special characters and extra spaces
    name = name.strip()
    name = name.replace(".", "")  # Remove periods
    name = " ".join(name.split())  # Ensure only single spaces between words
    return name

# Apply the cleaning function to the 'Name' column
combined_bpi_df_new['Name'] = combined_bpi_df_new['Name'].apply(clean_name)

# Define a function to standardize common name issues (e.g., capitalization, suffixes like Jr., III)
def standardize_name(name):
    parts = name.split()
    if len(parts) > 1 and parts[-1] in {'Jr', 'III', 'II', 'IV'}:
        # Handle suffixes like Jr., III properly
        base_name = " ".join(parts[:-1])
        suffix = parts[-1]
        return f"{base_name.title()} {suffix}"
    return name.title()

# Apply the standardization function to the 'Name' column
combined_bpi_df_new['Name'] = combined_bpi_df_new['Name'].apply(standardize_name)

# Save the cleaned and standardized dataset
combined_bpi_df_new.to_csv('Cleaned_CombinedBPI.csv', index=False)
