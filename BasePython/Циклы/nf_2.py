count = 1

while count != 12:
    if count == 3:
        print(f"Шаг №{count} был пропущен")
        count += 1
        continue
    print(f"шаг стирки №{count}")
    count += 1
else:
    print("Работа цикла завершена")

# Первое задание
count = 0

while count !=5:
    count += 1
    print(count, end=' ')
else:
    print("\nКонец")

i = 20

while i > 0:
    if i % 2 == 0:
        print(i, end=' ')
    i -= 1

while True:
    message = input()
    processing_user_text = message.strip().lower().capitalize()
    if "Как меня зовут?" in processing_user_text:
        print("Вас зовут Александр")

    if message == 'exit':
        break
    else:
        print(message)
print("Работа окончена")