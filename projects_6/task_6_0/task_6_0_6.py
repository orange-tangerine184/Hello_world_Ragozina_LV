import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

def result(df):
    strings = []
    for gender, group in df.groupby('gender'):
        q1 = group['length_cm'].quantile(0.25)
        q3 = group['length_cm'].quantile(0.75)
        iqr = q3 - q1
        strings.append(f"{gender}:")
        strings.append(f"Q1 (25%): {q1:.2f} cm")
        strings.append(f"Q3 (75%): {q3:.2f} cm")
        strings.append(f"IQR: {iqr:.2f} cm\n")
    return "\n".join(strings)


with open("gender_iqr.txt", "w") as f:
    f.write(result(df))



