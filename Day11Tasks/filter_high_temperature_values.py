# Q11 : Filter High Temperature Values 
# A weather station records temperatures: 
# [28, 31, 35, 27, 40, 22] 
# Scenario: 
# The system needs temperatures above 30°C. 
# Task: 
# ● Filter the values greater than 30 using NumPy boolean filtering. 
import numpy as np 
temperatures = [28,31,35,27,40,22]
arr = np.array(temperatures)
filtered_temps = []
for temp in arr:
    if temp > 30:
        filtered_temps.append(True)
    else:
        filtered_temps.append(False)
newarr = arr[filtered_temps]
print(newarr)
