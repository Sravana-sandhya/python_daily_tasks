# Q10 : University Staff Management (Hierarchical Inheritance) 
# A university has different staff types such as Professor, LabAssistant, and 
# Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
# to manage and display their information. 
class Staff:
    def display(self):
        print("University Staff")
class Professor(Staff):
    def display1(self):
        print("Name: Ravi")
        print("Designation: Professor")
class LabAssistant(Staff):
    def display2(self):
        print("Name: Ramesh")
        print("Designation: Lab Assistant")
class Administrator(Staff):
    def display3(self):
        print("Name: Suresh")
        print("Designation: Administrator")
p = Professor()
l = LabAssistant()
a = Administrator()
p.display()
p.display1()
print()
l.display()
l.display2()
print()
a.display()
a.display3()