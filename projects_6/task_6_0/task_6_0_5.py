import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

def result(df):
    strings = []
    for i in df.columns:
        if i != 'boar_id' and i != 'gender' and i != 'weight_kg':
            strings.append(f"{i}:")
            strings.append(f"Percentile 25 (Q1):\t{df[i].quantile(0.25):.1f}")
            strings.append(f"Median 50 (Q2):\t\t{df[i].quantile(0.50):.1f}")
            strings.append(f"Percentile 75 (Q3):\t{df[i].quantile(0.75):.1f}")
            strings.append(f"Percentile 90:\t\t{df[i].quantile(0.90):.1f}")
            strings.append(f"Percentile 95:\t\t{df[i].quantile(0.95):.1f}")
            strings.append(f"Max:\t\t\t\t{df[i].quantile(1.00):.1f}")
            strings.append("\n")
    return "\n".join(strings)

with open("all_quantile.txt", "w", encoding="utf-8") as f:
    f.write(result(df))