import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

def result(df):
    strings = []
    for gender, group in df.groupby('gender'):
            var = group['tusk_length_cm'].var()
            std = group['tusk_length_cm'].std()
            strings.append(f"{gender}:")
            strings.append(f"Variance is {var:.2f}")
            strings.append(f"Standart deviation is {std:.2f}")
            mean = group['tusk_length_cm'].mean()
            cv = (std / mean) * 100
            strings.append(f"Coefficient of variation is {cv:.2f} %\n")
    return "\n".join(strings)

with open("all_cv_gender.txt", "w") as f:
    f.write(result(df))
