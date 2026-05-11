import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

def result(df):
    strings = []
    for i in df.columns:
        if i != 'boar_id':
            strings.append(f"{i}: {df[i].mode()[0]}")
    return "\n".join(strings)

with open("all_mode.txt", "w") as f:
    f.write(result(df))