def ele(list, i=0):
    if i == len(list):
        return
    print(list[i])
    ele(list, i + 1)


raushan = ["mango", "banana", "apple"]
ele(raushan)