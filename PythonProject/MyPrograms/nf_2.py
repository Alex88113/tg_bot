import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="result_work_func.log",
    filemode="w",
    format="%(asctime)s -%(levelname)s -%(message)s",
    encoding="utf-8"
)

def my_decorator(func):
    async def wrapper(*args, **kwargs):
        print("Инициализация")
        await asyncio.sleep(2)
        
        try:
            if kwargs and 'name' in kwargs:
                processed_name = kwargs['name'].lower().strip().capitalize()
                kwargs["name"] = processed_name
                
            elif args:
                processed_name = args[0].lower().strip().capitalize() if args else ''
                args = (processed_name, ) + args[1:]
                
            else:
                 processed_name = 'hui'
        
            logging.info("Обработанное имя: {}".format(processed_name))
        
            result = await func(*args, **kwargs)
            
            print("Работа завершена.")
            return result
    
        except (TypeError, ValueError) as e:
            error_msg = f"errors: {e}" 
            logging.error(error_msg)
            print(error_msg)
            return None
        
        finally:
            print("Конец!")
    return wrapper

@my_decorator
async def greeting_func(name: str):
    await asyncio.sleep(1)
    print("Первая задача запущена")
    return "Hi {}".format(name)

@my_decorator
async def greeting_friend(name_friend: str):
    print("Вторая задача запущена")
    return "Hello {}".format(name_friend)

async def main():
    results = await asyncio.gather(
        greeting_func("Shura"),
        greeting_friend("Tomy")
    )

asyncio.run(main())
