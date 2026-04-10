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
    sum_odd = 0
    i = 0
    
    while i < num:
        if array[i] % 2 != 0:
            sum_odd = sum_odd + array[i]
        i = i + 1

print(f"Сумма равна: {sum_odd}")
