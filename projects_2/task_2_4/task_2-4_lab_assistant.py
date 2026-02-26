volume = int(input("Введите нужный объём раствора (мл): "))

salt_mass = volume * 0.009 
mass_rounded = round(salt_mass, 2)
water_volume = volume

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write("-"*20)
    file.write(f"\nОбщий объём: {volume} мл\n")
    file.write(f"Масса соли: {mass_rounded} г\n")
    file.write(f"Объём воды: {water_volume} мл\n")

