import pandas as pd
# pd.set_option("display.max_columns", None, "display.max_rows", None)
csv = pd.read_csv("Batting.csv")

df = pd.DataFrame(csv)

drop_ls = ["Austin Adams","Carlos Perez","Chris Young","Daniel Robertson","Javy Guerra","Luis Garcia","Matt Duffy","Will Smith"]

drop = df[df["Name"]  drop_ls]

df.drop(drop, axis = "index", inplace=True)

# df = df[df["Season"] == 2016]
# print(df.dtypes)
# print(df.columns)
print(df["playerId"].value_counts())
print(df["Name"].value_counts())

compare = df["playerId"].compare(df["Name"])
# print(compare)
# for x in range(2015,2024):
#     df = df[df["Season"] == x]
#     print(x)
    # print(df["playerId"].value_counts())
    # print(df["Name"].value_counts())

# df["Name"].to_csv("names.csv")
# df["playerId"].to_csv("playerId.csv")




