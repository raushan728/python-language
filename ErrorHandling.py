a = int(input("Enter any two number :"))
b = int(input())
try:
    print(a/b)
except Exception as e:
    print(f"{e} is not posibile")    