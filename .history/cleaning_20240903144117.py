import pandas as pd
# pd.set_option("display.max_columns", None, "display.max_rows", None)
csv1 = pd.read_csv("data/Batting.csv")
csv2 = pd.read_csv("data/Pitching.csv")

df = pd.DataFrame(csv1)

drop_names = ["Austin Adams","Carlos Perez","Chris Young","Daniel Robertson","Javy Guerra","Luis Garcia","Matt Duffy","Will Smith"]

print(df.columns)

for x in range()



