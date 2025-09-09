import asyncio

def check_types_data(func):
    async def wrapper(my_hobby: str, age: int):
        try:
            await asyncio.sleep(1)
            if not isinstance(my_hobby, str):
                raise ValueError("Неподходящий тип данных.")
            if not isinstance(age, int):
                raise ValueError("Должна быть строка")
            processing_hobby = my_hobby.strip().lower().capitalize()
            print(f"Your is hobby -> {processing_hobby}, and you are {age} old")

            result = await func(my_hobby, age)
            return result

        except (TypeError, NameError) as e:
            print(f"errors in {e}")

        finally:
            print("Конец!")
    return wrapper

@check_types_data
async def my_data(my_hobby: str, age: int) -> str:
    await asyncio.sleep(1)
    return f"My hobby is {my_hobby} and me is {age} old."

async def test_coroutine():
    try:
        result = await my_data("PROGRAMMING", 19)
        print(f"final result: {result}")
    except Exception as b:
        print("error in -> ", b)

asyncio.run(test_coroutine())


