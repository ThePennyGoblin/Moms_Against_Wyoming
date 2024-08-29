import pandas as pd

csv = pd.read_csv("Batting.csv")

df = pd.DataFrame(csv)


# print(df.dtypes)
print(df.columns)
print(df["playerId"].value_counts())
print(df["Name"].value_counts())

for x in range(2015):
    df = df[df["Season"] == x]

    print(df["playerId"].value_counts())
    print(df["Name"].value_counts())