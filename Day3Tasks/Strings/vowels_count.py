# Q6 : Write a Python program to count the number of vowels in a string.
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Number of vowels:", count)