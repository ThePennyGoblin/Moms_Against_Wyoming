import pandas as pd
pd.set_option("display.max_columns", None, "display.max_rows", None)
csv = pd.read_csv("Batting.csv")

df = pd.DataFrame(csv)

# df = df[df["Season"] == 2018]
# print(df.dtypes)
# print(df.columns)
# print(df["playerId"].value_counts())
# print(df["Name"].value_counts())

compare = df["playerId"].compare(df["Name"])
print(compare)
# for x in range(2015,2024):
#     df = df[df["Season"] == x]
#     print(x)
#     print(df["playerId"].value_counts())
#     print(df["Name"].value_counts())