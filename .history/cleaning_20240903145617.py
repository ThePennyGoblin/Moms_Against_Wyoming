import pandas as pd
pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("data/Batting.csv")
csv2 = pd.read_csv("data/Pitching.csv")

df = pd.DataFrame(csv1)
years = [2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
# print(df.dtypes)



for year in years:
    df = df[df["Season"] == year]
    print(year)
    print(df)




