import pandas as pd
import numpy as np
import tensorflow as tf

Bat = pd.read_csv("Batters2.csv")
Pit = pd.read_csv("Pitchers2.csv")
inj = pd.read_csv("injury_report_combined_years_v4.csv")

print(Bat.columns,Pit.columns,inj.columns)