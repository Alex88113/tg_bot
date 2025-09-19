# Первая задача
"""
Вычислить площадь треугольника по теореме Герона
На вход программе подаются три целых числа, результатом вычислений должно быть вещественное число.
"""

first_side = int(input())
second_side = int(input())
last_side = int(input())

if first_side + second_side > last_side and first_side + last_side > second_side and second_side + last_side > first_side:
    p = (first_side + second_side + last_side) / 2
    result = round((p * (p - first_side) * (p - second_side) * (p * last_side)) ** 0.5, 2)
    print("Результат:", result)
else:
    print("Такого треугольника нет.")


number = int(input())
if (-15 < number <= 12) or (14 < number <= 17) or (number >= 19):
    print(True)
else:
    print(False)

