#Write a Python program that generates 20 random numbers between 1 and 200 using 
#the random module and store them in a list. 
#Then using the math module, compute and display: 
#● Maximum value 
#● Minimum value 
# Square root of the maximum number 
#● Logarithm of the minimum number
import random
import math
numbers = []
for i in range(20):
    numbers.append(random.randint(1,200))
print(numbers)
max_num = max(numbers)
min_num = min(numbers)
print(max_num)
print(min_num)
print(math.sqrt(max_num))
print(math.log(min_num))