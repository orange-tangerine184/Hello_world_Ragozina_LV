import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

def result(df):
    strings = []
    for i in df.columns:
        if i != 'boar_id' and i != 'gender':
            strings.append(f"{i}: {df[i].median():.2f}")
    return "\n".join(strings)

with open("all_median.txt", "w", encoding="utf-8") as f:
    f.write(result(df))