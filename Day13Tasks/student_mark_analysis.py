# Q2 : Student Marks Analysis 
# Given marks of 5 students in 3 subjects: 
# marks = np.array([ 
# [70, 80, 90], 
# [60, 75, 85], 
# [50, 65, 70], 
# [90, 95, 85], 
# [40, 55, 60] 
# ]) 
# Task: 
# ● Calculate total marks of each student. 
# ● Identify students whose total marks are above the class average.
import numpy as np
marks = np.array([[70, 80, 90],[60, 75, 85],[50, 65, 70], [90, 95, 85],[40, 55, 60]])
total = np.array([np.sum(marks[0]),np.sum(marks[1]),np.sum(marks[2]),np.sum(marks[3]),np.sum(marks[4])])
average = np.sum(total) / len(total)
above_average = total[total > average]
print(above_average)
print("Total marks:", total)
print("Class average:", average)
