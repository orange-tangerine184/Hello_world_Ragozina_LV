import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'wild_boars.csv'))

all_length = df['tusk_length_cm']
max_length = df['tusk_length_cm'].max()
min_length = df['tusk_length_cm'].min()

with open("tusk_length.txt", "w") as f:
    f.write(all_length.to_string())
    f.write(f"\nМаксимальная длина равна {max_length}")
    f.write(f"\nМинимальная длина равна {min_length}")
