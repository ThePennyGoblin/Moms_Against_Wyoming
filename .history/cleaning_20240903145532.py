import pandas as pd
pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("data/Batting.csv")
csv2 = pd.read_csv("data/Pitching.csv")

df = pd.DataFrame(csv1)
years = [2015,2016,2017,2018,20]
# print(df.dtypes)








