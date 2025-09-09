import functools

def decorator(func):
    @functools.wraps(func) # Почему пишется сперва этот декоратор перед написание обёртки?
    def wrapper_decorator(*args, **kwargs):
        print("Начало работы декоратора")
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator

@decorator
def greeting_user(name: str) -> str:
    return f"Hi {name}, where are you from?"

print(greeting_user("Shura"))

def processing_func(my_func):
    @functools.wraps(my_func)
    def wrapper(*args, **kwargs):
        print(f"Начало вызова метода: {my_func.__name__}")
        function_declaration = my_func(*args, **kwargs)
        processing_letters = function_declaration.lower().strip()
        return processing_letters
    return wrapper

@processing_func
def text_func(text: str) -> str:
    return f"this is my text -> {text}"
print(text_func('go go go!!!'))

@processing_func
def my_email(email: str):
    return f"Your is email adress: {email}"
print(my_email('sdhwdhWKJDW@MGME.COM'))