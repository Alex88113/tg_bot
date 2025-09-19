# Первое задание
numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(2, 25)
numbers.extend([60, 70])

print(numbers)

# Второе на удаление элементов
fruits = ["apple", "banana", "cherry", "banana", "date"]
fruits.remove("banana")
element_fruits_list = fruits.pop(0)
fruits.pop(-1)
print(f"Итоговый список: {fruits}\nУдалил: {element_fruits_list}")

# Третье задание
shopping_list = []
products = input("Введите три продукта через запятую -> ").split(',')
shopping_list.extend(products)
shopping_list.pop(1)
shopping_list.insert(0, "молоко")
print(f"Итоговый список -> {shopping_list}")

# Четвертый квест
grades = [4, 5, 3, 4, 2, 5]
grades.remove(2)
grades.extend([5, 5])
removed_grade = grades.pop(0)
average_score = sum(grades) / len(grades)
result = average_score
print(f"Финальный список: {grades}\nСредняя оценка = {float(result)}")
print(f"Удалил |{removed_grade}| ")

