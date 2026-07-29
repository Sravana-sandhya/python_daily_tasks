# Q6: Employee Salary Management System 
# A company stores employee data in a file employees.txt in the format: 
# EmployeeName Salary 
# Example: 
# Ramesh 25000 
# Sita 30000 
# Arun 28000 
# Write a Python program that: 
# ● Reads employee data from the file 
# ● Displays all employee details 
# ● Finds the employee with the highest salary 
# ● Appends a new employee record to the file. 
file = open("employees.txt","r")
highest_salary = 0
highest_employee = ""
print("Employee Details")
for line in file:
    print(line, end="")
    name,salary = line.split()
    if int(salary) > highest_salary:
        highest_salary = int(salary)
        highest_employee = name
file.close()
print("\nHighest Salary Employee")
print(highest_employee, highest_salary)

file = open("employees.txt", "a")

name = input("Enter Employee Name: ")
salary = input("Enter Salary: ")

file.write(name + " " + salary + "\n")

file.close()