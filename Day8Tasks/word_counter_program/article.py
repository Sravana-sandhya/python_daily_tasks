# Q5: Word Counter Program 
# A writer saves an article in a file called article.txt. Write a Python program that: 
# ● Opens and reads the file 
# ● Counts the number of words, lines, and characters in the file 
# ● Displays the results.

file = open("article.txt","r")
data = file.read()
words = len(data.split())
lines = len(data.split("\n"))
characters = len(data)
print("Number of Words =", words)
print("Number of Lines =", lines)
print("Number of Characters =", characters)

file.close()