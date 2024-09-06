import pandas as pd

# Load the first CSV file
pitching_post_data = pd.read_csv('Moms_Against_Wyoming/(Copy) lahman_1871-2023_csv/lahman_1871-2023_csv/PitchingPost.csv')

# Fill missing values using .loc to avoid chained assignment
pitching_post_data.loc[:, 'BAOpp'] = pitching_post_data['BAOpp'].fillna(pitching_post_data['BAOpp'].mean())
pitching_post_data.loc[:, 'ERA'] = pitching_post_data['ERA'].fillna(pitching_post_data['ERA'].mean())
pitching_post_data.loc[:, 'IBB'] = pitching_post_data['IBB'].fillna(0)
pitching_post_data.loc[:, 'WP'] = pitching_post_data['WP'].fillna(0)
pitching_post_data.loc[:, 'HBP'] = pitching_post_data['HBP'].fillna(0)
pitching_post_data.loc[:, 'BK'] = pitching_post_data['BK'].fillna(0)
pitching_post_data.loc[:, 'BFP'] = pitching_post_data['BFP'].fillna(0)
pitching_post_data.loc[:, 'SH'] = pitching_post_data['SH'].fillna(0)
pitching_post_data.loc[:, 'SF'] = pitching_post_data['SF'].fillna(0)
pitching_post_data.loc[:, 'GIDP'] = pitching_post_data['GIDP'].fillna(0)

# For playerID, replace missing values with 'Unknown'
pitching_post_data.loc[:, 'playerID'] = pitching_post_data['playerID'].fillna('Unknown')

# Review cleaned data
print(pitching_post_data.info())
print(pitching_post_data.head())

# Save cleaned data to a new CSV file
pitching_post_data.to_csv('cleaned_pitching_post_data.csv', index=False)


# Load the CSV file
pitching_data = pd.read_csv('Moms_Against_Wyoming/(Copy) lahman_1871-2023_csv/lahman_1871-2023_csv/Pitching.csv')

# Fill missing values
pitching_data.loc[:, 'BAOpp'] = pitching_data['BAOpp'].fillna(pitching_data['BAOpp'].mean())
pitching_data.loc[:, 'ERA'] = pitching_data['ERA'].fillna(pitching_data['ERA'].mean())
pitching_data.loc[:, 'IBB'] = pitching_data['IBB'].fillna(0)
pitching_data.loc[:, 'WP'] = pitching_data['WP'].fillna(0)
pitching_data.loc[:, 'HBP'] = pitching_data['HBP'].fillna(0)
pitching_data.loc[:, 'BK'] = pitching_data['BK'].fillna(0)
pitching_data.loc[:, 'BFP'] = pitching_data['BFP'].fillna(0)
pitching_data.loc[:, 'SH'] = pitching_data['SH'].fillna(0)
pitching_data.loc[:, 'SF'] = pitching_data['SF'].fillna(0)
pitching_data.loc[:, 'GIDP'] = pitching_data['GIDP'].fillna(0)

# For playerID, replace missing values with 'Unknown'
pitching_data.loc[:, 'playerID'] = pitching_data['playerID'].fillna('Unknown')

# Review cleaned data
print(pitching_data.info())
print(pitching_data.head())

# Save cleaned data to a new CSV file
pitching_data.to_csv('cleaned_pitching_data.csv', index=False)


# Load the CSV file
pitch_data_2008 = pd.read_csv('Pitch Data - 2008.csv')

# Fill missing values
pitch_data_2008.loc[:, 'ba'] = pitch_data_2008['ba'].fillna(pitch_data_2008['ba'].mean())
pitch_data_2008.loc[:, 'iso'] = pitch_data_2008['iso'].fillna(pitch_data_2008['iso'].mean())
pitch_data_2008.loc[:, 'babip'] = pitch_data_2008['babip'].fillna(pitch_data_2008['babip'].mean())
pitch_data_2008.loc[:, 'slg'] = pitch_data_2008['slg'].fillna(pitch_data_2008['slg'].mean())
pitch_data_2008.loc[:, 'woba'] = pitch_data_2008['woba'].fillna(pitch_data_2008['woba'].mean())
pitch_data_2008.loc[:, 'bat_speed'] = pitch_data_2008['bat_speed'].fillna(pitch_data_2008['bat_speed'].mean())
pitch_data_2008.loc[:, 'swing_length'] = pitch_data_2008['swing_length'].fillna(pitch_data_2008['swing_length'].mean())

