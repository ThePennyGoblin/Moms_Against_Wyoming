import pandas as pd
# pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("data/Batting.csv")
csv2 = pd.read_csv("data/Pitching.csv")

df = pd.DataFrame(csv1)

for x in range(0,9):
    year = 2015
    df = df[df["Season"] == year + x]
    print(df)



