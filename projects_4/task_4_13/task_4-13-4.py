num = int(input("Введите натуральное число: "))
i = 1
sum = 0

if num <= 0:
    print("Не получится посчитать для отрицательного :(")
else:
    while i <= num:
        sum += i
        i = i + 1

print(f"Факториал {num}! = {sum}")
