import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

def result(df):
    strings = []
    for i in df.columns:
        if i != 'boar_id' and i != 'gender':
            strings.append(f"{i}:")
            strings.append(f"Variance is {df[i].var():.2f}")
            strings.append(f"Standart deviation is {df[i].std():.2f}")
            cv = (df[i].std() / df[i].mean()) * 100
            strings.append(f"Coefficient of variation is {cv:.2f} %\n")
    return "\n".join(strings)

with open("all_cv.txt", "w", encoding="utf-8") as f:
    f.write(result(df))
    