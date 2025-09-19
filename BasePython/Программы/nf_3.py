first_number = int(input())
last_number = int(input())

if first_number % last_number == 0:
    print("Число:", first_number, 'чётное')
    print("first number:", first_number, "|", "last number:", last_number)
    print("Тип:", type(first_number), "|", type(last_number))

elif (first_number % 2 == 0) or last_number % 2 == 0:
    print("Во втором условии число чётные")
    print("Число переменной (first_number):", first_number)
    print("Значение переменной (last_number):", last_number)

elif not first_number % 2 == 0 and not last_number % 2 == 0:
    print("Чётных чисел нет.")
else:
    print("Чётных чисел не обнаружено")