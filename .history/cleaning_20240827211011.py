import pandas as pd

csv = pd.read_csv("Batting.csv")

df = pd.DataFrame(csv)

print(df)
