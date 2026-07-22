# Q5 :  Write a function to check whether a number is even or odd. 
def number(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = number(5)
print(result)
