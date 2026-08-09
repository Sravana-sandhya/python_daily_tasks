#Q5 : Reshape & Row Averages 
# A dataset: 
# data = np.arange(1, 13) 
# Task: 
# ● Reshape it into a 3×4 matrix 
# ● Compute average of each row
import numpy as np
data = np.arange(1, 13)
matrix = data.reshape(3, 4)
row_average = np.array([np.sum(matrix[0]) / len(matrix[0]),np.sum(matrix[1]) / len(matrix[1]),np.sum(matrix[2]) / len(matrix[2])])
print("Matrix:")
print(matrix)
print("Row averages:", row_average)