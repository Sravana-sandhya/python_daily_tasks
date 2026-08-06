# Q3 :Sorting Product Prices 
# An e-commerce company stores product prices in a NumPy array. 
# Scenario: 
# Prices = [499, 299, 799, 199, 599] 
# Task: 
# ● Convert it into a NumPy array. 
# ● Sort the prices in ascending order.
import numpy as np
prices = [499, 299, 799, 199, 599]
prices = np.array(prices)
print("Prices in ascending order:", np.sort(prices))
