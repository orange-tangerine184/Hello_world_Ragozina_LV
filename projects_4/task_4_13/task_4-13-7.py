num = int(input("Введите количество чисел в массиве: "))

if num <= 0:
    print("Не получится посчитать для отрицательного или нуля :(")
else:
    array = []
    i = 0
    while i < num:
        element = float(input(f"array[{i}] = "))
        array.append(element)
        i = i + 1

sum = 0
i = 0
while i < num:
    sum = sum + array[i]
    i = i + 1

average = sum / num

print(f"Среднее значение {average}")
