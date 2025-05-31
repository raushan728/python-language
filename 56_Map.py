def square(n):
    return n * n


l = [1, 2, 3]
# Method 1
l2 = []
for i in l:
    l2.append(square(i))
print(l2)
# Method 2
print(list(map(square, l)))
