import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename='types_check.log', filemode='a', encoding='utf-8', format='%(asctime)s - %(levelname)s - %(message)s')

def chek_types_decorators(func):
    def wrapper(*args, **kwargs):
        try:
            logging.info(func(*args, **kwargs))
            return func(*args, **kwargs).upper().strip()
        except (TypeError, ValueError) as error:
            logger.debug(f"Ошибка возникшая в результате выполнения кода, содержится в -> {error}")
            return "Ошибка записанна в файл -> types_check.log"
        except Exception as error:
            logger.error(f"error: {error}")
            return None
        finally:
            print('проверка завершенна.')
    return wrapper

@chek_types_decorators
def my_func(word: str) -> str:
    return word
print(my_func('ijfjjiejj'))