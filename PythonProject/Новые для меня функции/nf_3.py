from loguru import logger

logger.add(
"final_result.log",
    level="INFO",
    format="<yellow>{time:HH::mm::ss}</yellow> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
)
logger.info("Скрипт запущен")

def user_data(name: str, surname: str, password: int):
    try:
        if not isinstance(name, str) and not isinstance(surname, str):
            raise ValueError("Требуются строки")
        elif name == '' or surname == '':
            raise ValueError("Строки не должны быть пусты")
        if not isinstance(password, int):
            raise ValueError("Пароль должен состоять только из цифр")

        processing_name = name.strip().lower().capitalize()
        processing_surname = surname.lower().strip().capitalize()

        dict_data = dict(name=processing_name, surname_user=processing_surname, your_password=password)
        logger.info("Обработанные пользовательские данные")
        logger.info('=================================================')
        logger.info(dict_data)
        logger.debug("Никаких проблем в процессе выполнения не обнаружено")
        print("Запись данных успешно завершена!")
        logger.info('=================================================')
        return dict_data

    except Exception as e:
        logger.error(f"Ошибка содержится в: {e}")

    return None

result = user_data("shura", 'kucheryayh', 372376)
print(result)

logger.info("Работа завершена")