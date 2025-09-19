mystring = 'hello'
myfloat = 10.0
myint = 20

if mystring == 'helle':
    print("String: %s" % mystring)
else:
    print("Такого значения в переменной с именем", mystring.__name__)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
else:
    print("Одно из условий не выполнено")
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
else:
    print("Неверные значения")