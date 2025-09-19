#number = int(input("Введите первое число > "))
#number2 = int(input("Введите второе число > "))

#if int(number) >= int(number2):
   # print("Число", int(number), 'больше или равно', int(number2))
#else:
  #  print(number, 'меньше чем', number2)

#age = int(input("Сколько вам лет?: "))
#name = input("Как тебя зовут? > ")

#if 16 <= int(age) <= 18 and name == "Shura":
    #print("Возраст подходит, имя тоже")
#else:
    #print("Одна из переменных имеет неверные значения")

#number = int(input("Введите первое число > "))
#number2 = int(input("Введите второе число > "))

#if int(number) % 2 == 0 and int(number2) % 2 == 0:
 #   print("Числа чётные")
#else:
 #   print("Одно или оба числа являются нечётными")


#day_of_the_week = input("Какой следующий день недели?: ")
#if day_of_the_week == "Воскресенье":
 #   print("Сегодня выходной, в колледж идти на пары не нужно")
#elif (day_of_the_week == "Понедельник") or day_of_the_week == "Вторник":
 #   print("Придётся собираться на занятия")
#else:
 #   print("В колледж идти сегодня не требуется")


min_hours = int(input())
max_hours = int(input())
quantity_hours_sleep = int(input())

if min_hours <= quantity_hours_sleep < max_hours:
    print("Это нормально")
elif quantity_hours_sleep < A:
    print("Недосып")
else:
    print("Пересып")
