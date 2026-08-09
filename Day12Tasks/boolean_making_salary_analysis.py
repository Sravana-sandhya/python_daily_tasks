# Q11 : Boolean Masking for Salary Analysis 
# Scenario: 
# Employee salaries: 
# [25000, 40000, 15000, 50000, 30000] 
# Task: 
# ● Filter salaries above 30000. 
# ● Count how many employees satisfy this condition. 
import numpy as np
salaries = np.array([25000, 40000, 15000, 50000, 30000])
filter_arr = []
for salary in salaries:
    if salary > 30000:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
print("Boolean Mask:", filter_arr)
filtered_salaries = salaries[filter_arr]
print("Filtered Salaries:", filtered_salaries)
print("Count of Employees with Salary > 30000:", len(filtered_salaries))
