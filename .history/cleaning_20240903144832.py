import pandas as pd
# pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("data/Batting.csv")
csv2 = pd.read_csv("data/Pitching.csv")

df = pd.DataFrame(csv1)

print(df.dtypes)

print(range(2015))

for year in range(2016,2023):
    df = df[df["Season"] == year]
    print(year)
    print(df)




