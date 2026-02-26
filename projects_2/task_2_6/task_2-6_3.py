donor_type = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient_type = input("Введите фенотип группы крови репициента (I, II, III, IV): ").strip().upper()


if donor_type == recipient_type:
    print("Переливание крови возможно, так как группы совпадают")
elif donor_type == "I":
    print("Поереливание крови возможно, так как она относится к нулевой (I)")
else:
    print("Переливание крови невозможно")

