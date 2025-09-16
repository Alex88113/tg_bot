import logging

logging.basicConfig(
    level="DEBUG",
    filename="result_work_calculate.log",
    filemode='a',
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

def addition_numbers(numbers: int, numbers2: int, operations: str):
    logging.info(f"Вызван метод: {addition_numbers.__name__}")
    try:
        if not isinstance(numbers, (int, float)) and isinstance(numbers2, (int, float)):
            raise ValueError("Нужны числа")
    except Exception as e:
        logging.error("Ошибка содержится в:", e)
        print("Ошибка записана в файл -> result_work_calculate")

    if operations == '+':
        addition_values = numbers + numbers2 # исправил имя переменной с numbers на numbers2
        logging.info(f"Сумма двух операндов равна = {addition_values}")
        logging.info('---------------------------------')
        return "Результат записан в файл -> result_work_calculate.log"
    else:
         return "Неизвестная операция"

def subtractions_numbers(numbers: (int, float), numbers2: (int, float), operations: str):
    logging.info(f"Вызван метод: {subtractions_numbers.__name__}")
    # Проверка типа значений переменных (numbers, numbers2) на наличие чисел.
    try:
        if not isinstance(numbers, (int, float)) and isinstance(numbers2, (int, float)):
            raise ValueError("Нужны числа")
    except Exception as e:
        logging.error(e)

    # Блок кода отвечающий за проверку определённой операции, для ёё совершения.
    if operations == '-':
        difference_numbers = numbers - numbers2 # исправил имя переменной с numbers на numbers2
        logging.info(f"Разность числе равна = {float(difference_numbers)}")
        logging.info('---------------------------------')
        print("Разность двух операндов вычислена")
        return "Результат вычислений записан в файл -> result_work_calculate.log"
    else:
        return "Такой операции несуществует"

def multiplications_values(numbers: int, numbers2: (int, float), operations: str):
    logging.info(f"Вызван метод: {multiplications_values.__name__}")
    try:
        if not isinstance(numbers, (int, float)) and isinstance(numbers2, (int, float)):
            raise ValueError("Нужны числа")
    except Exception as e:
        logging.debug("Ой..Возникла ошибка!")
        logging.error(e)
        return "Ошибка записана в файл result_work_calculate.log"

    if operations == '*':
        compositions_numbers = numbers * numbers2
        logging.info(f"Произведение двух чисел равно = {compositions_numbers}")
        logging.info('---------------------------------')
        return "Вычисление завершено успешно!"
    else:
        return "Такой операции нет."


def division(numbers: (int, float), numbers2: (int, float), operation: str):
    logging.info(f"Вызван метод: {division.__name__}")
    try:
        # проверка типов
        if not isinstance(numbers, (int, float)) or not isinstance(numbers2, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")

        if operation == '/' or operation == '//':
            if numbers2 == 0:
                raise ZeroDivisionError("Делить на ноль нельзя")

            if operation == '/':
                result_division = numbers / numbers2
                logging.info(f"Результат обычного деления = {result_division}")
                logging.info('---------------------------------')
                return "Результат деления записан в файл -> result_work_calculate.log"
            else:
                result_division2 = numbers // numbers2
                logging.info(f"Результат целочисленного деления равен = {result_division2}")
                logging.info('---------------------------------')
                return "Результат деления записан в файл -> result_work_calculate.log"
        else:
            return 'Такой операции нет'

    except (ZeroDivisionError, TypeError, ValueError) as e:
        logging.error(f"Ошибка: {e}")
        return "Баг записан в файл |result_work_calculate|"
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {e}")
        logging.info('---------------------------------')
        return "Баг записан в файл |result_work_calculate|"
# возведение чисел в степень

def exponentiation(numbers: (int,float), numbers2: (int, float), operation: str):
    logging.info('---------------------------------')
    logging.info(f"Вызван метод: {exponentiation.__name__}")

    try:
        if not isinstance(numbers, (int, float)) or not isinstance(numbers2, (int, float)):
            logging.info('---------------------------------')
            raise ValueError("Значения должны быть числами")
    except TypeError as e:
        logging.info('---------------------------------')
        logging.debug(f"Ой..возник баг")
        logging.error(e)
        logging.info('---------------------------------')
        return 'Ошибка записана в файл result_work_calculate'

    if operation == '**':
        exponentiation_numbers1 = numbers ** 2
        exponentiation_numbers2 = numbers ** 2

        logging.info(f"Число: {numbers} в квадрате = {exponentiation_numbers1}")
        logging.info(f"Число: {numbers2} в квадрате = {exponentiation_numbers2}")
        return "Возведение успешно завершено"
    else:
        return "Такой операции нет"

result1 = addition_numbers(1, 34, '+')
result2 = subtractions_numbers(13.32, 1000.323, '-')
result3 = multiplications_values(232, 900, '*')
result4 = division(34, 0, '/')
result5 = exponentiation(8, 6, '**')

logging.info(result5)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
