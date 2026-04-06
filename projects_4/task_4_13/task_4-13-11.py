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
    sum_even_i = 0
    count_even = 0
    i = 0
    
    while i < num:
        if i % 2 == 0:
            sum_even_i = sum_even_i + array[i]
            count_even = count_even + 1
        i = i + 1

average = sum_even_i / count_even

print(f"Среднее значение: {average}")
