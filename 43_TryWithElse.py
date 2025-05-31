try:
    n = int(input("Enter a number :"))
    c = 1/n
    print(c)
except Exception as _:
    print("Zero division is not Possible")  
else:
    print("Division successful")      