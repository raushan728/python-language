def readFile(Filename):
    try:
        with open(Filename, "r") as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"file not fount {Filename}")


readFile("r.txt")
readFile("r2.txt")
readFile("r3.txt")
