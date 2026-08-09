# Q7 : Filter Positive Even Numbers from Dataset 
# Scenario: 
# A dataset contains mixed values: 
# arr =Q [-5, 10, 15, -2, 20, 25, 30] 
# Task: 
# ● Convert to NumPy array. 
# ● Filter values that are: 
# ○ Positive 
# ○ Even 
import numpy as np
arr = [-5, 10, 15, -2, 20, 25, 30] 
arr = np.array(arr)
positive_even = arr[(arr > 0) & (arr % 2 == 0)]
print("Positive Even Numbers:", positive_even)