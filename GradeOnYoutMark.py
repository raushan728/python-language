mark = int(input("Enter your marks :"))
if(mark>=90):
    print("your grade : A")
elif(mark >=80 and mark <90):
    print("your grade : B")
elif(mark>=70 and mark <80):
    print("your grade : C")
elif(mark >=60 and mark<70):
    print("your grade is : D")
elif(mark>=33 and mark< 60):
    print("your are pass")
else:
    print("you are fail,plese try again")
