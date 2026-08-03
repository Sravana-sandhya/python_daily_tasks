# Q1 : Student Information System (Class & Object) A school wants a program to store student details. Create a Student class with attributes such as name, roll number, and marks. Create objects for at least three students and display their details. 
class student:
    def __init__(self,name,rollnumber,marks):
        self.name = name
        self.rollnumber = rollnumber
        self.marks = marks
    def display(self):
        print("Name:",self.name)
        print("rollnumber:",self.rollnumber)
        print("marks:",self.marks)
#Creating objects
s1 = student("sandya",1,80)
s2 = student("jaswitha",2,85)
s3 = student("yamini",3,90)
s1.display()
s2.display()
s3.display()