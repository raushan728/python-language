# a  =[1,2,3,4,5,6,7,8,9,2,4,535,4,67,87,899]
# b = []
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)        


a = [1,2,3,4,5,6,7,8,9,2,4,535,4,67,87,899]
b = [i for i in a if i%2==0]
print(b)


#same output