try:
    n = int(input("Enter a number :"))
    c = 1/n
    print(c)
except Exception as _:
    print("Zero division is not Possible")  
    exit()
finally:
    print("W are done")  #Executed both times    
print("Thanks for using")   #if will not execute .what if an error occurs. 