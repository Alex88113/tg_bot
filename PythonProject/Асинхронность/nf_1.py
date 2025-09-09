import asyncio # импортируемый модуль


async def count(): # async - определяет асинхронную функцию
    print("One")
    await asyncio.sleep(1) # await - приостанавливает выполнение работы кода на 1 секунду, а asyncio.sleep() возращает управление циклу обработки событий, после 1 секунды.
    print("Two")
    await asyncio.sleep(1)
    print("Three")

async def main(): # Запуск корутин. P.S: корутина это запускаемые объекты.
    await asyncio.gather(count()) # gather - благодару ему можно запускать несколько асинхронных функций одновременно.

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Время выполнения этой асинхронной функции заняло: {elapsed:0.2f} секунды.")


asyncio.run(main()) # запускает выполнение все корутин из функции main().
