#Q10 : Advanced Simulation System 
# Scenario: 
# Simulate exam results and generate reports. 
# Task: 
# ● Generate random marks using random 
# ● Store in NumPy array 
# ● Convert to Pandas DataFrame 
# ● Use OOP to represent Student 
# ● Use conditions + loops to assign grades 
# ● Save report to file 
# ● Handle errors using try-except 
# ● Use math module for statistics
import random
import numpy as np
import pandas as pd
import math
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.grade = ""
students = [
    Student("Sravana"),Student("Ravi"),Student("Anu"),Student("Kiran"),Student("Priya")]
try:
    for student in students:
        student.marks = [random.randint(0, 100) for i in range(3)]
    marks_array = np.array([student.marks for student in students])
    print("Marks:")
    print(marks_array)
    for student in students:
        average = sum(student.marks) / len(student.marks)
        if average >= 90:
            student.grade = "A"
        elif average >= 75:
            student.grade = "B"
        elif average >= 60:
            student.grade = "C"
        elif average >= 50:
            student.grade = "D"
        else:
            student.grade = "F"
    data = []
    for student in students:
        average = sum(student.marks) / len(student.marks)
        data.append([student.name,student.marks[0],student.marks[1],student.marks[2],average,student.grade])
    df = pd.DataFrame(data,columns=["Name","Python","Maths","Science","Average","Grade"])
    print("\nStudent Report:")
    print(df)
    all_marks = marks_array.flatten()
    mean = math.fsum(all_marks) / len(all_marks)
    print("\nOverall Mean:", mean)
    df.to_csv("exam_report.txt", index=False)
    print("\nReport saved successfully.")
except Exception as e:
    print("Error:", e)