reagent_name = input("Введите имя нового прибора: ")
reagent_number = input("Введите его количество (не полтора землекопа....): ")

f = open("inventory.txt", "w", encoding="utf-8")
print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_number} штук", file=f)
f.close()
