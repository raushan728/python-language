#@staticmethod - No need to create an object!

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # 8


#@classmethod -  When we need to modify class-level attributes.

class Employee:
    company = "Google"  # Class variable

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company  # Modifying class attribute

print(Employee.company)  # Google
Employee.change_company("Microsoft")  # Changing class attribute
print(Employee.company)  # Microsoft


#super() - This allows the Child class to reuse the logic from Parent.

class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        super().show()  # Calls Parent's show() method
        print("Child class method")

c = Child()
c.show()