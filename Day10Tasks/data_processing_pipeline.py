# Q10 : Data Processing Pipeline 
# A data pipeline receives the following array: 
# [12, 7, 25, 3, 18, 10] 
# Scenario: 
# 1. Convert the list into a NumPy array. 
# 2. Sort the array. 
# 3. Split the sorted array into two equal parts. 
# 4. Calculate the sum of each part. 
# Output: 
# ● Sorted array 
# ● Two split arrays 
# ● Sum of each part
import numpy as np
arr = np.array([12, 7, 25, 3, 18, 10])
sorted_arr = np.sort(arr)
part1, part2 = np.split(sorted_arr, 2)
print("Sorted Array:", sorted_arr)
print("First Part:", part1)
print("Second Part:", part2)
print("Sum of First Part:", part1.sum())
print("Sum of Second Part:", part2.sum())