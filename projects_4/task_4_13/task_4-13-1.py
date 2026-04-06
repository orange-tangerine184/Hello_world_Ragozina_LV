num_A = float(input("Введите 1 число: "))
num_B = float(input("Введите 2 число: "))
num_C = float(input("Введите 3 число: "))
num_D = float(input("Введите 4 число: "))

min = num_A

if num_B < min:
    min = num_B
if num_C < min:
    min = num_C
if num_D < min:
    min = num_D

print(f"Минимально значение: {min}")
