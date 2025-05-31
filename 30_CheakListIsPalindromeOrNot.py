n =int(input("enter your any three numbers one by one :"))
n2 =int(input())
n3 = int(input())
total = [n,n2,n3]
copy_list = total.copy()
total.reverse()
if(total==copy_list):
    print("Your list is a palindrome")
else:
    print("Your list is not a palidrome")