# Q12 : Sorting Customer Names 
# A system stores customer names: 
# ["Ravi", "Anil", "Sita", "John"] 
# Task: 
# ● Convert it to a NumPy array. 
# ● Sort the names alphabetically. 

import numpy as np
customer_names = ["Ravi", "Anil", "Sita", "John"]
arr = np.array(customer_names)
sorted_names = np.sort(arr)
print(sorted_names)
