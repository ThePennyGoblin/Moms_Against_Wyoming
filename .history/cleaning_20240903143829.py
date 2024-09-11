import pandas as pd
# pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("dataBatting.csv")
csv2 = pd.read_csv("Pitching.csv")

df = pd.DataFrame(csv1)

drop_names = ["Austin Adams","Carlos Perez","Chris Young","Daniel Robertson","Javy Guerra","Luis Garcia","Matt Duffy","Will Smith"]

print(df.value_counts())

# df = df[df["Season"] == 2016]
# print(df.dtypes)
# # print(df.columns)
# print(df["playerId"].value_counts())
# print(df["Name"].value_counts())

# for x in range(2015,2024):
#     df = df[df["Season"] == x]
#     print(x)
    # print(df["playerId"].value_counts())
    # print(df["Name"].value_counts())

# df["Name"].to_csv("names.csv")
# df["playerId"].to_csv("playerId.csv")




