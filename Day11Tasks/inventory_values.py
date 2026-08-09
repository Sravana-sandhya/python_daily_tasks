# Q6 : Check Data Type of Inventory Values 
# A warehouse stores product quantities: 
# [10, 20, 30, 40] 
# Task: 
# ● Convert it into a NumPy array. 
# ● Print the data type (dtype) of the array.
import numpy as np 
product_quantities = [10,20,30,40]
arr = np.array(product_quantities)
print(arr.dtype)