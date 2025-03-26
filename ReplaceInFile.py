with open("raushan.txt", "r") as f:
    data = f.read()
    new = data.replace("Raushan", "Rahul")
with open("raushan.txt", "w") as f:
    f.write(new)
    print(new)
