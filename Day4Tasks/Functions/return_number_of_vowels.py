# Q9 : Write a function that takes a string as input and returns the number of vowels
def count_vowels(text):
    count = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

result = count_vowels("Hello")

print("Number of vowels =", result)