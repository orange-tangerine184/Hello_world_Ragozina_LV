num = int(input("Введите количество чисел в массиве: "))
i = 1

if num <= 0:
    print("Не получится посчитать для отрицательного или нуля :(")
else:
    array = []
    i = 0
    print("Введите элементы массива:")
    while i < num:
        element = int(input(f"array[{i}] = "))
        array.append(element)
        i = i + 1
    sum_odd_i = 0
    i = 0
    
    while i < num:
        if i % 2 != 0:
            sum_odd_i = sum_odd_i + array[i]
        i = i + 1

print(f"Сумма равна: {sum_odd_i}")
