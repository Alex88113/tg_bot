def decorator(func):# в скобах это параметр или аргумент функции?
    def wrapper(): # почему именно wrapper?
        print("This is my first decorator!")
        func()
        print("End.")
    return wrapper # Это для чего?

def say_whee():
    print("Hi bro!")

result_func = decorator(say_whee)
result_func()