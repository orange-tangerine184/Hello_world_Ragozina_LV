num = float(input("Введите количество чисел N: "))
i = 1

if num <= 0:
    print("Не получится посчитать для отрицательного или нуля :(")
else:
    sum = 0
    while i <= num:
        sum = sum + i ** 2
        i = i + 1

print(f"Сума квадратов {num} чисел равен {sum}")
