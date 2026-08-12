# Q17 : Employee Bonus Calculator (Decorators & OOP) 
# A company wants to apply a bonus calculation automatically before displaying the 
# salary. Create an Employee class and use a decorator that modifies the salary by 
# adding a bonus before displaying it.

def bonus(func):
    def wrapper(self):
        self.salary = self.salary + 5000
        func(self)
    return wrapper
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @bonus
    def display(self):
        print(self.name,self.salary)
e = Employee("sandya", 30000)
e.display()