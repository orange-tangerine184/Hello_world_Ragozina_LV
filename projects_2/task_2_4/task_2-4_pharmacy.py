capsule_number = int(input("Введите общее количество произведённых капсул: "))
packing_capacity = int(input("Введите вместимость одной упаковки: "))

full_packing = capsule_number // packing_capacity
capsule_remains = capsule_number % packing_capacity

print("-"*3 + "Отчёт фасовочного цеха" + "-"*3)
print(f"Полных упаковок:{full_packing:>15}")
print(f"Остаток капсул:{capsule_remains:>15}")
