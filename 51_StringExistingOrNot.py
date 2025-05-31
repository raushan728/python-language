def cheak():
    with open("raushan.txt","r") as f:
      data = f.read()
    if "Rahul" in data:
      print("Found")
    else:
         print("Not found")

cheak() 