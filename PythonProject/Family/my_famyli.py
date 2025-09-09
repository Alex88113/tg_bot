import logging
from abc import ABC, abstractmethod
from typing import Dict

logging.basicConfig(
    level=logging.INFO,
    filename="my_family.log",
    filemode='w',
    format="%(asctime)s -%(levelname)s -%(message)s",
    encoding="utf-8"
)

error_logger = logging.getLogger("error_log")
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler("error.log", encoding="utf-8")
error_logger.addHandler(error_handler)

def log_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Инициализация декоратора логирования...")
        logging.info("----Вызов метода----")
        logging.info(f"Метод: {func.__name__}")
        logging.info(f"Класс: {func.__class__.__name__}")

        try:
            logging.info(f"Dad: {getattr(self, "_dad", "не найден")}")
            logging.info(f"Mother: {getattr(self,  '_mother',  'не найдена')}")
            logging.info(f"First brother: {getattr(self, '_first brother', 'не найден')}")
            logging.info(f"Second brother: {getattr(self, '_second brother')}")

            logging.info(f"Last brother: {getattr(self, '_last brother', 'не найден')}")
            logging.info(f"Sister: {getattr(self, '_sister', 'имя не существует')}")
            logging.info("===================")

        except Exception as e:
            logging.error(f"errors: {e}")
            return {}

        result = func(self, *args, **kwargs)
        logging.info("Запись завершенна.")
        return result
    return wrapper

class Family(ABC):
    def __init__(self, dad: str, mother: str, first_brother: str, second_brother: str, last_brother: str, sister: str):
        self._dad = dad
        self._mother = mother
        self._first_brother = first_brother
        self._second_brother = second_brother
        self._last_brother = last_brother
        self._sister = sister

    @log_decorator
    def _log_info_my_family(self):
        logging.info("====Производится запись членов семьи====")
        logging.info(f'dad: {self._dad}')
        logging.info(f"mother: {self._mother}")
        logging.info(f"first brother: {self._first_brother}")
        logging.info(f"second brother: {self._second_brother}")
        logging.info(f"last_brother: {self._last_brother}")
        logging.info(f"sister: {self._sister}")
        logging.info("Запись завершенна.")

    @abstractmethod
    def processing_names_my_family(self) -> Dict[str, str]:
        pass

class PersonMyFamily(Family):
    @log_decorator
    def processing_names_my_family(self) -> Dict[str, str]:
        try:
            list_names_family = {
                "dad": self._dad,
                "mother": self._mother,
                "first_brother": self._first_brother,
                "second_brother": self._second_brother,
                "last_brother": self._last_brother,
                "sister": self._sister
            }

            processed_names_family = {}
            for role, name in list_names_family.items():
                processed_name = name.lower().strip().title()
                processed_names_family[role] = processed_name
                logging.info(f"{role}: {processed_name}")
            return processed_names_family
        except Exception as e:
            error_bags = f"Возникла ошибка: {e}"
            error_logger.error(error_bags)
            logging.error(error_bags)
            return {}

def test_methods():
    try:
        family = PersonMyFamily(
            " andrei",
            "tatyana ",
            "deNIs",
            "Sasha",
            " KeriLL",
            "Nastya"
        )

        family._log_info_my_family()
        processed_names_family = family.processing_names_my_family()

        if processed_names_family:
            for role, name in processed_names_family.items():
                print(f"{role}: {name}")
        else:
            print("Не удалось обработать имена")
        return processed_names_family


    except Exception as e:
        error_logger.error("Ошибка была найдена в test_methods: {}".format(e))
        return None

if __name__ == "__main__":
    test_methods()

