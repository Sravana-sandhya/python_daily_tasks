# Q12 : Random Dataset Normalization + Filtering 
# Scenario: 
# ● Generate 8 random float values between 0 and 1. 
# Task: 
# 1. Normalize by multiplying with 100 
# 2. Filter values greater than 50 
# 3. Sort the filtered values
import numpy as np
data = np.random.rand(8)
print("Original Data:", data)
data = data * 100
print("data:",data)
filtered = data[data > 50]
print("Filtered Values:", filtered)
sorted_filtered = np.sort(filtered)
print("Sorted Filtered Values:", sorted_filtered)