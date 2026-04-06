num = int(input("Введите натуральное число: "))
i = 1
factorial = 1

if num < 0:
    print("Не получится посчитать для отрицательного :(")
else:
    while i <= num:
        factorial *= i
        i = i + 1

print(f"Факториал {num}! = {factorial}")
