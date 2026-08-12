# Q10 : Write a Python program with a function that returns the largest of three numbers. 
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = largest(10, 25, 15)

print("Largest number =", result)
