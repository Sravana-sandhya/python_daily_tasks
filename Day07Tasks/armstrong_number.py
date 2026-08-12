# 1. Armstrong Number 
# Question: 
# Write a program to check whether a given number is an Armstrong number or not. 
# Definition: 
# A number is called an Armstrong number if the sum of the cubes of its digits is equal to the 
# number itself. 
# Example: 
# Number = 153 
# Calculation: 
# 1³ + 5³ + 3³ 
# = 1 + 125 + 27 
# = 153 
# Output: 
# 153 is an Armstrong number 
num = int(input("Enter number:"))
original = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10
if original == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

