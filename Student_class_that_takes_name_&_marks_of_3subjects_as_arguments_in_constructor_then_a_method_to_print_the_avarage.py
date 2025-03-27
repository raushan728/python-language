class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getavg(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print("Hi", self.name, "your avarage score is:", avg)


s = Student("Rausha Singh", (90, 98, 99))
s2 = Student("Rahul kumar", [67, 98, 45])
s2.getavg()
