num_1 = float(input("Введите, сколько чисел будем сравнивать: "))

if num_1 <= 0:
    print("Не получится посчитать для отрицательного или нуля :(")
else:
    max_num = float(input("Введите число 1: "))
    i = 2  
    while i <= num_1:
        num_2 = float(input(f"Введите число {i}: "))
        if max_num < num_2:
            max_num = num_2
        i = i + 1
    
    print(f"Максимальное число {max_num}")
