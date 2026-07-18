# Q5 : Write a Python program that takes a number and prints its bitwise NOT (~) value.
n = int(input("Enter a number:"))
result = ~n
print(result)

# in bitwise NOT operation, the bits of the number are inverted 1 become 0 and 0 become 1
# for example if we take 4 as input
# 4 - 0100
# for any number ~n = -(n+1)
# ~4 = -(4+1) = -5
