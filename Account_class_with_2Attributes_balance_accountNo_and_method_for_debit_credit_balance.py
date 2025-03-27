class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was dibited\n Available balance = ", self.aviable())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited\n Available balance = ", self.aviable())

    def aviable(self):
        return self.balance


s1 = Account(100000, 7367932477)
s1.debit(300)