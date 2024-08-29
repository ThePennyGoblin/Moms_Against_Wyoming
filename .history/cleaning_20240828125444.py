import pandas as pd
# # pd.set_option("display.max_columns", None, "display.max_rows", None)
# csv = pd.read_csv("Batting.csv")

# df = pd.DataFrame(csv)

# # df = df[df["Season"] == 2016]
# # print(df.dtypes)
# # print(df.columns)
# print(df["playerId"].value_counts())
# print(df["Name"].value_counts())

# compare = df["playerId"].compare(df["Name"])
# # print(compare)
# # for x in range(2015,2024):
# #     df = df[df["Season"] == x]
# #     print(x)
#     # print(df["playerId"].value_counts())
#     # print(df["Name"].value_counts())

# # df["Name"].to_csv("names.csv")
# # df["playerId"].to_csv("playerId.csv")


import pandas as pd

# Load the entire CSV file into a DataFrame
file_path = 'Batting.csv'
df = pd.read_csv(file_path)

# Split the data into two sections based on assumed column names
# Adjust these column names and indices as necessary
df1 = df[['PlayerID1', 'PlayerName1']].dropna()
# df2 = df[['PlayerID2', 'PlayerName2']].dropna()

# Rename columns to unify them for comparison
df1.columns = ['PlayerID', 'PlayerName']
df2.columns = ['PlayerID', 'PlayerName']

# Convert DataFrames to dictionaries for easy lookup
dict1 = pd.Series(df1.PlayerName.values, index=df1.PlayerID).to_dict()
dict2 = pd.Series(df2.PlayerName.values, index=df2.PlayerID).to_dict()

# Find mismatches
mismatches = []

# Compare PlayerIDs and names
for player_id, name1 in dict1.items():
    name2 = dict2.get(player_id)
    if name2 and name1 != name2:
        mismatches.append((player_id, name1, name2))

# Output mismatches
if mismatches:
    print("Mismatches found:")
    for player_id, name1, name2 in mismatches:
        print(f"PlayerID: {player_id}, Name in Section 1: {name1}, Name in Section 2: {name2}")
else:
    print("No mismatches found.")
