print("=== Анализ последовательности ДНК ===\n")

dna_input = input("Введите последовательность ДНК: ").strip()
dna_upper = dna_input.upper()

print(f"\nПоследовательность в верхнем регистре: {dna_upper}")

count_a = dna_upper.count('A')
count_t = dna_upper.count('T')
count_g = dna_upper.count('G')
count_c = dna_upper.count('C')
total_length = len(dna_upper)

percent_a = (count_a / total_length) * 100
percent_t = (count_t / total_length) * 100
percent_g = (count_g / total_length) * 100
percent_c = (count_c / total_length) * 100

print(f"Подсчёт нуклеотидов:\nA: {count_a}\nT: {count_t}\nG: {count_g}\nC: {count_c}\n")
print(f"Процент содержания нуклеотидов:\nA: {percent_a:.2f}\nT: {percent_t:.2f}\nG: {percent_g:.2f}\nC: {percent_c:.2f}\n")
print(f"Общая длина: {total_length} нуклеотидов")

