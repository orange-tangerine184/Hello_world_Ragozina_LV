weight = float(input("Введите Ваш вес (кг): "))
height_cm = float(input("Введите Ваш рост (см): "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)
print("-"*3 + "Отчёт о состоянии здоровья" + "-"*3)
print(f"Рост:\t\t{height_cm} см\nВес:\t\t{weight} кг")
print(f"Индекс массы тела пациента: {bmi:.2f}")
