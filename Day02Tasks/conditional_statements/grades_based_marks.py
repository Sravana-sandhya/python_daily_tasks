# Q5 : Write a program to assign grades based on marks (for example: A, B, C, Fail)
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 50:
    print("Grade  D")
else:
    print("You have failed the exam")