# For player_name, replace missing values with 'Unknown'
pitch_data_2008.loc[:, 'player_name'] = pitch_data_2008['player_name'].fillna('Unknown')

# Review cleaned data
print(pitch_data_2008.info())
print(pitch_data_2008.head())

# Save cleaned data to a new CSV file
pitch_data_2008.to_csv('cleaned_pitch_data_2008.csv', index=False)


# Load the CSV file
pitch_data_2020 = pd.read_csv('Pitch Data - 2020.csv')

# Fill missing values
pitch_data_2020.loc[:, 'ba'] = pitch_data_2020['ba'].fillna(pitch_data_2020['ba'].mean())
pitch_data_2020.loc[:, 'iso'] = pitch_data_2020['iso'].fillna(pitch_data_2020['iso'].mean())
pitch_data_2020.loc[:, 'babip'] = pitch_data_2020['babip'].fillna(pitch_data_2020['babip'].mean())
pitch_data_2020.loc[:, 'slg'] = pitch_data_2020['slg'].fillna(pitch_data_2020['slg'].mean())
pitch_data_2020.loc[:, 'woba'] = pitch_data_2020['woba'].fillna(pitch_data_2020['woba'].mean())
pitch_data_2020.loc[:, 'bat_speed'] = pitch_data_2020['bat_speed'].fillna(pitch_data_2020['bat_speed'].mean())
pitch_data_2020.loc[:, 'swing_length'] = pitch_data_2020['swing_length'].fillna(pitch_data_2020['swing_length'].mean())

# For player_name, replace missing values with 'Unknown'
pitch_data_2020.loc[:, 'player_name'] = pitch_data_2020['player_name'].fillna('Unknown')

# Review cleaned data
print(pitch_data_2020.info())
print(pitch_data_2020.head())

# Save cleaned data to a new CSV file
pitch_data_2020.to_csv('cleaned_pitch_data_2020.csv', index=False)

# MERGING

# Load the cleaned datasets
pitching_post_data = pd.read_csv('cleaned_pitching_post_data.csv')
pitching_data = pd.read_csv('cleaned_pitching_data.csv')
pitch_data_2008 = pd.read_csv('cleaned_pitch_data_2008.csv')
pitch_data_2020 = pd.read_csv('cleaned_pitch_data_2020.csv')

# Ensure the player_id in pitch_data_2008 and pitch_data_2020 are strings to match playerID
pitch_data_2008['player_id'] = pitch_data_2008['player_id'].astype(str)
pitch_data_2020['player_id'] = pitch_data_2020['player_id'].astype(str)
pitching_post_data['playerID'] = pitching_post_data['playerID'].astype(str)
pitching_data['playerID'] = pitching_data['playerID'].astype(str)

# Merge pitching_post_data and pitching_data based on playerID and yearID
merged_data = pd.merge(pitching_post_data, pitching_data, on=['playerID', 'yearID'], how='outer', suffixes=('_post', '_regular'))

# Merge the combined dataset with pitch_data_2008 on playerID and player_id (both as strings now)
merged_data = pd.merge(merged_data, pitch_data_2008, left_on='playerID', right_on='player_id', how='outer')

# Merge the result with pitch_data_2020 on playerID and player_id (both as strings now)
final_merged_data = pd.merge(merged_data, pitch_data_2020, left_on='playerID', right_on='player_id', how='outer')

# Inspect the final merged dataset
print(final_merged_data.info())
print(final_merged_data.head())

# Save the final merged dataset to a CSV file
final_merged_pitching_data = 'final_merged_pitching_data.csv'
final_merged_data.to_csv(final_merged_pitching_data, index=False)


# Load the final merged dataset
final_merged_data = pd.read_csv('final_merged_pitching_data.csv')

# Step 1: Drop rows with missing 'playerID' or 'yearID'
final_merged_data.dropna(subset=['playerID', 'yearID'], inplace=True)

# Step 2: Drop columns with more than 80% missing data
threshold = len(final_merged_data) * 0.8
final_merged_data.dropna(thresh=threshold, axis=1, inplace=True)

# Step 3: Fill missing values for numerical columns with the mean
final_merged_data.fillna(final_merged_data.mean(), inplace=True)

# Step 4: Save the cleaned dataset to a new CSV file
final_merged_data.to_csv('final_cleaned_pitching_data.csv', index=False)

# Review the cleaned data
print(final_merged_data.info())


