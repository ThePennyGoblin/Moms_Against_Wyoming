import pandas as pd
import unidecode

df = pd.read_csv("hold/")

def reformat_name(name):
    name = unidecode.unidecode(name)
    if pd.isna(name):
        return ''
    last_first = name.split(", ")
    if len(last_first) == 2:
        return f"{last_first[1]} {last_first[0]}"
    return name