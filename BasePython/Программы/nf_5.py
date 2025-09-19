# Реализация калькулятора

first_numbers = float(input())
second_numbers = float(input())
operation = input() # это будет применяемая операция к числам

if operation == "+":
    summa_numbers = first_numbers + second_numbers
    print(summa_numbers)

elif operation == "-":
    difference_numbers = first_numbers - second_numbers
    print(difference_numbers)

elif operation == '/':
    if second_numbers == 0:
        print("Деление на 0")
    else:
        result_division = first_numbers / second_numbers
        print(result_division)

elif operation == "mod":
    if second_numbers == 0:
        print("Деление на 0")
    else:
        result = first_numbers % second_numbers
        print(result)

elif operation == "div":
    if second_numbers == 0:
        print("Деление на 0")
    else:
        result = first_numbers // second_numbers
        print(result)

elif operation == "pow":
    result = first_numbers ** second_numbers
    print(operation)
else:
    print("Неизвестная операция")