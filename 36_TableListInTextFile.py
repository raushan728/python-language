while True:
    print("Enter q to exit")
    n = input("Enter a number :")
    if n == "q":
        exit()
    int(n)
    t = [n * i for i in range(1, 11)]
    with open("raushan.txt", "a") as f:
        f.write(str(t))
        f.write("\n")
