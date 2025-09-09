import asyncio

# Реализовать корутину которая будет:
# Выводить сообщение об запуске кофе машины и началом её работы
# Чтобы уведомляла о приготовленном кофе
# Сообщала  об завершении варки

async def making_coffe(times: int, status_coffee_machine=False):
    print("Запуск кофе машины...")
    await asyncio.sleep(times)
    status = status_coffee_machine == True
    print("Происходит приготовление кофе, пожалуйста подождите 2 секунды.")
    await asyncio.sleep(2)
    print("Ваш кофе готов, наслаждайтесь его потрясающим вкусом!")

async def result_making_coffee():
    result = await making_coffe(1)
    print("Варка завершена.")

asyncio.run(result_making_coffee())
# Создание этой корутины завершено.

