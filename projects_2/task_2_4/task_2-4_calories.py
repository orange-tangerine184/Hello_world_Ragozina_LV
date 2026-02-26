protein_mass = int(input("Введите массу белков в продукте (г): "))
fat_mass = int(input("Введите массу жиров в продукте (г): "))
carb_mass = int(input("Введите массу углеводов в продукте (г): "))

calories_result = protein_mass * 4 + fat_mass * 9 + carb_mass * 4
print(f"Общая калорийность равна: {calories_result} ккал.")
