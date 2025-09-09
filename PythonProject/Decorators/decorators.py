import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    filename="result_work_my_processing_decorators",
    filemode='a',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def processing_decorator(my_func):
    def wrapper(*args, **kwargs):
        print("Начало")
        advertisement_func = my_func(*args, **kwargs)
        processing_value_func = advertisement_func.lower().strip().title()
        print("Обработка завершена.")
        print("Обработанные данные сохранены в файле - 'result_work_my_processing_decorator'")
        logging.info(f"Обработанные {processing_value_func}")
        return processing_value_func
    return wrapper

@processing_decorator
def user_data(name: str, surname: str, city: str):
    users_data = dict(name=name, surname=surname, city=city)
    logging.info(f"Данные без обработки -> {users_data}")
    return f"Пользовательские данные {users_data}"

print(user_data("Shura", 'KuCheryavyh', 'SevASTOPOL'))