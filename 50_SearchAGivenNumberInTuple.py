n = int(input("Enter your number :"))
raushan =(1,2,3,4,5,6,7,8,9)
i=0
while i<len(raushan):
    if raushan[i]== n:
        print("found at index :",i)
        break
    i+=1 
else:
        print("not found")