# Q6 : Multi-Level List Transformation (Advanced List Comprehension) 
# A dataset contains: 
# data = [[1, 2, 3], [4, 5], [6]] 
# Task: 
# ● Flatten the list using list comprehension. 
# ● Then create a new list containing squares of only even numbers. 
data = [[1, 2, 3], [4, 5], [6]] 
flattened = [x for sublist in data for x in sublist]
squares = [x * x for x in flattened if x % 2 == 0]
print("Flattened:" ,flattened)
print("Squares of Even numbers:", squares)