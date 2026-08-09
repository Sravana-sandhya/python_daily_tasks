# Q3 : Employee Data Copy Issue (Shallow vs Deep Copy) 
# A company stores employee data: 
# employees = [[101, "A"], [102, "B"], [103, "C"]] 
# Scenario: 
# ● Create a shallow copy of the list. 
# ● Modify one nested list (e.g., change "A" to "Z"). 
# ● Observe changes in both lists. 
# Task: 
# ● Explain why the change reflects in both. 
# ● Fix it using deep copy.
import copy
employees = [[101, "A"], [102, "B"], [103, "C"]] 
shallow = copy.copy(employees)
shallow[0][1] = "z"
print("Original:", employees)
print("Shallow Copy:", shallow)
print("Explanation: In a shallow copy, only the outer list is copied. The nested lists are still shared by the original and copied lists.")
employees = [[101, "A"], [102, "B"], [103, "C"]]
deep = copy.deepcopy(employees)
deep[0][1] = "Z"
print("Original:", employees)
print("Deep Copy:", deep)