# Q10 : Write a Python program to remove duplicate characters from a string.
string = "programming"

result = ""

for ch in string:
    if ch not in result:
        result = result + ch

print("String after removing duplicates:", result)