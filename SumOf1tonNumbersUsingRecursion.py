def sum(n):
    if n == 1:
        return 1
    return sum(n-1)+n


a = int(input("Enter a number :"))
print("Sum is", sum(a))