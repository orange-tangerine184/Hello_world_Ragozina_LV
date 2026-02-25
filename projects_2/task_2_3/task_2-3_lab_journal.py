full_name = input("Введите своё ФИО: ")
data_number = input("Введите дату обращения: ")
experiment_name = input("Введите название проведённого эксперимента: ")
result_name = input("Ведите вывод своей работы: ")
border = "+" + "-"*60 + "+\n"
width = 60


with open("journal.txt", "w", encoding="utf-8") as file:
    file.write(border)
    file.write(f'|{f"Электронный лабораторный журнал":^{width}}|\n')
    file.write(border)
    file.write(f'|{f"ФИО исследователя: {full_name}":<{width}}|\n')
    file.write(f'|{f"Дата: {data_number}":<{width}}|\n')
    file.write(f'|{f"Эксперимент: {experiment_name}":<{width}}|\n')
    file.write(border)
    file.write(f'|{"Вывод:":<{width}}|\n')
    
    for i in range(0, len(result_name), width):
        file.write(f'|{result_name[i:i+width]:<{width}}|\n')
    file.write(border)

