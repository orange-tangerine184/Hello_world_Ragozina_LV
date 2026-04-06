num = int(input("Введите количество чисел в массиве: "))
i = 1

if num <= 0:
    print("Не получится посчитать для отрицательного или нуля :(")
else:
    array = []
    i = 0
    print("Введите элементы массива:")
    for i in range(num):
        element = float(input(f"array[{i}] = "))
        array.append(element)
    
    count = 0
    for element in array:
        if element > 0:
            count = count + 1

print(f"Количество положительных чисел: {count}")
