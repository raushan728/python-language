a = 54  # Global variable


def fun1():
    global a
    print(f"statement 1 : {a}")  # output 54
    a = 8  # local variable
    print(f"statement 2 : {a}")  # output 8


fun1()
print(f"statement 3 : {a}")  # output 8
