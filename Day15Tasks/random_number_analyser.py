#Q2 : Random Number Analyzer 
# Scenario: 
# A system generates random numbers for testing. 
# Task: 
# ● Use random to generate 10 numbers 
# ● Store in a list 
# ● Use loop + condition to count even/odd numbers 
# ● Use set to remove duplicates
import random
numbers = []
for i in range(10):
    num = random.randint(1,100)
    numbers.append(num)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
unique_numbers = set(numbers)
print("Generated Numbers:", numbers)
print("Even Count:", even)
print("Odd Count:", odd)
print("Unique Numbers:", unique_numbers)

    