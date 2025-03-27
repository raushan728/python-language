"""Create a class called Order which stores item & its price.
Use Dunder function_gt__() to convey that:
order1 > order2 if price of order1 > price of order2"""


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, price):
        return self.price > o2.price


o1 = Order("chips", 20)
o2 = Order("Tea", 15)
print(o1 > o2)
