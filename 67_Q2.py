"""Define a Employee class with attributes role, department & salary. This c showDetails() method.
Create an Engineer class that inherits properties from Employee & F
attributes: name & age."""


class Emp:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetail(self):
        print("Role = ", self.role, "\nDept = ", self.dept, "\nSal = ", self.sal)


s = Emp("Accountant", "Finance", 60000)
s.showDetail()
