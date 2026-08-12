# 3. Palindrome Number 
# Question: 
# Write a program to check whether a number is a Palindrome. 
# Definition: 
# A number is a Palindrome if it reads the same forward and backward. 
# Example: 
# Number = 121 
# Reverse = 121 
# Output: 
# 121 is a Palindrome number 
num = int(input("Enter a number:"))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("Palindrome Number")
else :
    print("Not Palindrome")
