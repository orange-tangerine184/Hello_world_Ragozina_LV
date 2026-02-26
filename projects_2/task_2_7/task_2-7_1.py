files = ["seq1", "seq2", "seq3", "seq4"]

sample_date = "20.02.2026"

print("=== Добавление даты взятия образца ===\n")
print(f"Дата: {sample_date}\n")

for name in files:
    new_name = f"{name}_{sample_date}.fasta"
    print(new_name)

