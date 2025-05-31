def fac(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    print("Factriol is ", f)


n = int(input("Enter a number :"))
fac(n)