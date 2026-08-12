# Q1: Develop a Python program to manage student marks for three subjects. Store the subject 
# names in a tuple, maintain unique student names in a set, and store each student’s marks 
# in a list inside a dictionary where the key is the student name. Create user-defined 
# functions to add a student with marks, display all student records, and calculate the average 
# marks of a student. Implement a recursive function to calculate the total marks from the list of 
# marks. The program should interact with the user through a simple menu. Also include 
# exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError 
# (average calculation issues), TypeError (incorrect data type in marks), and NameError (when a 
# student name entered does not exist in the dictionary). 
# Example Output: 
# 1. Add Student 
# 2. Display Students 
# 3. Calculate Average 
# 4. Exit 
# Enter choice: 1 
# Enter student name: Rahul 
# Enter marks for Math: 80 
# Enter marks for Science: 85 
# Enter marks for English: 90 
# 1. Add Student 
# 2. Display Students 
# 3. Calculate Average 
# 4. Exit 
# Enter choice: 2 
# Rahul : [80, 85, 90] 
# 1. Add Student 
# 2. Display Students 
# 3. Calculate Average 
# 4. Exit 
# Enter choice: 3 
# Enter student name to calculate average: Rahul 
# Total Marks: 255 
# Average Marks: 85.0 
# 1. Add Student 
# 2. Display Students 
# 3. Calculate Average 
# 4. Exit 
# Enter choice: 4

# TUPLE 
subjects = ("Math","Science","English")
#SET
students = set()
#DICTIONARY
student_marks = {}
# Recursive function to calculate total marks
def total_marks(marks,index=0):
    if index == len(marks):
        return 0
    return marks[index]+total_marks(marks,index+1)
#function to add student
def add_student():
    name = input("Enter student name: ")
    marks = []
    try:
        for subject in subjects:
            mark = int(input(f"Enter marks for {subject}:"))
            marks.append(mark)
        students.add(name)
        student_marks[name] = marks
        print("Student added successfully.")
    except ValueError:
        print("Invalid input! please enter numeric marks.")
#function to display students
def display_students():
    if len(student_marks) == 0:
        print("No student record found.")
    else:
        for name,marks in student_marks.items():
            print(name, ":", marks)
# Function to calculate average
def calculate_average():
    try:
        name = input("Enter student name to calculate average: ")

        if name not in student_marks:
            raise NameError

        marks = student_marks[name]

        # TypeError
        for i in marks:
            if not isinstance(i, int):
                raise TypeError

        total = total_marks(marks)
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")
# Main Program
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid choice.")