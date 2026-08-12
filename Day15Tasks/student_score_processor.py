#Q1 :Student Score Processor 
# Scenario: 
# A teacher stores student names and marks in a list of tuples. 
# Task: 
# ● Convert data into a dictionary 
# ● Use a loop + condition to find students scoring above 50 
# ● Use math module to calculate average 
# ● Store results in a text file
import math
students = [("Ravi", 70), ("Sita", 45), ("Anu", 80), ("Rahul", 30)]
student_dict = dict(students)
passed_students = []
for name, marks in student_dict.items():
    if marks > 50:
        passed_students.append(name)
marks = list(student_dict.values())
total = math.fsum(marks)
average = total / len(marks)
file = open("student_results.txt", "w")
file.write("Students scoring above 50:\n")
for name in passed_students:
    file.write(name + "\n")
file.write("Average Marks: " + str(average))
file.close()
print("Results stored in student_results.txt")