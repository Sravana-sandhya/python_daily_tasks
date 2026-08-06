# Q8 : Inventory Update System 
# A warehouse has an inventory stored in a matrix. 
# [[10, 15], 
# [20, 25]] 
# Scenario: 
# A new shipment increases every item quantity by 2 units. 
# Task: 
# ● Add 2 to every element using NumPy. 
# ● Print the updated inventory.
import numpy as np
inventory = np.array([[10, 15], [20, 25]])
updated_inventory = inventory + 2
print("Updated Inventory:\n", updated_inventory)