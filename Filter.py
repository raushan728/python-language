def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False


g = lambda x: x > 10
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 65, 5, 76, 3, 3, 56, 657, 7, 7, 878]
print(list(filter(greater_than_5, l)))
print(list(filter(g, l)))
