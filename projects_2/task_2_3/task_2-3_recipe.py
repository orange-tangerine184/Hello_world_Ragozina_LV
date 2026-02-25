medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара: ")
temperature_sterilisation = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\n{agar_concentration}\n{temperature_sterilisation}")

print("Файл 'recipe.txt' успешно сформирован!")
