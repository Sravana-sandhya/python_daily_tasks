from utilities.math_operations import add,multiply
from utilities.string_operations import uppercase,count_characters
a = int(input("Enter your first number:" ))
b = int(input("Enter your second number:"))
print(add(a,b))
print(multiply(a,b))
text = input("Enter a string:")
print(uppercase(text))
print(count_characters(text))              