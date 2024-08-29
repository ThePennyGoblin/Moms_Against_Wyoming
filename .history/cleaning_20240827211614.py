import pandas as pd

csv = pd.read_csv("Batting.csv")

df = pd.DataFrame(csv)

print(df.columns)
print(df["playerId"].value_counts())
print(df["Name"].value_counts())
