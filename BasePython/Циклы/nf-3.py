numbers = [1, 3, 4, 6, 4, 8, 6, 8]
counter = len(numbers) -1

while counter >= 0:
    if numbers[counter] % 2 == 0:
        numbers.pop(counter)
    counter -= 1
print(numbers)

numbers = [1, 2, 3, 5, 6, 7, 4, 8, 4]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
    else:
        i += 1 # Увеличивает индекс для перехода к следующему элементу
print(' '.join(map(str, numbers)))  # 1 3 5 7

data = input().split() # Разделение двух чисел при вводе
number_of_participants = int(data[0])
multiplicity = int(data[1])

list_winners = [] # Список победителей

i = 1

while i <= number_of_participants:
    if i % multiplicity == 0: # Моя ошибка была в том, что я прочекивал общее кол - во участников, а не каждого.
        list_winners.append(i)
    i += 1

print(f"Список победителей с номерами -> |{list_winners}|")
